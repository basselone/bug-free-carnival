import re
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db import Database
import db as ff
import config as cfg
import db_api
import button as but
import ast
import json
logging.basicConfig(level=logging.INFO)
bot = Bot(token=cfg.telegram_bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database('database.db')
class ozid(StatesGroup):
    americano = State()
    americano1 = State()
    americano2 = State()
    double = State()
    double1 = State()
    double2 = State()
    kapuch = State()
    kapuch1 = State()
    kapuch2 = State()
    kapuch3 = State()
    latte = State()
    latte1 = State()
    latte2 = State()
    latte3 = State()
    hot = State()
    hot1 = State()
    hot2 = State()
    hot3 = State()
    banana = State()
    banana1 = State()
    banana2 = State()
    banana3 = State()
    maka = State()
    maka1 = State()
    maka2 = State()
    maka3 = State()
    coob = State()
    zakazkofe = State()
    zakazkofe1 = State()

@dp.message_handler(commands=['start'])
async def message_start(message: types.Message):
    admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
    admin.add(but.admin_c)
    admin.add(but.admin_c1)
    admin.add(but.otziv_na_nap, but.texpod)
    admin.add(but.zakazat_kofe)
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.from_user.id in cfg.managers_id:
        await message.answer(
        text='Здраствуйте, доступные сейчас команды для вас 👇',reply_markup=admin)
    else:
        await message.answer(
            text='Здраствуйте, доступные сейчас команды для вас 👇', reply_markup=start)

@dp.message_handler(text="Оставить отзыв на напиток")
async def message_start(message: types.Message):
    if not message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano,but.kapuchino)
        napitki.add(but.latte,but.banana_raf)
        napitki.add(but.double_expresso,but.makachino)
        napitki.add(but.menu,but.hot_chocolad)
        await message.answer(
        text='Выберете напиток на который хотитие оставить отзыв 👇',reply_markup=napitki)
    else:
        admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
        admin.add(but.admin_c)
        admin.add(but.admin_c1)
        admin.add(but.otziv_na_nap, but.texpod)
        admin.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=admin)


@dp.message_handler(text="ТЕХ.ПОДДЕРЖКА")
async def message_start(message: types.Message):
    if not message.from_user.id in cfg.managers_id:
        cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cancel.add(but.cancel)
        await message.answer(
            text='Напишите своё сообщение что бы отправить его администрации', reply_markup=cancel)
    else:
        cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cancel.add(but.cancel)
        await message.answer(
            text='Напишите своё сообщение что бы отправить его администрации', reply_markup=cancel)
    await (ozid.coob.set())

@dp.message_handler(text="Заказать кофе ☕️")
async def message_start(message: types.Message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but.menu)
    await message.answer(
            text='👉Ссылка на сайт👈', reply_markup=menu)

@dp.message_handler(text="Заказать кофе")
async def message_start(message: types.Message):
    napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
    napitki.add(but.americano, but.kapuchino)
    napitki.add(but.latte, but.banana_raf)
    napitki.add(but.double_expresso, but.makachino)
    napitki.add(but.menu, but.hot_chocolad)
    await message.answer(
            text='Выберете напиток который хотите выбрать:', reply_markup=napitki)
    await (ozid.zakazkofe.set())

@dp.message_handler(state=ozid.zakazkofe)
async def process_button_2_press(message: types.Message, state: FSMContext):
    text = message.text
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but.menu)
    await message.answer("Укажите адрес куда нужно доставить кофе", reply_markup=menu)
    await (ozid.zakazkofe1.set())

@dp.message_handler(state=ozid.zakazkofe1)
async def process_button_2_press(message: types.Message, state: FSMContext):
    text = message.text
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but.menu)
    await message.answer("Оплата сейчас или на месте?", reply_markup=menu)
    await (ozid.zakazkofe2.set())


@dp.message_handler(text="Ответ на вопрос от покупателя")
async def otvet(message: types.Message):
    if message.from_user.id in cfg.managers_id:
        cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cancel.add(but.cancel)
        await message.answer(
            text='Выберете нужное сообщение нажмите ответ и пишите ответ', reply_markup=cancel)
        await (ozid.coob.set())
    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)


