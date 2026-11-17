
def recognize_dialog_act(sentence):
    sentence = sentence.lower().strip()

    if sentence.endswith("?"):
        return "Question"
    elif sentence.startswith(("hi", "hello", "hey")):
        return "Greeting"
    elif any(word in sentence for word in ["thank you", "thanks"]):
        return "Thanking"
    elif sentence.startswith(("please", "can you", "could you")):
        return "Request"
    elif sentence.startswith(("bye", "goodbye")):
        return "Farewell"
    else:
        return "Statement"

dialog = input("Enter a conversation: ")

for sentence in dialog.split("."):
    if sentence.strip():
        print(sentence.strip(), "->", recognize_dialog_act(sentence))
