from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from decouple import config

class Form(StatesGroup):
    name = State()
    target = State()
    contact = State()
    send_to_admin = State()

start_router = Router()



@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer(f'Приветствую! Напишите, пожалуйста, название компании:')
    await state.set_state(Form.name)


@start_router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Принято. Теперь напишите цель проекта:')
    await state.set_state(Form.target)


@start_router.message(Form.target)
async def process_target(message: Message, state: FSMContext):
    await state.update_data(target=message.text)
    await message.answer('Записал. И так же укажите свои контакты:')
    await state.set_state(Form.contact)


@start_router.message(Form.contact)
async def process_contact(message: Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await message.answer('Благодарю! Данные направлены администратору! Ожидайте!')
    user_data = await state.get_data()
    result = (
        f"Название компании: {user_data['name']}\n"
        f"Цель проекта: {user_data['target']}\n"
        f"Контакты: {user_data['contact']}"
    )
    await message.bot.send_message(config('admin_id'), result)


# @start_router.message(Form.send_to_admin)
# async def send_order_to_admin(message: Message, state: FSMContext, bot:types.BotCommand):