@dp.message_handler(text="Назад в меню")
async def message_start(message: types.Message):
    if not message.from_user.id in cfg.managers_id:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Меню 👇', reply_markup=start)
    else:
        admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
        admin.add(but.admin_c)
        admin.add(but.admin_c1)
        admin.add(but.otziv_na_nap, but.texpod)
        admin.add(but.zakazat_kofe)
        await message.answer(
            text='Меню 👇', reply_markup=admin)


@dp.message_handler(state=ozid.coob)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text.lower() == "отмена":
        if not message.from_user.id in cfg.managers_id:
            start = types.ReplyKeyboardMarkup(resize_keyboard=True)
            start.add(but.otziv_na_nap, but.texpod)
            start.add(but.zakazat_kofe)
            await message.answer("Отменено, вы возвращенны в меню 👇", reply_markup=start)
        else:
            admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
            admin.add(but.admin_c)
            admin.add(but.admin_c1)
            admin.add(but.otziv_na_nap, but.texpod)
            admin.add(but.zakazat_kofe)
            await message.answer("Отменено, вы возвращенны в меню 👇", reply_markup=admin)
    else:
        if message.from_user.id in cfg.managers_id:
            if message.reply_to_message:
                try:
                    parsing_target = '[(]{1}(.{0,20})[)]{1}'
                    reply_id = re.findall(parsing_target, str(message.reply_to_message.text))
                    username_parsing = '([@]{1}.{0,30})[ (]{2}'
                    username = re.findall(username_parsing, str(message.reply_to_message.text))
                    await bot.send_message(chat_id=reply_id[0],
                                        text='Ответ от менеджера: \n\n'
                                                f'{message.text}')
                    try:
                        admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        admin.add(but.admin_c)
                        admin.add(but.admin_c1)
                        admin.add(but.otziv_na_nap, but.texpod)
                        admin.add(but.zakazat_kofe)
                        await bot.send_message(chat_id=message.from_user.id,
                                            text=f'Ваш ответ для {username[0]} был успешно доставлен',reply_markup = admin)
                        message_set = False
                        reply_message_id = message.reply_to_message.message_id
                        message_list = db_api.get_all_messages()
                        for message_data in message_list:
                            local_message_list = ast.literal_eval(message_data[1])
                            for local_messages in local_message_list:
                                if local_messages['message_id'] == reply_message_id:
                                    messages_set_id = message_data[0]
                                    message_set = True
                        if message_set:
                            old_message_data = db_api.get_singe_message(id=messages_set_id)
                            local_old_message_list = ast.literal_eval(old_message_data[1])
                            old_text = old_message_data[2]
                            for old_local_messages in local_old_message_list:
                                await bot.edit_message_text(chat_id=old_local_messages['chat_id'], message_id=old_local_messages['message_id'], text=f"{old_text}\n\n✓")
                            db_api.delete_message(id=messages_set_id)

                    except IndexError:
                        admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        admin.add(but.admin_c)
                        admin.add(but.admin_c1)
                        await bot.send_message(chat_id=message.from_user.id,
                                           text=f'Ваш ответ для {reply_id[0]} был успешно доставлен')
                except IndexError:
                    await bot.send_message(chat_id=message.from_user.id,
                                       text=f"Не удается найти идентификатор пользователя или имя пользователя в этом сообщении")
            else:
                admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
                admin.add(but.admin_c)
                admin.add(but.admin_c1)
                admin.add(but.otziv_na_nap, but.texpod)
                admin.add(but.zakazat_kofe)
                await bot.send_message(chat_id=message.from_user.id,
                                   text='Вы не можете отправить сообщения самому себе!\nдоступные сейчас команды:',reply_markup = admin)
        else:

            current_messages_list = []
            for managers in cfg.managers_id:
                text_to_send = f"Сообщение от @{message.from_user.username} ({message.from_user.id}):\n\n{message.text}"
                message_data = (await bot.send_message(chat_id=managers,
                                   text=text_to_send))
                current_messages_list.append({
                    'message_id': message_data['message_id'],
                    'chat_id': message_data['chat']['id']
                })
            db_api.add_message(message_data=str(current_messages_list), text=text_to_send)
            start = types.ReplyKeyboardMarkup(resize_keyboard=True)
            start.add(but.otziv_na_nap, but.texpod)
            start.add(but.zakazat_kofe)
            await bot.send_message(chat_id=message.from_user.id,
                               text='Ваше сообщение успешно доставлено менеджеру, вам ответят в ближайшее время.',reply_markup = start)
            await bot.send_message(chat_id=message.from_user.id, text="Вы возвращенны в меню 👇")
