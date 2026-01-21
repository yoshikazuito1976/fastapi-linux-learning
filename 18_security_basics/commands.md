# commands.md（18_security_basics 動作確認用）

この章では `X-Token` ヘッダを使った「超シンプル認証」を実装しています。  
ここでは **動作確認のための curl コマンド集** と **何が起きているかの解説** をまとめます。

> 重要：
> - **ヘッダ必須** にしている実装だと、ヘッダ未指定時は **401 ではなく 422** になります（FastAPIの入力検証で止まるため）。
> - **ヘッダ未指定を 401 にしたい** 場合は、`X-Token` を Optional にして自前で 401 を返す実装にします。

---

## 0. 起動

### uvicorn で起動

```bash
uvicorn main:app --reload
```

`--reload` は開発用。ファイル変更があると自動で再起動します。

---

## 1. ヘルスチェック（/）

```bash
curl -i http://127.0.0.1:8000/
```

### 期待する結果

```
HTTP/1.1 200 OK
```

JSON で `status: ok` などが返る

### 何を確認している？

- サーバが起動していること
- ルーティング（`/`）が正しく登録されていること

---

## 2. 認証が必要なエンドポイント（/secure）

この `/secure` は `X-Token` ヘッダが必要な想定です。

### 2-A. ヘッダ無しでアクセス

```bash
curl -i http://127.0.0.1:8000/secure
```

#### 結果パターン1：422 Unprocessable Entity

（`X-Token` を「必須」として宣言している実装の場合）

```
HTTP/1.1 422 Unprocessable Entity
```

body に `"detail": [...]` 形式の validation error が入る

**なぜ 422？**

FastAPI は、`Header(...)` のように **必須入力** として宣言された値が不足している場合、エンドポイントに到達する前に **入力検証（validation）で止める** ためです。

この段階では「認証の成否」以前に「必要な入力が欠けている」扱い。

#### 結果パターン2：401 Unauthorized

（`X-Token` を Optional にして、ヘッダ無しを自前で 401 にしている実装の場合）

```
HTTP/1.1 401 Unauthorized
```

`{"detail":"Missing X-Token"}` のような body

**なぜ 401？**

ヘッダを Optional 扱いにして、認証関数の中で「無いなら 401」を返しているためです。

---

### 2-B. 間違ったトークンでアクセス（401になる）

```bash
curl -i -H "X-Token: wrong-token" http://127.0.0.1:8000/secure
```

#### 期待する結果

```
HTTP/1.1 401 Unauthorized
```

`{"detail":"Invalid token"}` のような body

#### 何を確認している？

- `Depends(verify_token)` が先に実行されること
- 条件が合わない場合に 401 で止まること

---

### 2-C. 正しいトークンでアクセス（200になる）

```bash
curl -i -H "X-Token: secret-token" http://127.0.0.1:8000/secure
```

#### 期待する結果

```
HTTP/1.1 200 OK
```

`{"message":"You are authenticated", ...}` のような body

#### 何を確認している？

- 認証（verify）が通るとエンドポイント処理が実行されること
- `verify_token` の戻り値が `Depends` 経由で受け取れること

---

## 3. 追加：レスポンスボディだけ確認したい場合

### ボディだけ表示（ステータス行やヘッダを省略）

```bash
curl http://127.0.0.1:8000/secure -H "X-Token: secret-token"
```

### JSONを見やすく整形（jq がある場合）

```bash
curl -s http://127.0.0.1:8000/secure -H "X-Token: secret-token" | jq .
```

---

## 4. 追加：ステータスコードだけ取りたい場合

```bash
curl -o /dev/null -s -w "%{http_code}\n" http://127.0.0.1:8000/secure
```

出力例：`422` や `401` や `200`

### 何に便利？

- CI や自動テストの「疎通確認」
- 「返ってくるコード」だけを確認したいとき

---

## 5. まとめ（422 と 401 の違い）

- **422**：必要な入力が不足している（FastAPI の validation で止まる）
- **401**：入力は揃っているが、認証に失敗している（認証関数で止める）

学習では、どちらの設計もあり得ます。
教材としては、

- 「ヘッダが無い → 401」にしたいなら Optional + 自前 401

- 「入力不足は validation の責務」と割り切るなら 422

という選択になります。