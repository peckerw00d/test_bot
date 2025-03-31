from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import F

import aiosqlite

from tabulate import tabulate

from utils.parse_table_data import parse_table_data
from db.repository import repo

router = Router()


class Form(StatesGroup):
    waiting_for_document = State()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    kb = [
        [KeyboardButton(text="Прислать xls файл")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!",
        reply_markup=keyboard,
    )


@router.message(F.text == "Прислать xls файл")
async def handle_button(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.waiting_for_document)
    await message.answer(
        "Отправьте свой файл формата xls. "
        "Файл должен включать в себя таблицу с полями: title - название, "
        "url - ссылка на сайт источник и xpath - путь к элементу с ценой."
    )


@router.message(Form.waiting_for_document, F.document)
async def handle_document(message: Message, state: FSMContext):
    file_id = message.document.file_id
    file = await message.bot.get_file(file_id=file_id)
    file_path = file.file_path

    downloaded_file = await message.bot.download_file(file_path)
    with open(f"downloads/{message.document.file_name}", "wb") as new_file:
        new_file.write(downloaded_file.read())

    data = await parse_table_data(f"downloads/{message.document.file_name}")

    try:
        await repo.add_data(data=data)

    except aiosqlite.Error as err:
        print(f"Возникла ошибка при загрузки данных в БД: {err}")

    table = tabulate(data, headers=["title", "url", "xpath"], tablefmt="plain")
    await message.answer(
        f"<b>Содержимое вашего документа:</b>\n\n<pre>{table}</pre>", parse_mode="HTML"
    )

    await state.clear()
