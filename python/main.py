from openai import OpenAI
from voice import speak, listen
from memory import save_memory, load_memory
from whatsapp import send_message
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

memory = load_memory()

print("🤖 Adil AI Started!")

if "name" not in memory:

    name = input("Bot: Tumhara naam kya hai?\nYou: ")

    memory["name"] = name

    save_memory(memory)

else:
    name = memory["name"]

print(f"\nBot: Welcome back {name} 😄")

speak(f"Welcome back {name}")

while True:
    # user = input(f"\n{name}: ")
    user = listen()

    if "whatsapp" in user.lower():
        send_message()
        continue

    if user.lower() == "exit":
        print("Bot: Bye 👋")
        speak("Bye")
        break

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a smart AI assistant."
            },
            {
                "role": "user",
                "content": user
            }
        ]
    )

    reply = response.choices[0].message.content

    print("\nBot:", reply)

    speak(reply)
    
    