
import re

def parse_fopc(expression):
    tokens = re.findall(r'[A-Za-z_]\w*|[(),&|~]', expression)
    print("Tokens:", tokens)

    if expression.count("(") != expression.count(")"):
        print("Invalid FOPC Expression")
    elif re.fullmatch(r'[\w\s(),&|~]+', expression):
        print("FOPC Expression Parsed Successfully")
    else:
        print("Invalid Expression")

expression = input("Enter logical expression: ")
parse_fopc(expression)
