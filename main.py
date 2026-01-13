from fastapi import FastAPI

# FastAPIインスタンスを作成
app = FastAPI()

fake_items_db = [{
    "item_name": "Foo"
}, {
    "item_name": "Bar"
}, {
    "item_name": "Baz"
}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


# パスパラメータ
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# クエリパラメータ
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # return {"skip": skip, "limit": limit}
    return fake_items_db[skip: skip + limit]
