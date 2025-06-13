
from flask import Flask,render_template,request,session,redirect,url_for
from os import urandom
import default_gen
from default_gen import char_map_all
app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(32)

@app.route('/')
def main():
    return render_template('html/main_page.html')

@app.route('/dictionary')
def dictionary():
    return render_template('html/dictionary.html')

@app.route('/about')
def about():
    return render_template('html/about.html')

@app.route('/contact')
def contact():
    return render_template('html/contact.html')

@app.route('/login')
def login():
    return render_template('html/login.html')




@app.route('/change', methods = ['POST'])
def encode():
    msg = request.json
    text = msg.get('text')
    select_start = msg.get('select_start')
    select_end = msg.get('select_end')
    if msg.get('select?'):
        replaced =  default_gen.replace_text(text[select_start:select_end].lower(),char_map_all)
        text = text[:select_start] + replaced + text[select_end:]
    else:
        text = default_gen.replace_text(text,default_gen.char_map2)
    

    return text



#if site not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('html/error404.html'), 404


if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)