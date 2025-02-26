# Business Chatbot

A free AI-powered chatbot for small businesses, built using Python, Flask, and OpenRouter’s Dolphin3.0-Mistral-24B API. Runs locally with a minimal web interface.

## Features
- Handles customer queries (e.g., business hours, general assistance).
- Zero-cost solution using OpenRouter’s free tier.
- Modern design with a dark green background, centered layout, and custom styling.

## Setup
1. Install Python 3.8+.
2. Create and activate a virtual environment: `python -m venv venv` and `venv\Scripts\activate` (Windows).
3. Install dependencies: `pip install flask requests gunicorn`.
4. Get an OpenRouter API key from `openrouter.ai`.
5. Update `OPENROUTER_API_KEY` in `chatbot.py`.
6. Run locally: `python chatbot.py`.
7. Access at `http://localhost:5000`.

## Skills Demonstrated
- Python
- Flask
- API Integration
- Web Development (HTML/CSS)