@dp.message_handler(text="Американо")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano, but.kapuchino)
        napitki.add(but.latte, but.banana_raf)
        napitki.add(but.double_expresso, but.makachino)
        napitki.add(but.hot_chocolad, but.menu)
        napitki.add(but.o6)
        xx = db.aromatx()
        xc = db.krepostx()
        xv = db.gorkostx()
        us = db.usam()
        if (xx == None):
            xx = 0
        if (xc == None):
            xc = 0
        if (xv == None):
            xv = 0
        if (us == None):
            us = 0
        await message.answer(f"Американо\nКоличество оценивших: {us}\nАромат: {xx}\nКрепость: {xc}\nГорькость: {xv}", reply_markup=napitki)
    else:
        americano = types.ReplyKeyboardMarkup(resize_keyboard=True)
        americano.add(but.o1, but.o2)
        americano.add(but.o3, but.o4)
        americano.add(but.o5, but.menu)
        await message.answer(
            text='Оцените Аромат напитка от 1 до 5 👇', reply_markup=americano)
        await ozid.americano.set()

@dp.message_handler(state=ozid.americano)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.aromat(txt)
        americano = types.ReplyKeyboardMarkup(resize_keyboard=True)
        americano.add(but.o1, but.o2)
        americano.add(but.o3, but.o4)
        americano.add(but.o5, but.menu)
        await message.answer("Оцените крепость напитка от 1 до 5 👇",reply_markup=americano)
        await ozid.americano1.set()


@dp.message_handler(state=ozid.americano1)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.krepost(txt)
        americano = types.ReplyKeyboardMarkup(resize_keyboard=True)
        americano.add(but.o1, but.o2)
        americano.add(but.o3, but.o4)
        americano.add(but.menu, but.o5)
        await message.answer("Оцените горькость напитка от 1 до 5 👇",reply_markup=americano)
        await ozid.americano2.set()


@dp.message_handler(state=ozid.americano2)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        tx = 1
        db.amusers(tx)
        txt = message.text
        db.gorkost(txt)
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer("Спасибо за оценку!", reply_markup=start)
        await message.answer("Вы в меню")

@dp.message_handler(text="Двойное экспрессо")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano, but.kapuchino)
        napitki.add(but.latte, but.banana_raf)
        napitki.add(but.double_expresso, but.makachino)
        napitki.add(but.hot_chocolad, but.menu)
        napitki.add(but.o10)
        xx = db.aromatxdouble()
        xc = db.krepostxdouble()
        xv = db.gorkostxdouble()
        us = db.usdo()
        if (xx == None):
            xx = 0
        if (xc == None):
            xc = 0
        if (xv == None):
            xv = 0
        if (us == None):
            us = 0
        await message.answer(f"Двойное экспрессо\nКоличество оценивших: {us}\nАромат: {xx}\nКрепость: {xc}\nГорькость: {xv}", reply_markup=napitki)
    else:
        double = types.ReplyKeyboardMarkup(resize_keyboard=True)
        double.add(but.o1, but.o2)
        double.add(but.o3, but.o4)
        double.add(but.menu, but.o5)
        await message.answer(
            text='Оцените Аромат напитка от 1 до 5 👇', reply_markup=double)
        await ozid.double.set()

@dp.message_handler(state=ozid.double)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.aromatdouble(txt)
        double = types.ReplyKeyboardMarkup(resize_keyboard=True)
        double.add(but.o1, but.o2)
        double.add(but.o3, but.o4)
        double.add(but.menu, but.o5)
        await message.answer("Оцените крепость напитка от 1 до 5 👇",reply_markup=double)
        await ozid.double1.set()

