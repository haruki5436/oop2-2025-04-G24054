from record_audio import record_audio
from split_audio import split_audio
from transcribe_audio import transcribe_audio
from save_text import save_text

def main():
    # ①録音
    record_audio()

    # ②音声分割
    files = split_audio()

    # ③文字起こし
    text = transcribe_audio(files)

    # ④保存
    save_text(text)

if __name__ == "__main__":
    main()
