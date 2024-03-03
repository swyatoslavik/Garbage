from aiogram.dispatcher.filters.state import StatesGroup, State


class GetGeo(StatesGroup):
    type = State()
