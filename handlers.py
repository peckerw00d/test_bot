from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ContentType,
    Document,
)
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import F

router = Router()


class Form(StatesGroup):
    waiting_for_document = State()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    kb = [
        [KeyboardButton(text="КНОПКА")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!",
        reply_markup=keyboard,
    )


@router.message(F.text == "КНОПКА")
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

    await message.answer(f"Документ {message.document.file_name} успешно загружен!")
    await state.clear()
