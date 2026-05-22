from flask import Flask, render_template
from flask import request, jsonify
from openai import OpenAI
import json
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# MEMORY

def load_memory():

    try:

        with open("memory.json", "r") as file:

            return json.load(file)

    except:

        return {}

def save_memory(memory):

    with open("memory.json", "w") as file:

        json.dump(memory, file)

# OPENROUTER

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("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")
)

# HOME

@app.route("/")
def home():

    return render_template("index.html")

# ABOUT

@app.route("/about")
def about():

    return render_template("about.html")

# CHAT API

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    memory = load_memory()

    if "my name is" in user_message.lower():

        name = user_message.lower().replace(
            "my name is",
            ""
        ).strip()

        memory["name"] = name

        save_memory(memory)

    try:

        response = client.chat.completions.create(

            model="openai/gpt-3.5-turbo",

            messages=[

                {
                    "role": "system",

                    "content":
                    f"You are Adil AI. User memory: {memory}"
                },

                {
                    "role": "user",

                    "content": user_message
                }
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({
            "reply": reply
        })

    except Exception as e:

        print(e)

        return jsonify({
            "reply": "Error aa gaya 😅"
        })

# RUN

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)