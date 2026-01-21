# 18_security_basics

この章では、FastAPI における **セキュリティの基本的な考え方** を学びます。

ここで扱う「セキュリティ」は、  
**本番レベルの堅牢な実装** ではなく、

> FastAPI では  
> セキュリティがどのような構造で実現されているのか  

を理解することを目的としています。

---

## この章のゴール

この章を終えた時点で、次のことができるようになることを目標とします。

- 認証（Authentication）と認可（Authorization）の違いを説明できる
- FastAPI で「認証チェック」が **関数として実装されている** ことを理解する
- `Depends()` を使ったシンプルな認証処理を書ける
- 「セキュリティは DI と強く結びついている」ことを説明できる

---

## セキュリティの基本用語

### 認証（Authentication）

- 「あなたは誰ですか？」を確認すること
- 例：
  - トークン
  - ユーザー名とパスワード
  - APIキー

### 認可（Authorization）

- 「あなたは何をしていいですか？」を確認すること
- 例：
  - 管理者だけがアクセスできるAPI
  - 一般ユーザーは閲覧のみ可能

👉 この章では **主に認証のみ** を扱います。

---

## FastAPI におけるセキュリティの考え方

FastAPI では、セキュリティは特別な仕組みではありません。

基本は次の考え方です。

- リクエストの前に「チェック用の関数」を実行する
- 問題があれば例外を発生させる
- 問題がなければ、そのまま処理を続行する
- このチェック関数を `Depends()` で注入する

つまり、

> **セキュリティ = 依存性注入（DI）された関数**

です。

---

## シンプルな認証の例（ヘッダチェック）

ここでは、HTTPヘッダに含まれるトークンを使った  
**最小構成の疑似認証** を実装します。

### サンプルコード

```python
from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def verify_token(x_token: str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    return x_token

@app.get("/secure")
def secure_endpoint(token: str = Depends(verify_token)):
    return {"message": "You are authenticated"}
```

### このコードで起きていること

#### 1. `verify_token` は普通の関数

- 特別なクラスではない
- 普通の Python 関数

#### 2. ヘッダを自動で受け取っている

```python
x_token: str = Header(...)
```

- リクエストヘッダ `X-Token` を受け取る
- 無ければエラーになる

#### 3. 条件に合わなければ 401 を返す

```python
raise HTTPException(status_code=401)
```

- この時点で処理は終了
- エンドポイント関数は実行されない

#### 4. `Depends()` によって前処理として実行される

```python
token: str = Depends(verify_token)
```

- エンドポイントの前に `verify_token` が実行される
- これが「セキュリティ層」になる

---

## なぜ DI と相性がいいのか

認証処理を関数として切り出しているため、

- **再利用できる**
- **差し替えられる**
- **テストしやすい**

```python
# 今回
def verify_token(...):
    ...

# 将来
def verify_jwt(...):
    ...

# さらに将来
def verify_oauth(...):
    ...
```

👉 **エンドポイントのコードを変えずに、セキュリティだけを入れ替えられる**

これが FastAPI の大きな強みです。

---

## ⚠️ 注意：この実装は本番向けではありません

今回のコードは、

- **学習用**
- **構造理解用**

です。

実際の開発現場では、

- **JWT**
- **OAuth2**
- **外部IDプロバイダ**
- **環境変数による秘密情報管理**

などが使われます。

ただし、

> **「Depends で注入する関数として認証を実装する」**

という構造は同じです。

---

## まとめ

- セキュリティは「特別な魔法」ではない
- FastAPI では **関数 + Depends** で実現されている
- 今日は「強さ」より「構造理解」を重視する
- DI の理解が、そのままセキュリティ理解につながる
