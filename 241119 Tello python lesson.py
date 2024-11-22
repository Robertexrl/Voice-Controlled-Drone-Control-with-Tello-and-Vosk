#!/usr/bin/env python
# coding: utf-8

# Welcome to Squadrone's workshop, this is a hands on workshop and I promise you will have fun!
# 
# 
# 
# **Mission 1 Fly Hello tello mission, take off, go up 100cm, turn 360 degrees (we pretend the drone says hello world!), and then we land.**
# 
# This is an explanation of the first part of the code, it does look complex but don't worry, you will learn it with time: 
# 
# Import Modules;
# 
# import socket: This brings in the socket module, which lets the program send and receive data over a network. import threading: This is used to run code in different threads at the same time, like doing two things at once. import time: This is used to make the program wait for a certain amount of time. Set Up Addresses:
# 
# tello_address = ('192.168.10.1', 8889): This is the address of the Tello drone. It's like the drone's home address on the internet. local_address = ('', 9000): This is the address for your computer. It's like saying, "I'll be waiting at door number 9000 to talk to the drone." Create a UDP Connection:
# 
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM): This creates a new way for your computer to talk to other devices using UDP, which is a fast but simple type of internet communication. Bind to Local Address:
# 
# sock.bind(local_address): This tells your computer to get ready to send and receive messages at door number 9000. Send Message Function:
# 
# def send(message, delay): This is a set of instructions that lets you send a message to the drone. Inside the send function: It tries to send a message to the drone. If it can't, it will tell you there was an error. time.sleep(delay): After sending the message, it waits for a bit (this is the delay). Receive Message Function:
# 
# def receive(): This set of instructions listens for messages from the drone. Inside the receive function: It keeps checking for messages from the drone. If it gets a message, it shows you what the message says. If there's a problem and it can't listen anymore, it will stop trying and tell you there was an error. Listening Thread:
# 
# receiveThread = threading.Thread(target=receive): This creates a special task that can listen for drone messages while the rest of the program does other things. receiveThread.daemon = True: This makes sure that this special task doesn't keep running forever if the main program stops. receiveThread.start(): This starts the special task, so it begins listening for messages from the drone. That's it! This code sets up a way for your computer to send instructions to a Tello drone and listen to what the drone says back, all while being able to do other things at the same time.

# In[5]:


# Import the necessary modules
import socket
import threading
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock.bind(local_address)

# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

#Put Tello into command mode
send("command", 3)

# Send the takeoff command
send("takeoff", 5)

# Go up by 100 cm
send("up 100", 4)

# Perform a 360-degree clockwise yaw
send("cw 360", 5)

# Land
send("land", 5)

# Print message
print("Mission completed successfully!")

# Close the socket
sock.close()


# **Mission 2, let's fly the drone in a square pattern**
# Move forward 100, left yaw 90, etc.

# In[2]:


# Import the necessary modules
import socket
import threading
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection to send the command to Tello
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock.bind(local_address)

# Function to send commands to Tello with a delay
def send(message, delay):
    try:
        sock.sendto(message.encode(), tello_address)
        print(f"Sending message: {message}")
    except Exception as e:
        print(f"Error sending: {e}")
    time.sleep(delay)

# Function to receive responses from Tello
def receive():
    while True:
        try:
            response, ip_address = sock.recvfrom(128)
            print(f"Received message: {response.decode(encoding='utf-8')}")
        except Exception as e:
            print(f"Error receiving: {e}")
            sock.close()
            break

# Start a thread to continuously listen for responses
receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

# Main commands to fly the Tello drone in a square pattern
try:
    # Put Tello into command mode
    send("command", 3)
    
    # Take off
    send("takeoff", 4)
    
    # First side of the square
    send("forward 100", 4)  # Move forward 100 cm
    send("cw 90", 3)        # Rotate 90 degrees clockwise
    
    # Second side of the square
    send("forward 100", 4)  # Move forward 100 cm
    send("cw 90", 3)        # Rotate 90 degrees clockwise
    
    # Third side of the square
    send("forward 100", 4)  # Move forward 100 cm
    send("cw 90", 3)        # Rotate 90 degrees clockwise
    
    # Fourth side of the square
    send("forward 100", 4)  # Move forward 100 cm
    send("cw 90", 3)        # Rotate 90 degrees clockwise
    
    # Land
    send("land", 5)

    print("Square flight pattern completed successfully!")

finally:
    # Close the socket
    sock.close()


# **Mission 3, let's fly the drone in a square pattern, but this time we will use the loop function**
# 

