#create node
class Node():
    def __init__(self, id, title, quantity, price):
        self.id = id
        self.title = title
        self.quantity =  quantity
        self.price =  price
        self.next = None 
        self.prev = None
    def print_node(self, node):
        print("{:^8}""|{:^16}""|{:^18}""|{:^8}".format("ID","Title","Quantity", "Price"))
        print("{:^8}""|{:^16}""|{:^18}""|{:^8}".format(node.id,node.title,node.quantity, node.price))
    def convert_to_binary(self,element):   
        #calculate binary value
        binary_str = ""
        if element == 0:
            return binary_str
        elif element ==1:
            return "1"            
        else:
            return self.convert_to_binary(element//2)+str(element%2)

#CLASS MY LIST
class my_list():#Double linked list
    def __init__(self):
        self.head =  None
        self.tail =  None
    #Add element at the beginning of the list
    def insertion(self,element):
        new_node = Node(element)
        self.head.prev =  new_node
        new_node.next = self.head
        self.head =  new_node
    # Add element at the end of the list
    def pushback(self,node):
        #new_node = Node(element)
        if self.head == None:
            self.head = node
            self.tail = node
        else:      
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail =  node
    #delete first element
    def deletion(self):
        self.head  = self.head.next
        self.head.prev =  None
    #Display the complete list
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.id, temp.title, temp.quantity, temp.price)
            temp = temp.next
    #Search element
    def search(self, element):
        temp = self.head
        while temp is not None:
            if temp.id == element:
                return temp
            else: temp = temp.next
        return -1
    #delete element using given key
    def delete(self,node): 
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            pre = node.prev
            nxt = node.next
            pre.next = nxt
            nxt.prev = pre
    #print linked list   
    def print_all(self):
        print("{:^8}""|{:^16}""|{:^18}""|{:^8}".format("ID","Title","Quantity", "Price"))
        temp =  self.head
        while temp is not None:
            #print(temp)
            print("{:^8}""|{:^16}""|{:^18}""|{:^8}".format(temp.id,temp.title,temp.quantity, temp.price))
            temp = temp.next
    #merge sort
    #if value1< value2 return true, else return false
    def compare(self,value1, value2):
        for i in range(min(len(value1), len(value2))):
            if value2[i] > value1[i]:
                return True
            elif value2[i] < value1[i]:
                return False
            else:
                continue
        if len(value1)> len(value2):
            return False
        else: return True 

        
    #PROCEED MERGE SORT
    #Get middle by using The Tortoise and The Hare Approach:
        #using two pointer: fast(2X) and slow(1X) then return position of slow pointer
    def getMiddle(self,lst):
        slow = lst.head
        fast = lst.head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    #Merge function to merge two list in mergesort function:
    def Merge(self, list1, list2):
        merged_lst = my_list()
        temp1 = list1.head
        temp2 = list2.head
        while temp1 != None and temp2 != None:            
            id1 = temp1.id
            node_temp1 =  Node(temp1.id, temp1.title, temp1.quantity, temp1.price)
            id2 = temp2.id
            node_temp2 = Node(temp2.id, temp2.title, temp2.quantity, temp2.price)
            if self.compare(id1,id2) == False:
                merged_lst.pushback(node_temp2)
                temp2 = temp2.next
                continue
            elif self.compare(id1, id2) == True:
                merged_lst.pushback(node_temp1)
                temp1 = temp1.next
                continue
        while temp1 != None:
            node_temp1 =  Node(temp1.id, temp1.title, temp1.quantity, temp1.price)
            merged_lst.pushback(node_temp1)
            temp1 = temp1.next
        while temp2 != None:
            node_temp2 = Node(temp2.id, temp2.title, temp2.quantity, temp2.price)
            merged_lst.pushback(node_temp2)
            temp2 = temp2.next
        return merged_lst
    def mergesort(self,lst):
        if lst.head.next == None:
            return lst
        else:
            mid = self.getMiddle(lst)
            #using getmiddle to seprate lst
            #creat list1
            list1 = my_list()
            list1.head = lst.head
            list1.tail = mid
            #create list2
            list2 = my_list()
            list2.head = mid.next
            list2.tail = lst.tail
            #update head, tail
            list1.tail.next =  None
            list2.head.prev = None
            new_list1 = self.mergesort(list1)
            new_list2 = self.mergesort(list2)
            final = self.Merge(new_list1,new_list2) 
            return final    
    def edit(self, element):
            temp = self.head
            while temp is not None:
                if temp.id == element:
                    #edit product's infor. leave input feild empty if don't want to change field
                    print("Information of product", element)
                    print("Please leave the input field empty if you don't want to change this feild")
                    temp.print_node(temp)

                    #edit id
                    id = input("Please edit id:")
                    if len(id)!=0:
                        temp.id =  id
                    #edit product's name
                    Title  = input("Please edit product's name:")
                    if len(Title)!=0:
                        temp.title =  Title
                    #edit quantity
                    quantity = -1
                    input_qtt = input("Please edit quantiy of product:")
                    if len(input_qtt)!=0:
                        #check input format
                        while quantity <=0:
                            try :quantity = int(input_qtt)
                            except: 
                                print("You input wrong data type")
                                input_qtt = input("Please re-enter product quantiy:")
                                #quantity =-1
                                continue
                            if quantity <= -1: 
                                print("You input minus value")
                                input_qtt = input("Please re-enter product quantiy:")
                                continue
                        temp.quantity = quantity
                    #edit price
                    price = -1
                    input_price= input("Please edit price of product:")
                    if len(input_price)!=0:
                        #check input format
                        while price <=-1:
                            try :price = float(input_price)
                            except: 
                                print("You input wrong data type")
                                input_price = input("Please re-enter product's price:")
                                continue
                            if price <= -1:
                                print("You input minus value")
                                input_price = input("Please re-enter product's price:")
                                continue
                        temp.price = price 
                    return temp
                else: temp = temp.next
            return -1
