#!/usr/bin/python3
'''
Module to execute the functions
'''
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import storage
import models


class HBNBCommand(cmd.Cmd):
    """
        ------------------------------------------
        HBNBCommand class
        program called console.py that contains
        the entry point of the command interpreter
        ------------------------------------------
    """
    prompt = "(hbnb) "
    name_classes = {'BaseModel': BaseModel,
                    'User': User,
                    'Amenity': Amenity,
                    'City': City,
                    'Place': Place,
                    'State': State,
                    'Review': Review}
    ints = ['number_rooms', 'number_bathrooms', 'max_guest', 'price_by_night']
    floats = ['latitude', 'longitude']

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        return False

    def do_create(self, args):
        """Create a new instance of type:
        ex: create BaseModel
        ex: create User
        ex: create Amenity
        ex: create City
        ex: create Place
        ex: create State
        ex: create Review"""
        arguments = args.split()
        kwargs = {}
        if len(arguments) == 0:
            print("** class name missing **")
            return (False)
        elif arguments[0] not in self.name_classes:
            print("** class doesn't exist **")
            return (False)
        else:
            new_instance = self.name_classes[arguments[0]](**kwargs)
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        """Prints instance based on the class name and id
        ex: show BaseModel 1212
        ex: show User 1213
        ex: show Amenity 1214
        ex: show City 1234
        ex: show Place 4321
        ex: show State 4567
        ex: show Review 4567"""
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return (False)
        elif arguments[0] not in self.name_classes:
            print("** class doesn't exist **")
            return (False)
        elif len(arguments) == 1:
            print("** instance id missing **")
            return (False)
        elif len(arguments) == 2:
            keys = arguments[0] + "." + arguments[1]
            all_objects = storage.all()
            if keys in all_objects:
                print(all_objects[keys])
                return (False)
            else:
                print("** no instance found **")
                return (False)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        ex: destroy BaseModel 1212
        ex: destroy User 1213
        ex: destroy Amenity 1214
        ex: destroy City 1234
        ex: destroy Place 4321
        ex: destroy State 4567
        ex: destroy Review 4567"""
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return (False)
        elif arguments[0] not in self.name_classes:
            print("** class doesn't exist **")
            return (False)
        elif len(arguments) == 1:
            print("** instance id missing **")
            return (False)
        elif len(arguments) == 2:
            keys = arguments[0] + "." + arguments[1]
            all_objects = storage.all()
            if keys in all_objects.keys():
                all_objects.pop(keys)
                storage.save()
                return (False)
            else:
                print("** no instance found **")

    def do_all(self, args):
        '''Print all string representation of all instances
        ex: all
        ex: all nameclass'''
        arguments = args.split()
        all_objects = storage.all()
        if len(arguments) == 0:
            for obj_id in all_objects.keys():
                obj = all_objects[obj_id]
                print(obj)
        elif len(arguments) == 1:
            all_objects = storage.all()
            if arguments[0] in self.name_classes:
                for key, value in all_objects.items():
                    name = key.split(".")
                    if name[0] == arguments[0]:
                        obj = all_objects[key]
                        print(obj)
            else:
                print("** class doesn't exist **")
                return (False)

    def do_update(self, args):
        """Update an instance
        Usage: update <class name> <id> <attribute name> <attribute value>"""
        arguments = args.split()
        all_objects = storage.all()
        if len(arguments) == 0:
            print("** class name missing **")
            return (False)
        elif arguments[0] not in self.name_classes:
            print("** class doesn't exist **")
            return (False)
        elif len(arguments) == 1:
            print("** instance id missing **")
            return (False)
        elif len(arguments) == 2:
            keys = arguments[0] + "." + arguments[1]
            all_objects = storage.all()
            if keys not in all_objects.keys():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
                return (False)
        elif len(arguments) == 3:
            print("** value missing **")
            return (False)
        else:
            keys = arguments[0] + "." + arguments[1]
            all_objects = storage.all()
            if keys not in all_objects.keys():
                print("** no instance found **")
                return (False)
            else:
                all_objects = storage.all().get(keys)
                setattr(all_objects, arguments[2], "{}".format(arguments[3]))
                all_objects.save()

    def default(self, args):
        arguments = args.split(".")
        if arguments[0] in self.name_classes and arguments[1] == "all()":
            self.do_all(arguments[0])
        elif arguments[0] in self.name_classes and arguments[1] == "count()":
            all_objects = storage.all()
            count = 0
            for key in all_objects.keys():
                token = key.split(".")
                if token[0] == arguments[0]:
                    count = count + 1
            print(count)
        else:
            print("*** Unknown syntax: {}".format(args))

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
