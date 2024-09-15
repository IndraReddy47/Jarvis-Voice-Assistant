import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import sys

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "b59719c4900444cfb14a98561ee11969"

def speak(text):
    engine.say(text)
    engine.runAndWait()

'''def aiprocess(command):
    client = OpenAI(
  api_key = "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",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant and your name is jarvis you are very skilled and capable of answer anything across various topics"},
        {
            "role": "user", "content": "command ? "
        }
    ]
)

    return (completion.choices[0].message.content)
'''


def processcommand(c):
        if "open google" in c.lower():
            webbrowser.open("https://www.google.co.in/")
        elif "open facebook" in c.lower():
            webbrowser.open("https://www.facebook.com/")
        elif "open twitter" in c.lower():
            webbrowser.open("https://x.com/home")
        elif "open youtube" in c.lower():
            webbrowser.open("https://www.youtube.com/")
        elif c.lower().startswith("play"):
            song = c.lower().split(" ")[1]
            link = musiclibrary.music[song]
            webbrowser.open(link)

        elif "news" in c.lower():
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
            # Parse the JSON response   
                data = r.json()
            
            # Extract the articles
                articles = data.get('articles', [])
            
            # Print the titles of the top headlines
                for article in articles:
                    speak(article['title'])

        elif "exit" in c.lower():
            print("the program is stopped. thank you")
            sys.exit()


       # else:
       #    output = aiprocess(command)
       #   speak(output)
       #   pass

       

if __name__ == "__main__":
    speak("initializing jarvis..... ")

    #listen for the wake word jarvis

    while True:
    # obtain audio from the microphone
        r = recognizer
        print("recognizing....")

        try:
            with sr.Microphone() as source:
                print("listening.....")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "jarvis"):
                speak("yeah")

                with sr.Microphone() as source:
                    print("jarvis active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)



        except Exception as e:
            print("error; {0}".format(e))