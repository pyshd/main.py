from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from pyexpat.errors import messages
from aiogram.filters.command import Command
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer("Готов!;)", reply_markup=kb.main)

    @router.message(F.text == "НАЧАТЬ")
    async def catalog(message: Message):
        await message.answer("Чтобы остановить викторину отправте или нажмите кнопку stop", reply_markup=kb.get_number)
        await message.answer("Выберите уровень сложности", reply_markup=kb.catalog)




@router.callback_query(F.data == "LIGHT")
async  def easy(callback: CallbackQuery):
    await callback.answer("вы выбрали уровень:)")
    await callback.message.answer("Вы выбрали легкий уровень.")

    @router.callback_query(F.data == "MEDIUM")
    async def easy(callback: CallbackQuery):
        await callback.answer("вы выбрали уровень:)")
        await callback.message.answer("Вы выбрали средний уровень.")

    @router.callback_query(F.data == "HARD")
    async def easy(callback: CallbackQuery):
        await callback.answer("вы выбрали уровень:)")
        await callback.message.answer("Вы выбрали сложный уровень.")


@router.message(F.text=="stop")
async def stop(message: Message, state: FSMContext):
       await state.finish()
       await message.answer("Stopped", reply_markup=kb.main)

