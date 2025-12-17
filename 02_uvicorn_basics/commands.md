# 02 uvicorn Basics – Command Log

このファイルでは、uvicorn の起動と挙動確認に関して、
実際に実行したコマンドと、その結果の要点を記録します。

詳細な生ログは `logs/` ディレクトリに保存しています。

## Python / uvicorn の実体確認
```bash
which python
which uvicorn
```
```
/home/siwuser/work/fastapi-linux-learning/fastapi-env/bin/python
/home/siwuser/work/fastapi-linux-learning/fastapi-env/bin/uvicorn
```

確認事項：
- uvicorn は仮想環境配下の Python から実行されています。
- system Python ではなく、プロジェクト専用環境が使われています。

## uvicorn プロセスの確認
```bash
ps aux | grep uvicorn

siwuser 2889 ... python3 ... uvicorn app:app
```
確認事項：
- uvicorn は Linux のプロセスとして起動しています。
- 実体は Python プロセスであり、FastAPI 自体はプロセスではありません。

## uvicorn の起動
```bash

uvicorn app:app --log-level info
```
uvicorn の起動ログ（抜粋）
```
INFO:     Started server process [3174]
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000

** HTTP リクエストの確認 **
INFO: 127.0.0.1 - "GET / HTTP/1.1" 200 OK
INFO: 127.0.0.1 - "GET /favicon.ico HTTP/1.1" 200 OK
```
確認事項：
- ブラウザからの HTTP リクエストが uvicorn に届いています。
- uvicorn が Web サーバとして振る舞っていることが分かります。

-----
ログの保存場所について
操作ログ：logs/commands.log
サーバログ：logs/uvicorn.log

commands.md には概要のみを記載し、
詳細なログは logs ディレクトリを参照します。



