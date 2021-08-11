from typing import *;
import readline;

import lex;
import scan;
import error; 

class Console:
    def __init__(self, command_table: Dict[str, Callable[..., Any]], prompt: str):
        self.command_table = command_table;
        self.prompt = prompt;
    def runRepl(self):
        while True:
            raw_input = input(self.prompt);
            try:
                self.parse(raw_input);
            except Exception as e:
                print(type(e).__name__, ":", e);
    def parse(self, input: str):
        scanned_input: List[str] = scan.scan(input);
        function_name: str = scanned_input[0];
        scanned_input.pop(0);
        lexed_input = lex.lex(scanned_input);
        function: Callable[..., Any] = self.help;
        if function_name == "help":
            self.help();
            return;
        else:
            try:
                function = self.command_table[function_name];
            except:
                raise error.NoSuchCommand("You typed in the name of a command that does not exist.");
        function(*lexed_input);
    def help(self):
        for (name, _) in self.command_table:
            print(name)

def horbs(*args):
    print(args[0]);

console = Console({"horbs": horbs}, ">> ");
console.runRepl();