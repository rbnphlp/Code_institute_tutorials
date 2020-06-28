import os
from flask import Flask,render_template,redirect,request,session
from datetime import datetime


# Create a instance of the class:
app=Flask(__name__)

app.secret_key="mykey"


# add  messages :
messages=[]

def add_messages(username,message):
#Use a Decorator  
 now=datetime.now().strftime("%H:%M:%S")

 messages_dic={"timestamp": now,"from":username,"message":message}

 messages.append(messages_dic)


@app.route('/',methods=["GET","POST"]) # Add routes for both post and get methods
def index():
    if request.method=="POST":
        # Get username from the form 
        session["username"]=request.form["username"]
        
    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route("/<username>",methods=["GET","POST"])
def user(username):
    if request.method=="POST":
        username=session["username"]
        #get the message from the messahe form
        message=request.form["message"]
        add_messages(username,message)
        return(redirect(session["username"]))

    return render_template("chat.html")


    return (render_template("chat.html",username=username,chat_messages=messages))


@app.route("/<username>/<message>")
def send_message(username,message):

    add_messages(username,message)

    return(redirect("/"+username))



if __name__=="__main__":
    app.run(host=os.environ.get("IP","0.0.0.0"),
    port=int(os.environ.get("PORT","5000")),debug=True)


