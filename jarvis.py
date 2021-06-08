import pyautogui
import time
import smtplib
import random
import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from selenium import webdriver
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


engine = pyttsx3.init('sapi5')
vocies = engine.getProperty('voices')
engine.setProperty('voices', vocies[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Abhinav Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Abhinav Sir!")

    else:
        speak("Good Evening Abhinav Sir!")

    speak("I am Krishna. Please tell me how may I help you")
    print("Wishing my friend")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


with open('C:\\Users\\abhin\\password.txt') as f:
    password = f.read()

frommail = 'abhinav.gupta.02.08@gmail.com'


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(frommail, password)
    server.sendmail(frommail, to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia,")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening Google")
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.google.com/")

        elif 'open stack overflow' in query:
            speak("Opening Stakoverflow")
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.stackoverflow.com/")

        elif 'play music' in query:
            speak("Playing Random Song from your folder")
            music_dir = "C:\\Users\\abhin\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif 'the date' in query:
            strdate = datetime.datetime.now().strftime("%D")
            print(strdate)
            speak(f"Sir today's date is {strdate}")

        elif 'open vs code' in query:
            speak("Opening Vs Code")
            vspath = "C:\\Users\\abhin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)

        elif 'open chrome' in query:
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromepath)

        elif 'email to abhinav' in query:
            try:
                speak("What Should I send?")
                content = takeCommand()
                to = "abhinavgupta020208@gmail.com"
                print("Sending email")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry Sir mail couldn't be send. Due to errors:")
                print(e)
                
        elif 'email to abhinav' in query:
            try:
                speak("What Should I send?")
                content = takeCommand()
                to = "abhinavgupta020208@gmail.com"
                print("Sending email")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry Sir mail couldn't be send. Due to errors:")
                print(e)

        elif 'open gmail' in query:
            try:
                speak("Opening Gmail in Chrome for Neha")
                driver = webdriver.Chrome(
                    executable_path='C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe')
                driver.get('https://mail.google.com/mail/u/0/#inbox')
                username = driver.find_element_by_xpath('//*[@id="identifierId"]')
                username.click()
                username.send_keys('2018.neha.gupta@ves.ac.in')
                next = driver.find_element_by_xpath(
                    '//*[@id="identifierNext"]/div/button/div[2]')
                next.click()
                time.sleep(3)
                password = driver.find_element_by_xpath(
                    '//*[@id="password"]/div[1]/div/div[1]/input')
                password.click()
                with open('C:\\Users\\abhin\\2018nehapass.txt') as g:
                    password2 = g.read()
                password.send_keys(password2)
                next = driver.find_element_by_xpath(
                    '//*[@id="passwordNext"]/div/button/div[2]')
                next.click()
            except Exception as e:
                print('Sorry')

        elif 'how are you' in query:
            speak("I an fine Sir. Thank You for asking")

        elif 'your name' in query:
            speak("My name is Jarvis and I can do many tasks.")

        elif 'multiply' in query:
            try:
                speak("Please say the first number")
                number1 = takeCommand()
                speak("Please say the Second number")
                number2 = takeCommand()
                speak(
                    f"{number1} multiplied by {number2} equals to {int(number1)*int(number2)}")
                print(
                    f"{number1} multiplied by {number2} equals to {int(number1)*int(number2)}")
            except Exception as e:
                print(e)
                speak("sorry I couldn't multiply the numbers due to internal errors")

        elif 'add' in query:
            try:
                speak("Please say the first number")
                num1 = takeCommand()
                speak("Please say the Second number")
                num2 = takeCommand()
                speak(
                    f"{num1} plus {number2} equals to {int(num1)+int(num2)}")
                print(
                    f"{num1} plus {number2} equals to {int(num1)+int(num2)}")
            except Exception as e:
                print(e)
                speak("sorry I couldn't Add the numbers due to internal errors")

        elif 'Subtract' in query:
            try:
                speak("Please say the first number")
                numb1 = takeCommand()
                speak("Please say the Second number")
                numb2 = takeCommand()
                speak(
                    f"{numb1} multiplied by {numb2} equals to {int(numb1)-int(numb2)}")
                print(
                    f"{numb1} multiplied by {numb2} equals to {int(numb1)-int(numb2)}")
            except Exception as e:
                print(e)
                speak("sorry I couldn't Subtract the numbers due to internal errors")

        elif 'the table of' in query:
            try:
                speak("Please repeat the number")
                tableof = takeCommand()
                if tableof == None:
                    break
                for i in range(1, 11):
                    a = int(tableof) * i
                    speak(f"{tableof} into {i} equals to {a}")
                    print(f"{tableof} into {i} equals to {a}")
            except Exception as e:
                speak("sorry I couldn't say the table due to internal errors")

        elif 'open whatsapp' in query:
            whatsapppath = "C:\\Users\\abhin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapppath)

        elif 'open telegram' in query:
            telegrampath = "C:\\Users\\abhin\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telegrampath)

        elif 'the square' in query:
            try:
                speak("Please repeat the number")
                squ = takeCommand()
                a = int(squ)
                b = a * a
                speak(f"The square of {squ} is {b}")
            except Exception as e:
                speak("sorry I couldn't say the table due to internal errors")

        elif 'the weather' in query:
            speak("You can see the weather and temperature on the screen")
            driver = webdriver.Chrome(
                executable_path='C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe')
            driver.get(
                'https://weather.com/en-IN/weather/today/l/98f2fa2e5164f762a871e01c8ce7c8f88b1c92c907d8870d7b646a16bbe523db')

        elif 'the temperature' in query:
            speak("You can see the weather and temperature on the screen")
            driver = webdriver.Chrome(
                executable_path='C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe')
            driver.get(
                'https://weather.com/en-IN/weather/today/l/98f2fa2e5164f762a871e01c8ce7c8f88b1c92c907d8870d7b646a16bbe523db')

        elif 'search' in query:
            a = query.replace("search ", "")
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.google.com/")
            search = driver.find_element_by_xpath(
                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            search.click
            search.send_keys(a)
            time.sleep(1)
            pyautogui.keyDown('enter')
            
        elif 'shutdown' in query:
            speak("Now turning off the pc...")
            try:
                pyautogui.moveTo(30, 1055)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(19, 998)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click(33, 899)
                pyautogui.click()
                pyautogui.click()
            except Exception as e:
                print(e)
                speak("Couldn't Shutdown the pc due to internal error")

        elif 'turn off' in query:
            speak("Now turning off the pc...")
            try:
                pyautogui.moveTo(30, 1055)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(19, 998)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click(33, 899)
                pyautogui.click()
                pyautogui.click()
            except Exception as e:
                print(e)
                speak("Couldn't turn off the pc due to internal error")

        elif 'restart' in query:
            speak("Now restarting the pc...")
            try:
                pyautogui.moveTo(30, 1055)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(19, 998)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(45, 931)
                pyautogui.click()
                pyautogui.click()
            except Exception as e:
                print(e)
                speak("Couldn't restart the pc due to internal error")

        elif 'hibernate' in query:
            ("Hibernating the pc")
            try:
                pyautogui.moveTo(30, 1055)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(19, 998)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(63, 811)
                pyautogui.click()
                pyautogui.click()
            except Exception as e:
                print(e)
                speak("Couldn't sleep the pc due to internal error")

        elif 'sleep' in query:
            speak("Making the pc sleep...")
            try:
                pyautogui.moveTo(30, 1055)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(19, 998)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(51, 809)
                pyautogui.click()
                pyautogui.click()
            except Exception as e:
                print(e)
                speak("Couldn't hibernate the pc due to internal error")

        elif 'close the program' in query:
            break

        else:
            print("Sorry I cant do this right now")
