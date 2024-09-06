from flask import Flask, redirect, render_template, url_for


app=Flask(__name__)

@app.route('/',methods=["POST", "GET"])
def index():
    return render_template('chat.html')


if __name__=="__main__":
    app.run(host="127.0.0.1",
               port=5000,
               debug=True)