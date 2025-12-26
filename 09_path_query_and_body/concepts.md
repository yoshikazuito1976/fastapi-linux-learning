# Concepts: FastAPI と Pydantic

このファイルでは、  
09章で暗黙的に使われている **Pydantic** について補足する。

## Pydantic とは

Pydantic は、**データの形と型を定義し、検証するためのライブラリ**である。

FastAPI は、リクエストで受け取る値を処理する際に、
内部で Pydantic を利用している。

## FastAPI と Pydantic の関係

- FastAPI：HTTP の受け取り方を決める
- Pydantic：受け取った値が正しいかを判断する

FastAPI で型ヒントを書いた瞬間、
その検証は Pydantic に委ねられる。

## 型変換と検証

HTTP リクエストで届く値は、すべて文字列である。

Pydantic はそれを、

- 指定された型に変換し
- 変換できなければエラーと判断する

## 「省略可能かどうか」はどこで決まるか

値が必須か、省略可能かは、
関数の引数定義（型ヒント・デフォルト値）によって決まる。

これは FastAPI 独自のルールではなく、
Pydantic の振る舞いによるものである。

## この章での位置づけ

この章では、

- Pydantic を直接使いこなす
- Validation を制御する

ことは行わない。

目的は、
**「定義によって挙動が決まっている」ことを理解すること**である。

詳細な Validation や Error Handling は、
次章以降で扱う。
