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
                margin: 0;
                padding: 0;
                background-color: #f5f5f5;
            }
            header {
                background-color: #333;
                color: white;
                padding: 20px;
                text-align: center;
                font-size: 1.8em;
                font-weight: bold;
            }
            .center-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: calc(100vh - 80px); /* 100% viewport height minus header */
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
        <header>Forest Fire Tracking App v1.0.0 - Bare Minimum</header>
        <div class="center-container">
            <form action="/echo_user_input" method="POST">
                <label for="user_input">Please enter a text:</label><br>
                <input type="text" name="user_input" id="user_input"><br>
                <input type="submit" value="Submit!">
            </form>
        </div>
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
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f5f5f5;
            }}
            header {{
                background-color: #333;
                color: white;
                padding: 20px;
                text-align: center;
                font-size: 1.8em;
                font-weight: bold;
            }}
            .center-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: calc(100vh - 80px);
                text-align: center;
            }}
            a {{
                margin-top: 20px;
                color: #4CAF50;
                text-decoration: none;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <header>Forest Fire Tracking App v1.0.0 - MVP</header>
        <div class="center-container">
            <h2>You entered:</h2>
            <p><strong>{input_text}</strong></p>
            <a href="/">← Go back</a>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()