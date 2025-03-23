from fastapi import Query, APIRouter, Body, FastAPI
import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel, Field

app = FastAPI()


hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 5, "title": "Москва", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]


@app.get("/hotels")
def get_hotels(
    hotel_id: int | None = Query(None, description="Айдишник"),
    title: str | None = Query(None, description="Название отеля"),
    page: int | None = Query(1, ge=1, description="Страница"),
    per_page: int | None = Query(3, ge=1, description="Количество отелей на странице"),
):
    global hotels
    hotels_ = []

    for hotel in hotels:
        if hotel_id is not None and hotel["id"] != hotel_id:
            continue
        if title is not None and hotel["title"] != title:
            continue
        hotels_.append(hotel)

    hotels_start = per_page * (page - 1)

    hotels_end = (
        hotels_start + per_page
        if hotels_start + per_page < len(hotels_)
        else len(hotels_)
    )
    return hotels_[hotels_start:hotels_end]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
