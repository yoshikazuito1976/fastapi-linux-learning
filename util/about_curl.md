# about curl  
― HTTP を観察・操作するための道具 ―

この教材では、API や Web 通信を **「使う」だけでなく「観察する」** ことを重視します。  
そのために `curl` を使用します。

---

## curl とは何か

`curl` は、HTTP をはじめとする通信を **コマンドラインから直接操作・確認するためのツール**です。

- Web ブラウザの代わり
- API クライアント
- 通信確認ツール

として使えます。

重要なのは、  
**curl の主目的は「通信の中身を見る・制御すること」** であり、  
ファイルダウンロード専用のツールではない、という点です。

---

## curl でできること

- HTTP リクエストを送る（GET / POST / PUT / DELETE など）
- Header を付ける・確認する
- Status Code を確認する
- Body（JSON など）を送る
- Response をそのまま確認する
- 必要であればファイルとして保存する

👉 **HTTP の Request / Response を観察する**のが得意

---
## curl で HTTP メソッドを指定する
### 基本ルール

- curl は デフォルトで GET

- それ以外は オプションで明示する
--- 
### -X オプション（HTTP メソッド指定）
```bash
curl -X POST http://localhost:8000/items
```
- -X = HTTP method を指定

- POST / PUT / PATCH / DELETE などが使える

### 代表例
|メソッド|例|
|-------|--|
|GET|	curl http://localhost:8000/items|
|POST|	curl -X POST http://localhost:8000/items|
|PUT|	curl -X PUT http://localhost:8000/items/1|
|DELETE|	curl -X DELETE http://localhost:8000/items/1|
---
### -d を使うと POST になる（重要）

curl には 少しクセがあります。
```bash
curl -d "name=apple" http://localhost:8000/items
```

この場合：

- -X POST を書いていなくても

- 自動的に POST になる

👉
-d（data）を使うと POST 扱いになる、という挙動。
---
### 教材向けの整理

- メソッドを明示したい → -X POST

- データを送る → -d
---
## `-i` オプションについて

curl はデフォルトでは Response Body だけを表示します。
HTTP の挙動を観察するため、この教材では `-i` を付けて実行します。

- `-i` は response header を表示するためのオプションです。

- `-i` は **“include”** の略です。

- `-i` =  include response headers in the output

---
### JSON を送る場合（FastAPI で一番使う）
```bash
curl -i -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"apple","price":120}'
```

### 何をしているか
|オプション	|役割|
|----------|----|
|-X POST|	POST メソッド|
|-H|	Header を指定|
|-d	|Body（JSON）を送信|

👉
HTTP Request を手で組み立てている
---
## PUT / PATCH の例
### PUT（全体更新）
```bash
curl -i -X PUT http://localhost:8000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"apple","price":150}'
```

### PATCH（一部更新）
```bash
curl -i -X PATCH http://localhost:8000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"price":150}'
```

### DELETE の例
```bash
curl -i -X DELETE http://localhost:8000/items/1
```

- Body を送らないことも多い

- Status Code（204 / 200）を観察するのがポイント

### -G（ちょっとマニアックだが整理すると良い）
```bash
curl -G http://localhost:8000/items -d "limit=10"
```

- -d を Query Parameter として使う

- 普段はあまり使わないが、存在は知っておくと良い

### curl オプション整理（POST 系まとめ）
|オプション	|意味|
|----------|----|
|-X|HTTP メソッド指定|
|-d|Body を送る（POST 扱いになる）|
|-H|Header 指定|
|-G|-d を Query にする|
|-i|Response Header 表示|
---
### FastAPI 教材での位置づけ（重要）

この教材では：

- GET：観察の基本

- POST：Body / Validation / Status Code

- PUT / PATCH：設計理解（REST）

- DELETE：Status Code（204 など）観察

👉
curl は「API を叩く道具」ではなく、
**HTTP を理解する実験装置。**

### HTTPメソッドをcurlコマンドで理解する

curl は GET だけでなく、POST / PUT / PATCH / DELETE など
すべての HTTP メソッドを扱えます。
curl を使うことで、HTTP Request を自分の手で組み立て、
API の挙動を観察できます。

---

## curl と wget の違い

`curl` と `wget` は、どちらも URL を扱えますが、目的が異なります。

| ツール | 主な目的 |
|------|--------|
| **curl** | 通信の観察・操作 |
| **wget** | ファイルの取得 |

### curl
- API テスト向き
- Header / Status Code を見るのが簡単
- 通信の確認・デバッグ向き

### wget
- ファイル取得に特化
- 再試行・再開が得意
- 大容量ファイル向き

この教材では、

- **API / HTTP の理解 → curl**
- **データ取得・教材取得 → wget**

という使い分けをします。

---

## curl でファイルを保存する理由

curl は本来、レスポンスを **標準出力（画面）に表示**します。

```bash
curl http://example.com/file.txt
```
ファイルとして保存したい場合は、
「出力先を指定する」 オプションを付けます。

## -o と -O の違い
### -o（小文字）
```bash
curl -o local.txt http://example.com/file.txt
```

o は output（出力）

保存するファイル名を 自分で指定する

👉
「この通信結果を、この名前で保存する」

### -O（大文字）
```bash
curl -O http://example.com/file.txt
```

URL の末尾の名前を使って保存する

リモート側のファイル名をそのまま使う

👉
「相手がそう呼んでいる名前で保存する」

### まとめ
|オプション|	意味|
|---------|--------|
|-o|	output を指定（自分で名前を決める）|
|-O|	remote 名で output（URL の名前を使う）|

-O は curl を wget 的に使いたいときの補助機能です。

---

### リダイレクトに注意（-L）

Web では、ダウンロード URL がリダイレクトされることがよくあります。

curl -L -O http://example.com/download


-L：リダイレクトを追従する

GitHub などでは必須なことが多い

---
### この教材での curl の位置づけ

この教材では、curl を次の目的で使います。

- Request / Response を観察する

- Status Code を確認する

- Header の変化を見る

- API の挙動を理解する

「ファイルを落とすため」ではなく、
「通信を理解するため」 の道具として扱います。

## まとめ

- curl は通信を観察・操作するツール

- ファイル保存は副次的な機能

- -o は output 指定

- -O は remote 名を使うための補助

- wget とは目的が違う

curl を使いこなすことは、
HTTP を理解する近道です。