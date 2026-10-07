from google import genai
import os

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY is not set.")
    exit()

client = genai.Client(api_key=api_key)

print("===================================")
print("       GEN-AI STUDY ASSISTANT")
print("===================================")
print("Ask me any study question.")
print("Type 'exit' to stop.\n")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        print("Assistant: Goodbye! Happy studying 😊")
        break

    if not question:
        continue

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question
        )

        print("Assistant:", response.text)
        print()

    except Exception as e:
        print("Error:", e)
        print()
