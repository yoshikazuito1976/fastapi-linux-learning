# FastAPI × Linux Learning Log

このリポジトリは、**FastAPI を Linux 環境で学ぶための学習ログ兼、教材化の原型**です。  
フレームワークの使い方だけでなく、**OS・プロセス・ネットワーク視点**から  
「FastAPI がどのように動いているのか」を理解することを目的としています。

---

## このリポジトリの位置づけ

- 個人的な学習ログ（草を生やす 🌱）
- 将来的な教材化・Notion再編集の一次情報
- FastAPI / ASGI / uvicorn の理解を深めるための実験場

> 内容は随時更新・修正されます。  
> 完成されたチュートリアルではありません。

---

## 学習方針

本シリーズでは、以下の方針を重視します。

- **Linux 前提**
  - Manjaro / Debian / VM / コンテナ環境
  - Windows ネイティブ環境は扱わない
- **最小構成から始める**
  - いきなり nginx / systemd / EC2 に行かない
- **OS視点で観察する**
  - プロセス（ps, pstree）
  - ポート（ss）
  - 実行主体は誰か？
- **Why を README に残す**
  - なぜそうなるのか
  - なぜ別の選択肢ではないのか

---

## 学習のゴール

- FastAPI が **単体では動かない**ことを説明できる
- uvicorn が **何者で、何をしているのか**説明できる
- 「EC2 にしたら何が増えるだけなのか」を言語化できる
- Apache / nginx / uvicorn の役割の違いを整理できる

---

## 構成（予定）

```text
## 章立て案（2025-12-26時点 / repo現状に合わせて更新）

### 前提（すでにmainに存在）
- 01_environment
- 02_uvicorn_basics
- 03_FastAPI_Basics
- 04_endpoint_Concepts
- 05_endpoint_Basics
- 06_post_Method_and_Tools
- 07_request_response
- 08_http_methods_overview
- 09_path_query_and_body

### 10以降（予定）
- 10_validation_and_error_handling
- 11_status_code_and_response_control
- 12_response_header_and_cookie
- 13_logging_and_application_log
- 14_exception_and_debugging
- 15_application_structure
- 16_dependency_injection_basics
- 17_security_basics
- 18_external_api_request
- 19_runtime_and_process
- 20_simple_deployment
- 99_summary_and_next_steps

※ 旧案の「08_path_query_and_body」は現状「09_path_query_and_body」として運用する。

