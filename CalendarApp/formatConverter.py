from pydub import AudioSegment


def formatting(fromFile, toFile):
    track = AudioSegment.from_file(fromFile, format='m4a')
    file_handle = track.export(toFile, format='wav')
    print(file_handle)
