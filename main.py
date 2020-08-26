from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '1234567890'

if __name__ == '__main__':
    app.run()
