import os

from flask import Flask


# Create a instance of the class:
app=Flask(__name__)

#Use a Decorator  

@app.route('/')
def index():

    return("Hello world")



if __name__=="__main__":
    app.run(host=os.environ.get("IP","0.0.0.0"),
    port=int(os.environ.get("PORT","5000")),debug=True)


