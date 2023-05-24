from pydub import AudioSegment

m4a_file = 'test_m4a.m4a'
wav_filename = r"D:\test_wav.wav"
track = AudioSegment.from_file(m4a_file, format='m4a')
file_handle = track.export(wav_filename, format='wav')