from Node import *
        
class LinkedList():
    def __init__(self,head = None,tail = None):
        """
        Represents a doubly linked list of `Node` objects with various utility methods.

        :param head: The head node of the list. Defaults to None.
        :type head: Node or None
        :param tail: The tail node of the list. Defaults to None.
        :type tail: Node or None

        :raises HeadError: If `head` is not a Node or None.
        :raises TailError: If `tail` is not a Node or None.
        """
        if (head is not None and not isinstance(head, Node)):
            raise HeadError
        if (tail is not None and not isinstance(tail, Node)):
            raise TailError
        self.head = head
        self.tail = tail
        self.current = tail
        self.reverse = False
        self.size = 0
    
    def get_size(self):
        """
        Retrieves the size of the linked list.

        :return: The number of nodes in the linked list.
        :rtype: int
        """
        return self.size
    
    def Find(self,data):
        """
        Searches for a node by its data.

        :param data: The data to search for.
        :type data: str
        :return: True if the data is found, False otherwise.
        :rtype: bool
        """
        this_node = self.tail
        while this_node:
            if this_node.get_data() == data:
                return True
            else:
                this_node = this_node.get_next()
        return False
    
    def addtail(self,data,distance):
        """
        Adds a new node to the tail of the list.

        :param data: The data for the new node.
        :type data: str
        :param distance: The distance for the new node.
        :type distance: int

        :raises DuplicateStationError: If the data already exists in the list.
        """
        if(self.Find(data)):
            raise DuplicateStationError
        new_node = Node(data,distance,self.head)
        if self.head:
            tail_node = self.tail
            self.tail = new_node
            new_node.set_next(tail_node)
            tail_node.set_prev(new_node)
        else:
            self.head = new_node
            self.tail = new_node
        self.current = self.tail
        self.size += 1

    def addhead(self,data,distance):
        """
        Adds a new node to the head of the list.

        :param data: The data for the new node.
        :type data: str
        :param distance: The distance for the new node.
        :type distance: int

        :raises DuplicateStationError: If the data already exists in the list.
        """
        if(self.Find(data)):
            raise DuplicateStationError
        new_node = Node(data,distance,None,self.head)
        if self.tail:
            head_node = self.head
            self.head = new_node
            new_node.set_prev(head_node)
            head_node.set_next(new_node)
        else:
            self.head = new_node
            self.tail = new_node
        self.current = self.tail
        self.size += 1
    
    def remove(self,data):
        """
        Removes a node by its data.

        :param data: The data of the node to remove.
        :type data: str
        """
        this_node = self.head
        while this_node:
            if this_node.get_data() == data:
                next = this_node.get_next()
                prev = this_node.get_prev()
                if next and prev:
                    prev.set_next(this_node.get_next())
                    next.set_prev(this_node.get_prev())
                elif not next and not prev:
                    self.tail = None
                    self.head = None
                elif not next:
                    prev.set_next(this_node.get_next())
                    self.head = prev
                elif not prev:
                    self.tail = this_node.get_next()
                    next.set_prev(None)
                    self.current = self.tail
                    self.tail.set_distance(0)
                self.size -= 1
                break
            else:
                this_node = this_node.get_prev()
    
    def moveforward(self):
        """
        Moves the current pointer forward in the list.

        :return: A dictionary containing information about the move.
        :return: `from` - position from which the pointer moved.
        :rtype: str
        :return: `to` - position where the pointer is now.
        :rtype: str
        :return: `distance` distance from the original position to new
        :rtype: int
        :return: `finish` True if its the final destination otherwise False
        :rtype: bool
        :rtype: dict
        """
        this_node = self.current
        next = this_node.get_next()
        if(not self.reverse):
            if(next is not None and next.get_data()):
                    self.current = self.current.get_next()
                    return {"from":this_node.get_data(),"to":self.current.get_data(),"distance":next.get_distance(),"finish":False}
            else:                
                self.reverse = True
                return self.__movebackward(this_node)
        else:
            return self.__movebackward(this_node)
    
    def __movebackward(self,this_node):
        """
        Moves the current pointer backward in the list.

        :param this_node: The current node.
        :type this_node: Node

        :raises NodeError: If `this_node` is not a Node.

        :return: A dictionary containing information about the move.
        :return: `from` - position from which the pointer moved.
        :rtype: str
        :return: `to` - position where the pointer is now.
        :rtype: str
        :return: `distance` distance from the original position to new
        :rtype: int
        :return: `finish` True if its the final destination otherwise False
        :rtype: bool
        :rtype: dict
        """
        if(this_node is not None and not isinstance(this_node, Node)):
            raise NodeError
        prev = this_node.get_prev()
        if(prev is not None and prev.get_data()):
            self.current = self.current.get_prev()
            if(prev.get_prev() is None):
                return {"from":this_node.get_data(),"to":self.current.get_data(),"distance":this_node.get_distance(),"finish":True}
            return {"from":this_node.get_data(),"to":self.current.get_data(),"distance":this_node.get_distance(),"finish":False}
        else:
            self.reverse = False
            self.current = self.tail
            return self.moveforward()
            # print("Konec")
            # return {"from":self.current.get_data(),"to":self.current.get_data(),"distance":this_node.get_distance()}
    
    def current_station(self):
        """
        Retrieves the data of the current station.

        :return: The data of the current station.
        :rtype: str
        """
        return self.current.get_data()
    
    def FindAll(self):
        """
        Retrieves all data from the list.

        :return: A list of all data in the list.
        :rtype: list[str]
        """
        MyData = []
        this_node = self.tail
        while this_node:
            MyData.append(this_node.get_data())
            this_node = this_node.get_next()
        return MyData
    
    def nextdistance(self):
        """
        Retrieves the distance to the next node or the previous node based on the direction.

        :return: The distance to the next or previous node.
        :rtype: int
        """
        this_node = self.current
        next = this_node.get_next()
        if(self.reverse):
            return this_node.get_distance()
        else:
            if(next):
                return next.get_distance()
            else:
                prev = this_node.get_prev()
                return prev.get_distance()
            
    
    def __str__(self):
        """
        Generates a string representation of the linked list.

        :return: A string representation of the list.
        :rtype: str
        """
        MyString = ""
        this_node = self.tail
        while this_node:
            MyString += f"{this_node.get_data()}, "
            this_node = this_node.get_next()
        if(MyString == ""):
            return "nemá stanice"
        else:
            return "ma stanice "+MyString[:-2]

    
# MyList = LinkedList()
# MyList.addtail("555",1)
# MyList.addtail("888",1)
# MyList.addtail("121212",1) 
# MyList.addhead("999",1)
# MyList.remove("121212")
# print(MyList.head.get_data())
# print(MyList.tail.get_data())
# print(MyList.FindAll())
# print(MyList.current.get_data())
# print(MyList.moveforward())
# print(MyList.moveforward())
# print(MyList.moveforward())
# print(MyList.moveforward())
# print(MyList.moveforward())
# print(MyList.Find("121212"))



        