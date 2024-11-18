# Voice-Controlled-Drone-Control-with-Tello-and-Vosk
This repository showcases a voice-controlled drone system using Tello, Vosk for speech recognition, and PyAudio. It processes audio inputs to execute commands like "take off," "land," and "do a back flip," leveraging Vosk for recognition and djitellopy for drone control.
Voice-Controlled Drone Control with Tello and Vosk
This repository demonstrates how to build a voice-controlled drone system using the Tello drone, Vosk for speech recognition, and PyAudio. The code allows you to control the drone with voice commands such as "take off," "land," and "do a back flip." It integrates the Vosk speech recognition library to process audio inputs and map commands to drone actions via the djitellopy library.

Prerequisites
To run this code successfully, the following steps must be completed:

1. Install Required Libraries
Ensure the following Python libraries are installed in your environment:

djitellopy for Tello drone control.
vosk for offline speech recognition.
pyaudio for accessing microphone input. You can install these using pip:
bash
Copy code
pip install djitellopy vosk pyaudio
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
Usage
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/voice-controlled-drone.git
cd voice-controlled-drone
Run the Jupyter Notebook (Voice_Controlled_Drone_Control_Tello_with_Logo.ipynb) or the Python script (voice_controlled_drone.py) in your Python environment.

Issue voice commands via your microphone, and watch the Tello drone execute them in real time!

Notes
If the system doesn't recognise a command, it will prompt you to add it to the code.
