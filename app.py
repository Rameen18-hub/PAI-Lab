# from flask import Flask, jsonify, render_template
# import requests

# app= Flask(__name__)
# JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

# @app.route("/")


# @app.route("/")
# def home():
#     return render_template("index.html") 

# def home():
#     return jsonify({
#         "message": "Welcome to the Random Joke API! Go to /joke to get a random joke."

#     })

# @app.route("/joke")
# def get_joke():
#     try:
#         response = requests.get(JOKE_API_URL)
#         data = response.json()

#         if data["type"] == "single":
#             joke = data["joke"]
#         else:
#             joke = f"{data['setup']}  {data['delivery']}"

#         return jsonify({
#             "joke" : joke
#         })
#     except Exception as e:
#         return jsonify({
#             "error": "Could not fetch joke",
#             "details": str(e)
#         }),500

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/joke")
def get_joke():
    try:
        response = requests.get(JOKE_API_URL)
        data = response.json()

        if data["type"] == "single":
            joke = data["joke"]
        else:
            joke = f"{data['setup']} {data['delivery']}"

        return jsonify({
            "joke": joke
        })

    except Exception as e:
        return jsonify({
            "error": "Could not fetch joke",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)

