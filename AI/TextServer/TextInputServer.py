from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable cross-origin requests
import json

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
CORS(app)  # Allow requests from any origin (needed for Cloudflare Tunnel)

latest_message = ""

@app.route('/submit', methods=['POST'])
def receive_message():
    global latest_message
    data = request.get_json()
    latest_message = data.get("text", "")
    print("Received:", latest_message)

    # Run your debugging / NLP functions
    try:
        with open('invalid.json', 'w') as file:
            json.dump({latest_message}, file,indent=4)
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    # Respond with JSON
    return jsonify({
        "response": f"You said: {latest_message} Recieved"
    })

if __name__ == '__main__':
    # Make server accessible externally (Cloudflare tunnel will forward requests here)
    app.run(host="0.0.0.0", port=5000, debug=True)
