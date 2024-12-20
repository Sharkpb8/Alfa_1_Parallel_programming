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
        with self.assertRaises(EmptyInputError):
            Node(None,5)
        with self.assertRaises(EmptyInputError):
            Node("StationA")
        with self.assertRaises(EmptyInputError):
            Node(None,None)

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
        with self.assertRaises(DistanceLenghtError):
            n.set_distance(-1)

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
    def test_initialization(self): 
        self.train = Train("R", 1234, 100, 50, 200, 10, LinkedList())

    def test_invalid_train_type(self):
        with self.assertRaises(TypeTypeError):
            Train(50, 1234, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TypeTypeError):
            Train(False, 1234, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TypeTypeError):
            Train([], 1234, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TypeTypeError):
            Train(5.5, 1234, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TypeTypeError):
            Train(None, 1234, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainTypeError):
            Train("Ahoj", 1234, 100, 50, 200, 10, LinkedList())
    
    def test_invalid_train_train_number(self):
        with self.assertRaises(TrainNumberTypeError):
            Train("R", "1234", 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberTypeError):
            Train("R", [], 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberTypeError):
            Train("R", 5.5, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberTypeError):
            Train("R", None, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberLenghtError):
            Train("R", 40, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberLenghtError):
            Train("R", -1, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberLenghtError):
            Train("R", 808080, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberTypeError):
            Train("R", False, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberTypeError):
            Train("R", True, 100, 50, 200, 10, LinkedList())
        with self.assertRaises(TrainNumberLenghtError):
            Train("R", -5000, 100, 50, 200, 10, LinkedList())

    def test_invalid_train_speed(self):
        with self.assertRaises(SpeedTypeError):
            Train("R", 1234, "100", 50, 200, 10, LinkedList())
        with self.assertRaises(SpeedTypeError):
            Train("R", 1234, [], 50, 200, 10, LinkedList())
        with self.assertRaises(SpeedTypeError):
            Train("R", 1234, 5.5, 50, 200, 10, LinkedList())
        with self.assertRaises(SpeedTypeError):
            Train("R", 1234, None, 50, 200, 10, LinkedList())
        with self.assertRaises(SpeedTypeError):
            Train("R", 1234, False, 50, 200, 10, LinkedList())
        with self.assertRaises(SpeedError):
            Train("R", 1234, -50, 50, 200, 10, LinkedList())
        
    def test_invalid_train_capacity(self):
        with self.assertRaises(CapacityTypeError):
            Train("R", 1234, 100, "50", 200, 10, LinkedList())
        with self.assertRaises(CapacityTypeError):
            Train("R", 1234, 100, [], 200, 10, LinkedList())
        with self.assertRaises(CapacityTypeError):
            Train("R", 1234, 100, 5.5, 200, 10, LinkedList())
        with self.assertRaises(CapacityTypeError):
            Train("R", 1234, 100, None, 200, 10, LinkedList())
        with self.assertRaises(CapacityTypeError):
            Train("R", 1234, 100, False, 200, 10, LinkedList())
        with self.assertRaises(CapacityError):
            Train("R", 1234, 100, -50, 200, 10, LinkedList())
    
    def test_invalid_train_fuel(self):
        with self.assertRaises(FuelTypeError):
            Train("R", 1234, 100, 50, "200", 10, LinkedList())
        with self.assertRaises(FuelTypeError):
            Train("R", 1234, 100, 50, [], 10, LinkedList())
        with self.assertRaises(FuelTypeError):
            Train("R", 1234, 100, 50, 5.5, 10, LinkedList())
        with self.assertRaises(FuelTypeError):
            Train("R", 1234, 100, 50, None, 10, LinkedList())
        with self.assertRaises(FuelTypeError):
            Train("R", 1234, 100, 50, False, 10, LinkedList())
        with self.assertRaises(FuelError):
            Train("R", 1234, 100, 50, -5000, 10, LinkedList())  

    def test_invalid_train_consumption(self):
        with self.assertRaises(ConsumptionTypeError):
            Train("R", 1234, 100, 50, 200, "10", LinkedList())
        with self.assertRaises(ConsumptionTypeError):
            Train("R", 1234, 100, 50, 200, [], LinkedList())
        with self.assertRaises(ConsumptionTypeError):
            Train("R", 1234, 100, 50, 200, 5.5, LinkedList())
        with self.assertRaises(ConsumptionTypeError):
            Train("R", 1234, 100, 50, 200, None, LinkedList())
        with self.assertRaises(ConsumptionError):
            Train("R", 1234, 100, 50, 200, False, LinkedList())
        with self.assertRaises(ConsumptionError):
            Train("R", 1234, 100, 50, 200, -10, LinkedList())

    def test_invalid_train_consumption(self):
        with self.assertRaises(TracksTypeError):
            Train("R", 1234, 100, 50, 200, 10, "LinkedList()")
        with self.assertRaises(TracksTypeError):
            Train("R", 1234, 100, 50, 200, 10, [])
        with self.assertRaises(TracksTypeError):
            Train("R", 1234, 100, 50, 200, 10, 5.5)
        with self.assertRaises(TracksTypeError):
            Train("R", 1234, 100, 50, 200, 10, None)
        with self.assertRaises(TracksTypeError):
            Train("R", 1234, 100, 50, 200, 10, False)
        with self.assertRaises(TracksTypeError):
            Train("R", 1234, 100, 50, 200, 10, -5)
    
    def test_valid_train(self):
        Train("R", 1234, 100, 50, 200, 10, LinkedList())
    
    def test_valid_data(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        self.assertEqual(t.type,"R")
        self.assertEqual(t.train_number,1234)
        self.assertEqual(t.speed,100)
        self.assertEqual(t.capacity,50)
        self.assertEqual(t.current_passangers,[])
        self.assertEqual(t.fuel,200)
        self.assertEqual(t.current_fuel,200)
        self.assertEqual(t.consumption,10)
        self.assertIsInstance(t.tracks,LinkedList)
    
    def test_addstation(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        t.addstation("StationA", 0)
        self.assertEqual(t.getallstations(),["StationA"])
        with self.assertRaises(EmptyInputError):
            t.addstation(None,50)
        with self.assertRaises(EmptyInputError):
            t.addstation("StationA")
        with self.assertRaises(EmptyInputError):
            t.addstation(None,None)
    
    def test_removestation(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        t.addstation("StationA", 0)
        t.addstation("StationB", 0)
        self.assertEqual(t.getallstations(),["StationA","StationB"])
        t.removestation("StationB")
        self.assertEqual(t.getallstations(),["StationA"])
        with self.assertRaises(EmptyInputError):
            t.removestation()
    
    def test_size(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        t.addstation("StationA", 0)
        t.addstation("StationB", 0)
        self.assertEqual(t.gettrackssize(),2)
    
    def test_fuel(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        self.assertEqual(t.getcurrentfuel(),200)
    
    def test_moveforward(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        t.addstation("StationA", 0)
        t.addstation("StationB", 20)
        self.assertEqual(t.movetrain(),{"from":"StationA","to":"StationB","distance":20,"finish":False})
        self.assertEqual(t.movetrain(),{"from":"StationB","to":"StationA","distance":20,"finish":True})
    
    def test_distance(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        t.addstation("StationA", 0)
        t.addstation("StationB", 20)
        self.assertEqual(t.distancetonext(),20)
    
    def test_concat(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        self.assertEqual(t.concat(),"R1234")
    
    def test_fuelneeded(self):
        t = Train("R", 1234, 100, 50, 200, 10, LinkedList())
        t.addstation("StationA", 0)
        t.addstation("StationB", 20)
        t.current_fuel = 0
        self.assertEqual(t.fuelneeded(),200)

    def test_needrefill(self):
        t = Train("R", 1234, 100, 50, 300, 10, LinkedList())
        t.addstation("StationA", 0)
        t.addstation("StationB", 20)
        t.current_fuel = 0
        self.assertTrue(t.needrefill(20))
        t.current_fuel = 300
        self.assertFalse(t.needrefill(20))
        with self.assertRaises(EmptyInputError):
            t.needrefill()
        with self.assertRaises(TravelTypeError):
            t.needrefill("")
        with self.assertRaises(TravelTypeError):
            t.needrefill(5.5)
        with self.assertRaises(TravelTypeError):
            t.needrefill(False)
        with self.assertRaises(TravelTypeError):
            t.needrefill([])
    
    def test_refull(self):
        t = Train("R", 1234, 100, 50, 300, 10, LinkedList())
        t.current_fuel = 0
        self.assertEqual(t.current_fuel,0)
        t.refuel(20)
        self.assertEqual(t.current_fuel,20)
        with self.assertRaises(EmptyInputError):
            t.refuel()
        with self.assertRaises(FuelTypeError):
            t.refuel("")
        with self.assertRaises(FuelTypeError):
            t.refuel(5.5)
        with self.assertRaises(FuelTypeError):
            t.refuel(False)
        with self.assertRaises(FuelTypeError):
            t.refuel([])
    
    def test_consumefuel(self):
        t = Train("R", 1234, 100, 50, 300, 10, LinkedList())
        self.assertEqual(t.current_fuel,300)
        t.consumefuel(10)
        self.assertEqual(t.current_fuel,200)
        with self.assertRaises(LowFuelError):
            t.consumefuel(1000)
        with self.assertRaises(EmptyInputError):
            t.consumefuel()
        with self.assertRaises(DistanceTypeError):
            t.consumefuel("")
        with self.assertRaises(DistanceTypeError):
            t.consumefuel(5.5)
        with self.assertRaises(DistanceTypeError):
            t.consumefuel(False)
        with self.assertRaises(DistanceTypeError):
            t.consumefuel([])
    
    def test_trainposition(self):
        t = Train("R", 1234, 100, 50, 300, 10, LinkedList())
        t.addstation("StationA", 0)
        t.addstation("StationB", 20)
        t.addstation("StationC", 30)
        self.assertEqual(t.trainposition(),{"current_station":"StationA","direction":False})
        t.movetrain()
        self.assertEqual(t.trainposition(),{"current_station":"StationB","direction":False})
        t.movetrain()
        t.movetrain()
        self.assertEqual(t.trainposition(),{"current_station":"StationB","direction":True})
    
    def test_addpassangers(self):
        t = Train("R", 1234, 100, 50, 300, 10, LinkedList())
        t.addstation("StationA", 0)
        t.addstation("StationB", 20)
        self.assertFalse(t.addpassangers("ahoj"))
        self.assertEqual(t.current_passangers,["ahoj"])
        t.capacity = 1
        self.assertTrue(t.addpassangers("ahoj"))
        with self.assertRaises(EmptyInputError):
            t.addpassangers()
        with self.assertRaises(PassangerTypeError):
            t.addpassangers(5)
        with self.assertRaises(PassangerTypeError):
            t.addpassangers(5.5)
        with self.assertRaises(PassangerTypeError):
            t.addpassangers(False)
        with self.assertRaises(PassangerTypeError):
            t.addpassangers([])


if __name__ == "__main__":
    unittest.main()