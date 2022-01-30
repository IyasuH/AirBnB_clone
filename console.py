#!/usr/bin/python3
"""Console to test data locally"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    class_exi = {'BaseModel', 'User', 'State', 'City',
                 'Amenity', 'Place', 'Review'}

    def do_create(self, class_name):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""

        if class_name == 'BaseModel':
            obj = BaseModel()
        elif class_name == 'User':
            obj = User()
        elif class_name == 'State':
            obj = State()
        elif class_name == 'City':
            obj = City()
        elif class_name == 'Amenity':
            obj = Amenity()
        elif class_name == 'Place':
            obj = Place()
        elif class_name == 'Review':
            obj = Review()

        if len(class_name) != 0 and class_name != "":
            if class_name not in self.class_exi:
                print("** class doesn't exist **")
            else:
                obj.save()
                print(obj.id)
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Prints the string representation of
        an instance based on the class name and id"""
        arg = shlex.split(args)
        if len(arg) == 0 or arg[0] == "":
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            class_name = arg[0]
            id_n = arg[1]
            if class_name not in self.class_exi:
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                key = class_name + "." + id_n
                if key in all_objs:
                    print(all_objs[key])
                else:
                    ("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        arg = shlex.split(args)
        if len(arg) == 0 or arg[0] == "":
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            class_name = arg[0]
            id_n = arg[1]
            if class_name not in self.class_exi:
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
        if class_name != "" and class_name not in self.class_exi:
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
        arg = shlex.split(args)
        if len(arg) == 0 or arg[0] == "":
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
            if (class_name not in self.class_exi):
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
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
