# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/slack", methods=["POST"])
# def slack():
#     return jsonify({"text": "Slack endpoint working ✅"})

# if __name__ == "__main__":
#     app.run(port=5000)
#this works
# import os
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify

# # ✅ Load environment variables
# load_dotenv()
# REPLICATE_TOKEN = os.getenv("REPLICATE_API_TOKEN")
# SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# # Temporary check (remove after confirming)
# print("Replicate:", REPLICATE_TOKEN)
# print("Slack:", SLACK_TOKEN)

# # Create Flask app
# app = Flask(__name__)

# # Slack endpoint
# @app.route("/slack", methods=["POST"])
# def slack():
#     return jsonify({"text": "Slack endpoint working ✅"})

# # Run the app
# if __name__ == "__main__":
#     app.run(port=5000)

# import os
# from dotenv import load_dotenv
# from flask import Flask, request, Response

# # ✅ Load environment variables
# load_dotenv()

# REPLICATE_TOKEN = os.getenv("REPLICATE_API_TOKEN")
# SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# # Temporary check
# print("Replicate:", REPLICATE_TOKEN)
# print("Slack:", SLACK_TOKEN)

# app = Flask(__name__)
#this works
# print("Replicate:", REPLICATE_TOKEN)
# print("Slack:", SLACK_TOKEN)

# from dotenv import load_dotenv
# import os
# import requests  # for making API calls

# # 1️⃣ Load your .env file
# load_dotenv()

# # 2️⃣ Get your Replicate API token
# replicate_token = os.getenv("REPLICATE_API_TOKEN")


# import os
# import requests
# from flask import Flask, request, jsonify
# from dotenv import load_dotenv

# # -------------------------------
# # Load environment variables
# # -------------------------------
# load_dotenv()
# REPLICATE_TOKEN = os.getenv("REPLICATE_API_TOKEN")
# SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# # Temporary check (remove after testing)
# print("Replicate:", REPLICATE_TOKEN)
# print("Slack:", SLACK_TOKEN)

# # -------------------------------
# # Flask App
# # -------------------------------
# app = Flask(__name__)

# @app.route("/slack", methods=["POST"])
# def slack():
#     data = request.json

#     # Extract Slack event info
#     event = data.get("event", {})
#     user_text = event.get("text")
#     channel_id = event.get("channel")
#     thread_ts = event.get("ts")

#     if not user_text:
#         return jsonify({"text": "No prompt found!"})

#     # -------------------------------
#     # Call Replicate API
#     # -------------------------------
#     replicate_url = "https://api.replicate.com/v1/predictions"
#     headers = {
#         "Authorization": f"Token {REPLICATE_TOKEN}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "black-forest-labs/flux-kontext-pro",
#         "input": {"prompt": user_text}
#     }

#     try:
#         response = requests.post(replicate_url, headers=headers, json=payload)
#         result = response.json()
#         # Grab first image output
#         image_url = result.get("output", [])[0]
#     except Exception as e:
#         print("Replicate API error:", e)
#         return jsonify({"text": "Failed to generate image 😅"})

#     # -------------------------------
#     # Send image back to Slack
#     # -------------------------------
#     slack_post_url = "https://slack.com/api/chat.postMessage"
#     slack_payload = {
#         "channel": channel_id,
#         "text": "Here’s your generated image!",
#         "thread_ts": thread_ts,
#         "blocks": [
#             {
#                 "type": "image",
#                 "image_url": image_url,
#                 "alt_text": "Generated Image"
#             }
#         ]
#     }
#     slack_headers = {"Authorization": f"Bearer {SLACK_TOKEN}"}
#     requests.post(slack_post_url, headers=slack_headers, json=slack_payload)

#     return jsonify({"text": "Generating your image... ✅"})


# # -------------------------------
# # Run the Flask app
# # -------------------------------
# if __name__ == "__main__":
#     app.run(port=5000)


# app.py
from dotenv import load_dotenv
import os
import requests
from flask import Flask, request, jsonify

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()
REPLICATE_TOKEN = os.getenv("REPLICATE_API_TOKEN")
SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Temporary check (remove after testing)
print("Replicate:", REPLICATE_TOKEN)
print("Slack:", SLACK_TOKEN)

# -------------------------------
# Flask App
# -------------------------------
app = Flask(__name__)

@app.route("/slack", methods=["POST"])
def slack():
    data = request.json

    # ---- 1️⃣ Handle Slack URL verification ----
    if data.get("type") == "url_verification":
        return jsonify({"challenge": data["challenge"]})

    # ---- 2️⃣ Handle normal Slack events ----
    event = data.get("event", {})
    user_text = event.get("text")
    channel_id = event.get("channel")
    thread_ts = event.get("ts")

    if not user_text:
        return jsonify({"text": "No prompt found!"})

    # -------------------------------
    # Call Replicate API
    # -------------------------------
    replicate_url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {REPLICATE_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "black-forest-labs/flux-kontext-pro",
        "input": {"prompt": user_text}
    }

    try:
        response = requests.post(replicate_url, headers=headers, json=payload)
        result = response.json()
        # Grab first image output
        image_url = result.get("output", [])[0]
    except Exception as e:
        print("Replicate API error:", e)
        return jsonify({"text": "Failed to generate image 😅"})

    # -------------------------------
    # Send image back to Slack
    # -------------------------------
    slack_post_url = "https://slack.com/api/chat.postMessage"
    slack_payload = {
        "channel": channel_id,
        "text": "Here’s your generated image!",
        "thread_ts": thread_ts,
        "blocks": [
            {
                "type": "image",
                "image_url": image_url,
                "alt_text": "Generated Image"
            }
        ]
    }
    slack_headers = {"Authorization": f"Bearer {SLACK_TOKEN}"}
    requests.post(slack_post_url, headers=slack_headers, json=slack_payload)

    return jsonify({"text": "Generating your image... ✅"})

# -------------------------------
# Run the Flask app
# -------------------------------
if __name__ == "__main__":
    app.run(port=5000)

