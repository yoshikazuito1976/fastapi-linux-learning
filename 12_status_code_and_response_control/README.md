# 12 Status Code and Response Control を観察する

この章では、FastAPI が **どのような HTTP Status Code と Response を返しているのか**を観察し、  
それを **自分で制御できるようになること**を目的とします。

これまでの章では、

- エンドポイントを作る
- パラメータを受け取る
- バリデーションやエラーを扱う

といった「APIを動かす」ことを中心に学んできました。

この章では一段階進んで、  
**「そのレスポンスは、クライアントにとってどんな意味を持つのか」**  
を意識します。

---

## この章のゴール

この章を終えたら、次のことができるようになることを目指します。

- HTTP Status Code の役割を説明できる
- FastAPI で status code を明示的に指定できる
- Response を自分で返す意味を理解できる
- 成功と失敗をコードで表現できる

---

## なぜ Status Code を意識するのか

FastAPI は、何も指定しなくても **200 OK** を返してくれます。

これはとても便利ですが、  
同時に **「考えなくても動いてしまう」** という落とし穴でもあります。

API は画面ではなく、**クライアントとの契約**です。

- 正常に処理されたのか
- データが作成されたのか
- 入力が間違っているのか

これらは **HTTP Status Code によって伝えられます**。

この章では、
> 「とりあえず 200 を返す API」  
から  
> 「意味のある Response を返す API」

へ進みます。

---

## この章で扱う内容

- HTTP Status Code の基本的な分類
- FastAPI で status code を指定する方法
- Response を直接返す方法
- HTTPException を使ったエラー表現
- curl を使った Response の観察

---

## この章の構成

12_status_code_and_response_control/
├─ README.md
├─ concepts.md
├─ main.py
└─ exercises.md


**concepts.md**  
  Status Code と Response に関する概念整理
**main.py**  
  最小構成のサンプル API
**exercises.md**  
  curl を使った観察と簡単な演習

---

## 学習の進め方（おすすめ）

1. `main.py` を起動する
2. curl でエンドポイントを叩く
3. Status Code と Response を確認する
4. `concepts.md` で整理する
5. 余裕があれば `exercises.md` に挑戦する

---

## 次の章とのつながり

この章で学ぶ **Response 制御**は、次の章以降の土台になります。

- 13章：Response Header / Cookie
- 14章：Logging / Application Log
- 15章：Exception と Debugging

**Response を自分で作る感覚**を持っていないと、  
これらの章は理解しづらくなります。

この章は、後半の章に進むための重要なステップです。

---

まずは「Status Code を見る」ことから始めましょう。
