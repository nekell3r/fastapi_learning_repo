from fastapi import FastAPI, Query, Body
import uvicorn

app = FastAPI()

hotels = [
    {"id": 1, "title": "Sochi", "name" : "sochi"},
    {"id": 2, "title": "Dubai", "name" : "dubai"},
    {"id": 3, "title": "wrong_title", "name": "wrong_name"}
]

@app.get("/hotels")
def get_hotels():
    return hotels
@app.put("/hotels/{hotel_id}")
def reload_hotel(
        hotel_id: int,
        title: str = Body(embed=True),
        name: str = Body(embed=True),
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = title
            hotel["name"] = name
            break
    return {"status": "OK"}

@app.patch("/hotels/{hotel_id}")
def update_hotel(
        hotel_id : int,
        title: str | None = Body(embed=True),
        name: str | None = Body(embed=True)
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if title and title != hotel["title"]:
                hotel["title"] = title
            if name and name != hotel["name"]:
                hotel["name"] = name
            break

if __name__ == "__main__":
     uvicorn.run("main:app", reload=True)