from fastapi import FastAPI

# FastAPIインスタンスを作成
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# パスパラメータ
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
