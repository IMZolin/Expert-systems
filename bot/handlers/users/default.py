import random
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from bot.commands import get_default_commands
from bot.forms.forms import TaskStateGroup
from bot.keyboards.default.default import get_default_markup
from loader import dp, bot
from models import User
from services.users import get_user_info, update_user
from utils.tasks.task_0.task_0 import get_task, get_answer
from utils.tasks.task_2.task_2 import task_test
from bot.keyboards.inline.task import get_hint_inline_markup
from aiogram.types import InputFile

task_1_template = InputFile("utils\\tasks\\task_1\\caesar_cipher_template.py")
task_1_dict = InputFile("utils\\tasks\\task_1\\dict.py")

words = {'атеизм': 'щлювбё',
         'башмак': 'изафзт',
         'газель': 'ьщбюех',
         'градус': 'ёугжцф',
         'доктор': 'еплупс',
         'двойка': 'омщфхк',
         'ерунда': 'юймжэщ',
         'жвачка': 'смквхк',
         'запрет': 'ришщны',
         'истина': 'жпржлю',
         'кремль': 'ущнхфе',
         'курорт': 'ъгаюав',
         'камень': 'вчдьеу',
         'капкан': 'цлыцлщ',
         'люстра': 'щляаюн',
         'момент': 'ьюьфэв',
         'мясник': 'щлюъхч',
         'обычай': 'хзвюжр',
         'офицер': 'пхйчёс',
         'разрыв': 'оюёоща',
         'расист': 'чжшпшщ',
         'талант': 'жфафвж',
         'трость': 'нлймнч',
         'указка': 'ытзптз',
         'фигура': 'узвтпя',
         'филиал': 'эсфсиф',
         'циклоп': 'эпстхц',
         'челнок': 'тажийё',
         'шарада': 'ршишьш',
         'щетина': 'фандиы',
         'щелчок': 'нщалгя',
         'эгоист': 'дйхпшщ',
         'эколог': 'щжкзкя',
         'юбилей': 'эазкди',
         'юность': 'оюявгм',
         'ювелир': 'аджнкт',
         'японец': 'удгвщк',
         'ятреб': 'бфтжг',
         'янтарь': 'рядсвн',
         'смазка': 'ойэезэ',
         'снимок': 'ычтцшф',
         'агония': 'чъёеац',
         'аноним': 'жфхфпу',
         'нектар': 'йбжоьм',
         'огурец': 'ларнву'}

user_words = {}
matched_words = {}


@dp.message_handler(CommandStart())
async def _start(message: Message, user: User):
    text = f'Привет {user.name}!\nСегодня я буду помогать тебе получать удовольствие!\nВведи фамилию и имя, например: Иванов Иван'
    await message.answer(text, reply_markup=get_default_markup(user))
    # user_words[user.id] = tuple(words.values())
    # for user, words_tuple in user_words.items():
    #     user_matched_words = {}
    #     for word, coded_word in words.items():
    #         if coded_word in words_tuple:
    #             user_matched_words[word] = coded_word
    #     matched_words[user] = user_matched_words
    # print(user_words)
    await TaskStateGroup.set_name.set()


@dp.message_handler(state=[TaskStateGroup.set_name, TaskStateGroup.change_name])
async def process_name(message: Message, state: FSMContext, user: User):
    name = message.text.strip()
    await update_user(user.id, name=name)
    await message.answer(f"Ваше имя было обновлено до {name}.")
    if (await state.get_state()) == TaskStateGroup.set_name.state:
        await TaskStateGroup.task1.set()
        r = random.randint(2, 32)
        await message.answer(
        text=f"<b>Задание 1: Шифр Цезаря</b>\nРасшифруйте: {get_task(r)}\nМожете закодировать шифр Цезаря, используя шаблон.\nОтвет в качестве сообщения с расшифронным словом(не файл)",
        reply_markup=get_hint_inline_markup(),
        parse_mode="html")
        await bot.send_document(document=task_1_template, chat_id=user.id)
    else:
        await state.finish()

@dp.callback_query_handler(lambda c: c.data.startswith('hint'), state=TaskStateGroup.task1)
async def show_hint(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Может вот такую подсказочку?\nhttps://calculatorium.ru/cryptography/caesar-cipher")


@dp.message_handler(commands=['change_name'])
async def change_name(message: Message):
    await TaskStateGroup.change_name.set()
    await message.answer('Введи фамилию и имя, например: Иванов Иван')


@dp.message_handler(text='Help! 🆘')
@dp.message_handler(CommandHelp())
async def _help(message: Message, user: User):
    commands = get_default_commands()

    text = ('Help! 🆘') + '\n\n'
    for command in commands:
        text += f'{command.command} - {command.description}\n'

    await message.answer(text)



    