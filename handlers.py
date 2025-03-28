from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ContentType,
    Document,
)
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


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

