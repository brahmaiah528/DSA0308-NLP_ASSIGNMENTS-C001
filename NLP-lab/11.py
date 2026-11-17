
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return pos + 1
        return None

    for production in grammar[symbol]:
        current_pos = pos

        for item in production:
            result = parse(item, words, current_pos)

            if result is None:
                break

            current_pos = result
        else:
            return current_pos

    return None

sentence = "the cat chased a dog"
words = sentence.split()

result = parse("S", words, 0)

if result == len(words):
    print("Sentence is Accepted")
else:
    print("Sentence is Rejected")
