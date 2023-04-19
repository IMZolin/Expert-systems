import random
from typing import Tuple
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from bot.forms.forms import TaskStateGroup
from bot.keyboards.inline.task import get_finish_test_inline_markup, get_hint_inline_markup, get_next_test_inline_markup
from loader import dp, bot
from models import User
from services.users import get_user_info, update_user
from utils.tasks.task_2.task_2 import get_task_text, get_student_result, task_test
from aiogram.types import InputFile

task_1_template = InputFile("utils\\tasks\\task_1\\caesar_cipher_template.py")
task_1_dict = InputFile("utils\\tasks\\task_1\\dict.py")
task_2_path = "utils/tasks/task_2/task_2_py_files"
task_2_image = InputFile("utils\\tasks\\task_2\\task_2.png")
task_2_template = InputFile("utils\\tasks\\task_2\\template_2.py")
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
         'ястреб': 'буфтжг',
         'янтарь': 'рядсвн',
         'смазка': 'ойэезэ',
         'снимок': 'ычтцшф',
         'агония': 'чъёеац',
         'аноним': 'жфхфпу',
         'нектар': 'йбжоьм',
         'огурец': 'ларнву'}


ans2 = ['3', '5', '4', '4', '5', '5', '23', '13', '135', '4']
ans3 = [1.9219280948873623, 0.4689955935892812, 1.8464393446710154, 0.0, 3.321928094887362, 1.0, 1.0, 1.5219280948873621, 0.0, 2.807354922057604]
selected_words = {}
@dp.callback_query_handler(lambda c: c.data.startswith('test'))
async def task1(callback_query: CallbackQuery, user: User):
    await TaskStateGroup.task1.set()
    await update_user(user.id, None, None, None, None, None, 1)
    random_key = random.choice(list(words.keys()))
    random_word = words[random_key]
    selected_words[user.id] = {'key': random_key, 'word': random_word}
    await callback_query.message.answer(
    text=f"<b>Задание 1: Шифр Цезаря</b>\nРасшифруйте: {random_word}\nМожете закодировать шифр Цезаря, используя шаблон.\nОтвет в качестве сообщения с расшифронным словом(не файл)",
    reply_markup=get_hint_inline_markup(),
    parse_mode="html")
    # await bot.send_document(document=task_1_template, chat_id=user.id)


@dp.message_handler(state=TaskStateGroup.task1)
async def task1_process(message: Message, user: User, state: FSMContext):
    if message.text == selected_words[user.id]['key']:
        await message.answer(text="Верно!", reply_markup=None)
        await update_user(user.id, None, 5, None, None, 5, 2)
        # await message.answer(text=f"{get_user_info(user)}", parse_mode="html")
        await TaskStateGroup.task2.set()
        await message.answer(text=f"<b>Задание 2: Найм на работу</b>\n\n", parse_mode="html")
        # await bot.send_photo(photo=task_2_image, chat_id=user.id)
        # await bot.send_document(document=task_2_template, chat_id=user.id)
    else:
        await message.answer(text="Увы, но нет... Может вот такую подсказочку?\n" +
                                    "https://calculatorium.ru/cryptography/caesar-cipher", reply_markup=None)


@dp.callback_query_handler(lambda c: c.data.startswith('task2'))
async def show_hint(callback_query: CallbackQuery, user: User) -> None:
    # await callback_query.message.answer(text=f"{get_user_info(user)}", parse_mode="html")
    await TaskStateGroup.task2.set()
    await callback_query.message.answer("<b>Задание 2: Найм на работу</b>\nНеобходимо реализовать систему управления (функцию Select) со стратегией первый подходящий, приближающий нас к решению, которая вернет либо принятое решение(найм/отказ), либо следующий вопрос, который нужно задать кандидату.", parse_mode="html")


@dp.message_handler(state=TaskStateGroup.task2)
async def task2(message: Message, user: User):
    user_ans = message.text.split(' ')
    scores_2 = 0
    if(len(user_ans) != 10):
        await message.answer(f"Упс.. Попробуй ещё раз. Длинна ответа должна равняться 10\nДлинна вашего сообщения:{len(user_ans)}")
    else:
        for i in range(len(user_ans)):
            if user_ans[i] in ans2[i]:
                scores_2 += 2
        await update_user(user.id, None, None, scores_2, None, None, None)     
        if scores_2 == 20:
            await message.answer(text=f"Проверил. Ваш результат: {scores_2}/20")
            await message.answer("<b>Задание 3: Информационная энтропия</b>\nВам необходимо реализовать 2 функции: class_probabilities и entropy. Первая вычисляет вероятности классов, а вторая энтропию этих классов", parse_mode="html")
            await update_user(user.id, None, None, None, None, user.scores+user.task_2_scores, 3)
            await TaskStateGroup.task3.set()
        else:
            await message.answer(text=f"Проверил. Ваш результат: {scores_2}/20", reply_markup=get_next_test_inline_markup())   


@dp.callback_query_handler(lambda c: c.data.startswith('task3'))
async def show_hint(callback_query: CallbackQuery, user: User) -> None:
    # await callback_query.message.answer(text=f"{get_user_info(user)}", parse_mode="html")
    await TaskStateGroup.task3.set()
    await callback_query.message.answer("<b>Задание 3: Информационная энтропия</b>\n\n", parse_mode="html")


@dp.message_handler(state=TaskStateGroup.task3)
async def task3(message: Message, state: FSMContext, user: User):
    # await message.answer(text=f"{get_user_info(user)}", parse_mode="html")
    user_ans = message.text.split('\n')
    scores = user.scores
    scores_3 = 0
    epsilon = 1e-10
    print(user_ans)
    if(len(user_ans) != 10):
        await message.answer(f"Упс.. Попробуй ещё раз. Длинна ответа должна равняться 10\nДлинна вашего сообщения:{len(user_ans)}")
    else:
        for i in range(len(user_ans)):
            if abs(float(user_ans[i]) - ans3[i]) < epsilon:
                scores_3 += 1
        # scores += scores_3
        await update_user(user.id, None, None, None, scores_3, user.scores+user.task_2_scores, 3)   
    if scores_3 == 10:
        await state.finish()
        await message.answer(text=f"Проверил. Ваш результат: {scores_3}/10")
    else:
        await message.answer(text=f"Проверил. Ваш результат: {scores_3}/10", reply_markup=get_finish_test_inline_markup())

@dp.callback_query_handler(lambda c: c.data.startswith('next'), state=TaskStateGroup.task2)
async def show_next(callback_query: CallbackQuery, user: User) -> None:
    await update_user(user.id, None, None, None, user.scores + user.task_2_scores, None, 3) 
    await callback_query.message.answer("<b>Задание 3: Информационная энтропия</b>", parse_mode="html")
    await TaskStateGroup.task3.set()

@dp.callback_query_handler(lambda c: c.data.startswith('finish'), state=TaskStateGroup.task3)
async def show_next(state: FSMContext, user: User) -> None:
    await update_user(user.id, None, None, None, None, user.scores + user.task_3_scores, 3) 
    await state.finish()