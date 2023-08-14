#!/usr/bin/python3
"""
Console DOC
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class Doc
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        DOC
        """
        return True

    def do_EOF(self, args):
        """
        DOCs
        """
        return True

    def emptyline(self):
        """
        Docs
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
