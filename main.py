import record_audio   # ← ファイル名が同じでもOKな書き方
from transcribe_audio import transcribe_audio
from save_text import save_text

def main():
    # ① 音声を録音
    record_audio.record_audio()  # ← モジュール名＋関数名で呼ぶ

    # ② 録音した音声を文字起こし
    text = transcribe_audio("recorded.wav")

    # ③ 文字起こし結果を保存
    save_text(text)

if __name__ == "__main__":
    main()
