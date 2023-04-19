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
# from utils.tasks.task_0.task_0 import get_task, get_answer
from utils.tasks.task_2.task_2 import task_test
from bot.keyboards.inline.task import get_hint_inline_markup, get_start_task2_inline_markup, get_start_task3_inline_markup, get_start_test_inline_markup
from aiogram.types import InputFile

task_1_template = InputFile("utils\\tasks\\task_1\\caesar_cipher_template.py")
task_1_dict = InputFile("utils\\tasks\\task_1\\dict.py")

@dp.message_handler(CommandStart())
async def _start(message: Message, user: User):
    text = f'Привет {user.name}!\nСегодня я буду помогать тебе получать удовольствие!'
    await message.answer(text, reply_markup=get_default_markup(user))
    await TaskStateGroup.set_name.set()
    await message.answer('Введи фамилию и имя и группу, например: Иванов Иван /2')

@dp.message_handler(state=[TaskStateGroup.change_name, TaskStateGroup.set_name])
async def process_change_name(message: Message, state: FSMContext, user: User):
    name = message.text.strip()
    await update_user(user.id, name=name)
    if (await state.get_state()) == TaskStateGroup.set_name.state:
        if user.current_step == 0:
            await message.answer(f"Ваше имя было обновлено до {name}.", reply_markup=get_start_test_inline_markup())
        elif user.current_step == 2:
            TaskStateGroup.task2.set()
            await message.answer(f"Ваше имя было обновлено до {name}.\n", parse_mode="html", reply_markup=get_start_task2_inline_markup())
        elif user.current_step == 3:
            await message.answer(f"Ваше имя было обновлено до {name}.\n<b>Задание 3: Информационная энтропия</b>", parse_mode="html", reply_markup=get_start_task3_inline_markup())  
    else:    
        await message.answer(f"Ваше имя было обновлено до {name}.")
    await state.finish()
    

@dp.callback_query_handler(lambda c: c.data.startswith('hint'), state=TaskStateGroup.task1)
async def show_hint(callback_query: CallbackQuery) -> None:
    await callback_query.message.answer("Может вот такую подсказочку?\nhttps://calculatorium.ru/cryptography/caesar-cipher")


@dp.message_handler(commands=['change_name'])
async def change_name(message: Message, user: User):
    await TaskStateGroup.change_name.set()
    await message.answer('Введи фамилию и имя и группу, например: Иванов Иван /2')


@dp.message_handler(text='Help! 🆘')
@dp.message_handler(CommandHelp())
async def _help(message: Message, user: User):
    commands = get_default_commands()

    text = ('Help! 🆘') + '\n\n'
    for command in commands:
        text += f'{command.command} - {command.description}\n'
    await message.answer(text)



    