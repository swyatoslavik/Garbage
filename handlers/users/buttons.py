from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsPrivate
from handlers.users.menu import menu
from keyboards.default import kb_send_location
from loader import dp
from states.get_info import GetGeo
from utils.find_smth import find_smth
from utils.geocoder import geocoder


@dp.message_handler(IsPrivate(),
                    text=['📍Мусорные баки', '📍Переработка мусора',
                          '📍Вывоз мусора'])
async def find_obj(message: types.Message, state: FSMContext):
    answer = message.text

    await message.answer(f"Выбран раздел {answer}. Что будем делать?",
                         reply_markup=kb_send_location)
    await state.update_data(type=answer)
    await GetGeo.type.set()


@dp.message_handler(IsPrivate(),
                    content_types=['location'],
                    state=GetGeo.type)
async def get_geo(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    data = await state.get_data()
    ttype = data.get("type")
    ddata = find_smth(latitude, longitude, ttype)

    try:
        key, value = next(iter(ddata.items()))
        address_name = key if key else geocoder(value['lat'], value['lon'])
    except StopIteration:
        address_name = None

    if address_name:
        await message.answer("Ближайший найденный объект:")
        await dp.bot.send_venue(
            message.from_user.id,
            value['lat'],
            value['lon'],
            ttype,
            address_name
        )
    else:
        await message.answer(
            f"К сожалению, мы не смогли найти {ttype} неподалёку(")
    await state.finish()
    await menu(message)


@dp.message_handler(IsPrivate(), text=['🤔Проблемы и факты',
                                       '♻️Полезная информация с видами мусора и как правильно его сортировать'])
async def problems_and_facts(message: types.Message):
    answer = message.text
    if answer == "🤔Проблемы и факты":
        await message.answer("🤔Проблемы и факты\n"
                             "В данном разделе вы можете ознакомится с проблемами и фактами, которые в данный период времени актуальные и очень важные ⬇️\n"
                             "• Мусор губит животных 🐾\n"
                             " Ежегодно миллионы птиц и морских обитателей принимают мусор (пакеты, провода, алюминий) за еду, давятся им, травятся или задыхаются. А некоторые попадают в пластиковые предметы как в ловушку, что приводит к их гибели 😔\n"
                             "• Самый распространенный мусор - сигаретные окурки 🚬\n"
                             "Каждый год по всему миру выбрасывают около 4,5 млрд табачных фильтров. Поэтому борьба с вредными привычками – это полезно не только для здоровья, но и для природы 🌿\n"
                             "• Пластик бессмертен ❌\n"
                             "По оценкам экологов, весь пластик, который когда-либо был произведен человеком, до сих пор находится в окружающей среде. А это примерно 8 млрд тонн с хвостиком. При этом только в Мировом океане каждый год оказывается до 13 млн тонн пластиковых вещей. Экологи прогнозируют, что через тридцать лет количество пластика в океане превысит суммарную массу рыб 😳\n"
                             "Это совсем маленькое количество фактов и проблем в мире, связанные с мусором. Но все эти проблемы мы можем решить самостоятельно ❗️\n")
    elif answer == "♻️Полезная информация с видами мусора и как правильно его сортировать":
        await message.answer(
            "♻️Полезная информация с видами мусора и как правильно его сортировать\n"
            "В данном разделе вы можете ознакомится с видами мусора и как его сортировать ♻️\n"
            "•Пищевой мусор 🍎\n"
            "•Пластик 🔵\n"
            "•Макулатура 📝\n"
            "•Стекло 🔎\n"
            "•Резина 🛞\n"
            "•Текстиль 👖\n"
            "•Строительный мусор 🔨\n"
            "•Опасные и чрезвычайно опасные отходы 🔋\n"
            "Как же всё это правильно сортировать? 😳\n"
            "1.Теоретическая подготовка: узнайте всё о маркировке, выясните адреса пунктов приёма вторсырья, найдите ближайшие или удобные вам контейнеры 🗑️\n"
            "2. Начните сортировку с одного-двух видов отходов. Лучше перерабатывать немного, но качественно, чем много, но с ошибками ☝🏻\n"
            "3. Обустройте «сортировочную»: купите контейнеры и ёмкости под те или иные виды мусора, выделите под них удобное и скрытое от глаз место ❗️\n"
            "4. Придумайте, что делать со съедобными отходами. Установите измельчитель в раковине или приобретите ёмкость для компостирования (в квартире) или создайте компостную яму (на своём участке) 🍎\n"
            "5. Не забывайте достаточно очищать вторсырьё перед сдачей на переработку. Некоторые пункты сбора, например, просят приносить пластиковые бутылки с допустимыми маркировками исключительно без обёрток, а для других пунктов это не проблема. Лучше заранее узнавать требования каждого пункта, прежде чем везти туда вторсырьё 📍\n"
            "6. Помните об опасных отходах: батарейки, краски, технику и лекарства необходимо хранить отдельно от другого мусора и сдавать строго в специальные пункты приёма. Поэтому под это добро выделите отдельный контейнер дома (можно небольшой: вряд ли там будет скапливаться очень много отходов) 📦\n"
            "7. Следите за благотворительными инициативами. Часто они проходят в удобных и доступных многим людям ТЦ и магазинах у дома. В таком случае отсортированные отходы можно сдать куда быстрее, чем хранить их и ждать подходящего случая для вывоза в специализированный пункт приёма 🚮\n"
            "Все это поможет хотя бы немного снизить экологическую проблему, которая так актуальна сейчас 🙏🏻")
    else:
        await message.answer("ЧЗХ!?")
    await menu(message)


@dp.message_handler(IsPrivate(), text="👨‍💻Помощь")
async def command_help(message: types.Message):
    await message.answer(
        "Как же пользоваться ботом? 🤔\n"
        "Все очень просто:\n"
        "1. Зайдите в главное меню 🏠\n"
        "2. Выберите пункт, который вам необходим 📲\n"
        "3. Отправьте свою геолокацию 📍\n"
        "4. Бот выдаст вам ближайшие мусорные баки, производство вывоза мусора или центры переработки мусора 🏢\n\n"
        "Спасибо, что воспользовались нашим ботом ❤️")


@dp.message_handler(IsPrivate(), text="Назад ↩️")
async def command_back(message: types.Message):
    await menu(message)


@dp.message_handler(IsPrivate(), text="🏠Главное меню")
async def work_with_orders(message: types.Message):
    await menu(message)
