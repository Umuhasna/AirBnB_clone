#!/usr/bin/python3
"""
Console DOC
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


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

    def do_create(self, arg):
        """
        Docs
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    obj = BaseModel()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "User":
                    obj = User()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "State":
                    obj = State()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "City":
                    obj = City()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "Amenity":
                    obj = Amenity()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "Place":
                    obj = Place()
                    obj.save()
                    print(obj.id)
                elif args_array[0] == "Review":
                    obj = Review()
                    obj.save()
                    print(obj.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Docs
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                class_name = args_array[0]
                if class_name in allowed_classes:
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(
                                class_name, args_array[1])
                        if search_string in objs_dict:
                            print(objs_dict[search_string])
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Docs
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                class_name = args_array[0]
                if class_name in allowed_classes:
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(
                                class_name, args_array[1])
                        if search_string in objs_dict:
                            del (objs_dict[search_string])
                            models.storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Docs
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                class_name = args_array[0]
                if class_name in allowed_classes:
                    final_list = []
                    for key, value in models.storage.all().items():
                        if (class_name in key):
                            final_list.append(str(value))
                    print(final_list)
                else:
                    print("** class doesn't exist **")
        else:
            final_list = []
            for key, value in models.storage.all().items():
                final_list.append(str(value))
            print(final_list)

    def do_update(self, arg):
        """
        Docs
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                class_name = args_array[0]
                if class_name in allowed_classes:
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(
                                class_name, args_array[1])
                        if search_string in objs_dict:
                            if len(args_array) > 2:
                                if len(args_array) > 3:
                                    if (args_array[3]
                                            not in
                                            ["created_at",
                                                "updated_at", "id"]):
                                        setattr(objs_dict[search_string], str(
                                            args_array[2]), str(args_array[3]))
                                else:
                                    print("** value missing **")
                            else:
                                print("** attribute name missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_User(self, arg):
        """
        Docs
        """
        class_name = "User"
        self.data_model_func(arg, class_name)

    def do_BaseModel(self, arg):
        """
        Docs
        """
        class_name = "BaseModel"
        self.data_model_func(arg, class_name)

    def do_State(self, arg):
        """
        Docs
        """
        class_name = "State"
        self.data_model_func(arg, class_name)

    def do_City(self, arg):
        """
        Docs
        """
        class_name = "City"
        self.data_model_func(arg, class_name)

    def do_Amenity(self, arg):
        """
        Docs
        """
        class_name = "Amenity"
        self.data_model_func(arg, class_name)

    def do_Place(self, arg):
        """
        Docs
        """
        class_name = "Place"
        self.data_model_func(arg, class_name)

    def do_Review(self, arg):
        """
        Docs
        """
        class_name = "Review"
        self.data_model_func(arg, class_name)

    def data_model_func(self, arg, class_name):
        """
        Docs
        """
        allowed_methods = [".all()", ".count()"]
        show_regex = re.compile(r"\.show\(\"(.*?)\"\)")
        delete_regex = re.compile(r"\.destroy\(\"(.*?)\"\)")
        update_regex = re.compile(r"\.update\(\"(.*?)\", \"(.*?)\", (.*?)\)")
        update_dict_regex = re.compile(r"\.update\(\"(.*?)\",(.*?)\)")
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                command_method = args_array[0]
                if command_method in allowed_methods:
                    if command_method == ".all()":
                        self.do_all(class_name)
                    if command_method == ".count()":
                        self.get_count(class_name)
                elif (show_regex.search(args_array[0]) is not None):
                    obj_id = show_regex.search(args_array[0]).group(1)
                    self.do_show("{} {}".format(class_name, obj_id))
                elif (delete_regex.search(args_array[0]) is not None):
                    obj_id = delete_regex.search(args_array[0]).group(1)
                    self.do_destroy("{} {}".format(class_name, obj_id))
                elif (update_regex.search(arg) is not None):
                    obj_id = update_regex.search(arg).group(1)
                    obj_attr_name = update_regex.search(arg).group(2)
                    obj_attr_value = update_regex.search(arg).group(3)
                    self.do_update("{} {} {} {}".format(
                        class_name, obj_id, obj_attr_name, obj_attr_value))
                elif (update_dict_regex.search(arg) is not None):
                    obj_id = update_dict_regex.search(arg).group(1)
                    obj_dict = eval(update_dict_regex.search(arg).group(2))
                    for key, value in obj_dict.items():
                        self.do_update("{} {} {} {}".format(
                            class_name, obj_id, key, value))

    def get_count(self, class_name):
        """
        Docs
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if class_name in allowed_classes:
            final_list = []
            for key, value in models.storage.all().items():
                if (class_name in key):
                    final_list.append(str(value))
            print(len(final_list))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
