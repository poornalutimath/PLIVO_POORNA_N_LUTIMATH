# SLACK AI IMAGE GENERATOR

# Slack AI Image Generator Bot

## Overview
This project is a **Slack bot** that generates images from text prompts using **Replicate’s Flux LoRA model**. It is built with **Python**, **Flask**, and uses **ngrok** for local development to expose your Flask server for Slack event subscriptions.

The bot listens for messages in Slack channels or direct messages, sends the prompt to the Replicate API to generate an image, and posts the resulting image back to the same Slack thread.

## Features
- Generates images from text prompts directly in Slack.
- Handles Slack URL verification automatically.
- Posts images to the same thread for a seamless user experience.
- Modular structure for easy maintenance and upgrades.

## Requirements
- Python 3.8+
- Flask
- Requests
- python-dotenv
- ngrok (for local testing)
- Replicate API token
- Slack Bot Token

## Setup Instructions

### 1. Clone the repository
```bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt


REPLICATE_API_TOKEN=your_replicate_api_token_here
SLACK_BOT_TOKEN=your_slack_bot_token_here

ngrok http 5000

python main.py

project-folder/
│
├── main.py          # Flask app initialization and environment setup
├── routes.py        # Slack webhook route and Replicate API integration
├── .env             # Environment variables (not committed)
├── requirements.txt # Python dependencies
├── README.md        # Project documentation

