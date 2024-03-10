#!/usr/bin/python3
"""
Console for the Airbnb clone project.

This program provides a command-line interface to
interact with the application.
"""
import cmd
import shlex
from models.__init__ import storage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB project.
    """

    prompt = "(hbnb) "
    valid_classes = {
        "BaseModel": BaseModel,
        "City": City,
        "State": State,
        "User": User,
        "Review": Review,
        "Amenity": Amenity,
        "Place": Place
    }

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached (Ctrl+D)
        """
        return True

    def emptyline(self):
        """
        Handles an empty line input by the user.
        """
        pass

    def do_create(self, args):
        """Create instance of a BaseModel

        """
        if args is None or args == "":
            print("** class name missing **")
        elif args not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            new_object = HBNBCommand.valid_classes[args]()
            new_object.save()
            print(new_object.id)
            storage.save()

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = arg.split(" ")
        all_objs = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            k = args[0] + "." + args[1]
            if k not in all_objs:
                print("** no instance found **")
            else:
                obj = all_objs[k]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
                storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split(" ")
        all_objs = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            if k in all_objs:
                print(all_objs[k])
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = shlex.split(arg)
        if args and args[0]:
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return

        all_objs = storage.all()
        result = []
        for obj_key in all_objs:
            if not args or all_objs[obj_key].__class__ == cls:
                result.append(str(all_objs[obj_key]))
        print(result)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split(" ")
        all_objs = storage.all()
        if len(arg) <= 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            if k not in all_objs:
                print("** no instance found **")
            else:
                del all_objs[k]
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
