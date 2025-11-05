# oop2-2025-04-G24054

# 🎙️ 音声録音＆文字起こしアプリ  
（オブジェクト指向プログラミングⅡ グループ課題）

---

## 📘 プロジェクト概要

このプログラムは、**マイクから10秒間の音声を録音し、その音声を文字起こししてテキストファイルに保存する**アプリケーションです。  
`mlx_whisper`（Apple Silicon向け高速モデル）を利用しており、ローカル環境で動作します。

---

## 🧩 ファイル構成

oop2-2025-04-G24054/
├── main.py # 全体を実行するメインスクリプト
├── record_audio.py # マイク録音（10秒間）
├── transcribe_audio.py # 音声→テキスト変換（Whisper使用）
├── save_text.py # テキストを保存（上書きしない）
├── requirements.txt # 依存モジュール一覧
└── README.md # この説明書


---

## 🚀 実行手順

### 1️⃣ 事前準備（初回のみ）
Pythonがインストールされていることを確認し、以下のモジュールを導入してください：

bash
pip install ffmpeg-python pydub mlx_whisper numpy
※ macOS の場合は ffmpeg の導入も必要です：
brew install ffmpeg

2️⃣ プログラムを実行
python main.py

🔹 実行の流れ
10秒間マイクから録音
音声ファイルを一時保存 (python-audio-output.wav)
Whisperで文字起こし
結果を transcription_YYYYMMDD_HHMMSS.txt に保存

🧠 使用技術
役割	使用技術
音声録音	ffmpeg-python
音声処理	pydub
音声認識	mlx_whisper（Whisper Base モデル）
ファイル保存	Python標準モジュール

⚙️ Whisperモデルの設定
本プログラムでは、Hugging Face上のモデル
mlx-community/whisper-base-mlx
を自動でダウンロードして利用します。

def transcribe_audio(filepaths, model_path="mlx-community/whisper-base-mlx"):

💾 出力例
実行後、以下のようなファイルが生成されます：
transcription_2025-11-05_221530.txt
中身の例：
こんにちは。これはテスト録音です。



👥 作成者情報
k24054 北川晴樹

🧾 コミットログ
- Add record_audio.py (音声録音機能)
- Add transcribe_audio.py (文字起こし機能)
- Add save_text.py (保存処理)
- Update main.py (全体統合)

💬 まとめ
このプロジェクトでは、グループ開発の流れ（役割分担・GitHubでの統合・モジュール分離） を体験しました。
特に、音声データの扱い方やモデル管理の重要性を学びました。
