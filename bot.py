import enum
import random

from aiogram import Bot, Dispatcher, types

import task_0
import task_1
import task_2
import task_3
from config import TOKEN
import bot_engine
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InputFile

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

students = []

change_name_lets_go_btn = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=1
).add(
    "Вперед!",
    "Изменить фамилию и имя",
)
tip_btn = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=1
).add(
    "Подсказка: 200$"
)
lets_go_btn = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=1
).add("Вперед!")


class LabStage(enum.Enum):
    step_0 = 'Фамилия и имя заполнено'
    step_1 = 'Изменение имени и фамилии'
    step_2 = 'Тестовое задание c шифратором отправлено'
    step_3 = 'Тестовое задание c шифратором принято'
    step_4 = 'Задание 1: Select с условиями if-else отправлено'
    step_5 = 'Задание 1: Select с условиями if-else принято'
    step_6 = 'Задание 2: энтропия отправлено'
    step_7 = 'Задание 2: энтропия принято'
    step_8 = 'Задание 3: энтропия отправлено'
    step_9 = 'Задание 3: энтропия принято'


task_prices = {
    LabStage.step_0: 500,
    LabStage.step_1: 0,
    LabStage.step_2: 1000,
    LabStage.step_3: 1000,
}

task_1_file = InputFile("task_1.png")
task_1_template = InputFile("template_1.py")
task_2_file = InputFile("task_2.png")
task_2_template = InputFile("template_2.py")
task_3_template = InputFile("template_3.py")

meme_file = InputFile("meme.jpg")


class Student:
    user_id: int = 0
    name: str = None
    balance: int = 0
    completed_steps = []
    sent_answers = []
    current_step = None
    task_1_best = None

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def set_name(self, name):
        self.name = name

    def update_balance(self, value: int):
        self.balance += value

    def update_steps(self, step):
        self.completed_steps.append(step)
        self.current_step = step

    def update_answers(self, answer):
        self.sent_answers.append(answer)


def main_loop():
    executor.start_polling(dp)


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await bot.send_message(text="Привет! Сегодня я буду помогать тебе получать удовольствие!", chat_id=msg.from_user.id)
    await bot.send_message(text="Пожалуйста, введи свою фамилию и имя:",
                           chat_id=msg.from_user.id)
    student: Student = bot_engine.get_student_by_id(students, msg.from_user.id)
    if student is not None:
        student.update_balance(0)
        student.current_step = LabStage.step_0
        students.remove(student)


@dp.message_handler(commands=['list'])
async def process_start_command(msg: types.Message):
    bot_engine.get_students_results(students)
    list_cmd_file = InputFile("results.csv")
    await bot.send_document(document=list_cmd_file, chat_id=msg.from_user.id)


@dp.message_handler(commands=['getid'])
async def process_start_command(msg: types.Message):
    await bot.send_message(text=f"Ваш id для обращения в поддержку: {msg.from_user.id}",
                           chat_id=msg.from_user.id, reply_markup=None)


@dp.message_handler(lambda msg: msg.text == 'Изменить фамилию и имя')
async def change_name(msg: types.Message):
    student: Student = bot_engine.get_student_by_id(students, msg.from_user.id)
    if student is None:
        await send_error(msg)
    else:
        await bot.send_message(text=f"Введите новые фамилию и имя:", chat_id=student.user_id, reply_markup=None)
        student.current_step = LabStage.step_1


async def send_error(msg: types.Message):
    await bot.send_message(text=f"Произошли технические шоколадки, отправь скрин переписки админам",
                           chat_id=msg.from_user.id, reply_markup=None)


