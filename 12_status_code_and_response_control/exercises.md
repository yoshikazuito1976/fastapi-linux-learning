# Exercises: Status Code / Response / Logging を観察する

この演習では、FastAPI アプリを起動し、

- Status Code
- Response
- Access Log

の **3つがどのように連動しているか** を観察します。

この章では **logging の設定や実装は行いません**。  
ログはすでに設定されているものとして扱います。

---

## 前提条件

- `../utils/logging.conf` が存在する
- アクセスログは `logs/access.log` に出力される
- `logs/` ディレクトリは事前に作成済みである

```bash
mkdir -p logs
```
---
## 演習0：アプリケーションを起動する

```bash
uvicorn main:app \
  --reload \
  --log-config ../utils/logging.conf
```
### 確認ポイント
- エラーなく起動するか

- 起動後、logs/access.log が作成されているか

```bash
ls logs
```
--- 
## 演習1：FastAPI に任せた Response を観察する
```bash
curl -i http://localhost:8000/auto
```
### 確認ポイント
- Status Code はいくつか

- Content-Type は何か

- Body の形式はどうなっているか

### ログを確認
``` bash
tail logs/access.log
```
### 考えてみよう
- Response はどこで作られているか

- ログは誰が書いているか
--- 
## 演習2：Status Code を指定した Response を確認する
``` bash
curl -i -X POST http://localhost:8000/create
```
### 確認ポイント
- Status Code が 201 になっているか
- /auto のときと何が違うか

### ログを確認
```bash

tail logs/access.log
```
### 考えてみよう
- Status Code の違いはログにどう表れているか

- ログの出力形式は変わっているか
---
## 演習3：Response を自分で返す例を観察する
``` bash
curl -i http://localhost:8000/custom-response
```
### 確認ポイント
- Status Code はいくつか

- /auto や /create と何が違うか

### ログを確認
```bash
tail logs/access.log
```
### 考えてみよう
- Response を自分で返しても、ログの扱いは変わるか

- FastAPI と uvicorn の役割分担はどこにあるか
---
## 演習4：HTTPException によるエラーを確認する

```bash
curl -i http://localhost:8000/bad-request
```
### 確認ポイント
- Status Code は何か
- Body の detail はどこで定義されたか

### ログを確認
```bash
tail logs/access.log
```
### 考えてみよう
- エラーでもログは残るか

- 正常系と異常系でログの形式は変わるか
---
## 演習5：FastAPI が自動で返す 422 を観察する

```bash
curl -i "http://localhost:8000/items?limit=abc"
```
### 確認ポイント
- Status Code は何か

- Body にどのような情報が含まれているか

### ログを確認
```bash
tail logs/access.log
```
```bash
curl -i "http://localhost:8000/items?limit=10"
```
### 確認ポイント
- Status Code はどう変わったか

- ログの出力はどう変わったか
---
## 演習6：Response と Logging の関係を整理する
### 次の問いに答えてみましょう。

- Response が返るとは、何が起きていることか

- なぜコードに logging を書いていなくてもログが出るのか

- Status Code とログはどこで結びついているのか
---
## まとめ
この章で確認したこと：

- Response は必ず返っている

- Status Code は Response の一部である

- ログはアプリケーションの外側で記録されている

- FastAPI / uvicorn が多くの処理を自動で担っている