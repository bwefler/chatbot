from openai import OpenAI
client = OpenAI()


user_input = input("\nAsk something...\n\n")

#Function to form reponse
def form_response(model, messages):
    response = client.chat.completions.create(
        model = model,
        messages = messages
    )
    return response.choices[0].message.content

model = "gpt-3.5-turbo"
messages = [
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
]
print(form_response(model, messages))
