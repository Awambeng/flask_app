from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!' + ' this is my first web application with the python framework flask'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
