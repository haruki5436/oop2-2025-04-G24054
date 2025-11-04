from datetime import datetime

def save_text(text, filename="transcript.txt"):
    """
    文字起こし結果を追記モードで保存（上書きしない）
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n{text}\n\n")
    print("文字起こし結果を保存しました:", filename)
