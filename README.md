# fastapi-uv-sample

Python の Web フレームワーク FastAPI の学習用リポジトリ。
公式チュートリアル（<https://fastapi.tiangolo.com/learn/>）をベースに、pip を使用している箇所を uv に置き換えて学習する。

## 1. uv で新規Pythonプロジェクトを作成

以下のコマンドを実行。

```bash
uv init
```

## 2. FastAPI と Uvicorn のインストール

FastAPI と ASGI サーバーである Uvicorn を uv で追加。

```bash
uv add fastapi
uv add "uvicorn[standard]"
```

実行結果

```text
Using CPython 3.9.6
Creating virtual environment at: .venv
Resolved 13 packages in 365ms
Prepared 10 packages in 223ms
Installed 11 packages in 26ms
 + annotated-doc==0.0.4
 + annotated-types==0.7.0
 + anyio==4.12.1
 + exceptiongroup==1.3.1
 + fastapi==0.128.0
 + idna==3.11
 + pydantic==2.12.5
 + pydantic-core==2.41.5
 + starlette==0.49.3
 + typing-extensions==4.15.0
 + typing-inspection==0.4.2
Resolved 26 packages in 308ms
Prepared 9 packages in 135ms
Installed 9 packages in 20ms
 + click==8.1.8
 + h11==0.16.0
 + httptools==0.7.1
 + python-dotenv==1.2.1
 + pyyaml==6.0.3
 + uvicorn==0.39.0
 + uvloop==0.22.1
 + watchfiles==1.1.1
 + websockets==15.0.1
```

## 3. サーバー起動

main.pyを公式チュートリアルの通りに編集し、以下のコマンドでアプリケーションを起動。

```bash
uv run uvicorn main:app --reload
```

ブラウザで <http://127.0.0.1:8000> にアクセスすると、JSON レスポンスが返る。

実行結果

```text
INFO:     Will watch for changes in these directories: ['/Users/nt-m/fastapi-uv-sample']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [10206] using WatchFiles
INFO:     Started server process [10211]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:54615 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:54615 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:54616 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:54616 - "GET /openapi.json HTTP/1.1" 200 OK
```
