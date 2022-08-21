from pynput.keyboard import Key, Listener

def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interogatives = ("how", "why", "how", "did you", "can you", "what")

    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)



results = []

# user_input = input("Say something: ")

# if len(user_input) == 0:
#     print("oops!")
# else:
#     while True:

#         if user_input == "\end":
#             break
#         else:
#             results.append(sentence_maker(user_input))

# if len(results) == 0:
#     print("Program complete")
# else:
#     print(" ".join(results))

results = []
while True:
    user_input = input("Say something: ")

    if user_input == "\end":
        break
    elif len(user_input) == 0:
        print("You havent' entered anything. Type a sentence or type '\end' to end the program.")
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
