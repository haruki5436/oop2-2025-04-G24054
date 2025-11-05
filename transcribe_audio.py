import mlx_whisper
from pydub import AudioSegment
import numpy as np

def preprocess_audio(sound):
    """Whisperに渡すための音声データを整形"""
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound

def transcribe_audio(filepaths, model_path="mlx-community/whisper-base-mlx"):
    """
    音声ファイルのリストを受け取り、順に文字起こしを行う
    """
    texts = []
    for path in filepaths:
        sound = preprocess_audio(AudioSegment.from_file(path, format="wav"))
        arr = np.array(sound.get_array_of_samples()).astype(np.float32) / 32768.0
        result = mlx_whisper.transcribe(arr, path_or_hf_repo=model_path)
        texts.append(result["text"] if isinstance(result, dict) else str(result))
    return "\n".join(texts)
