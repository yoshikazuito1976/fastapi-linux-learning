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

## Chapter Structure

このリポジトリは、FastAPI を「書き方」ではなく  
**HTTP と Web アプリケーションの振る舞いを観察する**ことを目的に、  
段階的な章構成で整理しています。

### 基礎・準備
- 01_environment  
- 02_uvicorn_basics  

### FastAPI の基本構造
- 03_FastAPI_Basics  
- 04_endpoint_Concepts  
- 05_endpoint_Basics  
- 06_post_Method_and_Tools  

### HTTP Request / Response の理解
- 07_request_response  
- 08_http_methods_overview  
- 09_path_query_and_body  

### 入力検証とレスポンス制御（予定）
- 10_validation_and_error_handling  
- 11_status_code_and_response_control  
- 12_response_header_and_cookie  

### ログ・例外・デバッグ（予定）
- 13_logging_and_application_log  
- 14_exception_and_debugging  

### アプリケーション設計と運用（予定）
- 15_application_structure  
- 16_dependency_injection_basics  
- 17_security_basics  
- 18_external_api_request  
- 19_runtime_and_process  
- 20_simple_deployment  

### まとめ
- 99_summary_and_next_steps  

※ 各章は README / main.py / requests.md などを組み合わせて構成されます。

---

## License

This repository is licensed under the MIT License.

© 2026 Yoshikazu Ito

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

(The rest of the MIT License text)

This repository is provided primarily for educational purposes.
Students are encouraged to read, modify, and reuse the code as part of their learning.



