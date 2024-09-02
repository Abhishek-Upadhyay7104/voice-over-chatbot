import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import pyjokes
import pywhatkit as kit
import random
import cv2
import pyautogui
import operator
import requests
import sys
import time
from plyer import notification
import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, BOTH, SUNKEN
from PIL import Image, ImageTk
from threading import Thread

# Constants for custom styling
BG_COLOR = "#D2C6E2"
BUTTON_COLOR = "#F9F4F2"
BUTTON_FONT = ("Arial", 14, "bold")
BUTTON_FOREGROUND = "black"
HEADING_FONT = ("white", 24, "bold")
INSTRUCTION_FONT = ("Helvetica", 14)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


entry = None
stop_flag = False  # Define the stop_flag variable at the top of the script


def wish_time():
    global entry
    x = entry.get()
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 6:
        speak('Good night! Sleep tight.')
    elif 6 <= hour < 12:
        speak('Good morning!')
    elif 12 <= hour < 18:
        speak('Good afternoon!')
    else:
        speak('Good evening!')
    speak(f"{x} How can I help you?")


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        speak("say something")
        recognizer.pause_threshold = 0.8
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for 1 second of ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        speak("recognizing")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def perform_task():
    global stop_flag
    while not stop_flag:
        query = take_command().lower()  # Converting user query into lower case
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation error (when the search term has multiple possible meanings)
                print(f"There are multiple meanings for '{query}'. Please be more specific.")
                speak(f"There are multiple meanings for '{query}'. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                # Handle page not found error (when the search term does not match any Wikipedia page)
                print(f"'{query}' does not match any Wikipedia page. Please try again.")
                speak(f"'{query}' does not match any Wikipedia page. Please try again.")

        elif "what is" in query:
            speak("searching wikipedia.....")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "who is" in query:
            speak("searching wikipedia.....")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'play song' in query:
            song = query.replace('play', "")
            speak("Playing " + song)
            kit.playonyt(song)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'search' in query:
            s = query.replace('search', '')
            kit.search(s)

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")
            
        elif 'open code' in query:
            code_path = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'who created you' in query:
            print("Two third year BCA students, I created with python Language, in Visual studio code.")
            speak("Two third year BCA students, I created with python Language, in Visual studio code.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'play movie' in query:
            movi_dir = "F:\\movies"
            movies = os.listdir(movi_dir)
            random_movie = movies[4:]
            os.startfile(os.path.join(movi_dir, random.choice(random_movie)))

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k ==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'tell me my ip address' in query:
            speak("checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak(f"your ip address is {ipAdd}")
            except Exception as e:
                speak("sorry, due to network issue i am not able to fetch your ip address")

        elif 'volume up' in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            
        elif 'mute' in query or 'unmute' in query:
            pyautogui.press("volumemute")

        elif 'open notepad' in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)


        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location.replace(" ", "+"))

        elif 'write on notepad' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("what should, I write on notepad")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                notepad_text = r.recognize_google(audio)
                pyautogui.press("win")
                time.sleep(1)
                pyautogui.write("notepad")
                pyautogui.press("enter")
                time.sleep(1)
                pyautogui.write(notepad_text, interval=0.2)
                speak("Text written on Notepad successfully")

        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'close command prompt' in query:
            os.system("taskkill /f /im cmd.exe")

        elif 'open paint' in query:
            npath = "C:\\Windows\\System32\\mspaint.exe"
            os.startfile(npath)

        elif 'draw a square' in query:
            pyautogui.moveTo(x = 400, y = 300, duration = 1)
            pyautogui.leftClick
            distance = 400
            pyautogui.dragRel(distance, 0, duration = 1)
            pyautogui.dragRel(0, distance, duration = 1)
            pyautogui.dragRel(-distance, 0, duration = 1)
            pyautogui.dragRel(0, -distance, duration = 1)

        elif 'red colour' in query:
            pyautogui.moveTo(x = 970, y = 76, duration = 1)
            pyautogui.click(x = 970, y = 76, clicks = 1, interval = 0, button = "left")

        elif 'draw a rectangular spiral' in query:
            pyautogui.moveTo(x = 400, y = 300, duration = 1)
            pyautogui.leftClick
            distance = 300
            while distance >0:
                pyautogui.dragRel(distance, 0, 0.1, button = "left")
                distance = distance - 10
                pyautogui.dragRel(0, distance, 0.1, button = "left")
                pyautogui.dragRel(-distance, 0, 0.1, button = "left")
                distance = distance - 10
                pyautogui.dragRel(0, -distance, 0.1, button = "left")

        elif 'draw a line' in query:
            pyautogui.moveTo(x = 1000, y = 300, duration = 1)
            pyautogui.leftClick
            pyautogui.dragRel(400, 0, 1)

        elif 'close paint' in query:
            os.system("taskkill /f /im mspaint.exe")

        elif 'close movie' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")


        elif 'exit' in query or 'go to sleep' in query:
            speak("thanks for giving your time")
            stop_voice_assistant()


def stop_voice_assistant():
    global stop_flag
    speak("Stopping the Voice Assistant.")
    stop_flag = True


def start_voice_assistant():
    global stop_flag
    wish_time()
    perform_task()
    stop_flag = False  # Reset the flag to False when starting the voice assistant


def main():
    # Create the main GUI window
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("500x700")
    root.configure(bg=BG_COLOR)

    def on_button_click():
        global stop_flag
        if not stop_flag:
            stop_flag = False  # Reset the flag to False when starting the voice assistant
            Thread(target=start_voice_assistant).start()
        else:
            stop_voice_assistant()

    # Load and set the background image
    background_image = Image.open(
        "wallpaperflare.com_wallpaper.jpg")  # Replace "path/to/your/background_image.jpg" with the actual image file path
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = ttk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    f1 = ttk.Frame(root)
    f1.pack(pady=100)  # Add some padding to the frame to center it vertically

    image2 = Image.open("p.jpg")  # Replace "path_to_image2.jpg" with the actual path to your image
    resized_image = image2.resize((120, 120))
    p2 = ImageTk.PhotoImage(resized_image)
    l2 = ttk.Label(f1, image=p2, relief=SUNKEN)
    l2.pack(side="top", fill="both")

    # Heading
    heading_label = ttk.Label(root, text="Voice Assistant", font=HEADING_FONT, background=BG_COLOR)
    heading_label.pack(pady=20)

    global entry
    f1 = ttk.Frame(root)
    f1.pack()
    l1 = ttk.Label(f1, text="Enter Your Name", font=INSTRUCTION_FONT, background=BG_COLOR)
    l1.pack(side=LEFT, fill=BOTH)
    entry = ttk.Entry(f1, width=30)
    entry.pack(pady=10)

    # Instruction
    instruction_label = ttk.Label(root, text="Click the button below to start the Voice Assistant.",
                                  font=INSTRUCTION_FONT, background=BG_COLOR)
    instruction_label.pack(pady=10)

    # Create and place a button on the GUI
    button = ttk.Button(root, text="Start Voice Assistant", command=on_button_click,
                        style="VoiceAssistant.TButton")
    button.pack(pady=20)

    # Style the button
    style = ttk.Style(root)
    style.configure("VoiceAssistant.TButton", font=BUTTON_FONT, background=BUTTON_COLOR, foreground=BUTTON_FOREGROUND)

    # Run the GUI main loop
    root.mainloop()


if __name__ == "__main__":
    main()