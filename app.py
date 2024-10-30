from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    
    return HELLO_HTML.format(
            str(datetime.now()))

HELLO_HTML = """
    <form action="{{ url_for("gfg")}}" method="post">
    <label for="firstname">First Name:</label>
    <input type="text" id="firstname" name="fname" placeholder="firstname">
    <label for="lastname">Last Name:</label>
    <input type="text" id="lastname" name="lname" placeholder="lastname">
    <button type="submit">Login</button>"""

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)