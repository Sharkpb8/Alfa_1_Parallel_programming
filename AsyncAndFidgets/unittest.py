import unittest
from Entity import *

class TestEntity(unittest.TestCase):
    def creationname(self):
        with self.assertRaises(TypeError):
            e = Entity(5,5)
        with self.assertRaises(TypeError):
            e = Entity(4.5,5)
        with self.assertRaises(TypeError):
            e = Entity(("Lupic"),5)
        with self.assertRaises(TypeError):
            e = Entity(True,5)
        with self.assertRaises(TypeError):
            e = Entity(None,5)

    def creationhealth(self):
        with self.assertRaises(ValueError):
            e = Entity("Lupic","asd")
        with self.assertRaises(ValueError):
            e = Entity("Lupic",5.5)
        with self.assertRaises(ValueError):
            e = Entity(("Lupic"),(5))
        with self.assertRaises(ValueError):
            e = Entity("Lupic",True)

    def returns(self):
        e = Entity("Lupic",8)
        self.assertEqual(e.name,"Lupic")
        self.assertEqual(e.max_health,8)
        self.assertEqual(e.current_health,8)
        e = Entity("Lupic")
        self.assertEqual(e.max_health,100)
        self.assertEqual(e.current_health,100)
    
    def testtakedemage(self):
        e = Entity("Lupic",8)
        with self.assertRaises(TypeError):
            e.takedemage("asd")
        with self.assertRaises(TypeError):
            e.takedemage(5.5)
        with self.assertRaises(TypeError):
            e.takedemage((5))
        with self.assertRaises(TypeError):
            e.takedemage(True)
        with self.assertRaises(TypeError):
            e.takedemage(None)
        with self.assertRaises(ValueError):
            e.takedemage(-1)
        e.takedemage(5)
        self.assertEqual(e.current_health,3)
        