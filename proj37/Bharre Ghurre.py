# importing the required modules

import random
import pyttsx3
import speech_recognition as sr

i = random.randint(1000, 9999)
attempts = 1

# printing out instructions
print(" \t Bharre Gurre: The Guessing Game \n  ")
print(" \tInstructions \n")
print("For every digit that you guess correctly in the correct place, you have a 'bharre'.")
print("For every digit you guess correctly but in the wrong place, you get a 'gurre'.")
print("Every time the you make a guess, your number of attempts will be shown.")
print("Once you guess the entire number correctly, the game is over. \n")


# reading out instructions

engine = pyttsx3.init()
engine.setProperty('rate', 1000)
engine.say("For every digit that you guess correctly in the correct place, you have a 'bharrey'")
engine.say("For every digit you guess correctly but in the wrong place, you get a 'ghoorrey'.")
engine.say("Every time you make a guess, your number of attempts will be shown.")
engine.say("Once you guess the entire number correctly, the game is over.")

engine.runAndWait()


while True:
    try:
        print(" \t Bharre Gurre: The Guessing Game \n  ")

        print("Attempt Number:", attempts)

        bharre = []
        gurre = []

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say("Attempt Number: " + str(attempts))
        engine.say("Please guess a four digit number. Enter 0 to play another game.")

        # using text to speech to start game with user input

        engine.runAndWait()
        r = sr.Recognizer()

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say("Should we begin?")

        engine.runAndWait()

        a = input("Enter 'yes' to start.")

        if a == 'yes':

            # using speech recognition
            with sr.Microphone() as source:
                print("Speak:")
                engine = pyttsx3.init()
                engine.setProperty('rate', 150)
                engine.say("Speak.")

                engine.runAndWait()

                audio = r.listen(source)

            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 140)
                engine.say("Your number is" + r.recognize_google(audio))

                engine.runAndWait()

                print(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            num = int(r.recognize_google(audio))

        attempts += 1

        a = list(str(num))
        b = list(str(i))

        # basic code for the game
        if num == 0:
            break

        if len(a) < 4 or len(a) > 4:
            print("Please enter a four digit number")
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say("Please enter a four digit number")
            engine.runAndWait()

        for x in a:
            if b[a.index(x)] == x:
                bharre.append(x)
                # print(bharre)

            elif x in b:
                gurre.append(x)
                # print(gurre)

        if len(bharre) == len(a):
            print("You got lucky!!")

            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say("You got lucky!!")
            engine.runAndWait()
            break

        print(str(len(bharre)) + "Bharre   " + str(len(gurre)) + "Gurre")

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(str(len(bharre)) + "Bharre   " + str(len(gurre)) + "Gurre")
        engine.runAndWait()
        print(" \n")

    # Errors for string input and the like
    except ValueError:
        print("Don't act like an idiot and enter a number")
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say("Don't act like an idiot, and enter a number.")
        engine.runAndWait()
        print(" \n")
