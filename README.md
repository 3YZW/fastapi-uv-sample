# fastapi-uv-sample

Python の Web フレームワーク FastAPI の学習用リポジトリ。
公式チュートリアル（<https://fastapi.tiangolo.com/learn/>）をベースに、pip を使用している箇所を uv に置き換えて学習する。

## 1. uvで新規Pythonプロジェクトを作成

以下のコマンドを実行。

```bash
uv init
```

## 2. FastAPIのインストール

以下のコマンドを実行。

```bash
uv add fastapi
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
```
