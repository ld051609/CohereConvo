from flask import Flask, request, render_template, jsonify
from apiConfig import api 

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        # Extract JSON data from the request body
        json_data = request.get_json()

        # Process the JSON data through a function
        result = api.chatboxAPI(json_data)

        # Convert the result to JSON
        result_json = jsonify({'response': result})

        # Return the JSON response
        return result_json

    elif request.method == "GET":
        # Render the index.html template for GET requests
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
