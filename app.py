from flask import Flask, request, render_template

app = Flask('demo')

@app.route('/hello')
def hello():
    name = request.args.get('name')
    greeting = request.args.get('greeting')
    return '{greeting}, {name}!'.format(
        greeting=greeting, name=name)

@app.route('/bye')
def bye():
    return 'Goodbye!'

@app.route('/')
def main():
    return "You're at the beginning!"

@app.route('/wiki/<topic>')
def wiki(topic):
    return topic

@app.route('/welcome')
def welcome():
    name = request.args.get('name')
    return render_template(
        'welcome.html', name=name)

app.run(debug=True)
