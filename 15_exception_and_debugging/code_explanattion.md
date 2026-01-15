# Code Explanation – Exception and Debugging

このドキュメントでは、[main.py](main.py) に書かれているコードを上から順に読み解き、FastAPI における例外とデバッグの考え方を整理します。

## 1. import 文

```python
from fastapi import FastAPI, HTTPException
import logging
```

- **FastAPI** → アプリケーション本体
- **HTTPException** → HTTP レスポンスとして返すための例外
- **logging** → アプリケーション内部の状態を記録する仕組み

## 2. Logging の設定

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s : %(message)s"
)

logger = logging.getLogger(__name__)
```

### ここで行っていること

- ログのレベルを INFO に設定
- 出力形式を指定
- このファイル用の logger を作成

### 重要な考え方

- ログは「内部向け」
- ユーザーに返すものではない
- 後から振る舞いを説明するための材料

## 3. FastAPI アプリケーションの作成

```python
app = FastAPI()
```

- FastAPI アプリケーションを生成
- 以降、この `app` にエンドポイントを登録していく

## 4. ルートエンドポイント `/`

```python
@app.get("/")
def root():
    logger.info("root endpoint called")
    return {"message": "Exception and Debugging chapter"}
```

### ポイント

- リクエストを受け取ったことをログに残す
- 正常な JSON レスポンスを返す
- 例外は発生しない

## 5. 正常系のエンドポイント `/add`

```python
@app.get("/add")
def add(a: int, b: int):
    logger.info("add called: a=%s, b=%s", a, b)
    return {"result": a + b}
```

### ここで確認したいこと

- クエリパラメータ `a`, `b` が自動的に `int` に変換される
- FastAPI が**入力チェック**を行っている
- 正常な場合は例外は不要

## 6. 明示的に例外を発生させる `/divide`

```python
@app.get("/divide")
def divide(a: int, b: int):
    logger.info("divide called: a=%s, b=%s", a, b)

    if b == 0:
        logger.error("division by zero attempted")
        raise HTTPException(
            status_code=400,
            detail="division by zero is not allowed"
        )

    return {"result": a / b}
```

### ここが重要

- `raise HTTPException` により例外を発生させている
- FastAPI がこれを HTTP レスポンスに変換する
- クライアントには JSON エラーが返る

### 考え方

- これは**設計されたエラー**
- 想定内の異常を、明示的に扱っている

## 7. 想定外の例外が起きる `/crash`

```python
@app.get("/crash")
def crash():
    logger.info("crash endpoint called")
    return {"result": 1 / 0}
```

### 何が起きるか

- `ZeroDivisionError` が発生
- FastAPI が捕捉できない例外
- デバッグモードではスタックトレースが表示される

### 教材としての狙い

- すべての例外が `HTTPException` ではない
- 想定外のエラーはまず「観察」する

## 8. 例外とログの役割分担

| 役割           | 使うもの           |
|----------------|-------------------|
| 内部の記録     | Logging           |
| 外部への通知   | HTTPException     |
| 原因の追跡     | スタックトレース   |

## 9. デバッグ時の読み方

- 画面のエラー表示よりも**ターミナルのログ**
- スタックトレースは**下から読む**
- 「どこで失敗したか」を特定する

## 10. この章のまとめ

- 例外は失敗ではない
- ログと例外は役割が違う
- 説明できる状態にすることが重要