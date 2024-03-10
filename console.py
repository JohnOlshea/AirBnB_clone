#!/usr/bin/python3
"""
Console for the Airbnb clone project.

This program provides a command-line interface to
interact with the application.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB project.
    """
    
    prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
