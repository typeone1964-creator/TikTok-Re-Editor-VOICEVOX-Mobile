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

動画やテキストファイルから「文字起こし → 整形 → 音声合成」を自動実行するStreamlitアプリ。

**💻 ローカル版推奨** - PCでVOICEVOXをインストール済みなら、無料・無制限で使えます！

---

## 🚀 クイックスタート（ローカル版・推奨）

### ✅ 必要なもの
- Python 3.9以上
- VOICEVOX（無料）: https://voicevox.hiroshiba.jp/

### 📦 インストール手順

**1. このリポジトリをダウンロード**
```bash
git clone https://github.com/typeone1964-creator/TikTok-Re-Editor-VOICEVOX-Mobile.git
cd TikTok-Re-Editor-VOICEVOX-Mobile
```

**2. 必要なパッケージをインストール**
```bash
pip install -r requirements.txt
```

**3. VOICEVOXアプリを起動**
- VOICEVOXアプリケーションを起動してください
- バックグラウンドで動作していればOKです

**4. アプリを起動**
```bash
streamlit run app.py
```

**5. ブラウザで開く**
- 自動的にブラウザが開きます（`http://localhost:8501`）
- サイドバーで「ローカル版（PC必須）」を選択

これで完了です！✨

---

## 🌟 機能

### 📹 動画から生成
- **動画文字起こし**: Gladia APIを使用した自動文字起こし
- **テキスト整形**: Gemini APIで14文字/行に整形
- **ファイル名生成**: Gemini APIで適切なファイル名を自動生成
- **音声合成**: VOICEVOXを使用した音声生成

### 📄 テキストファイルから生成
- テキストファイル（.txt）を直接アップロード
- **API不要**でクォータ節約
- 整形なしでそのまま音声生成

### 🎙️ 共通機能
- **プレビュー機能**: キャラクター試聴、生成音声試聴
- **編集可能**: 整形済みテキストを手動編集可能
- **ダウンロード**: テキストと音声を両方ダウンロード可能
- **句読点自動削除**: ダウンロード時に本文のみから句読点（。、）を自動削除（タイトル・紹介文・ハッシュタグは維持）
- **長文対応**: クラウド版でも長いテキストを自動分割して音声生成（200文字ごと）

---

## 💻 ローカル版 vs 📱 クラウド版

| 項目 | ローカル版（推奨）💻 | クラウド版📱 |
|------|------------------|------------|
| **文字数制限** | ✅ なし（無制限） | ⚠️ あり（自動分割処理） |
| **速度** | ✅ 高速 | ⚠️ やや遅い |
| **料金** | ✅ 完全無料 | ⚠️ ポイント制（1日の制限あり） |
| **デバイス** | ⚠️ PCのみ | ✅ スマホ・タブレットOK |
| **安定性** | ✅ 非常に安定 | ⚠️ API依存（エラーの可能性） |
| **おすすめ度** | ⭐⭐⭐⭐⭐ | ⭐⭐ |

**💡 結論**: PCを持っているなら、ローカル版を使いましょう！

---

## 📖 使用方法

### ✅ 最もシンプルな使い方（推奨）

1. **VOICEVOXアプリを起動**
2. **このアプリを起動** (`streamlit run app.py`)
3. **「テキストから生成」タブ**を選択
4. テキストファイルをアップロード、または直接入力
5. **「GENERATE AUDIO」ボタン**をクリック
6. 音声をダウンロード

**これだけで完了！API不要です。**

### 📹 動画から生成する場合（上級者向け）

Gladia APIとGemini APIが必要です：

1. サイドバーで **Gladia API** と **Gemini API** キーを入力
2. **「動画から生成」タブ**を選択
3. 動画ファイルをアップロード
4. **「START」ボタン**をクリック
5. 自動的に文字起こし・整形が実行されます
6. テキストを編集（必要に応じて）
7. **「GENERATE AUDIO」ボタン**で音声生成
8. テキストと音声をダウンロード

