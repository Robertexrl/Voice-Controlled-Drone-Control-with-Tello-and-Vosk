# Voice-Controlled-Drone-Control-with-Tello-and-Vosk

This repository demonstrates how to build a voice-controlled drone system using the Tello drone, Vosk for speech recognition, and PyAudio. The code allows you to control the drone with voice commands such as "take off," "land," and "do a back flip." It integrates the Vosk speech recognition library to process audio inputs and map commands to drone actions.

Prerequisites
To run this code successfully, the following steps must be completed:

1. Install Required Libraries
Ensure the following Python libraries are installed in your environment:

vosk for offline speech recognition.
pyaudio for accessing microphone input. You can install these using pip:

pip install vosk pyaudio

2. Download the Vosk Speech Recognition Model
The Vosk library requires a pre-trained model for speech recognition. Follow these steps to download and set it up:

Visit the Vosk Model Repository.
Select and download a suitable model, such as the small English model: vosk-model-small-en-us-0.15.
Extract the downloaded file to a directory on your system, e.g., C:\path\to\vosk-model.

3. Update the Model Path in the Code
Modify the code to point to the directory where the Vosk model is saved. Update the following line in the script:

python
Copy code
model = Model(r"C:\\path\\to\\vosk-model-small-en-us-0.15")

4. Test Your Microphone
Ensure your microphone is functioning and accessible in Python. You can test it using PyAudio.

5. Connect the Tello Drone
Ensure your Tello drone is powered on and connected to your system via WiFi.

Features
Voice command recognition using Vosk.
Real-time drone control with commands such as:
"take off"
"land"
"move up"
"do a back flip"
"do a front flip"
"say hello"

Notes:
If the system doesn't recognise a command, it will prompt you to add it to the code.
