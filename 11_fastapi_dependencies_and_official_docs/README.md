# FastAPI Dependencies and Official Documentation

> Understanding what FastAPI does — and what it delegates

FastAPI は「高速でモダンな Web フレームワーク」として紹介されることが多いですが、
FastAPI 自身がすべての機能を実装しているわけではありません。

この章では、次の点を整理します。

- FastAPI 自身が担当している役割
- 他のライブラリに委ねている役割
- FastAPI 公式ドキュメントとの向き合い方

目的は、ライブラリ名を覚えることではなく、  
**FastAPI がどのような役割分担で成り立っているかを理解すること**です。

---

## FastAPI は「薄い」フレームワークである

FastAPI が主に担当しているのは、次のような役割です。

- HTTP リクエストの受け取り
- ルーティング
- Dependency Injection（依存性注入）
- Python オブジェクトを HTTP レスポンスへ変換
- OpenAPI ドキュメント（`/docs`）の生成

一方で、入力値の検証や実行基盤そのものは、
FastAPI の外側にあるライブラリに委ねられています。

この設計により、FastAPI は

- 構造が追いやすい
- 振る舞いを説明しやすい
- 一部の仕組みを差し替えやすい

という特徴を持っています。

---

## 主な依存ライブラリと役割分担

### Python の型アノテーション

Python の型アノテーション（`int`, `str`, `List`, `Annotated` など）は、
**「意図を宣言するための仕組み」**です。

FastAPI は型アノテーションを読み取り、

- 想定される入力の型
- Path / Query / Body の判定
- API ドキュメントの構造

を決定します。

型アノテーション自体は、**検証処理を実行しません**。

---

### Pydantic

Pydantic は、次の役割を担当しています。

- 入力値の validation（検証）
- データの変換・パース
- validation エラーの構造化

validation に失敗した場合、Pydantic が次の情報を決定します。

- `type` : エラーの種類（機械向け）
- `loc` : どこで失敗したか
- `msg` : 人間向けのエラーメッセージ
- `ctx` : 検証に使われた制約条件

FastAPI は、これらの情報を **生成していません**。  
Pydantic が生成した検証結果を受け取り、HTTP レスポンスとして返しているだけです。

---

### Starlette と Uvicorn

FastAPI は、内部的に **Starlette** の上に構築されています。

- Starlette が提供するもの
  - ASGI 対応
  - Request / Response オブジェクト
  - Middleware や Background Task

一方、**Uvicorn** は ASGI サーバとして動作し、

- アプリケーションの実行
- イベントループとの接続

を担当します。

つまり、

> FastAPI は単体では動かず、  
> ASGI サーバの上で実行されるフレームワークです。

---

### Logging（Python 標準ライブラリ）

ログ出力は、Python 標準の `logging` モジュールが担当します。

FastAPI はログの形式や出力先をほとんど定義しません。
そのため、

- `logging.conf`
- `dictConfig`
- Uvicorn のログ設定

などを使って、アプリケーションとは独立してログ設計を行います。

---

## なぜこの役割分担が重要なのか

依存ライブラリの役割を理解すると、次のことが分かるようになります。

- validation エラーの原因を正しく追える
- どこを修正すれば挙動が変わるか判断できる
- FastAPI に責任がない問題を切り分けられる

FastAPI を理解するとは、
**FastAPI が「何をしていないか」を理解すること**でもあります。

---

## FastAPI 公式ドキュメントについて

FastAPI の公式ドキュメントは情報量が多く、
最初からすべてを読む必要はありません。

このリポジトリは、公式ドキュメントの代替ではなく、

- 挙動の観察
- 構造の理解
- 読みどころの整理

を目的とした **補助教材**です。

疑問が生じたときは、
公式ドキュメントに戻って確認することを前提としています。

### 参考になる公式ページ（例）

- Tutorial / First Steps  
- Path Parameters / Query Parameters  
- Request Body  
- Validation  
- Handling Errors  

---

## この章の位置づけ

ここまでの章では、

- HTTP の流れを観察し
- Request / Response を理解し
- validation エラーの構造を確認してきました

この章は、それらを **構造的に整理するための中継点**です。

以降の章では、制御・構成・運用といった観点に進んでいきます。

---

## Summary

- FastAPI は意図的に「薄い」フレームワークである
- validation は Pydantic が担当している
- 型アノテーションは意図の宣言である
- 公式ドキュメントは仕様の一次情報
- この教材は公式を読むためのガイドである

FastAPI を理解することは、
そのエコシステムを理解することでもあります。

## Official Documentation Links

FastAPI は複数のライブラリによって構成されています。
ここでは、それぞれの **公式ドキュメントへの入口** を示します。

本リポジトリの各章で理解した内容を、
公式ドキュメントで確認・補強するための対応表です。

---

### FastAPI (Main Framework)

FastAPI の公式ドキュメントです。
API 設計・Request / Response・Dependency Injection などの仕様がまとめられています。

- https://fastapi.tiangolo.com/

特に参考になるページ：

- First Steps  
  https://fastapi.tiangolo.com/tutorial/first-steps/  
  → 本リポジトリ: 03〜06章

- Request Body  
  https://fastapi.tiangolo.com/tutorial/body/  
  → 本リポジトリ: 09章

- Path & Query Parameters  
  https://fastapi.tiangolo.com/tutorial/path-params/  
  https://fastapi.tiangolo.com/tutorial/query-params/  
  → 本リポジトリ: 09章

- Handling Errors  
  https://fastapi.tiangolo.com/tutorial/handling-errors/  
  → 本リポジトリ: 10章

---

### Pydantic (Validation and Data Models)

Pydantic は validation とデータモデルを担当します。
`type`, `loc`, `msg`, `ctx` などのエラー構造は、Pydantic によって定義されています。

- https://docs.pydantic.dev/

特に参考になるページ：

- Validation Errors  
  https://docs.pydantic.dev/latest/errors/  
  → 本リポジトリ: 10章

- Models  
  https://docs.pydantic.dev/latest/concepts/models/  
  → Request Body / ネストしたモデルの理解に対応

---

### Starlette (ASGI and Request/Response)

FastAPI は Starlette の上に構築されています。
Request / Response オブジェクトや Middleware の実装は Starlette に由来します。

- https://www.starlette.io/

参考ページ：

- Requests  
  https://www.starlette.io/requests/  
  → 本リポジトリ: 07章

- Responses  
  https://www.starlette.io/responses/  
  → 本リポジトリ: 07章

---

### Uvicorn (ASGI Server)

Uvicorn は FastAPI を実行する ASGI サーバです。
起動方法やログ設定は Uvicorn の仕様に依存します。

- https://www.uvicorn.org/

参考ページ：

- Settings and CLI  
  https://www.uvicorn.org/settings/  
  → 本リポジトリ: 02章 / logging設定

---

### Python Standard Library (typing / logging)

FastAPI は Python 標準機能を積極的に利用しています。

- typing  
  https://docs.python.org/3/library/typing.html  
  → 型アノテーションの仕様

- logging  
  https://docs.python.org/3/library/logging.html  
  → 本リポジトリ: logging章

---

## How to Use These Links

- 本リポジトリで **挙動を観察する**
- 疑問が生じたら **公式ドキュメントで仕様を確認する**
- 公式を「全部読む」必要はない

この教材は、公式ドキュメントを読むための **補助線** です。

