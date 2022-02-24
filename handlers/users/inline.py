
from loader import dp
from keyboards.inline.inl import menu
from aiogram import types
from data.get_news import news

@dp.inline_handler(text="news")
async def get_news(query: types.InlineQuery):
    await query.answer(results=news)

@dp.inline_handler(text='rasm')
async def get_photo(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id="rasm001",
                photo_url="https://files.glotr.uz/company/000/016/795/products/2021/01/07/2021-01-07-20-08-42-451038-51d39ca86de094d180d8fb873fb1c3ac.jpeg?_=ozbol",
                thumb_url="https://files.glotr.uz/company/000/016/795/products/2021/01/07/2021-01-07-20-08-42-451038-51d39ca86de094d180d8fb873fb1c3ac.jpeg?_=ozbol",
                caption="Apple iPhone 12 Pro Max 128 ГБ Graphite КРЕДИТА НЕТ\n\nNarxi: 14 380 000 сум/шт.",
                reply_markup=menu
            )
        ]
    )