from flask import Flask, make_response, jsonify, request, send_from_directory, render_template
import os
from datetime import datetime

thispath = os.path.dirname(os.path.realpath(__file__))

APPNAME = "xss-demo"
VERSION = "v0.1"

app = Flask(__name__)


messages = [
    {
        'name':'admin',
        'message':'This is a handy new message board.',
        'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    },
    {
        'name': 'devops',
        'message': 'Can we use this for chatting about the server?',
        'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    },
    {
        'name': 'admin',
        'message': 'Sure. It\'s secure.',
        'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    }

]

posturl = "http://localhost:8001/"

# Functions

def get_from_json (json, value):
    """
    :param json:
    :param value:
    :return:
    Check whether a value exists in a json blob """

    if value in json.keys():
            return json[value]
    else:
        return ""


@app.route('/', methods=['GET'])
def api_root_page_get():

    return render_template('index.html', messages=messages)



@app.route('/', methods=['POST'])
def api_root_page_post():

    name = request.form['name']
    message = request.form['message']
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    newmessage = {'name': name, 'message':message, 'timestamp': now}
    messages.append(newmessage)

    return render_template('index.html', messages=messages, posturl=posturl)


# Main Application Loop
if __name__ == '__main__':

    # Let's go :)
    app.run(debug=True, host='0.0.0.0', port=8001)



