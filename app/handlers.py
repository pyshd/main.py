from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import app.keyboards as kb

from app.task import choose_operation, generate_number, get_nums_borders, get_result, make_divisible
from app.states import QuizState

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Готов! ;)", reply_markup=kb.main)


@router.message(F.text == "НАЧАТЬ")
async def catalog(message: Message):
    await message.answer("Чтобы остановить викторину, отправьте или нажмите кнопку stop", reply_markup=kb.get_number)
    await message.answer("Выберите уровень сложности", reply_markup=kb.catalog)


@router.callback_query(F.data == "LIGHT")
async def easy(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Вы выбрали уровень :)")
    await state.set_state(QuizState.level)
    await state.update_data(level="LIGHT")
    await callback.message.answer("Вы выбрали легкий уровень.\nТеперь можно начинать!")
    await start_task(callback.message, state)


@router.callback_query(F.data == "MEDIUM")
async def medium(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Вы выбрали уровень :)")
    await state.set_state(QuizState.level)
    await state.update_data(level="MEDIUM")
    await callback.message.answer("Вы выбрали средний уровень.\nТеперь можно начинать!")
    await start_task(callback.message, state)


@router.callback_query(F.data == "HARD")
async def hard(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Вы выбрали уровень :)")
    await state.set_state(QuizState.level)
    await state.update_data(level="HARD")
    await callback.message.answer("Вы выбрали сложный уровень.\nТеперь можно начинать!")
    await start_task(callback.message, state)


async def start_task(message: Message, state: FSMContext):
    user_data = await state.get_data()
    level = user_data.get("level")
    operation = choose_operation()
    first_borders, second_borders = get_nums_borders(level, operation)

    first_num = generate_number(*first_borders)
    second_num = generate_number(*second_borders)
    if operation == "/":
        first_num, second_num = make_divisible(first_num, second_num)

    await state.update_data(task={
        "first_num": first_num,
        "second_num": second_num,
        "operation": operation,
        "result": get_result(first_num, second_num, operation)
    })
    
    await state.set_state(QuizState.task)

    await message.answer(f"Ваша задача: {first_num} {operation} {second_num} = ?")


@router.message(F.text, QuizState.task)
async def check_answer(message: Message, state: FSMContext):
    user_data = await state.get_data()
    task = user_data.get("task")

    if not task:
        await message.answer("Что-то пошло не так. Попробуйте начать заново.")
        return

    correctanswer = task["result"]

    try:
        useranswer = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, отправьте число!")
        return

    if useranswer == correctanswer:
        await message.answer("Правильно!")
        await start_task(message, state)
    else:
        await message.answer("Неправильно! Попробуйте еще раз.")
