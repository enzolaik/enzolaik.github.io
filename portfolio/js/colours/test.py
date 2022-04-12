from flask import Flask
app = Flask(name)
@app.route('/')
def index():
    return 'OLA!'
if name == "main":
    app.run(debug=False)