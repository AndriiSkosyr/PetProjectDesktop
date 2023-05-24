from pydub import AudioSegment


def formatting(m4a_file):
    wav_filename = r"D:\test_wav.wav"
    track = AudioSegment.from_file(m4a_file, format='m4a')
    file_handle = track.export(wav_filename, format='wav')
    print(file_handle)
