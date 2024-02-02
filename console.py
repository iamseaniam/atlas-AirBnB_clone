#!/usr/bin/python3
"""Console module"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "  

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self,arg):
        """Exit the program when EOF is reached"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the PRogram")

    def help_EOF(self):
        """Help message for the EOF command"""
        print("Exit mthe program when End-of_File (EOF) is reached")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
