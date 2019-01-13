from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route(''/showquestions1')
def showquestions():
    return render_template('quiz.html')

@app.route('/addanswer1', methods=['POST'])
def addanswer():
    _email_user = request.form['inputEmail']
    _cat1 = request.form['a1']
    _cat2 = request.form['a2']
    _cat3 = request.form['a3']
    _email_recipient = request.form['inputEmail_Recipient']

if _email_user and _cat1 and _cat2 and _cat3 and _email_recipient:
    return json.dumps({'html': '<span>All fields good !! </span>'})
else:
    return json.dumps({'html': <span>Enter the required fields </span>'})
if __name__ == '__main__':
    app.run(debug=True)
