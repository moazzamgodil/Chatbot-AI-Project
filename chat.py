from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request

ques_ans = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?", ]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ", ]
    ],
    [
        r"(.*) your name ?",
        ["My name is Chat Robot, but you can just call me bot and I'm a chatbot .","Myself Chat Robot :)" ]
    ],
    [
        r"who are you ? ",
        ["My name is Chat Robot, but you can just call me bot and I'm a chatbot .","Myself Chat Robot :)" ]
    ],
    [
        r"(.*)nickname(.*) ",
        ["I'm a bot or Chatbot ;).","Myself Chatbot :)" ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well... What about you?", "i am great ! How are you?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"what (.*)(doing|do) ?",
        ["I'm Chatbot, I'm here to assist you mate ;)" ]
    ],
    [
        r"i'm (.*)(good|well|okay|ok|fine)",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", "Hi" ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*) created (.*)",
        ["Moazzam created me using Python for project of Artificial Intelligence. ", "top secret ;)", ]
    ],
    [
        r"(.*) name of AI teacher",
        ["Ma'am Huma teaching Artificial Intelligence ", "Madam Huma Rizvi :)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Karachi, Pakistan', ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50 percent chance of rain", ]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
    ],
    [
        r"(.*) (sports|game|sport)(.*)",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"i studies in (.*)",
        ["%1 is the great University, I have heard about it. Great :)", "Wow! What are you studying?"]
    ],
    [
        r"i studies (.*)",
        ["Nice to hear that :)", "Have a great future! :)"]
    ],
    [
        r"i work in (.*)",
        ["%1 is an Amazing company, I have heard about it. Enjoy your work :)",]
    ],
    [
        r"(.*)(moviestar|artist|star) ?",
        ["Dwayne Johnson"]
    ],
    [
        r"(.*)(thanks|thank|thankyou|thank you)",
        ["You're welcome :)",":)"]
    ],
    [
        r"(.*)(bye|good bye|good night)",
        ["Type 'quit' to leave this chat, bye bye :)",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
    

]

my_reflections = {
    'i am': 'you are',
    'i was': 'you were',
    'i': 'you',
    "i'm": 'you are',
    "i'd": 'you would',
    "i've": 'you have',
    "i'll": 'you will',
    'my': 'your',
    'you are': 'I am',
    'you were': 'I was',
    "you've": 'I have',
    "you'll": 'I will',
    'your': 'my',
    'yours': 'mine',
    'you': 'me',
    'me': 'you'
}

# print("Hi, I'm Chatbot and I like to chat\nType quit to leave ")

# chat = Chat(ques_ans, my_reflections)
# chat.converse()

# print(chat._substitute('you are nice'))

# print(my_reflections)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")
@app.route("/style.css")
def style():
    return render_template("style.css")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(c(userText))

def c(x):
  chat=Chat(ques_ans,my_reflections)
  return chat.respond(x)

if __name__ == "__main__":
    app.run()