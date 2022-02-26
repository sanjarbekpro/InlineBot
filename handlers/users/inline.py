
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
            ),
            types.InlineQueryResultPhoto(
                id="rasm002",
                photo_url="https://files.glotr.uz/company/000/015/722/products/2020/05/25/2020-05-25-13-49-05-863538-eed3c8a25d6ea9a1c2c38e33476af15c.jpg?_=ozbol",
                thumb_url="https://files.glotr.uz/company/000/015/722/products/2020/05/25/2020-05-25-13-49-05-863538-eed3c8a25d6ea9a1c2c38e33476af15c.jpg?_=ozbol",
                title="Смартфон Realme RMX1927 5 Blue",
                description="Представляем вашему вниманию высококачественный смартфон марки Realme  RMX1927 5 (3+64) 5 современный и изящный смартфон, корпус которого выполнен из прочного пластика с мерцающей и приятной на ощупь поверхностью.",
                caption="Смартфон Realme RMX1927 5 Blue\n\nNarxi: 2 072 631 сум / шт.",
                reply_markup=menu
            ),

        ]
    )
@dp.inline_handler(text="video")
async def get_video(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultVideo(
                id="video001",
                video_url="https://videon.img.ria.ru/Out/Flv/20220224/2022_02_24__exwiioyt.4j3.mp4",
                thumb_url="https://cdnn21.img.ria.ru/images/07e6/02/15/1774188440_0:0:2768:1968_1440x900_80_1_1_fe927b87552f658b8e80cae0fe24513c.jpg.webp?source-sid=rian_photo",
                title="Владимир Владимирович Путин",
                description="МОСКВА, 24 фев - РИА Новости. Эксперты говорят, что внутри США создана империя лжи - трудно с этим не согласиться, заявил президент РФ Владимир Путин.",
                mime_type="video/mp4"
            )
 
        ]
    )

@dp.inline_handler()
async def get_data(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="12345",
                title="Путин объявил о начале военной операции на Украине ",
                input_message_content=types.InputTextMessageContent(
                    message_text="Россия начала военную операцию на Украине после обращения властей самопровозглашенных Донецкой и Луганской народных республик с просьбой 'оказать помощь в отражении агрессии Киева'. Об этом объявил президент России Владимир Путин в экстренном обращении в четверг. Он заявил, что Москва будет стремиться к 'демилитаризации и денацификации' Украины, призвал украинских военных сложить оружие и предупредил о незамедлительном ответе в случае попыток вмешаться в происходящее извне.."
                ),
                url="https://ru.euronews.com/2022/02/24/ukraine-moment-of-peril-wrap",
                thumb_url="https://ibb.co/txCtPZ2",
                description="Оккупация украинских территорий в планы Москвы не входит, заверил Путин, она выступает за право народов Украины на самоопределение. Также президент РФ повторил, что Россия не может допустить появления у Киева ядерного оружия, и напомнил о неприемлемом для нее расширении НАТО на Восток.",
                reply_markup=menu
            )
        ]
    )














# @dp.inline_handler(text="voice")
# async def get_voice(query: types.InlineQuery):
#     await query.answer(
#         results=[
#             types.InlineQueryResultCachedVoice(
#             id = "1",
#             voice_file_id="AwACAgQAAxkBAAICkmIVESIGnJDNyvYNXZUHBYATMEhRAAJrAgACdQeNUL6lqLJWYR_9IwQ",
#             title="AUF",
#             caption="AUF"
#         )
#     ]
#     )
