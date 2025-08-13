import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 5  # Duration of recording

print("Starting recording for 5 seconds...")
try:
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    print("Recording finished")

    # Check min/max to confirm data looks sane
    print("Audio min:", np.min(audio), "max:", np.max(audio))

    # Clip audio to [-1, 1] to avoid overflow and convert to int16 PCM
    audio_clipped = np.clip(audio, -1, 1)
    audio_int16 = np.int16(audio_clipped * 32767)

    write('test_record.wav', fs, audio_int16)
    print("Saved to test_record.wav")
except Exception as e:
    print("Error during recording:", e)
