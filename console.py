#!/usr/bin/python3
"""import modules"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '
    file = None
    def do_quit(self, endidx):
        'Quit command to exit the program'
        return True
    
    def do_EOF(self, line):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
