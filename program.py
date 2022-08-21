from pynput.keyboard import Key, Listener

def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interogatives = ("how", "why", "how", "did you", "can you", "what")

    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)



results = []

results = []
while True:
    user_input = input("Say something: ")

    if user_input == "\end":
        break
    elif len(user_input) == 0:
        print("You havent' entered anything. Type a sentence or type '\end' to end the program.")
    else:
        results.append(sentence_maker(user_input))

print("\n".join(results))
