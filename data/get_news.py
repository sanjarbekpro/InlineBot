import requests
from aiogram import types

url = "http://bekzod7.uz/api/v1/bloglist/"

data=requests.get(url).json()
news = []

for yangilik in data:
    news.append(
        types.InlineQueryResultArticle(
            id=yangilik["id"],
            title=yangilik["title"],
            input_message_content=types.InputTextMessageContent(
                message_text=yangilik['text'][:70]
            ),
            thumb_url=yangilik['photo'],
            description=yangilik['text'][:30]
        )
    )