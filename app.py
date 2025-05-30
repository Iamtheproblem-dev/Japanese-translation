from flask import Flask,render_template
from os import urandom

app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(32)

@app.route('/')
def main():
    msg = 'hello world'


    return render_template('html/main_page.html',media = msg)


if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)