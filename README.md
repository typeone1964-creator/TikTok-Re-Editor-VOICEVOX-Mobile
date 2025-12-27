---
title: TikTok Re-Editor VOICEVOX Mobile
emoji: 🎬
colorFrom: blue
colorTo: pink
sdk: streamlit
sdk_version: 1.31.0
app_file: app.py
pinned: false
---

# 🎬 TikTok Re-Editor VOICEVOX Mobile

動画やテキストファイルから「文字起こし → 整形 → 音声合成」を自動実行するアプリ。

---

## 🤔 どっちを使う？（初心者向けガイド）

### 📱 スマホ・タブレットで使いたい → **簡単版（ブラウザ版）**

**おすすめ度**: ⭐⭐⭐⭐ (初心者向け)

- ✅ ダウンロード不要
- ✅ インストール不要
- ✅ ブラウザで開くだけ
- ⚠️ 1日の使用制限あり

**👉 [こちらをクリック](https://huggingface.co/spaces/typeone1964/tiktok-re-editor-voicevox-mobile)**

---

### 💻 PCで本格的に使いたい → **PC版（ダウンロード版）**

**おすすめ度**: ⭐⭐⭐⭐⭐ (PCユーザー向け)

- ✅ 無制限・無料
- ✅ 高速・安定
- ⚠️ ダウンロード・設定が必要
- ⚠️ PCが必要

**👉 下の「PC版の使い方」へ**

---

## 📱 簡単版（ブラウザ版）の使い方

### ステップ1: リンクを開く

以下のリンクをクリックしてください：

**https://huggingface.co/spaces/typeone1964/tiktok-re-editor-voicevox-mobile**

### ステップ2: APIキーを入力（無料）

1. **左上の「> API設定」**をクリック
2. **「クラウド版（スマホOK）」**を選択
3. **VOICEVOX Cloud API Key**を入力
   - 👉 APIキー取得方法: https://voicevox.su-shiki.com/su-shikiapis/ で無料登録

### ステップ3: テキストをアップロード

1. **「テキストから生成」タブ**をクリック
2. テキストファイルをアップロード、または直接入力
3. **「GENERATE AUDIO」ボタン**をクリック
4. 音声をダウンロード

**これだけで完了！**

⚠️ **注意**: ブラウザ版は1日の使用回数に制限があります。たくさん使いたい場合は、PC版をおすすめします。

---

## 💻 PC版（ダウンロード版）の使い方

### 📋 必要なもの

1. **PC**（Windows、Mac、Linuxどれでも）
2. **Python**（無料ソフト）
3. **VOICEVOX**（無料ソフト）

---

### ステップ1: Pythonをインストール

**Pythonって何？**
プログラムを動かすために必要な無料ソフトです。

**インストール方法：**

#### Windows・Macの場合

1. https://www.python.org/downloads/ にアクセス
2. **黄色い「Download Python」ボタン**をクリック
3. ダウンロードしたファイルを開いて、画面の指示に従ってインストール
4. ✅ **「Add Python to PATH」にチェックを入れる**（重要！）

#### 確認方法

インストールできたか確認しましょう：

**Windowsの場合：**
1. **「スタートメニュー」** → **「cmd」**と入力 → **「コマンドプロンプト」**を開く
2. `python --version` と入力してEnter
3. `Python 3.9.x` のように表示されればOK

**Macの場合：**
1. **「アプリケーション」** → **「ユーティリティ」** → **「ターミナル」**を開く
2. `python3 --version` と入力してEnter
3. `Python 3.9.x` のように表示されればOK

---

### ステップ2: VOICEVOXをインストール

**VOICEVOXって何？**
音声を作るための無料ソフトです。

**インストール方法：**

1. https://voicevox.hiroshiba.jp/ にアクセス
2. **「ダウンロード」ボタン**をクリック
3. お使いのOS（Windows/Mac）に合ったファイルをダウンロード
4. ダウンロードしたファイルを開いて、画面の指示に従ってインストール

---

### ステップ3: このアプリをダウンロード

#### 方法A: ZIPでダウンロード（簡単）

1. https://github.com/typeone1964-creator/TikTok-Re-Editor-VOICEVOX-Mobile にアクセス
2. **緑色の「Code」ボタン**をクリック
3. **「Download ZIP」**をクリック
4. ダウンロードしたZIPファイルを解凍（右クリック → 「すべて展開」）

#### 方法B: Gitでダウンロード（上級者向け）

コマンドプロンプト（Windows）またはターミナル（Mac）で：
```bash
git clone https://github.com/typeone1964-creator/TikTok-Re-Editor-VOICEVOX-Mobile.git
```

---

### ステップ4: 必要なパッケージをインストール

**パッケージって何？**
このアプリを動かすために必要な部品です。

#### Windowsの場合

1. **解凍したフォルダ**を開く
2. フォルダ内の**何もないところで「Shift + 右クリック」**
3. **「PowerShellウィンドウをここで開く」**または**「コマンドウィンドウをここで開く」**を選択
4. 以下を入力してEnter：
   ```bash
   pip install -r requirements.txt
   ```
5. たくさん文字が流れて、最後に完了メッセージが出ればOK

#### Macの場合

1. **「ターミナル」**を開く
2. `cd ` と入力（スペース含む）
3. **解凍したフォルダ**をターミナルにドラッグ＆ドロップ
4. Enterを押す
5. 以下を入力してEnter：
   ```bash
   pip3 install -r requirements.txt
   ```
6. たくさん文字が流れて、最後に完了メッセージが出ればOK

---

### ステップ5: アプリを起動

#### 1. VOICEVOXを起動

まず、**VOICEVOXアプリ**を起動してください。
- 画面が表示されて、使える状態になればOKです
- このまま起動したままにしておいてください

#### 2. このアプリを起動

**Windowsの場合：**
1. アプリのフォルダで**「Shift + 右クリック」** → **「PowerShellウィンドウをここで開く」**
2. 以下を入力してEnter：
   ```bash
   streamlit run app.py
   ```

**Macの場合：**
1. **「ターミナル」**で、アプリのフォルダに移動（ステップ4と同じ）
2. 以下を入力してEnter：
   ```bash
   streamlit run app.py
   ```

#### 3. ブラウザで開く

- 自動的にブラウザが開きます
- 開かない場合は、ブラウザで以下のアドレスにアクセス：
  ```
  http://localhost:8501
  ```

**「localhost」って何？**
「あなたのPC」という意味です。あなたのPC上でアプリが動いています。

---

### ステップ6: 使ってみる

1. **サイドバー**（左上の「> API設定」）を開く
2. **「ローカル版（PC必須）」**を選択
3. **「テキストから生成」タブ**をクリック
4. テキストファイルをアップロード、または直接入力
5. **「GENERATE AUDIO」ボタン**をクリック
6. 音声をダウンロード

**完了です！🎉**

---

## 🔧 トラブルシューティング（困ったときは）

### ❌ 「VOICEVOXに接続できません」と表示される

**原因**: VOICEVOXアプリが起動していない

**解決方法**:
1. VOICEVOXアプリを起動してください
2. VOICEVOXが完全に起動するまで数秒待ってください
3. ブラウザをリロード（更新）してください

---

### ❌ 「python: command not found」と表示される

**原因**: Pythonがインストールされていない、またはPATHが通っていない

**解決方法**:
1. Pythonをインストールしてください（ステップ1参照）
2. インストール時に**「Add Python to PATH」にチェック**を入れてください
3. PCを再起動してください

---

### ❌ 「pip: command not found」と表示される

**原因**: Pythonのインストールに問題がある

**解決方法**:
- Windowsの場合: `pip` の代わりに `python -m pip` を使ってください
- Macの場合: `pip` の代わりに `pip3` を使ってください

---

### ❌ ブラウザ版でエラーが出る

**原因**: VOICEVOX Cloud APIの制限に達した、またはサーバーエラー

**解決方法**:
1. **PC版に切り替える**（推奨・無制限）
2. または、新しいAPIキーを取得する
3. または、1日待ってから再度試す

---

## 🙋 よくある質問（FAQ）

### Q1: プログラミングの知識がなくても使えますか？

**A**: はい！このガイドに従えば使えます。

- **超初心者向け**: ブラウザ版を使ってください（リンクをクリックするだけ）
- **PCユーザー向け**: PC版を使えば無制限に使えます（少し設定が必要）

---

### Q2: 有料ですか？

**A**: いいえ、完全無料です。

- ブラウザ版: 無料（1日の制限あり）
- PC版: 完全無料・無制限

---

### Q3: ブラウザ版とPC版、どっちがいい？

**A**: 状況によります。

| あなたの状況 | おすすめ |
|------------|---------|
| スマホ・タブレットしか持っていない | ブラウザ版 |
| PCを持っている | PC版（無制限・高速） |
| ちょっと試したい | ブラウザ版 |
| たくさん使いたい | PC版 |

---

### Q4: 「localhost」って何？

**A**: 「あなたのPC」という意味です。

- `http://localhost:8501` = あなたのPC上で動いているアプリにアクセスするアドレス
- 他の人のPCでは見えません（自分のPCだけで使います）

---

### Q5: 他の人にも使ってもらいたい

**A**: 2つの方法があります。

**簡単な方法**: ブラウザ版のリンクを教える
```
https://huggingface.co/spaces/typeone1964/tiktok-re-editor-voicevox-mobile
```

**PC版を使いたい場合**: その人も同じようにGitHubからダウンロードして設定する必要があります。

---

### Q6: スマホで使える？

**A**: はい、ブラウザ版なら使えます。

**ブラウザ版のリンク**:
https://huggingface.co/spaces/typeone1964/tiktok-re-editor-voicevox-mobile

PC版は、PCが必要です。

---

### Q7: エラーが出て使えない

**A**: 上の「トラブルシューティング」を確認してください。

それでも解決しない場合は、GitHubのIssuesで質問してください：
https://github.com/typeone1964-creator/TikTok-Re-Editor-VOICEVOX-Mobile/issues

---

## 📝 用語集（専門用語の説明）

| 用語 | 意味 |
|------|------|
| **Python** | プログラムを動かすための無料ソフト |
| **VOICEVOX** | 音声を作るための無料ソフト |
| **pip** | Pythonの部品をインストールするツール |
| **requirements.txt** | 必要な部品のリストが書かれたファイル |
| **localhost** | 「あなたのPC」という意味 |
| **API** | 他のサービスを使うための仕組み |
| **APIキー** | サービスを使うためのパスワードのようなもの |
| **GitHub** | プログラムを公開・共有するサイト |
| **Hugging Face** | AIアプリを公開・共有するサイト |

---

## 🌟 機能一覧

### 📹 動画から生成
- 動画をアップロードして自動で文字起こし
- テキストを自動整形
- ファイル名も自動生成

### 📄 テキストファイルから生成
- テキストファイル（.txt）をアップロード
- そのまま音声生成
- **API不要**

### 🎙️ 音声合成
- VOICEVOXのキャラクター選択
- 話速調整
- 長い文章も自動分割して音声生成

### 📝 その他
- テキスト編集機能
- 句読点自動削除機能
- テキストと音声の両方をダウンロード

---

## 📚 詳しい情報

- **GitHub**: https://github.com/typeone1964-creator/TikTok-Re-Editor-VOICEVOX-Mobile
- **ブラウザ版**: https://huggingface.co/spaces/typeone1964/tiktok-re-editor-voicevox-mobile

---

## 🙏 謝辞

- [VOICEVOX](https://voicevox.hiroshiba.jp/) - 音声合成エンジン
- [Streamlit](https://streamlit.io/) - アプリ作成ツール
- [Gladia](https://www.gladia.io/) - 文字起こしサービス
- [Google Gemini](https://ai.google.dev/) - テキスト整形AI

---

Made with ❤️ by typeone1964-creator
