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
