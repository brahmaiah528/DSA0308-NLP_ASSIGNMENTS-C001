
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

def earley_parser(sentence):
    words = sentence.split()
    n = len(words)
    chart = [set() for _ in range(n + 1)]

    chart[0].add(("S'", ("S",), 0, 0))

    for i in range(n + 1):
        changed = True

        while changed:
            changed = False

            for state in list(chart[i]):
                lhs, rhs, dot, start = state

                if dot < len(rhs):
                    next_symbol = rhs[dot]

                    if next_symbol in grammar:
                        for production in grammar[next_symbol]:
                            new_state = (next_symbol, tuple(production), 0, i)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                    elif i < n and next_symbol == words[i]:
                        chart[i + 1].add(
                            (lhs, rhs, dot + 1, start)
                        )

                else:
                    for old_state in list(chart[start]):
                        old_lhs, old_rhs, old_dot, old_start = old_state

                        if old_dot < len(old_rhs) and old_rhs[old_dot] == lhs:
                            new_state = (
                                old_lhs, old_rhs, old_dot + 1, old_start
                            )
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

    return ("S'", ("S",), 1, 0) in chart[n]


sentence = "the cat chased a dog"

if earley_parser(sentence):
    print("Sentence is Accepted")
else:
    print("Sentence is Rejected")

