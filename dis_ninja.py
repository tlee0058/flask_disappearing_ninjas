from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('image.html')

@app.route('/ninja/<color>')
def display_color(color):
    return render_template('ninja.html', color = color)

app.run(debug=True)