from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello! I am Flask running on a docker instance.'


if __name__ == '__main__':
    # Note the extra host argument. If we didn't have it, our Flask app
    # would only respond to requests from inside our container
    # Default port is 5000
    app.run('0.0.0.0')
