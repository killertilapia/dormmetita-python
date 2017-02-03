
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_action():
    return 'Hello Eric!'


if __name__ == '__main__':
    app.run(debug=True)

