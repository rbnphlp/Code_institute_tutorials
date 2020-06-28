import os
from flask import Flask,render_template,redirect
from datetime import datetime


# Create a instance of the class:
app=Flask(__name__)



# add  messages :
messages=[]

def add_messages(username,message):
#Use a Decorator  
 now=datetime.now().strftime("%H:%M:%S")

 messages.append("({}) {}: {}".format(now,username,message))


def get_messages(messages):
    return("<br>".join(messages))


@app.route('/')
def index():

    return("<h1>Hello there</h1>")


@app.route("/<username>")
def user(username):
    return("<h1>Welcome {0} </h1>{1}".format(username,get_messages(messages)))


@app.route("/<username>/<message>")
def send_message(username,message):

    add_messages(username,message)

    return(redirect("/"+username))



if __name__=="__main__":
    app.run(host=os.environ.get("IP","0.0.0.0"),
    port=int(os.environ.get("PORT","5000")),debug=True)


