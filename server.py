from flask import request, abort, Flask
import json

app = Flask(__name__)



@app.route('/')
def index():
    return "<h1>Hello CleanNavi!</h1>"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        return request.json
    else:
        abort(400)


    

