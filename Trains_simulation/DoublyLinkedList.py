class  Node():
    def __init__(self,data,next_node = None,prev_node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def get_next(self):
        return self.next_node
    
    def set_next(sef,new_next_node):
        sef.next_node = new_next_node

    def get_prev(self):
        return self.prev_node
    
    def set_prev(sef,new_prev):
        sef.prev_node = new_prev 

    def get_data(self):
        return self.data
    
    def set_data(sef,new_data):
        sef.data = new_data
        
class LinkedList():
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail
        self.current = tail
        self.reverse = False
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def addtail(self,data):
        new_node = Node(data,self.head)
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
    def addhead(self,data):
        new_node = Node(data,None,self.head)
        if self.tail:
            head_node = self.head
            self.head = new_node
            new_node.set_prev(head_node)
            head_node.set_next(new_node)
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1
    
    def remove(self,data):
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
                    next.set_prev(self.tail)
                    self.current = self.tail
                self.size -= 1
                break
            else:
                this_node = this_node.get_prev()
    
    def moveforward(self):
        this_node = self.current
        next = this_node.get_next()
        if(not self.reverse):
            if(next is not None and next.get_data()):
                    self.current = self.current.get_next()
                    return {"from":this_node.get_data(),"to":self.current.get_data()}
            else:                
                self.reverse = True
                return self.movebackward(this_node)
        else:
            return self.movebackward(this_node)
    
    def movebackward(self,this_node):
        prev = this_node.get_prev()
        if(prev is not None and prev.get_data()):
            self.current = self.current.get_prev()
            return {"from":this_node.get_data(),"to":self.current.get_data()}
        else:
            self.reverse = False
            return {"from":this_node.get_data(),"to":this_node.get_data()}



    # def Find(self,data):
    #     this_node = self.head
    #     while this_node:
    #         if this_node.get_data() == data:
    #             return data
    #         else:
    #             this_node = this_node.get_next()
    #     return None
    
    def FindAll(self):
        MyData = []
        this_node = self.tail
        while this_node:
            MyData.append(this_node.get_data())
            this_node = this_node.get_next()
        return MyData
    
    def __str__(self):
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
# MyList.addtail(5)
# MyList.addtail(8)
# MyList.addtail(12) 
# MyList.addhead(9)
# MyList.remove(12)
# print(MyList.head.get_data())
# print(MyList.tail.get_data())
# print(MyList.FindAll())
# print(MyList.current.get_data())
# print(MyList.moveforward())
# print(MyList.moveforward())
# print(MyList.moveforward())
# print(MyList.moveforward())
# print(MyList.moveforward())



        