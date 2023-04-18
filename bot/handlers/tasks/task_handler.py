import random
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from bot.forms.forms import TaskStateGroup
from bot.keyboards.inline.task import get_hint_inline_markup
from loader import dp, bot
from models import User
from services.users import get_user_info, update_user
from utils.tasks.task_0.task_0 import get_task, get_answer
from utils.tasks.task_2.task_2 import get_task_text
from aiogram.types import InputFile

task_2_path = "utils\\tasks\\task_2\\task_2_py_files"
task_2_image = InputFile("utils\\tasks\\task_2\\task_2.png")
task_2_template = InputFile("utils\\tasks\\task_2\\template_2.py")

@dp.message_handler(state=TaskStateGroup.task1)
async def task1(message: Message, user: User):
    if message.text == get_answer().lower() or message.text == get_answer().upper() or message.text == 'Эксперт':
        await message.answer(text="Верно!", reply_markup=None)
        await message.answer(text=f"{get_user_info(user)}", parse_mode="html")
        await update_user(user.id, user.name, 1, 1)
        await TaskStateGroup.task2.set()
        await message.answer(text=get_task_text())
        await bot.send_photo(photo=task_2_image, chat_id=user.id)
        await bot.send_document(document=task_2_template, chat_id=user.id)
    else:
        await message.answer(text="Увы, но нет... Может вот такую подсказочку?\n" +
                                    "https://calculatorium.ru/cryptography/caesar-cipher", reply_markup=None)


@dp.message_handler(content_types=["document"], state=TaskStateGroup.task2)
async def task2(message: Message, user: User):
    await bot.download_file(file_path, new_path)
    await message.answer(text="Файл получил")
    await task_test(msg.from_user.id, new_path)
    text, bal = task_2.get_student_result(msg.from_user.id)
    await bot.send_message(text="Проверил:\n" + str(text), chat_id=msg.from_user.id)
    if bal > 0:
        student.current_step = LabStage.step_5
        student.update_balance(bal)
        await bot.send_message(text=f"{bot_engine.get_student_info(student)}", chat_id=student.user_id,
                                parse_mode="html")
