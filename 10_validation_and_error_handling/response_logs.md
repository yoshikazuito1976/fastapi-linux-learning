# レスポンスログ（curl + tee）

このファイルでは、第10章で実行した `curl` コマンドの  
**レスポンス本文（JSON）をログとして保存する方法**を示します。

ここで扱うログは、  
**サーバー側の access.log とは異なる「観察用ログ」**です。

---

## ログ保存用ディレクトリ

```bash
mkdir -p logs
```
---  
## 正常系レスポンスを保存する
```bash
curl -s "http://127.0.0.1:8010/items/10?q=hello&limit=5" \
  | tee -a logs/curl_response.log
```

- 画面に表示しつつ
- logs/curl_response.log に追記されます
---

## JSON を整形して保存する
### Python を使う場合
```bash
curl -s "http://127.0.0.1:8010/items/10?q=hello&limit=5" \
  | python -m json.tool \
  | tee -a logs/curl_response.log
```

### jq を使う場合（インストール済みなら）
```bash
curl -s "http://127.0.0.1:8010/items/10?q=hello&limit=5" \
  | jq \
  | tee -a logs/curl_response.log
```
---
## バリデーションエラー（422）を保存する
```bash
curl -s "http://127.0.0.1:8010/items/0?q=a&limit=100" \
  | python -m json.tool \
  | tee -a logs/curl_response.log
```
--- 
## なぜ tee を使うのか

- access.log
→ サーバー視点（URL / status / 時刻）

- curl + tee
→ 学習者視点（実際に返ってきた JSON）

本章では
**「API が何を返したかを観察し、あとから振り返れる形で残す」**
ことを目的としています。
---
## この章におけるログの整理
|ログ                  |目的                 |            
|----------------------|--------------------|
|uvicorn / access log  |サーバーの動作確認    |
|logs/curl_response.log|レスポンス観察・学習用|

---
## メモ
- レスポンスログには個人情報を含めないこと
- 本番環境では、レスポンス本文を無制限に保存しないこと