@dp.message_handler(state=ozid.double1)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.krepostdouble(txt)
        double = types.ReplyKeyboardMarkup(resize_keyboard=True)
        double.add(but.o1, but.o2)
        double.add(but.o3, but.o4)
        double.add(but.menu, but.o5)
        await message.answer("Оцените горькость напитка от 1 до 5 👇",reply_markup=double)
        await ozid.double2.set()


@dp.message_handler(state=ozid.double2)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        tx = 1
        db.dousers(tx)
        txt = message.text
        db.gorkostdouble(txt)
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer("Спасибо за оценку!", reply_markup=start)
        await message.answer("Вы в меню")

@dp.message_handler(text="Капучино")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano, but.kapuchino)
        napitki.add(but.latte, but.banana_raf)
        napitki.add(but.double_expresso, but.makachino)
        napitki.add(but.hot_chocolad, but.menu)
        napitki.add(but.o7)
        xx = db.aromatxkapuch()
        xc = db.krepostxkapuch()
        xv = db.gorkostxkapuch()
        xb = db.nasishxkapuch()
        us = db.uska()
        if (xx == None):
            xx = 0
        if (xc == None):
            xc = 0
        if (xv == None):
            xv = 0
        if (us == None):
            us = 0
        if (xb == None):
            xb = 0
        await message.answer(f"Капучино\nКоличество оценивших: {us}\nАромат: {xx}\nКрепость: {xc}\nГорькость: {xv}\nНасыщенность молока: {xb}", reply_markup=napitki)
    else:
        kapuch = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kapuch.add(but.o1, but.o2)
        kapuch .add(but.o3, but.o4)
        kapuch.add(but.menu, but.o5)
        await message.answer(
            text='Оцените Аромат напитка от 1 до 5 👇', reply_markup=kapuch)
        await ozid.kapuch.set()

@dp.message_handler(state=ozid.kapuch)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.aromatkapuch(txt)
        kapuch = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kapuch.add(but.o1, but.o2)
        kapuch.add(but.o3, but.o4)
        kapuch.add(but.menu, but.o5)
        await message.answer("Оцените крепость напитка от 1 до 5 👇",reply_markup=kapuch)
        await ozid.kapuch1.set()

@dp.message_handler(state=ozid.kapuch1)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.krepostkapuch(txt)
        kapuch = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kapuch.add(but.o1, but.o2)
        kapuch.add(but.o3, but.o4)
        kapuch.add(but.menu, but.o5)
        await message.answer("Оцените горькость напитка от 1 до 5 👇",reply_markup=kapuch)
        await ozid.kapuch2.set()

@dp.message_handler(state=ozid.kapuch2)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.gorkostkapuch(txt)
        kapuch = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kapuch.add(but.o1, but.o2)
        kapuch.add(but.o3, but.o4)
        kapuch.add(but.menu, but.o5)
        await message.answer("Оцените насыщенность молока в напитке от 1 до 5 👇",reply_markup=kapuch)
        await ozid.kapuch3.set()


@dp.message_handler(state=ozid.kapuch3)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        tx = 1
        db.kausers(tx)
        txt = message.text
        db.nasishkapuch(txt)
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer("Спасибо за оценку!", reply_markup=start)
        await message.answer("Вы в меню")

@dp.message_handler(text="Латте")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano, but.kapuchino)
        napitki.add(but.latte, but.banana_raf)
        napitki.add(but.double_expresso, but.makachino)
        napitki.add(but.hot_chocolad, but.menu)
        napitki.add(but.o8)
        xx = db.aromatxlatte()
        xc = db.krepostxlatte()
        xv = db.gorkostxlatte()
        xb = db.nasishxlatte()
        us = db.usla()
        if (xx == None):
            xx = 0
        if (xc == None):
            xc = 0
        if (xv == None):
            xv = 0
        if (us == None):
            us = 0
        if (xb == None):
            xb = 0
        await message.answer(f"Латте\nКоличество оценивших: {us}\nАромат: {xx}\nКрепость: {xc}\nГорькость: {xv}\nНасыщенность молока: {xb}", reply_markup=napitki)
    else:
        latte = types.ReplyKeyboardMarkup(resize_keyboard=True)
        latte.add(but.o1, but.o2)
        latte.add(but.o3, but.o4)
        latte.add(but.menu, but.o5)
        await message.answer(
            text='Оцените Аромат напитка от 1 до 5 👇', reply_markup=latte)
        await ozid.latte.set()

