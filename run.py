import os

from flask import Flask,render_template


# Create a instance of the class:
app=Flask(__name__)

#Use a Decorator  

@app.route('/')
def index():

    return("<h1>Hello there</h1>")


@app.route("/<username>")
def user(username):
    return("Hi"+username)


@app.route("/<username>/<message>")
def send_message(username,message):
    return("{0}:{1}".format(username,message))



if __name__=="__main__":
    app.run(host=os.environ.get("IP","0.0.0.0"),
    port=int(os.environ.get("PORT","5000")),debug=True)


