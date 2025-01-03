from flask import Flask
from dotenv import load_dotenv
import os   

load_dotenv()

app = Flask(__name__)

@app.route('/<random_string>')
def return_back(random_string):
    return f'{random_string}'

@app.route('/get-mode')
def get_mode():
    return os.getenv('MODE')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)