# In[3]:


# Import the necessary modules
import socket
import threading
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection to send the command to Tello
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock.bind(local_address)

# Function to send commands to Tello with a delay
def send(message, delay):
    try:
        sock.sendto(message.encode(), tello_address)
        print(f"Sending message: {message}")
    except Exception as e:
        print(f"Error sending: {e}")
    time.sleep(delay)

# Function to receive responses from Tello
def receive():
    while True:
        try:
            response, ip_address = sock.recvfrom(128)
            print(f"Received message: {response.decode(encoding='utf-8')}")
        except Exception as e:
            print(f"Error receiving: {e}")
            sock.close()
            break

# Start a thread to continuously listen for responses
receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

# Main commands to fly the Tello drone in a square pattern
try:
    # Put Tello into command mode
    send("command", 3)
    
    # Check battery level
    send("battery?", 3)
    
    # Additional commands can go here, e.g., takeoff, fly, etc.

    print("Battery level checked!")
    
    # Take off
    send("takeoff", 4)
    
    # Move in a square pattern (each side 100 cm)
    for _ in range(4):
        send("forward 100", 5)  # Move forward 100 cm
        send("cw 90", 4)       # Rotate 90 degrees clockwise
    
    # Land
    send("land", 5)

    print("Square flight pattern completed successfully!")

finally:
    # Close the socket
    sock.close()


# **Mission 4, amazing! time for the real deal! we are going to write a script that uses your voice to give instructions to the drone!**

# See if you can understand what is happening in the code below:
# 
# The first thing we need to do is download the vosk model called "vosk-model-small-en-us-0.15" and save it in your computer. Go to https://alphacephei.com/vosk/models
# 

# In[ ]:


# Important step, then you need to install the vosk and pyaudio packages
#!pip install vosk pyaudio #if you are using jupiter notebook
#pip install vosk pyaudio #if you are using a terminal


# In[ ]:


import socket
import threading
import time
import pyaudio
from vosk import Model, KaldiRecognizer

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection to send commands to Tello
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(local_address)

# Initialize Vosk model, enter here the location of the vosk model that you downloaded
model = Model(r"C:\Users\00097159\Squadrone\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
mic = pyaudio.PyAudio()
listening = False
stop_program = False  # Global flag to stop the program

# Function to send commands to Tello with a delay
def send(message, delay=3):
    try:
        sock.sendto(message.encode(), tello_address)
        print(f"Sending message: {message}")
    except Exception as e:
        print(f"Error sending: {e}")
    time.sleep(delay)

# Function to receive responses from Tello
def receive():
    global stop_program
    while True:
        try:
            response, ip_address = sock.recvfrom(128)
            print(f"Received message: {response.decode(encoding='utf-8')}")
        except Exception as e:
            print(f"Error receiving: {e}")
            print("Closing socket and ensuring the drone lands.")
            send("land", 5)  # Ensure the drone lands if communication is lost
            sock.close()
            stop_program = True  # Signal to stop the main loop
            break

# Start a thread to continuously listen for responses
receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

# Function to get voice commands
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
                response = result[14:-3]  # Extract recognized command
                listening = False
                stream.stop_stream()
                stream.close()
                return response
        except OSError:
            pass

# Function to analyze and execute commands
def analyze_command(command):
    global stop_program
    try:
        if command == "take off":
            send("takeoff", 5)
        elif command == "land":
            send("land", 5)
        elif command == "move up":
            send("up 100", 5)
        elif command == "back flip":
            send("flip b", 5)
        elif command == "front flip":
            send("flip f", 5)
        elif command == "say hi":
            send("cw 360", 5)
        elif command == "stop":
            print("Stop command received. Landing and closing socket.")
            send("land", 5)  # Ensure the drone lands safely
            sock.close()
            stop_program = True  # Signal to stop the main loop
        else:
            print("I don't understand the command, add it!")
    except Exception as e:
        print(f"Error executing command: {e}")

# Main program
try:
    # Put Tello into command mode
    send("command", 3)
    
    # Check the battery level
    send("battery?", 3)

    # Continuously listen for voice commands
    while not stop_program:
        print("Waiting for command...")
        command = get_command()
        if command:
            print(f"Command received: {command}")
            analyze_command(command)
        else:
            print("No command received.")

finally:
    if not stop_program:
        print("Ensuring the socket is closed safely.")
        sock.close()


# **Thank you for completing the workshop, feel free to share it and please follow us on instagram: @au.squadrone**
