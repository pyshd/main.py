from aiogram.fsm.state import StatesGroup, State


class QuizState(StatesGroup):
    level = State()
    task = State()
