from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/')
def main():
    values = request.json
    if values['type'] == 'confirmation' and values['group_id'] == 198161648:
        return 'e571d5fa' 

if __name__ == '__main__':
    app.run()