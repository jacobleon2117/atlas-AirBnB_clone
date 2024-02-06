#!/usr/bin/python
"""
Module for console
"""
import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def split_curly_braces(e_arg):
    """
    Splits the curly braces for the update method
    """
    curly_braces = re.search(r"\{(.*?)\}", e_arg)

    if curly_braces:
        id_with_comma = shlex.split(e_arg[:curly_braces.span()[0]])
        id = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, arg_dict
    else:
        commands = e_arg.split(",")
        if commands:
            try:
                id = commands[0]
            except Exception:
                return "", ""
            try:
                attr_name = commands[1]
            except Exception:
                return id, ""
            try:
                attr_value = commands[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    