---

## 🔧 トラブルシューティング

### ❌ 「VOICEVOXに接続できません」と表示される

**原因**: VOICEVOXアプリが起動していない

**解決方法**:
1. VOICEVOXアプリを起動してください
2. VOICEVOXが完全に起動するまで待ってください（数秒）
3. このアプリをリロードしてください

---

### ❌ 「音声生成に失敗しました」と表示される（ローカル版）

**原因**: VOICEVOXとの接続に問題がある

**解決方法**:
1. VOICEVOXアプリが起動しているか確認
2. ファイアウォールでポート50021がブロックされていないか確認
3. VOICEVOXを再起動してみる

---

### ❌ クラウド版でエラーが出る

**原因**: VOICEVOX Cloud APIの制限に達した、またはサーバーエラー

**解決方法**:
1. **ローカル版に切り替える**（推奨）
2. または、新しいAPIキーを取得する
3. 1日の制限がリセットされるまで待つ

**💡 おすすめ**: クラウド版には制限が多いので、ローカル版の使用を強く推奨します！

---

### ❌ `ModuleNotFoundError: No module named 'xxx'`

**原因**: 必要なパッケージがインストールされていない

**解決方法**:
```bash
pip install -r requirements.txt
```

---

## 🔑 必要なAPI

| API | 用途 | 必要なタイミング | 取得方法 |
|-----|------|------------------|----------|
| **Gladia API** | 動画の文字起こし | 動画から生成する時のみ | [gladia.io](https://www.gladia.io/) |
| **Gemini API** | テキスト整形・ファイル名生成 | 動画から生成する時のみ | [ai.google.dev](https://ai.google.dev/) |
| **VOICEVOX（ローカル版）** | 音声合成 | ローカル版使用時 | [voicevox.hiroshiba.jp](https://voicevox.hiroshiba.jp/) |
| **VOICEVOX Cloud API** | 音声合成 | クラウド版使用時 | [voicevox.su-shiki.com/su-shikiapis/](https://voicevox.su-shiki.com/su-shikiapis/) |

### 💡 重要

- **テキストファイルから生成する場合、Gladia/Gemini APIは不要です**
- **ローカル版推奨**: PCでVOICEVOXアプリを起動（無料・無制限）
- クラウド版: APIキーのみ必要（スマホOK・制限あり）

---

## 📱 スマホ・タブレットで使う（クラウド版）

PCがない場合のみ、クラウド版を使用できます：

1. 🔑 **VOICEVOX Cloud API キーを取得**
   - [voicevox.su-shiki.com/su-shikiapis/](https://voicevox.su-shiki.com/su-shikiapis/) にアクセス
   - 無料でAPIキーを生成

2. 🌐 **ブラウザでアプリにアクセス**
   - Hugging Face Spaces: https://huggingface.co/spaces/typeone1964/tiktok-re-editor-voicevox-mobile
   - サイドバーで「クラウド版（スマホOK）」を選択
   - VOICEVOX Cloud API Keyを入力

3. ✅ **完了！**
   - 音声生成できます

⚠️ **注意**: クラウド版はポイント制で1日の上限があります。エラーが出る場合は、ローカル版の使用を検討してください。

---

## 🛠️ 技術スタック

- **Frontend**: Streamlit
- **文字起こし**: Gladia API
- **テキスト整形**: Gemini API
- **音声合成**: VOICEVOX（ローカル版） / VOICEVOX Cloud API
- **音声処理**: pydub

---

## 📝 ライセンス

MIT License

---

## 🙏 謝辞

- [VOICEVOX](https://voicevox.hiroshiba.jp/) - 音声合成エンジン
- [Streamlit](https://streamlit.io/) - Webアプリフレームワーク
- [Gladia](https://www.gladia.io/) - 文字起こしAPI
- [Google Gemini](https://ai.google.dev/) - テキスト整形AI

---

Made with ❤️ using Streamlit, Gladia API, Gemini API, and VOICEVOX
