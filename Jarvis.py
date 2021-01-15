import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import pyjokes
import time
import winsound
import cv2
import smtplib
# import chat_bot



engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[0])

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def main():
    while True:
        command = str(input(">> "))
        print(bot.get_response(command))
        if "exit" in command:
            break

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Good morning sir..')
    elif hour >= 12 and hour < 18:
        talk('Good Afternoon sir...')
    else:
        talk("Good Evening sir...")
    talk('initializing jarvis')
    talk('jarvis installed successfully')
    talk('I am ready to take your commands')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir.....")
        r.pause_threshold = 1
        audio =  r.listen(source)
    try:
        print("Recognizing sir.....")
        command = r.recognize_google(audio)
        print(f"Boss said: {command}\n")

    except Exception as e :
        print(e)

        print("Sir could you say that again...")
        talk('sorry boss could you say that again')
        return"None"
    return command
def send_email(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('syedabdulkareem.13@gmail.com','Discoraja@69')
    server.sendmail('syedabdulkareem.13@gmail.com', to, content)
    server.close()

def send_whatsapp (to,content,whenH,whenM):
    pywhatkit.sendwhatmsg(to,content,whenH,whenM)

#Run Jarvis.
if __name__ == "__main__":
    wishme()
    while True:
        command = takecommand().lower()

        if 'wikipedia' in command:
            talk('Yes sir searching....')
            command = command.replace("Wikipedia", "")
            result = wikipedia.summary(command, sentences=1)
            talk('According to the wikipedia..')
            print(result)
            talk(result)

        elif 'play' in command:
            talk('Yes sir right away...')
            song = command.replace('play', '')
            talk('definitely sir playing your song' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('sir the current time is' + time)

        elif 'girlfriend' in command:
            talk('no sir i am in relationship with python')

        elif 'siri' in command:
            talk('I kinda like siri but sir......do you have any suggestions')

        elif 'seriously' in command:
            talk('yes sir.... i love her voice sir')

        elif 'shut up' in command:
             talk('okay sir not a problem')

        elif 'open google' in command:
            webbrowser.open("google.com")
            talk('Opening Google sir')

        elif 'open facebook' in command:
            webbrowser.open("facebook.com")
            talk('Opening Facebook sir')

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")
            talk('Opening Stackoverflow sir')

        elif 'open whatsapp web' in command:
            webbrowser.open("Whatsapp Web")
            talk('Opening whatsapp web sir')

        elif 'open youtube' in command:
            webbrowser.open("Youtube")
            talk('Opening Youtube sir')

        elif 'joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'weather' in command:
            info = wikipedia.summary('weather', 1)
            print(info)
            talk(info)

        elif 'change your voice to female' in command:
            talk('Changing my voice to Female one sir...')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1])
            talk('sir ... changed my voice to female one ')
            talk('and hows my new voice')

        elif ' change your voice to male' in command:
            talk('Changing my voice to male one sir...')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1])
            talk('sir ... changed my voice to male one ')
            talk('and hows my new voice')

        elif 'stop clock' in command:
            talk('yes sir press start to start')
            talk('and stop to end the Stop clock')
            choice = str(input("Enter start to start Stop clock"))
            if choice == "start":
                start_time_H = datetime.datetime.now().hour
                start_time_M = datetime.datetime.now().minute
                start_time_S = datetime.datetime.now().second
            choice2 = str(input("Enter stop to stop"))
            if choice2 == "stop":
                stop_time_H = datetime.datetime.now().hour
                stop_time_M = datetime.datetime.now().minute
                stop_time_S = datetime.datetime.now().second

            time_taken_H = stop_time_H - start_time_H
            time_taken_M = stop_time_M - start_time_M
            time_taken_S = stop_time_S - start_time_S

            print("Time taken is")
            print(timetakenH)
            talk('Hours taken..')
            talk(timetakenH)

            print("Minutes taken is")
            print(timetakenM)
            talk('Minutes taken..')
            talk(timetakenM)

            print("Seconds taken is")
            print(timetakenS)
            talk('Seconds taken...')
            talk(timetakenS)

        elif 'countdown' in command:
            talk('sure sir......')
            talk('enter the seconds for countdown and press enter to start')


            def countdown (t):
                while t:
                    minutes, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(minutes, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    t -= 1
                print("Time Up Sir...")
                talk('time up sir.....')
                winsound.PlaySound("*", winsound.SND_ALIAS)
                winsound.PlaySound("*", winsound.SND_ALIAS)



            t = input("Enter time in seconds:")
            countdown(int(t))

        elif 'set alarm' in command:

            talk('yes sir right away....')
            talk('please type the hours,to set the alarm sir...?')
            alarmH = int(input("What time do you want to wake up?"))
            talk('At what minute sir....?')
            alarmM = int(input("At what Minute?"))
            talk('AM or PM sir?')
            amPm = str(input("am or pm?"))

            if amPm == "pm" :
                alarmH = alarmH + 12

            while 1 == 1 :
                if (alarmH == datetime.datetime.now().hour and
                        alarmM == datetime.datetime.now().minute):
                    print("TIME UP")
                    talk('sir time up sir')
                    talk('sir time upp')
                    winsound.PlaySound("*", winsound.SND_ALIAS)
                    winsound.PlaySound("*", winsound.SND_ALIAS)
                    winsound.PlaySound("*", winsound.SND_ALIAS)
                    winsound.PlaySound("*", winsound.SND_ALIAS)

                    break

        elif 'open camera' in command:
            talk ('yes sir right away....')
            print("Opening camera sir.....")
            talk('sir to close the camera press q on your keyboard')
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame = cam.read()
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('camera', frame)

        elif 'activate motion capture' in command:
            print('Activating motion capture sir....')
            talk('activating motion capture sir....')
            talk('for Deactivating motion capture simply press q on your keyboard...')
            cam = cv2.VideoCapture(0)
            while (cam.isOpened()):
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
                for c in contours:
                    if cv2.contourArea(c) < 2000:
                        continue
                    x, y, h, w = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y), (x + h, y + w), (0, 255, 0), 2)
                    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('Jarvis Cam', frame1)

        elif 'email to alexa' in command:
            try:
                talk('sir what should I send...')
                content = takecommand()
                to = ('')
                sendEmail(to, content)
                talk = ('Your Email has been sent sir...')
            except Exception as e:
                print(e)
                talk('I am sorry sir.. , I am not able to sent this Email')

        elif 'send whatsapp messages' in command:
            try:
                talk('sir what should I send...')
                talk('sir say the number to whom it should be sent')
                to = takecommand()
                talk('what would be the message you want to send')
                content = takecommand()
                talk('at what hours do you want me to send')
                whenH = takecommand()
                talk('at what minutes do you want me to send')
                whenM = takecommand()
                sendwhatsapp(to,content,whenH,whenM)
                talk('message sent sir')
            except Exception as e:
                print(e)
                talk('I am sorry sir...., I am not able to sent the message')

        elif 'shut down my' in command:
            talk('okay sir as you commanded')
            pywhatkit.shutdown(90)
            talk('the computer will be shutting down in less than t minus 90 seconds')

        elif 'cancel shutdown' in command:
            talk('as you commanded to terminate shutdown')
            pywhatkit.cancelShutdown()
            talk('I have terminated the shutdown for you sir')

        elif 'Thanks you' in command:
            talk('not a problem sir ')
            talk('its my responsibility sir')

        # elif 'lets talk' in command:
        #     talk('I have somethings to catch up')
        #     talk('meet my friend SARA')
        #     talk('She is a chat_bot')
        #     chat_bot.main()








