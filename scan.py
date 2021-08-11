from typing import *;

def pushStringTo(string: str, array: List[str]) -> Tuple[str, List[str]]:
    if string != "":
        array.append(string);
    return ("", array);

def scan(input: str) -> List[str]: 
    current = "";
    output: List[str] = [];
    inQuote = False;

    for character in input:
        if inQuote:
            if character == '"':
                inQuote = False;
                current, output = pushStringTo(current, output);
            else:
                current += character;

        elif not inQuote:
            if character == '"':
                inQuote = True;
                current, output = pushStringTo(current, output);
            elif character == ' ':
                current, output = pushStringTo(current, output);
            else:
                current += character;

    current, output = pushStringTo(current, output);

    return output;