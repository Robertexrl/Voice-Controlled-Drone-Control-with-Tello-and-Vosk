
# SQUADRONE | Voice-Controlled Drone Control with Tello and Vosk

# This script demonstrates how to build a voice-controlled drone system using the Tello drone, Vosk for speech recognition, and PyAudio.
# Follow the steps below to understand the code and set up the project.

# Import required libraries
import pyaudio
from vosk import Model, KaldiRecognizer
from djitellopy import Tello

# Step 1: Initialize the Tello Drone
# Connect to the Tello drone using the djitellopy library.
tello = Tello()
tello.connect()

# Step 2: Initialize Vosk Speech Recognition
# Load the Vosk model for speech recognition and set up the Kaldi recognizer.
model = Model(r"C:\Users\00097159\Squadrone\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Step 3: Set Up PyAudio for Microphone Input
# Initialize the microphone input stream using PyAudio.
mic = pyaudio.PyAudio()
listening = False

# Step 4: Create a Function to Capture Voice Commands
# Capture audio from the microphone and process it using the Vosk recognizer.
def get_command():
    global listening
    listening = True
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    while listening:
        try:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                response = result[14:-3]  # Extracting the recognized command from the result string
                listening = False
                stream.stop_stream()
                stream.close()
                return response
        except OSError:
            pass

# Step 5: Analyze and Execute the Command
# Map the recognized command to a specific drone action.
def analyze_command(command):
    try:
        if command == "take off":
            tello.takeoff()
        elif command == "land":
            tello.land()
        elif command == "move up":
            tello.move_up(100)
        elif command == "do a back flip":
            tello.flip_back()
        elif command == "do a front flip":
            tello.flip_forward()
        elif command == "say hello":
            tello.rotate_clockwise(360)
        else: 
            print("I don't understand the command, add it!")
    except Exception as e:
        print(f"Error executing command: {e}")

# Step 6: Run the Command Loop
# Keep listening for commands and execute them as they are recognized.
while True:
    print("Waiting for command...")
    command = get_command()
    if command:
        print(f"Command received: {command}")
        analyze_command(command)
    else:
        print("No command received.")
