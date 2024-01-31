import re
import pyttsx3
import speech_recognition as sr

GREETING = 0
NAME = 1
INTERACTIONS = ["Hola, ¿Como estas?", "¿Como te llamas?"]


def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")
    return engine


def talk(engine, interaction):
    engine.say(interaction)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
    return text


def identify_greeting(reply):
    greeting = None
    patterns = ["^([A-Za-z]+) y tu", "^([A-Za-z]+)$", "yo estoy ([A-Za-z]+)$", "estoy ([A-Za-z]+)$",
                "^([A-Za-z]+) gracias"]
    for pattern in patterns:
        try:
            greeting = re.findall(pattern, reply.lower())[0]
        except IndexError:
            pass
    return greeting


def reply_greeting(engine, greeting):
    if greeting in ["bien", "excelente"]:
        talk(engine, "me alegra que estes {}".format(greeting))
    elif greeting == "mal":
        talk(engine, "Lamento escuchar eso...")


def identify_name(reply):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "soy ([A-Za-z]+)", "^([A-Za-z]+)$",
                "yo soy ([A-Za-z]+)", "^([A-Za-z]+) es mi nombre"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, reply.lower())[0]
        except IndexError:
            pass
    return name


def reply_name(engine, name):
    talk(engine, "Encantada de conocerte {}!!".format(name))


def main():
    engine = initialize_engine()

    interaction = False
    while not interaction:
        # Saludamos
        talk(engine, INTERACTIONS[GREETING])
        reply = listen()
        # Respondemos el saludo
        greet = identify_greeting(reply)
        if greet:
            reply_greeting(engine, greet)
            interaction = True
        else:
            talk(engine, "no te he entendido")
            interaction = False

    interaction = False
    while not interaction:
        # Preguntamos el nombre
        talk(engine, INTERACTIONS[NAME])
        reply = listen()
        # Respondemos el nombre
        name = identify_name(reply)
        if name:
            reply_name(engine, name)
            interaction = True
        else:
            talk(engine, "No te he entendido")
            interaction = False


if __name__ == "__main__":
    main()