@dp.message_handler(state=ozid.latte)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.aromatlatte(txt)
        latte = types.ReplyKeyboardMarkup(resize_keyboard=True)
        latte.add(but.o1, but.o2)
        latte.add(but.o3, but.o4)
        latte.add(but.menu, but.o5)
        await message.answer("Оцените крепость напитка от 1 до 5 👇",reply_markup=latte)
        await ozid.latte1.set()

@dp.message_handler(state=ozid.latte1)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.krepostlatte(txt)
        latte = types.ReplyKeyboardMarkup(resize_keyboard=True)
        latte.add(but.o1, but.o2)
        latte.add(but.o3, but.o4)
        latte.add(but.menu, but.o5)
        await message.answer("Оцените горькость напитка от 1 до 5 👇",reply_markup=latte)
        await ozid.latte2.set()

@dp.message_handler(state=ozid.latte2)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.gorkostlatte(txt)
        latte = types.ReplyKeyboardMarkup(resize_keyboard=True)
        latte.add(but.o1, but.o2)
        latte.add(but.o3, but.o4)
        latte.add(but.menu, but.o5)
        await message.answer("Оцените насыщенность молока в напитке от 1 до 5 👇",reply_markup=latte)
        await ozid.latte3.set()


@dp.message_handler(state=ozid.latte3)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        tx = 1
        db.lausers(tx)
        txt = message.text
        db.nasishlatte(txt)
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer("Спасибо за оценку!", reply_markup=start)
        await message.answer("Вы в меню")

@dp.message_handler(text="Макачино")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano, but.kapuchino)
        napitki.add(but.latte, but.banana_raf)
        napitki.add(but.double_expresso, but.makachino)
        napitki.add(but.hot_chocolad, but.menu)
        napitki.add(but.o11)
        xx = db.aromatxmaka()
        xc = db.krepostxmaka()
        xv = db.gorkostxmaka()
        xb = db.nasishxmaka()
        us = db.usma()
        if (xx == None):
            xx = 0
        if (xc == None):
            xc = 0
        if (xv == None):
            xv = 0
        if (us == None):
            us = 0
        if (xb == None):
            xb = 0
        await message.answer(f"Макачино\nКоличество оценивших: {us}\nАромат: {xx}\nКрепость: {xc}\nГорькость: {xv}\nНасыщенность молока: {xb}", reply_markup=napitki)
    else:
        maka = types.ReplyKeyboardMarkup(resize_keyboard=True)
        maka.add(but.o1, but.o2)
        maka.add(but.o3, but.o4)
        maka.add(but.menu, but.o5)
        await message.answer(
            text='Оцените Аромат напитка от 1 до 5 👇', reply_markup=maka)
        await ozid.maka.set()

@dp.message_handler(state=ozid.maka)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.aromatmaka(txt)
        maka = types.ReplyKeyboardMarkup(resize_keyboard=True)
        maka.add(but.o1, but.o2)
        maka.add(but.o3, but.o4)
        maka.add(but.menu, but.o5)
        await message.answer("Оцените крепость напитка от 1 до 5 👇",reply_markup=maka)
        await ozid.maka1.set()

@dp.message_handler(state=ozid.maka1)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.krepostmaka(txt)
        maka = types.ReplyKeyboardMarkup(resize_keyboard=True)
        maka.add(but.o1, but.o2)
        maka.add(but.o3, but.o4)
        maka.add(but.menu, but.o5)
        await message.answer("Оцените горькость напитка от 1 до 5 👇",reply_markup=maka)
        await ozid.maka2.set()

