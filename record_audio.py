import ffmpeg
import time

def record_audio(output_file='python-audio-output.wav', duration=10):
    """
    マイクから音声を録音して指定したファイルに保存する関数。

    Parameters
    ----------
    output_file : str
        保存するファイル名（デフォルト: 'python-audio-output.wav'）
    duration : int
        録音時間（秒）
    """
    try:
        print(f"{duration}秒間、マイクからの録音を開始します...")
        (
            ffmpeg
            .input(':1', format='avfoundation', t=duration)  # ← Mac用入力デバイス
            .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
            .run(overwrite_output=True)
        )
        print(f"録音が完了しました。{output_file}に保存されました。")

    except ffmpeg.Error as e:
        print(f"エラーが発生しました: {e.stderr.decode()}")
    except Exception as e:
        print(f"予期せぬエラー: {e}")
