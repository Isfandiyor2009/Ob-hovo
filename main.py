from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keybutton import registratsiya, back_button, ob_hovo
from openweather import getweatherinfo
from State import RegistrStae

load_dotenv()

telegramapi = '6231412999:AAGdYrkz8BM9e2i8VvBB611vb0gFGzSQl_I'
storage = MemoryStorage()
bot = Bot(telegramapi)
dp = Dispatcher(bot, storage=storage)
class Openwetherstate(StatesGroup):
    shahar = State()

@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer('Asalomu aleykum ob-hovo botimizga xush kelibsiz botni ishga tuwirish uchun registratsiyadan oting', reply_markup=registratsiya())



@dp.message_handler(text='®️Registratsiyadan otish')
async def registr(message: Message):
    await message.answer('Ism kiritng: ', reply_markup=back_button())
    await RegistrStae.name.set()


@dp.message_handler(state=RegistrStae.name)
async def getname(message: Message, state: FSMContext):
    if message.text == '🔙Orqaga' or message.text == '/start':
        await state.finish()
        await message.answer('Bosh menu: ', reply_markup=registratsiya())
    else:
        await message.answer('Familya kiriting: ')
        await state.update_data({'name': message.text})
        await RegistrStae.familya.set()

@dp.message_handler(state=RegistrStae.familya)
async def familya(message: Message, state: FSMContext):
    if message.text == '🔙Orqaga' or message.text == '/start':
        await state.finish()
        await message.answer('Bosh menu: ', reply_markup=back_button())
    else:
        await state.update_data({'familya': message.text})
        await message.answer('Yoshingizni kiriting:', reply_markup=registratsiya())
        await RegistrStae.age.set()

@dp.message_handler(state=RegistrStae.age)
async def getage(message: Message, state: FSMContext):
    if message.text == '🔙Orqaga' or message.text == '/start':
        await state.finish()
        await message.answer('Bosh menu: ', reply_markup=back_button())
    else:
        await state.update_data({'age': message.text})
        await message.answer('Telefon raqam kiriting:', reply_markup=registratsiya())
        await RegistrStae.phone.set()


@dp.message_handler(state=RegistrStae.phone)
async def phone(message: Message, state: FSMContext):
    if message.text == '🔙Orqaga' or message.text == '/start':
        await state.finish()
        await message.answer('📲Bosh menu: ', reply_markup=back_button())
    else:
        await state.update_data({'phone': message.text})
        await message.answer('gmail kiriting:', reply_markup=registratsiya())
        await RegistrStae.gmail.set()


@dp.message_handler(state=RegistrStae.gmail)
async def gmail(message: Message, state: FSMContext):
    if message.text == '🔙Orqaga' or message.text == '/start':
        await state.finish()
        await message.answer('📲Bosh menu: ', reply_markup=back_button())
    else:
        await state.update_data({'gmail': message.text})
        await RegistrStae.gmail.set()
        await message.answer('Registratsiya yakunlandi', reply_markup=ob_hovo())
        await message.answer('Edi ob-hovo botni ishga tushurishingiz mumkin')

        data = await state.get_data()
        user_name = message.from_user.username
        full_name = message.from_user.full_name
        char_id = message.from_user.id


        name = data['name']
        familya = data['familya']
        age = data['age']
        phone = data['phone']
        text = f'Ismi: {name}\n' \
               f'familya: {familya}\n' \
               f'age: {age}\n' \
               f'phone: {phone}\n' \
               f'username: @{user_name}\n' \
               f'full_name: {full_name}\n' \
               f'chat_id: {char_id}'

        await state.finish()
        await message.answer(text)


@dp.message_handler(text='🌤️Ob-hovo')
async def ob_hovov(message: Message):
    await message.answer('Shahar nomini kirting', reply_markup=back_button())
    await Openwetherstate.shahar.set()

@dp.message_handler(state=Openwetherstate.shahar)
async def weather(message: Message, state: FSMContext):
    if message.text == '🔙Orqaga':
        await state.finish()
        await message.answer('📱Mosh menu', reply_markup=ob_hovo())
    else:
        city = message.text
        info = getweatherinfo(city)
        if len(info) == 2:
            await message.answer_photo(photo=info[1], caption=info[0])
        else:
            await message.answer(text=info)


executor.start_polling(dp, skip_updates=True)