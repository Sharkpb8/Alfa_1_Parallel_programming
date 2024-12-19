import unittest
from Train import *

class TestNode(unittest.TestCase):
    def test_valid_initialization(self):
        n = Node("StationA", 10)
        self.assertEqual(n.get_data(), "StationA")
        self.assertEqual(n.get_distance(), 10)

    def test_invalid_initialization(self):
        with self.assertRaises(DataTypeError):
            Node(123, 10)
        with self.assertRaises(DataLenghtError):
            Node("A", 10)
        with self.assertRaises(DistanceTypeError):
            Node("StationA", "10")
        with self.assertRaises(DistanceLenghtError):
            Node("StationA", -1)

    def test_getters_and_setters(self):
        n = Node("StationA", 10)
        self.assertEqual(n.get_data(), "StationA")
        n.set_data("StationB")
        self.assertEqual(n.get_data(), "StationB")
        
        with self.assertRaises(DataLenghtError):
            n.set_data("A")
        
        self.assertEqual(n.get_distance(), 10)
        n.set_distance(20)
        self.assertEqual(n.get_distance(), 20)

    def test_next_prev(self):
        n = Node("StationA", 10)
        new_node = Node("StationC", 15)
        n.set_next(new_node)
        self.assertEqual(n.get_next(), new_node)
        n.set_prev(new_node)
        self.assertEqual(n.get_prev(),new_node)
        n.set_prev(None)
        self.assertEqual(n.get_prev(),None)
        n.set_prev(None)
        self.assertEqual(n.get_prev(),None)

class TestLinkedList(unittest.TestCase):
    def test_initialization(self):
        MyList = LinkedList()

    def test_add_and_remove_tail(self):
        MyList = LinkedList()
        MyList.addtail("StationA", 10)
        MyList.addtail("StationB", 20)
        self.assertEqual(MyList.size, 2)
        self.assertEqual(MyList.get_size(), 2)
        
        MyList.remove("StationA")
        self.assertEqual(MyList.size, 1)
        self.assertEqual(MyList.get_size(), 1)

    def test_add_and_remove_head(self):
        MyList = LinkedList()
        MyList.addhead("StationA", 10)
        MyList.addhead("StationB", 20)
        self.assertEqual(MyList.size, 2)
        self.assertEqual(MyList.get_size(), 2)

        MyList.remove("StationB")
        self.assertEqual(MyList.size, 1)
        self.assertEqual(MyList.get_size(), 1)

    def test_navigation(self):
        MyList = LinkedList()
        MyList.addhead("StationA", 10)
        MyList.addhead("StationB", 20)
        MyList.addhead("StationC", 30)
        
        move_result = MyList.moveforward()
        self.assertEqual(move_result["to"], "StationB")
        self.assertEqual(MyList.current_station(), "StationB")
        move_result = MyList.moveforward()
        self.assertEqual(move_result["to"], "StationC")
        self.assertEqual(MyList.current_station(), "StationC")

    def test_find(self):
        MyList = LinkedList()
        MyList.addhead("StationA", 10)
        self.assertTrue(MyList.Find("StationA"))
        self.assertFalse(MyList.Find("StationB"))
    
    def test_duplicate(self):
        MyList = LinkedList()
        MyList.addhead("StationA", 10)
        with self.assertRaises(DuplicateStationError):
            MyList.addhead("StationA", 20)

    def test_getall(self):
        MyList = LinkedList()
        MyList.addhead("StationA", 10)
        MyList.addhead("StationB", 20)
        MyList.addhead("StationC", 30)
        self.assertEqual(MyList.FindAll(),["StationA","StationB","StationC"])
    
    def test_next_distance(self):
        MyList = LinkedList()
        MyList.addhead("StationA", 10)
        MyList.addhead("StationB", 20)
        MyList.addhead("StationC", 30)
        self.assertEqual(MyList.nextdistance(),20)
        MyList.moveforward()
        self.assertEqual(MyList.nextdistance(),30)
    
    def test_navigation_reverse(self):
        MyList = LinkedList()
        MyList.addhead("StationA", 10)
        MyList.addhead("StationB", 20)
        MyList.addhead("StationC", 30)
        
        MyList.moveforward()
        MyList.moveforward()
        move_result = MyList.moveforward()
        self.assertTrue(MyList.reverse)
        self.assertEqual(move_result["to"], "StationB")
        self.assertEqual(MyList.current_station(), "StationB")
        move_result = MyList.moveforward()
        self.assertEqual(move_result["to"], "StationA")
        self.assertEqual(MyList.current_station(), "StationA")
    
    def test_movebackward(self):
        MyList = LinkedList()
        with self.assertRaises(AttributeError):
            MyList.__movebackward()

    def test_isinstance(self):
        MyList = LinkedList()
        self.assertEqual(MyList.head, None)
        self.assertEqual(MyList.tail, None)
        MyList.addhead("StationA", 10)
        self.assertIsInstance(MyList.head, Node)
        self.assertIsInstance(MyList.tail, Node)


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.tracks = LinkedList()
        self.tracks.addtail("StationA", 10)
        self.tracks.addtail("StationB", 20)
        
        self.train = Train("R", 1234, 100, 50, 200, 10, self.tracks)

    def test_valid_initialization(self):
        self.assertEqual(self.train.type, "R")
        self.assertEqual(self.train.speed, 100)
        
    def test_add_station(self):
        self.train.addstation("StationC", 30)
        self.assertTrue(self.tracks.Find("StationC"))

    def test_fuel_consumption(self):
        self.train.consumefuel(10)
        self.assertEqual(self.train.getcurrentfuel(), 100)

    def test_need_refill(self):
        self.assertFalse(self.train.needrefill(10))
        self.assertTrue(self.train.needrefill(30))

    def test_add_and_remove_passengers(self):
        self.assertFalse(self.train.addpassangers("StationB"))

if __name__ == "__main__":
    unittest.main()