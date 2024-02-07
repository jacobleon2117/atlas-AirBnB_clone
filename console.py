#!/usr/bin/python3

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
        print("Exiting HBNB console")
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        print("Exiting HBNB console")
        return True

    def validate_class(self, class_name):
        """
        Validate if the class name is valid.
        """
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** Invalid class name. Valid classes are: {} **".format
                  (", ".join(self.valid_classes)))
            return False
        return True

    def validate_instance(self, class_name, instance_id):
        """ Validate if the instance exists. """
        if class_name not in storage.all():
            print("** No instance found for class '{}' and id '{}' **".format
                  (class_name, instance_id))
            return False
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        class_name = arg.strip()
        if not class_name:
            print("** class name missing **")
            return

        if not self.validate_class(class_name):
            return

        try:
            new_instance = eval(f"{class_name}()")
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** Error creating instance: {} **".format(e))

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)
        if len(commands) != 2:
            print("** Usage: show <class_name> <id> **")
            return

        class_name, instance_id = commands
        if not self.validate_class(class_name):
            return
        if not self.validate_instance(class_name, instance_id):
            return

        print(storage.all()[class_name + '.' + instance_id])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)
        if len(commands) != 2:
            print("** Usage: destroy <class_name> <id> **")
            return

        class_name, instance_id = commands
        if not self.validate_class(class_name):
            return
        if not self.validate_instance(class_name, instance_id):
            return

        key = class_name + '.' + instance_id
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: all [class_name]
        """
        objects = storage.all()
        if arg:
            class_name = arg.strip()
            if not self.validate_class(class_name):
                return
            objects = {k: v for k, v in objects.items()
                       if k.startswith(class_name + ".")}
        for obj in objects.values():
            print(obj)

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class.
        Usage: <class name>.count()
        """
        class_name = arg.strip()
        if not self.validate_class(class_name):
            return

        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == class_name)
        print(count)

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
         commands = shlex.split(arg)
        if len(commands) < 4:
        print("** Usage: update <class_name> <id> <attr_name> <attr_value> **")
            return
        class_name, instance_id, attr_name = commands[:3]
        if not self.validate_class(class_name):
            return
        if not self.validate_instance(class_name, instance_id):
            return

        attr_value = ' '.join(commands[3:])

        obj = storage.all()[class_name + '.' + instance_id]
        setattr(obj, attr_name, attr_value)
        storage.save()

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid.
        """
        print("** Unknown command '{}' **".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
