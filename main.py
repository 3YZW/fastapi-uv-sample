from fastapi import FastAPI

# FastAPIインスタンスを作成
app = FastAPI()


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
    return {"skip": skip, "limit": limit}
