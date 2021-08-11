from typing import *;

def lex(input: List[str]) -> List[Union[str, int]]:
    output: List[Union[str, int]] = [];
    for argument in input:
        try:
            output.append(int(argument));
        except:
            output.append(argument);
    return output;