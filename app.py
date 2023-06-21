import logging
from button import rayonlar,yunusobod_hotel,olmazor_hotel,uch_tepahotel,Mirzo_ulugbek,Sergeli,yashnabad

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6222915607:AAFIomgOMWtgj2UumFVOjyQWVcEuuPe-rzM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup=rayonlar)

# reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
@dp.message_handler(text='yunusobod')
async def send_welcome(message: types.Message):
    await message.reply("siz yunusobod mehmonxonalarini tanladingiz",reply_markup=yunusobod_hotel)



@dp.message_handler(text='Velera hotel')
async def echo(message: types.Message):
    await message.answer_location(41.361909057815836, 69.2899871685746)

@dp.message_handler(text='The element hotel')
async def echo(message: types.Message):
    await message.answer_location(41.36187286794334, 69.28992072450559)

@dp.message_handler(text='Comfort Tashkent')
async def echo(message: types.Message):
    await message.answer_location(41.35819336326337, 69.29695084522113)

@dp.message_handler(text='Garnet')
async def echo(message: types.Message):
    await message.answer_location(41.35956983849164, 69.27788209483207)

@dp.message_handler(text='King plaza')
async def echo(message: types.Message):
    await message.answer_location(41.36104771742338, 69.27799679452914)

@dp.message_handler(text='ortga')
async def echo(message: types.Message):
    await message.answer("siz ortga qaytdingiz",reply_markup=rayonlar)

# tdnbjdcopjhvghhhhhhhbddddddddddddddddddddddddddddddddddddddddd

@dp.message_handler(text='olmazor')
async def send_welcome(message: types.Message):
    await message.reply("siz olmazor mehmonxonalarini tanladingiz",reply_markup=olmazor_hotel)



@dp.message_handler(text='Imo')
async def echo(message: types.Message):
    await message.answer_location(41.35897502274373, 69.21136594404193)

@dp.message_handler(text='Grand star')
async def echo(message: types.Message):
    await message.answer_location(41.3568018461213, 69.20811302910394)

@dp.message_handler(text='Olimpia')
async def echo(message: types.Message):
    await message.answer_location(41.36164665226342, 69.196157289542)

@dp.message_handler(text='Mustakilik street')
async def echo(message: types.Message):
    await message.answer_location(41.38409966436878, 69.1739365248643)

@dp.message_handler(text='Галаба боги')
async def echo(message: types.Message):
    await message.answer_location(41.39216652663119, 69.22447145371034)

@dp.message_handler(text='ortga')
async def echo(message: types.Message):
    await message.answer("siz ortga qaytdingiz",reply_markup=rayonlar)


# wedhygtqwuhkjsdhfghdchfffffffffffffffffffffffffffffffffffffffffffffffffff

@dp.message_handler(text='uch tepa')
async def send_welcome(message: types.Message):
    await message.reply("siz uch tepa mehmonxonalarini tanladingiz",reply_markup=uch_tepahotel)


@dp.message_handler(text='Boloxona')
async def echo(message: types.Message):
    await message.answer_location(41.28403323557566, 69.17836656763001)

@dp.message_handler(text='Robota')
async def echo(message: types.Message):
    await message.answer_location(41.30835091239576, 69.11944159627829)

@dp.message_handler(text='Kokaldosh talablar yotoqhonasi')
async def echo(message: types.Message):
    await message.answer_location(41.308040346963764, 69.13781978084275)

@dp.message_handler(text='Seven season')
async def echo(message: types.Message):
    await message.answer_location(41.28204020165276, 69.17120212176752)

@dp.message_handler(text='Samo')
async def echo(message: types.Message):
    await message.answer_location(41.280671625168566, 69.1947776901385)

@dp.message_handler(text='ortga')
async def echo(message: types.Message):
    await message.answer("siz ortga qaytdingiz",reply_markup=rayonlar)

# rerererererrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrerererrrrrrrrrrrrrrrr

@dp.message_handler(text='Mirzo ulugbek')
async def send_welcome(message: types.Message):
    await message.reply("siz Mirzo ulugbek mehmonxonalarini tanladingiz",reply_markup=Mirzo_ulugbek)


@dp.message_handler(text='Hexaл камал')
async def echo(message: types.Message):
    await message.answer_location(41.33877988201067, 69.3563416392946)

@dp.message_handler(text='Frankfort')
async def echo(message: types.Message):
    await message.answer_location(41.345222367734316, 69.32901300049599)

@dp.message_handler(text='Pear Tashkent')
async def echo(message: types.Message):
    await message.answer_location(41.336931940197765, 69.32521711467591)

@dp.message_handler(text='Eco Wallness')
async def echo(message: types.Message):
    await message.answer_location(41.32599204419185, 69.33554193365711)

@dp.message_handler(text='Mini hotel')
async def echo(message: types.Message):
    await message.answer_location(41.321772034581016, 69.3402902167492)

@dp.message_handler(text='ortga')
async def echo(message: types.Message):
    await message.answer("siz ortga qaytdingiz",reply_markup=rayonlar)

# vfdhjsgcghdjsdcvjhkkkkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj

@dp.message_handler(text='Sergeli')
async def send_welcome(message: types.Message):
    await message.reply("siz Sergeli mehmonxonalarini tanladingiz",reply_markup=Sergeli)


@dp.message_handler(text='Index')
async def echo(message: types.Message):                  
    await message.answer_location(41.20490193511811, 69.23599790863118)

@dp.message_handler(text='Sofa hotel Tashkent')
async def echo(message: types.Message):
    await message.answer_location(41.20827489538548, 69.20710967142635)

@dp.message_handler(text='South')
async def echo(message: types.Message):
    await message.answer_location(41.25805122779179, 69.22756481742907)

@dp.message_handler(text='Чоштеба узгариш')
async def echo(message: types.Message):
    await message.answer_location(41.248824139345736, 69.21023349131113)

@dp.message_handler(text='obi bed and breakfast')
async def echo(message: types.Message):
    await message.answer_location(41.22085070914671, 69.17976043072441)

@dp.message_handler(text='ortga')
async def echo(message: types.Message):
    await message.answer("siz ortga qaytdingiz",reply_markup=rayonlar)

# eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

@dp.message_handler(text='yashnabad')
async def send_welcome(message: types.Message):
    await message.reply("siz yashnabad mehmonxonalarini tanladingiz",reply_markup=yashnabad)



@dp.message_handler(text='Beshbolla')
async def echo(message: types.Message):
    await message.answer_location(41.27967536895482, 69.33323502107253)

@dp.message_handler(text='Maxwell')
async def echo(message: types.Message):
    await message.answer_location(41.28711101439769, 69.3394683554168)

@dp.message_handler(text='oaza asaka')
async def echo(message: types.Message):
    await message.answer_location(41.288113416853896, 69.31061247346123)

@dp.message_handler(text='Hotel avtoteh')
async def echo(message: types.Message):
    await message.answer_location(41.29738186780682, 69.32700564575093)

@dp.message_handler(text='Globus hotel')
async def echo(message: types.Message):
    await message.answer_location(41.31041877381356, 69.32884947488748)

@dp.message_handler(text='ortga')
async def echo(message: types.Message):
    await message.answer("siz ortga qaytdingiz",reply_markup=rayonlar)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)