from aiogram.dispatcher.filters.state import StatesGroup, State


class TaskStateGroup(StatesGroup):
    set_name = State()
    change_name = State()
    task1 = State()
    task2 = State()
    task3 = State()
