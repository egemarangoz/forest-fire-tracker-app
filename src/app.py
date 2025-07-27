#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Forest Fire Tracking App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                background-color: #f5f5f5;
            }
            h1 {
                font-size: 2em;
                font-weight: bold;
                margin-bottom: 40px;
            }
            label {
                font-size: 1.2em;
                margin-bottom: 10px;
            }
            input[type="text"] {
                padding: 8px;
                font-size: 1em;
                width: 300px;
                margin-bottom: 10px;
            }
            input[type="submit"] {
                padding: 8px 16px;
                font-size: 1em;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Forest Fire Tracking App v1.0.0 - MVP</h1>
        <form action="/echo_user_input" method="POST">
            <label for="user_input">Please enter a text:</label><br>
            <input type="text" name="user_input" id="user_input"><br>
            <input type="submit" value="Submit!">
        </form>
    </body>
    </html>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Response - Forest Fire App</title>
    </head>
    <body>
        <h2>You entered: {input_text}</h2>
        <br>
        <a href="/">Go back</a>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()