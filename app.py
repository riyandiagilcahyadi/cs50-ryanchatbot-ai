from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Groq API key kamu (sudah aku masukkan)
client = Groq(api_key="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")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": user_message}],
            model="llama-3.3-70b-versatile"  # Model gratis cepat di Groq
        )
        ai_reply = response.choices[0].message.content
    except Exception as e:
        ai_reply = f"Maaf, error: {str(e)}. Coba lagi!"

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
