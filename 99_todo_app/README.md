# 15. Todo API アプリケーション

FastAPIを使った完全なTodo管理アプリケーション

## 概要

このプロジェクトは、FastAPIを使用したRESTful Todo APIです。基本的なCRUD操作（作成、読み取り、更新、削除）を実装しています。

## 機能

### エンドポイント

| メソッド | エンドポイント | 説明 |
|---------|--------------|------|
| GET | `/` | API情報を取得 |
| POST | `/todos` | 新しいTodoを作成 |
| GET | `/todos` | 全てのTodoを取得（フィルタリング・ページネーション対応） |
| GET | `/todos/{todo_id}` | 特定のTodoを取得 |
| PUT | `/todos/{todo_id}` | Todoを更新 |
| DELETE | `/todos/{todo_id}` | Todoを削除 |
| GET | `/todos/stats/summary` | Todo統計情報を取得 |

### Todoデータモデル

```json
{
  "id": 1,
  "title": "FastAPIを学ぶ",
  "description": "FastAPIのドキュメントを読む",
  "completed": false,
  "created_at": "2026-01-14T12:00:00",
  "updated_at": "2026-01-14T12:00:00"
}
```

## セットアップと実行

### 1. 仮想環境をアクティベート

```bash
source ../fastapi-env/bin/activate
```

### 2. アプリケーションを起動

```bash
uvicorn main:app --reload
```

### 3. APIドキュメントにアクセス

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 使用例

### 1. Todoを作成

```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "FastAPIを学ぶ",
    "description": "基本的なエンドポイントを実装する",
    "completed": false
  }'
```

### 2. 全てのTodoを取得

```bash
curl "http://localhost:8000/todos"
```

### 3. 特定のTodoを取得

```bash
curl "http://localhost:8000/todos/1"
```

### 4. Todoを更新

```bash
curl -X PUT "http://localhost:8000/todos/1" \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true
  }'
```

### 5. Todoを削除

```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

### 6. フィルタリングとページネーション

```bash
# 完了済みのTodoのみ取得
curl "http://localhost:8000/todos?completed=true"

# 最初の10件をスキップして、次の5件を取得
curl "http://localhost:8000/todos?skip=10&limit=5"
```

### 7. 統計情報を取得

```bash
curl "http://localhost:8000/todos/stats/summary"
```

## 学習ポイント

### 1. Pydanticモデル
- `TodoBase`: 基本的なTodoフィールド
- `TodoCreate`: Todo作成用（入力バリデーション）
- `TodoUpdate`: Todo更新用（部分更新対応）
- `Todo`: レスポンス用（IDとタイムスタンプを含む）

### 2. HTTPメソッド
- `POST`: リソースの作成
- `GET`: リソースの取得
- `PUT`: リソースの更新
- `DELETE`: リソースの削除

### 3. ステータスコード
- `201 Created`: リソースの作成成功
- `200 OK`: リクエスト成功
- `204 No Content`: 削除成功（レスポンスボディなし）
- `404 Not Found`: リソースが見つからない

### 4. クエリパラメータ
- フィルタリング（`completed`）
- ページネーション（`skip`, `limit`）

### 5. パスパラメータ
- `{todo_id}`: URLからIDを取得

### 6. エラーハンドリング
- `HTTPException`を使用した適切なエラーレスポンス

### 7. バリデーション
- Pydanticの`Field`を使った入力検証
- `min_length`, `max_length`などの制約

## データの永続化について

現在の実装では、データはメモリ上（`todos_db`リスト）に保存されています。アプリケーションを再起動すると、データは失われます。

### 今後の改善案
- SQLiteやPostgreSQLなどのデータベースを使用
- SQLAlchemyやTortoiseORMなどのORMを統合
- ファイルベースの永続化（JSON、Pickle）

## トラブルシューティング

### ポートが既に使用されている場合

```bash
# 別のポートで起動
uvicorn main:app --reload --port 8001
```

### 仮想環境が有効か確認

```bash
which python
# /home/aisyu/work/fastapi-linux-learning/fastapi-env/bin/python と表示されるはず
```

## 関連ファイル

- [main.py](main.py) - メインアプリケーションコード
- [README.md](README.md) - このファイル

## 参考リンク

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/)
- [Pydantic公式ドキュメント](https://docs.pydantic.dev/)
- [REST API設計のベストプラクティス](https://restfulapi.net/)
