from Error import *

class Node():
    def __init__(self, data, distance, next_node=None, prev_node=None):
        if (not isinstance(data, str)):
            raise DataTypeError
        if (len(data) < 3):
            raise DataLenghtError

        if (not isinstance(distance, int)):
            raise DistanceTypeError

        if (next_node is not None and not isinstance(next_node, Node)):
            raise NextNodeError

        if (prev_node is not None and not isinstance(prev_node, Node)):
            raise PrevNodeError

        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node
        self.distance = distance

    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next_node):
        if (new_next_node is not None and not isinstance(new_next_node, Node)):
            raise NextNodeError
        self.next_node = new_next_node

    def get_prev(self):
        return self.prev_node
    
    def set_prev(self, new_prev):
        if (new_prev is not None and not isinstance(new_prev, Node)):
            raise PrevNodeError
        self.prev_node = new_prev 

    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        if (not isinstance(new_data, str)):
            raise DataTypeError
        if (len(new_data) < 3):
            raise DataLenghtError
        self.data = new_data
    
    def get_distance(self):
        return self.distance
    
    def set_distance(self, new_distance):
        if (not isinstance(new_distance, int)):
            raise DistanceTypeError
        self.distance = new_distance
