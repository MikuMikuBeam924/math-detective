import os
from flask import Flask
from flask_session import Session

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "detective-math-game-secret-key")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
