#!/usr/bin/python3
"""Console module"""

import cmd
import json
import models

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for the EOF command"""
        print("Exit the program when End-of_File (EOF) is reached")

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objects = models.storage.all()
            if obj_key in all_objects:
                print(all_objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objects = models.storage.all()
            if obj_key in all_objects:
                del all_objects[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objects = models.storage.all()
        if not args:
            print([str(all_objects[obj]) for obj in all_objects])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            print([str(all_objects[obj]) for obj in all_objects if args[0] in obj])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objects = models.storage.all()
            if obj_key not in all_objects:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                instance = all_objects[obj_key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(instance, attr_name, attr_value)
                instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
