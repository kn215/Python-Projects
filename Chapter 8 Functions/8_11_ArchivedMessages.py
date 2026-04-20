def show_messages(messages):
    """A function that prints a list of messages"""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message than move it to sent"""
    print("\nsending messages")
    while messages:
        current_messages = messages.pop()
        print(current_messages)
        sent_messages.append(current_messages)

messages = ['What is your name?', 'What are your plans this weekend?', 'Nice to meet you!']

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal List:")
print(messages)
print(sent_messages)
#show_messages(messages)