from pydub import AudioSegment

def split_audio(input_file="python-audio-output.wav", split_point_ms=4000):
    """
    音声ファイルを指定ミリ秒で前後に分割して保存する
    """
    audio = AudioSegment.from_file(input_file, format="wav")

    before = audio[:split_point_ms]
    after = audio[split_point_ms:]

    before.export("audio-output-before.wav", format="wav")
    after.export("audio-output-after.wav", format="wav")

    print("音声を分割しました: audio-output-before.wav, audio-output-after.wav")
    return ["audio-output-before.wav", "audio-output-after.wav"]
