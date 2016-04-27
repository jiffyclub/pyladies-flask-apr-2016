from flask import Flask

app = Flask('demo')

@app.route('/hello')
def hello():
    return 'Hello!'

app.run(debug=True)
