# make_all_files.py
#  Creates sample.txt, script.py, music.mp3, and video.mp4 safely.

import os

print("Starting file generation...")

# 1️ Create sample.txt
with open("sample.txt", "w") as f:
    f.write("This is a sample text file for UDP file transfer.\n")
print(" sample.txt created.")

# 2️ Create script.py
with open("script.py", "w") as f:
    f.write('print("This is a test Python script for UDP transfer.")\n')
print(" script.py created.")

# 3️ Create dummy music.mp3
try:
    from pydub.generators import Sine
    tone = Sine(440).to_audio_segment(duration=2000)
    tone.export("music.mp3", format="mp3")
    print(" music.mp3 created using pydub.")
except Exception as e:
    # If pydub not available, create a blank file instead
    with open("music.mp3", "wb") as f:
        f.write(b"\x00" * 10000)  # just a dummy file
    print(" pydub not installed. Created dummy music.mp3 instead.")

# 4️ Create dummy video.mp4
try:
    import cv2
    import numpy as np
    width, height = 320, 240
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('video.mp4', fourcc, 20.0, (width, height))

    for _ in range(40):  # 2 seconds of blank frames
        frame = np.ones((height, width, 3), np.uint8) * 255
        out.write(frame)

    out.release()
    print(" video.mp4 created using OpenCV.")
except Exception as e:
    # If OpenCV not installed, create a dummy file
    with open("video.mp4", "wb") as f:
        f.write(b"\x00" * 50000)
    print(" OpenCV not installed. Created dummy video.mp4 instead.")

print("\n All required files are ready in this folder:")
print(os.getcwd())