@dp.message_handler(state=ozid.maka2)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.gorkostmaka(txt)
        maka = types.ReplyKeyboardMarkup(resize_keyboard=True)
        maka.add(but.o1, but.o2)
        maka.add(but.o3, but.o4)
        maka.add(but.menu, but.o5)
        await message.answer("Оцените насыщенность молока в напитке от 1 до 5 👇",reply_markup=maka)
        await ozid.maka3.set()


@dp.message_handler(state=ozid.maka3)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        tx = 1
        db.mausers(tx)
        txt = message.text
        db.nasishmaka(txt)
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer("Спасибо за оценку!", reply_markup=start)
        await message.answer("Вы вернулись в меню")


@dp.message_handler(text="Горячий шоколад")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano, but.kapuchino)
        napitki.add(but.latte, but.banana_raf)
        napitki.add(but.double_expresso, but.makachino)
        napitki.add(but.hot_chocolad, but.menu)
        napitki.add(but.o12)
        xx = db.aromatxhot()
        xc = db.krepostxhot()
        xv = db.gorkostxhot()
        xb = db.nasishxhot()
        us = db.ushot()
        if (xx == None):
            xx = 0
        if (xc == None):
            xc = 0
        if (xv == None):
            xv = 0
        if (us == None):
            us = 0
        if (xb == None):
            xb = 0
        await message.answer(f"Горячий шоколад\nКоличество оценивших: {us}\nАромат: {xx}\nКрепость: {xc}\nГорькость: {xv}\nНасыщенность вкуса: {xb}", reply_markup=napitki)
    else:
        hot = types.ReplyKeyboardMarkup(resize_keyboard=True)
        hot.add(but.o1, but.o2)
        hot.add(but.o3, but.o4)
        hot.add(but.menu, but.o5)
        await message.answer(
            text='Оцените Аромат напитка от 1 до 5 👇', reply_markup=hot)
        await ozid.hot.set()

@dp.message_handler(state=ozid.hot)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.aromathot(txt)
        hot = types.ReplyKeyboardMarkup(resize_keyboard=True)
        hot.add(but.o1, but.o2)
        hot.add(but.o3, but.o4)
        hot.add(but.o5, but.menu)
        await message.answer("Оцените крепость напитка от 1 до 5 👇",reply_markup=hot)
        await ozid.hot1.set()

@dp.message_handler(state=ozid.hot1)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.kreposthot(txt)
        hot = types.ReplyKeyboardMarkup(resize_keyboard=True)
        hot.add(but.o1, but.o2)
        hot.add(but.o3, but.o4)
        hot.add(but.o5, but.menu)
        await message.answer("Оцените горькость напитка от 1 до 5 👇",reply_markup=hot)
        await ozid.hot2.set()

@dp.message_handler(state=ozid.hot2)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.gorkosthot(txt)
        hot = types.ReplyKeyboardMarkup(resize_keyboard=True)
        hot.add(but.o1, but.o2)
        hot.add(but.o3, but.o4)
        hot.add(but.o5, but.menu)
        await message.answer("Оцените насыщенность вкуса в напитке от 1 до 5 👇",reply_markup=hot)
        await ozid.hot3.set()


@dp.message_handler(state=ozid.hot3)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        tx = 1
        db.hotusers(tx)
        txt = message.text
        db.nasishhot(txt)
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer("Спасибо за оценку!", reply_markup=start)
        await message.answer("Вы вернулись в меню")

@dp.message_handler(text="Банановый раф")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano, but.kapuchino)
        napitki.add(but.latte, but.banana_raf)
        napitki.add(but.double_expresso, but.makachino)
        napitki.add(but.hot_chocolad, but.menu)
        napitki.add(but.o9)
        xx = db.aromatxbanana()
        xc = db.krepostxbanana()
        xv = db.gorkostxbanana()
        xb = db.nasishxbanana()
        us = db.usba()
        if (xx == None):
            xx = 0
        if (xc == None):
            xc = 0
        if (xv == None):
            xv = 0
        if (us == None):
            us = 0
        if (xb == None):
            xb = 0
        await message.answer(f"Банановый раф\nКоличество оценивших: {us}\nАромат: {xx}\nКрепость: {xc}\nГорькость: {xv}\nНасыщенность вкуса: {xb}", reply_markup=napitki)
    else:
        banana = types.ReplyKeyboardMarkup(resize_keyboard=True)
        banana.add(but.o1, but.o2)
        banana.add(but.o3, but.o4)
        banana.add(but.o5, but.menu)
        await message.answer(
            text='Оцените Аромат напитка от 1 до 5 👇', reply_markup=banana)
        await ozid.banana.set()

