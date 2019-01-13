from flask import Flask, render_template, flash, request, url_for, redirect
app = Flask(static_folder='C:\\Users\\kasey\\Desktop\\starterhacks\\starterhacks2019\\static')

@app.route("/")
def hello():
    return render_template("index.html", "backup.html")

if __name__ == '__main__':
    app.run(debug=True)
