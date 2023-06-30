from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrStae(StatesGroup):
    name = State()
    familya = State()
    age = State()
    phone = State()
    gmail = State()
    username = State()


