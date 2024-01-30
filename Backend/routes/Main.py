from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' 

# Blueprint imports
#from RustPlusWeb import RustPlus
#app.register_blueprint(User, url_prefix="/user")

@app.route("/")
def index():
    return "Hi"