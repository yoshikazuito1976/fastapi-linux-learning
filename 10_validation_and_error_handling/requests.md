
# Requests (curl) - 
## 10_validation_and_error_handling

## 起動:
```bash
uvicorn main:app --reload --port 8010
```
---
## 1) Path / Query の validation を観察する
### OK
```bash
curl -s "http://127.0.0.1:8010/items/10?q=hello&limit=5" | jq
```

### NG: item_id が範囲外（ge=1）
```bash
curl -s "http://127.0.0.1:8010/items/0?q=hello&limit=5" | jq
```

### NG: q が短すぎる（min_length=2）
```bash
curl -s "http://127.0.0.1:8010/items/10?q=a&limit=5" | jq
```

### NG: limit が範囲外（le=50）
```bash
curl -s "http://127.0.0.1:8010/items/10?q=hello&limit=100" | jq
```
---
## 2) Body(JSON) の validation を観察する
### OK
```bash
curl -s -X POST "http://127.0.0.1:8010/users" \
  -H "Content-Type: application/json" \
  -d '{"username":"yito","email":"foo@example.com","password":"passw0rd!"}' | jq
```

### NG: email がpatternに合わない
```bash
curl -s -X POST "http://127.0.0.1:8010/users" \
  -H "Content-Type: application/json" \
  -d '{"username":"yito","email":"not-an-email","password":"passw0rd!"}' | jq
```

### NG: password に数字がない（独自validator）
```bash
curl -s -X POST "http://127.0.0.1:8010/users" \
  -H "Content-Type: application/json" \
  -d '{"username":"yito","email":"foo@example.com","password":"password!!"}' | jq
```

### NG: username が短い
```bash
curl -s -X POST "http://127.0.0.1:8010/users" \
  -H "Content-Type: application/json" \
  -d '{"username":"ab","email":"foo@example.com","password":"passw0rd!"}' | jq
```
---
## 3) ネストしたモデルの validation を観察する
### OK
```bash
curl -s -X POST "http://127.0.0.1:8010/orders" \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"items":[{"sku":"ABC-001","qty":2},{"sku":"XYZ-009","qty":3}]}' | jq
```

### NG: qty が 0（ge=1）
```bash
curl -s -X POST "http://127.0.0.1:8010/orders" \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"items":[{"sku":"ABC-001","qty":0}]}' | jq
```

### NG: items が空（min_length=1）
```bash
curl -s -X POST "http://127.0.0.1:8010/orders" \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"items":[]}' | jq
```

## 4) HTTPException と 500 の違い
### HTTPException（404）
```bash
curl -i "http://127.0.0.1:8010/errors/demo?kind=http"
```
---
### 想定外例外（500）
```bash
curl -i "http://127.0.0.1:8010/errors/demo?kind=crash"
```

## 補足
- validation エラーは 422 Unprocessable Entity が返る
- エラー内容は response body の detail に JSON 形式で含まれる
- loc を見ることで どの入力が原因か を特定できる
- HTTPException は 意図して返すエラー
- 500 は 想定外のエラー（バグ）



