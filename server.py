from flask import Flask
import json

app = Flask(__name__)

@app.get('/')
def home():
    return 'Hello, World!'

@app.get('/test')
def test():
    return 'this is a test'


# // this will be the endpoints of the server

@app.get('/api/v1/about')
def about():
    me = {
        "name": "cesar",
        "age": 21,
        "hobbies": ["coding", "gaming", "listen to music"]
    }
    return json.dumps(me)

app.run(debug=True)