from pydub import AudioSegment


def formatting(from_file, to_file):
    track = AudioSegment.from_file(from_file, format='m4a')
    file_handle = track.export(to_file, format='wav')
    print(file_handle)