@dp.message_handler()
async def engine(msg: types.Message):
    student: Student = bot_engine.get_student_by_id(students, msg.from_user.id)
    if student is None:
        students.append(Student(msg.from_user.id, msg.text))
        student = bot_engine.get_student_by_id(students, msg.from_user.id)
        student.update_balance(0)
        student.current_step = LabStage.step_0

        await bot.send_message(text=f"Создан новый профиль!", chat_id=student.user_id)
        await bot.send_message(text=f"{bot_engine.get_student_info(student)}", chat_id=student.user_id,
                               parse_mode="html")
        await bot.send_message(text="Приступим к выполнению первого задания?", chat_id=student.user_id,
                               reply_markup=change_name_lets_go_btn)

    elif student.current_step == LabStage.step_0:
        r = random.randint(2, 32)
        await bot.send_message(
            text=f"Расшифруйте: {task_0.get_task(r)}",
            chat_id=student.user_id,
            reply_markup=tip_btn,
            parse_mode="html")
        student.current_step = LabStage.step_2

    elif student.current_step == LabStage.step_1:
        student.name = msg.text
        await bot.send_message(text="Фамилия и имя успешно изменены", chat_id=student.user_id,
                               reply_markup=change_name_lets_go_btn)
        student.current_step = LabStage.step_0

    elif student.current_step == LabStage.step_2:
        if msg.text == task_0.get_answer().lower() or msg.text == task_0.get_answer().upper() or msg.text == 'Эксперт':
            await bot.send_message(text="Верно!", chat_id=student.user_id, reply_markup=None)
            student.update_balance(task_prices[LabStage.step_2])
            student.current_step = LabStage.step_3
            await bot.send_message(text=f"{bot_engine.get_student_info(student)}", chat_id=student.user_id,
                                   parse_mode="html")
            await bot.send_message(text="Приступим к выполнению второго задания?\n", chat_id=student.user_id,
                                   reply_markup=lets_go_btn)
        else:
            await bot.send_message(text="Увы, но нет... Может вот такую подсказочку?\n" +
                                        "https://calculatorium.ru/cryptography/caesar-cipher", chat_id=student.user_id,
                                   reply_markup=tip_btn)

    elif student.current_step == LabStage.step_3:
        await bot.send_message(text=task_1.get_task_text(), chat_id=student.user_id)
        student.current_step = LabStage.step_4
        await bot.send_photo(photo=InputFile("task_1.png"), chat_id=student.user_id)
        await bot.send_document(document=InputFile("template_1.py"), chat_id=student.user_id)

    elif student.current_step == LabStage.step_4:
        await bot.send_message(text='Необходимо прикрепить файл .py', chat_id=student.user_id)

    elif student.current_step == LabStage.step_5:
        await bot.send_message(text=task_2.get_task_text(), chat_id=student.user_id)
        await bot.send_photo(photo=InputFile("task_2.png"), chat_id=student.user_id)
        await bot.send_document(document=InputFile("template_2.py"), chat_id=student.user_id)
        student.current_step = LabStage.step_6

    elif student.current_step == LabStage.step_6:
        await bot.send_message(text='Необходимо прикрепить файл .py', chat_id=student.user_id)

    elif student.current_step == LabStage.step_7:
        await bot.send_message(text=task_3.get_task_text(), chat_id=student.user_id)
        await bot.send_document(document=InputFile("template_3.py"), chat_id=student.user_id)
        student.current_step = LabStage.step_8

    elif student.current_step == LabStage.step_8:
        await bot.send_message(text='Необходимо прикрепить файл .py', chat_id=student.user_id)


@dp.message_handler(content_types=["document"])
async def engine_files(msg: types.Message):
    student: Student = bot_engine.get_student_by_id(students, msg.from_user.id)
    file_id = msg.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    # файл для первого задания
    if student.current_step == LabStage.step_4:
        new_path = "task_1_py_files/" + "task_1_" + str(msg.from_user.id) + ".py"
        await bot.download_file(file_path, new_path)
        await bot.send_message(text="Файл получил", chat_id=msg.from_user.id)
        await bot.send_message(text="Начинаю проверку", chat_id=msg.from_user.id)
        await task_1.task_test(msg.from_user.id, new_path)
        text, bal = task_1.get_student_result(msg.from_user.id)
        await bot.send_message(text="Проверил:\n" + str(text), chat_id=msg.from_user.id)
        if bal > 0:
            student.current_step = LabStage.step_5
            student.update_balance(bal)
            await bot.send_message(text=f"{bot_engine.get_student_info(student)}", chat_id=student.user_id,
                                   parse_mode="html")

    # файл для второго задания
    elif student.current_step == LabStage.step_6:
        new_path = "task_2_py_files/" + "task_2_" + str(msg.from_user.id) + ".py"
        await bot.download_file(file_path, new_path)
        await bot.send_message(text="Файл получил", chat_id=msg.from_user.id)
        await bot.send_message(text="Начинаю проверку", chat_id=msg.from_user.id)
        await task_2.task_test(msg.from_user.id, new_path)
        text, bal = task_2.get_student_result(msg.from_user.id)
        await bot.send_message(text="Проверил:\n" + str(text), chat_id=msg.from_user.id)
        if bal > 0:
            student.current_step = LabStage.step_7
            student.update_balance(bal)
            await bot.send_message(text=f"{bot_engine.get_student_info(student)}", chat_id=student.user_id,
                                   parse_mode="html")

    # файл для третьего задания
    elif student.current_step == LabStage.step_8:
        new_path = "task_3_py_files/" + "task_3_" + str(msg.from_user.id) + ".py"
        await bot.download_file(file_path, new_path)
        await bot.send_message(text="Файл получил", chat_id=msg.from_user.id)
        await bot.send_message(text="Начинаю проверку", chat_id=msg.from_user.id)
        await task_2.task_test(msg.from_user.id, new_path)
        text, bal = task_2.get_student_result(msg.from_user.id)
        await bot.send_message(text="Проверил:\n" + str(text), chat_id=msg.from_user.id)
        if bal > 0:
            student.update_balance(bal)
            await bot.send_message(text=f"{bot_engine.get_student_info(student)}", chat_id=student.user_id,
                                    parse_mode="html")


if __name__ == '__main__':
    main_loop()
