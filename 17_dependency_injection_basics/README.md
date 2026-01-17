# 17 Dependency Injection Basics

この章では、FastAPI における Dependency Injection（依存性注入 / DI）の基本概念を学びます。

DI は「少し難しそう」に見えますが、FastAPI では自然な書き方の延長として導入されています。

ここでは**仕組みを理解すること**を目的とし、複雑な設計やパターンの話には踏み込みません。

## この章でやること

- Dependency Injection（DI）の考え方を理解する
- FastAPI の `Depends` の役割を知る
- 「値を直接書く」コードとの違いを体感する
- なぜ DI がアプリケーション構造と相性がよいのかを理解する

## Dependency Injection とは？

Dependency Injection（依存性注入）とは、

> 関数やクラスが必要とするものを、自分で作らず、外から渡してもらう仕組み

のことです。

### 依存しているとは？

たとえば次のような関数があったとします。

```python
def read_items():
    user = get_current_user()
    return {"user": user}
```

この関数は、`get_current_user()` に**依存しています**。

疑問点：

- どこで定義されているか？
- テストのときに差し替えられるか？
- ログイン方式が変わったらどうするか？

こうした問題を整理するために使われるのが DI です。

## FastAPI における DI

FastAPI では、DI を `Depends` という仕組みで実現します。

```python
from fastapi import Depends

def get_current_user():
    return "ito"

@app.get("/items")
def read_items(user: str = Depends(get_current_user)):
    return {"user": user}
```

### ポイント

- `Depends()` に関数を渡す
- FastAPI が**自動でその関数を実行**
- 戻り値を引数として受け取れる
- 「関数を呼んでいる」のではない

### ここで重要な点

`Depends(get_current_user)` は、

`get_current_user()` を**自分で呼んでいるわけではなく**、
FastAPI が**必要なタイミングで呼び出している**

という点です。

つまり、

- いつ
- 何回
- どのリクエストに対して

呼ばれるかは FastAPI が管理します。

## なぜ DI を使うのか？

DI を使う理由は、大きく分けて次の3つです。

### 1. 責務を分離できる

- **エンドポイント**：HTTP の処理
- **依存関数**：認証、DB接続、設定取得など

役割が分かれ、コードが読みやすくなります。

### 2. テストしやすくなる

依存関数は**差し替え可能**です。

- 本番用の DB
- テスト用の DB
- ダミーのユーザー

などを簡単に切り替えられます。

### 3. アプリケーション構造と相性が良い

16章で学んだ

- `routers`
- `services`
- `dependencies`

といった構成は、DI を前提にすると**自然に意味を持ちます**。

## この章の位置づけ

この章は、

- DI を**使いこなす**
- **設計パターンを覚える**

ことが目的ではありません。

目的はただ一つです。

> FastAPI が「なぜこういう書き方になっているのか」を理解する

## 次に進むと…

この章を理解すると、

- 認証処理
- DB セッション管理
- 設定値の共有
- ミドルウェアとの関係

といった話が、「急に難しくならず」につながっていきます。

## 補足

- DI は Python 固有のものではありません
- 他のフレームワーク（Java, C#, Go）でも広く使われています
- FastAPI の DI は**かなり分かりやすい部類**です
