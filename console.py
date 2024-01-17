#!/usr/bin/python3
"""This module contains the cmd interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """A class of HBNBCommand

    implements the quit, EOF and help
    """
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
            """This method handles the EOF command
            """
            return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the ID.
        """
        class_name = line.strip()

        if not class_name:
            print("** class name missing **")
        else:
            known_classes = {'BaseModel': BaseModel}
            if class_name in known_classes:
                new_instance = known_classes[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        storage.reload()
        all_objs = storage.all()
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)

            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
