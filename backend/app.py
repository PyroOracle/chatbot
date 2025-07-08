from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chatbot():
    """""Renders the 'chatbot.html' template when the user navigates to the root URL. This serves as the main landing page of application."""
    return render_template('chatbot.html')
