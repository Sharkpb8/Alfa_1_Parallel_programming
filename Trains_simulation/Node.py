from Error import *

class Node():
    def __init__(self, data = None, distance = None, next_node=None, prev_node=None):
        """
        Represents a node in a doubly linked list.

        :param data: The string data of the node (minimum length 3).
        :type data: str
        :param distance: The distance value of the node (non-negative integer).
        :type distance: int
        :param next_node: Reference to the next node in the list.
        :type next_node: Node or None
        :param prev_node: Reference to the previous node in the list.
        :type prev_node: Node or None

        :raises EmptyInputError: If `data` or `distance` is missing.
        :raises DataTypeError: If `data` is not a string.
        :raises DataLenghtError: If `data` length is less than 3.
        :raises DistanceTypeError: If `distance` is not an integer.
        :raises DistanceLenghtError: If `distance` is negative.
        :raises NextNodeError: If `next_node` is not a Node or None.
        :raises PrevNodeError: If `prev_node` is not a Node or None.
        """
        if(data is None or distance is None):
            raise EmptyInputError
        if (not isinstance(data, str)):
            raise DataTypeError
        if (len(data) < 3):
            raise DataLenghtError

        if (not isinstance(distance, int)):
            raise DistanceTypeError
        if (distance < 0):
            raise DistanceLenghtError

        if (next_node is not None and not isinstance(next_node, Node)):
            raise NextNodeError

        if (prev_node is not None and not isinstance(prev_node, Node)):
            raise PrevNodeError

        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node
        self.distance = distance

    def get_next(self):
        """
        Retrieves the next node.

        :return: The next node or None if there is no next node.
        :type: Node or None
        """
        return self.next_node
    
    def set_next(self, new_next_node):
        """
        Updates the reference to the next node.

        :param new_next_node: The new next node.
        :type new_next_node: Node or None

        :raises NextNodeError: If `new_next_node` is not a Node or None.
        """
        if (new_next_node is not None and not isinstance(new_next_node, Node)):
            raise NextNodeError
        self.next_node = new_next_node

    def get_prev(self):
        """
        Retrieves the previous node.

        :return: The previous node or None if there is no previous node.
        :type: Node or None
        """
        return self.prev_node
    
    def set_prev(self, new_prev):
        """
        Updates the reference to the previous node.

        :param new_prev: The new previous node.
        :type new_prev: Node or None

        :raises PrevNodeError: If `new_prev` is not a Node or None.
        """
        if (new_prev is not None and not isinstance(new_prev, Node)):
            raise PrevNodeError
        self.prev_node = new_prev 

    def get_data(self):
        """
        Retrieves the data stored in the node.

        :return: The string data of the node.
        :type: str
        """
        return self.data
    
    def set_data(self, new_data):
        """
        Updates the data in the node with validation.

        :param new_data: The new data for the node.
        :type new_data: str

        :raises DataTypeError: If `new_data` is not a string.
        :raises DataLenghtError: If `new_data` length is less than 3.
        """
        if (not isinstance(new_data, str)):
            raise DataTypeError
        if (len(new_data) < 3):
            raise DataLenghtError
        self.data = new_data
    
    def get_distance(self):
        """
        Retrieves the distance value.

        :return: The distance value of the node.
        :type: int
        """
        return self.distance
    
    def set_distance(self, new_distance):
        """
        Updates the distance value with validation.

        :param new_distance: The new distance value.
        :type new_distance: int

        :raises DistanceTypeError: If `new_distance` is not an integer.
        :raises DistanceLenghtError: If `new_distance` is not an non-negative integer.
        """
        if (not isinstance(new_distance, int)):
            raise DistanceTypeError
        if(new_distance <0):
            raise DistanceLenghtError
        self.distance = new_distance