#!/usr/bin/python3
"""Console module"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    
    prompt = "(hbnb) "  
    
    def do_quit(self, arg):
        return True
    
    def do_EOF(self,arg):
        print()
        return True
    
    def emptyline(self):
        pass
    
    def help_quit(self):
        print("Quit command to exit the PRogram")
        
    def help_EOF(self):
        print("Exit mthe program when End-of_File (EOF) is reached")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
