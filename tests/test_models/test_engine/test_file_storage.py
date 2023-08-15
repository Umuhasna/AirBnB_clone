#!/usr/bin/python3
'''
Module
'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models


class TestFileStorage(unittest.TestCase):
    '''
    Docs
    '''

    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        Docs
        '''
        classDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        '''
        Docs
        '''
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.save.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocsNew(self):
        '''
        Docs
        '''
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.new.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocsAll(self):
        '''
        Docs
        '''
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.all.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocsReload(self):
        '''
        Docs
        '''
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.reload.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_file_path_Type(self):
        '''
        Docs
        '''
        self.assertIs(type(FileStorage._FileStorage__file_path), str)

    def test_objects_Type(self):
        '''
        Docs
        '''
        self.assertIs(type(FileStorage._FileStorage__objects), dict)

    def test_file_path(self):
        '''
        Docs
        '''
        file_storage = FileStorage()
        self.assertEqual(file_storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        '''
        Docs
        '''
        file_storage = FileStorage()
        file_storage._FileStorage__objects = {}
        self.assertEqual(file_storage._FileStorage__objects, {})
        obj = BaseModel()
        file_storage.new(obj)
        objects = file_storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), objects)
        self.assertEqual(objects["BaseModel.{}".format(obj.id)], obj)

    def test_method_all(self):
        '''
        Docs
        '''
        file_storage = FileStorage()
        objects = file_storage.all()
        self.assertEqual(objects, file_storage._FileStorage__objects)

    def test_method_new(self):
        '''
        Docs
        '''
        file_storage = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()

        file_storage.new(obj1)
        file_storage.new(obj2)

        self.assertIn(
                "BaseModel.{}".format(obj1.id),
                file_storage._FileStorage__objects)
        self.assertIn(
                "BaseModel.{}".format(obj2.id),
                file_storage._FileStorage__objects)

        self.assertEqual(
                file_storage._FileStorage__objects[
                    "BaseModel.{}".format(obj1.id)], obj1)
        self.assertEqual(
                file_storage._FileStorage__objects[
                    "BaseModel.{}".format(obj2.id)], obj2)

    def test_method_save(self):
        '''
        Docs
        '''
        file_storage = FileStorage()
        obj1 = BaseModel()

        file_storage.save()

        with open("file.json", "r") as f:
            json_string = f.read()

        self.assertIn("BaseModel.{}".format(obj1.id), json_string)

    def test_method_reload(self):
        '''
        Docs
        '''
        file_storage = FileStorage()
        base_model = BaseModel()
        file_storage.save()
        models.storage.reload()
        objects = file_storage._FileStorage__objects

        self.assertIn("BaseModel.{}".format(base_model.id), objects)


if __name__ == "__main__":
    unittest.main()
