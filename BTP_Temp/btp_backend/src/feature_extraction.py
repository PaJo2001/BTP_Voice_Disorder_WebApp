from pydub import AudioSegment
import speechpy
import scipy.io.wavfile as wavy


def extract_features(file_loc):
    newAudio = AudioSegment.from_wav(file_loc)
    fs, signal = wavy.read(file_loc)
    features = speechpy.feature.mfcc(signal, sampling_frequency=fs, frame_length=0.025, frame_stride=0.01, num_filters=40, fft_length=512, low_frequency=0, high_frequency=None)
    return features

