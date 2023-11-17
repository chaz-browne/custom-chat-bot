from openai import OpenAI
import sys, time, random

client = OpenAI(api_key="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")
#this is the area where all of my responses and the computer stores will be remembered.
conversation = []

#small function I made to add a cooler typing animation for my text
def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(.05)
    return ''
print_slow("I can be anything just tell me!\n")

#allows for small information to be stored about the character than we are creating
given_name = input(print_slow("What is their name?:\n"))
given_personality = input(print_slow("Describe their personality: \n"))
given_dislikes = input(print_slow("Describe what they dislike:\n"))
given_likes = input(print_slow("Describe what they like:\n"))

#a place to store all of the variables that we gave it.
character = f"""
Here's all the information about yourself!
Name: {given_name}
Personality: {given_personality}
Dislikes: {given_dislikes}
Likes: {given_likes}
"""
#adds characterinfo to the end of the list so that it remembers.
conversation.append({"role": "system", "content": character})

print_slow("Now say hi!\n")

#the conversation will continue until you send an "x"
    #takes a message you give it and stores the information
    #utilizes chatgpt so that a response can be given.   
    #locates the given response so that it can be grabbed.
    #adds the reply to the messages system so that it is remembered

while input != "quit()":

    new_message = input("")
    conversation.append({"role": "user", "content": new_message })
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.9,
        max_tokens=200
    )

    reply = completion.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})
    print_slow(reply)
