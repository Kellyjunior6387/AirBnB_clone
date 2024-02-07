#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instace and prints its id.
        """
        arg = parse(arg)
        if len:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print ("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg = parse(arg)
        obj_dict = storage.all()
        if len == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBcommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print ("**instance id missing **")
        elif "{}.{}".format(arg[0], arg[1] not in obj_dict.keys():
                print("** no instance found **")

    def do_EOF(self, arg):
        """Exit the program by typing EOF (Ctrl+D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
