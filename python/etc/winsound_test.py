import winsound
import time
# winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
for i in range(100, 8000, 100) :
    winsound.Beep(i, 100)
    print(i)
    time.sleep(0.1)

# import scipy.io.wavfile

