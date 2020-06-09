import os

from flask import Flask,render_template


# Create a instance of the class:
app=Flask(__name__)

#Use a Decorator  

@app.route('/')
def index():

    return(render_template("index.html"))



@app.route("/about")
def about():
    return(render_template("about.html"))


if __name__=="__main__":
    app.run(host=os.environ.get("IP","0.0.0.0"),
    port=int(os.environ.get("PORT","5000")),debug=True)


