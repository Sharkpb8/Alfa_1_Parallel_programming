import unittest
from Entity import *
from Enemy import *
from Player import *

class TestEntity(unittest.TestCase):
    def testcreationname(self):
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

    def testcreationhealth(self):
        with self.assertRaises(TypeError):
            e = Entity("Lupic","5")
        with self.assertRaises(TypeError):
            e = Entity("Lupic",5.5)
        with self.assertRaises(TypeError):
            e = Entity(("Lupic"),(5))
        with self.assertRaises(TypeError):
            e = Entity("Lupic",True)
        with self.assertRaises(ValueError):
            e = Entity("Lupic",0)
        with self.assertRaises(ValueError):
            e = Entity("Lupic",-1)

    def testreturns(self):
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
            e.takedemage("5")
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
        with self.assertRaises(ValueError):
            e.takedemage(0)
        e.takedemage(5)
        self.assertEqual(e.current_health,3)

class TestEnemy(unittest.TestCase):
    def testcreationdemage(self):
        with self.assertRaises(TypeError):
            e = Enemy("Lupic",50,5.5)
        with self.assertRaises(TypeError):
            e = Enemy("Lupic",50,"5")
        with self.assertRaises(TypeError):
            e = Enemy("Lupic",50,(5))
        with self.assertRaises(TypeError):
            e = Enemy("Lupic",50,True)
        with self.assertRaises(TypeError):
            e = Enemy("Lupic",50,None)
        with self.assertRaises(ValueError):
            e = Enemy("Lupic",50,0)
        with self.assertRaises(ValueError):
            e = Enemy("Lupic",50,-1)
    
    def testreturns(self):
        e = Enemy("Lupic",50,5)
        self.assertEqual(e.name,"Lupic")
        self.assertEqual(e.max_health,50)
        self.assertEqual(e.current_health,50)
        self.assertEqual(e.demage,5)
        self.assertTrue(250 <= e.xpgained >= 800)
    
    async def testattack(self):
        e = Enemy("Lupic",50,5)
        result = await e.attack()
        self.assertEqual(result, 5)

class TestPlayer(unittest.TestCase):
    def testcreationplayr(self):
        with self.assertRaises(TypeError):
            p = Player("Honza",100,5)
        with self.assertRaises(TypeError):
            p = Player("Honza",100,(5))
        with self.assertRaises(TypeError):
            p = Player("Honza",100,True)
        with self.assertRaises(TypeError):
            p = Player("Honza",100,None)
    
    def testreturns(self):
        p = Player("Honza",100,"Wizard")
        self.assertEqual(p.name,"Honza")
        self.assertEqual(p.max_health,100)
        self.assertEqual(p.current_health,100)
        self.assertEqual(p.playerclass,"Wizard")
        self.assertEqual(p.xp,0)
        self.assertEqual(p.level,1)
    
    def testaddxp(self):
        p = Player("Honza",100,"Wizard")
        with self.assertRaises(TypeError):
            p.addxp("5")
        with self.assertRaises(TypeError):
            p.addxp(5.5)
        with self.assertRaises(TypeError):
            p.addxp((5))
        with self.assertRaises(TypeError):
            p.addxp(None)
        with self.assertRaises(TypeError):
            p.addxp(False)
        p.addxp(100)
        self.assertEqual(100,p.xp)
        p.addxp(900)
        self.assertEqual(2,p.level)
        self.assertEqual(110,p.max_health)


if __name__ == '__main__':
    unittest.main()
