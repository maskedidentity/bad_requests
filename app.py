from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# HTML form page for GET requests
@app.route('/')
def hello():
    return HELLO_HTML.format(str(datetime.now()))

# Dynamic search endpoint in the URL
@app.route('/search/<query>', methods=['GET'])
def search(query):
    # Process the query as needed (e.g., analyze for SQL keywords, etc.)
    # Here, we just echo back the query and timestamp
    return jsonify({
        "message": "Search query received",
        "query": query,
        "timestamp": str(datetime.now())
    })

# Endpoint to handle GET, POST, PUT, DELETE requests
@app.route('/process', methods=['GET', 'POST', 'PUT', 'DELETE'])
def process_request():
    if request.method == 'GET':
        return jsonify({"message": "GET request received", "timestamp": str(datetime.now())})
    
    elif request.method == 'POST':
        data = request.form
        fname = data.get('fname', 'Unknown')
        lname = data.get('lname', 'Unknown')
        return jsonify({"message": "POST request received", "firstname": fname, "lastname": lname})
    
    elif request.method == 'PUT':
        data = request.json
        return jsonify({"message": "PUT request received", "data": data})
    
    elif request.method == 'DELETE':
        return jsonify({"message": "DELETE request received"})

# HTML template with form action fixed
HELLO_HTML = """
    <form action="/process" method="post">
    <label for="firstname">First Name:</label>
    <input type="text" id="firstname" name="fname" placeholder="firstname">
    <label for="lastname">Last Name:</label>
    <input type="text" id="lastname" name="lname" placeholder="lastname">
    <button type="submit">Submit</button>
    </form>
    <p>Use the /search/&lt;query&gt; endpoint in the URL to perform a search.</p>
"""

if __name__ == "__main__":
    # Run the app on all network interfaces
    app.run(host="0.0.0.0", port=5000, debug=True)
