# import librosa
# import numpy as np
# import matplotlib.pyplot as plt
# import librosa.display
# from numpy.fft import *
# import math
# import wave
# import struct
# from scipy.io import wavfile

# x, sr = librosa.load('25/lake1.wav', sr=None)

# window_size = 1024
# hop_length = 512 
# n_mels = 128
# time_steps = 384 

# window = np.hanning(window_size)
# stft= librosa.core.spectrum.stft(x, n_fft = window_size, hop_length = hop_length, window=window)
# out = 2 * np.abs(stft) / np.sum(window)

# plt.figure(figsize=(12, 4))
# ax = plt.axes()
# plt.set_cmap('hot')
# librosa.display.specshow(librosa.amplitude_to_db(out, ref=np.max), y_axis='log', x_axis='time',sr=sr)
# plt.savefig('spectrogramA.png', bbox_inches='tight', transparent=True, pad_inches=0.0 )


import requests
import wave
from PIL import Image
d="25"
sfs = []
n = 1
while True:
    r = requests.get(f"http://www.pythonchallenge.com/pc/hex/lake{n}.wav", auth=("butter", "fly"))
    if not r.ok: break
    d = r.content
    fn = f"{d}/lake{n}.wav"
    with open(fn, "wb") as f:
        f.write(d)
    sfs.append(wave.open(fn))
    n += 1

f = sfs[0].getnframes()
dim = int((f / 3) ** 0.5)
im = Image.new("RGB", (dim*5,dim*5), 0)
w, h = im.size
for i in range(n-1):
    y = i // 5
    x = i % 5
    d = sfs[i].readframes(f)
    im.paste(
        Image.frombytes("RGB", (dim, dim), d), 
        (dim * x, dim * y))
im.show()
