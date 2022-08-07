from flask import request, abort, Flask
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        return request.json
    else:
        abort(400)


    


if __name__ == '__main__':
    app.run()