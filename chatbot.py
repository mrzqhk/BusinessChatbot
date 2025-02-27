from flask import Flask, request, render_template
import requests
import time

app = Flask(__name__)

OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "MyChatbot"
}

def get_openrouter_response(user_input):
    data = {
        "model": "cognitivecomputations/dolphin3.0-mistral-24b:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant for a small business."},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 100
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Error: {response.text}"
    except KeyError:
        return "Sorry, the server returned an unexpected response."
    except requests.exceptions.RequestException as e:
        return f"Network error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["message"]
        reply = get_openrouter_response(user_input)
        time.sleep(1)  # Avoid rate limits
        return render_template("index.html", user_input=user_input, reply=reply)
    return render_template("index.html", user_input="", reply="")

if __name__ == "__main__":
    app.run(debug=True)
