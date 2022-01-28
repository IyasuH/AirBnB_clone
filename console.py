#!/usr/bin/python3
"""import modules"""
import cmd
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    def do_create(self, class_name):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if class_name:
            if class_name != 'BaseModel':
                print("** class doesn't exist **")
            else:
                obj = BaseModel()
                obj.save()
                print(obj.id)
        else:
            print("** class name missing **")


    def do_show(self, args):
        """Prints the string representation of
        an instance based on the class name and id"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            class_name = arg[0]
            id_n = arg[1]
            if class_name != 'BaseModel':
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                pint = None
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    if id_n == obj.id:
                        pint = obj
                        print(pint)

                if pint == None:
                    print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            class_name = arg[0]
            id_n = arg[1]
            if class_name != 'BaseModel':
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                key = class_name + "." + id_n
                if key in all_objs:
                    del all_objs[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, class_name):
        """Prints all string representation of
        all instances based or not on the class name"""
        if class_name != "" and class_name != 'BaseModel':
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list1 = []
            for key, values in all_objs.items():
                list1.append(str(values))

            print(list1)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            class_name = arg[0]
            id_n = arg[1]
            attr = arg[2]
            value = arg[3]
            if (class_name != 'BaseModel'):
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                pint = None
                key = class_name + "." + id_n
                if key in all_objs:
                    setattr(all_objs[key], attr, value)
                    storage.save()
                else:
                    print("** no instance found **")

    def do_quit(self, line):
        """quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