@dp.message_handler(state=ozid.banana)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.aromatbanana(txt)
        banana = types.ReplyKeyboardMarkup(resize_keyboard=True)
        banana.add(but.o1, but.o2)
        banana.add(but.o3, but.o4)
        banana.add(but.o5, but.menu)
        await message.answer("Оцените крепость напитка от 1 до 5 👇",reply_markup=banana)
        await ozid.banana1.set()

@dp.message_handler(state=ozid.banana1)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.krepostbanana(txt)
        banana = types.ReplyKeyboardMarkup(resize_keyboard=True)
        banana.add(but.o1, but.o2)
        banana.add(but.o3, but.o4)
        banana.add(but.o5, but.menu)
        await message.answer("Оцените горькость напитка от 1 до 5 👇",reply_markup=banana)
        await ozid.banana2.set()

@dp.message_handler(state=ozid.banana2)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        txt = message.text
        db.gorkostbanana(txt)
        banana = types.ReplyKeyboardMarkup(resize_keyboard=True)
        banana.add(but.o1, but.o2)
        banana.add(but.o3, but.o4)
        banana.add(but.o5, but.menu)
        await message.answer("Оцените насыщенность вкуса в напитке от 1 до 5 👇",reply_markup=banana)
        await ozid.banana3.set()


@dp.message_handler(state=ozid.banana3)
async def process_button_2_press(message: types.Message, state: FSMContext):
    await state.finish()
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start.add(but.otziv_na_nap, but.texpod)
    start.add(but.zakazat_kofe)
    if message.text == "Назад в меню":
        await message.answer("Вы вернулись в меню 👇", reply_markup=start)
    else:
        tx = 1
        db.bausers(tx)
        txt = message.text
        db.nasishbanana(txt)
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer("Спасибо за оценку!", reply_markup=start)
        await message.answer("Вы вернулись в меню")

@dp.message_handler(text="Отзывы на напитки")
async def message_start(message: types.Message):
    if message.from_user.id in cfg.managers_id:
        napitki = types.ReplyKeyboardMarkup(resize_keyboard=True)
        napitki.add(but.americano,but.kapuchino)
        napitki.add(but.latte,but.banana_raf)
        napitki.add(but.double_expresso,but.makachino)
        napitki.add(but.hot_chocolad, but.menu)
        await message.answer(
        text='Выберете напиток на который хотитие посмотреть отзыв',reply_markup=napitki)
    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)

@dp.message_handler(text="Удалить статистику Американо")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        db.delamericano()
        await message.answer("Вы удалили статистику Американо")

    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)

@dp.message_handler(text="Удалить статистику Капучино")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        db.delkapuch()
        await message.answer("Вы удалили статистику Капучино")

    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)

@dp.message_handler(text="Удалить статистику Латте")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        db.dellatte()
        await message.answer("Вы удалили статистику Латте")

    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)

@dp.message_handler(text="Удалить статистику Банановый раф")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        db.delbanana()
        await message.answer("Вы удалили статистику Банановый раф")

    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)

@dp.message_handler(text="Удалить статистику Двойное экспрессо")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        db.deldouble()
        await message.answer("Вы удалили статистику Двойное экспрессо")

    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)

@dp.message_handler(text="Удалить статистику Макачино")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        db.delmaka()
        await message.answer("Вы удалили статистику Макачино")

    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)

@dp.message_handler(text="Удалить статистику Горячий шоколад")
async def message_start(message: types.Message, state: FSMContext):
    if message.from_user.id in cfg.managers_id:
        db.delhot()
        await message.answer("Вы удалили статистику Горячий шоколад")

    else:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start.add(but.otziv_na_nap, but.texpod)
        start.add(but.zakazat_kofe)
        await message.answer(
            text='Не знаю такой команды, вы возвращены в меню 👇', reply_markup=start)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)