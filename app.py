<<<<<<< HEAD
from flask import Flask,render_template # type: ignore
=======
from flask import Flask,render_template,request,session
>>>>>>> caf9e8a807ec26e4ae3af14124eced721c166a75
from os import urandom
import default_gen

app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(32)

@app.route('/')
def main():
    #tutaj trzeba dac ten tekst
    msg = 'hello world'


    return render_template('html/main_page.html',media = msg)
@app.route('/change', methods = ['POST'])
def encode():
    msg = request.json
    app.logger.warning(msg.get('name'))
    text = default_gen.replace_text(msg.get('text'),default_gen.char_map10)
    

    return text


if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)