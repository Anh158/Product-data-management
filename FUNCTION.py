import DATA_STRUCTURE as DS
class productEngine():
    #1.Load data from file and display
    def load_data(self):
        self.product_list = DS.my_list()
        input_link =  input("Please enter the file path:")
        try: data_file =  open(input_link, mode = "r")
        except: 
            print("File's path is not correct")
            data_file = None
        if data_file is not None:
            str_data = data_file.readlines()
            data_file.close()
            for data in str_data:
                product_infor = data.rstrip("\n").split(",")
                id = product_infor[0]
                title = product_infor[1]
                quantiy = int(product_infor[2])
                price =  float(product_infor[3])
                product_node = DS.Node(id, title, quantiy, price)
                self.product_list.pushback(product_node)
            print("Load file successfully")
            self.display()
            return self.product_list         
    #2.Input and add to the end
    def add_newproduct(self):
        #enter new ID and check new ID
        id = None
        while id is None:
            id = input("Please enter product's ID: ")
            if len(id)==0:
                print("You haven't enter ID, please re-enter product ID")
                id = None
                continue
            if self.product_list.search(id) != -1:
                print("This id has been used, please choose another id")
                id = None
                continue
        #input product's name
        Title  = input("Please enter new product's name:")
        while len(Title)==0:
            Title = input("You haven't input Title of new product, please re-enter")
        # Check input value format
        quantity = -1
        input_qtt = input("Please enter quantiy of new product:")
        while quantity <=0:
            try :quantity = int(input_qtt)
            except: 
                print("You input wrong data type")
                input_qtt = input("Please re-enter product quantiy:")
                quantity =-1
                continue
            if quantity <= -1: 
                print("You input minus value")
                input_qtt = input("Please re-enter product quantiy:")
                continue
        #Check input value format
        price = -1
        input_price= input("Please enter price of new product:")
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
        add_Node = DS.Node(id, Title, quantity, price)
        add_Node.print_node(add_Node)
        self.product_list.pushback(add_Node)     
    #3.Display data
    def display(self):
        self.product_list.print_all()
    #4.Save product list to file
    def save_to_file(self):
        select = -1
        while select < 0 or select>1:
            try:select = int(input("Do you want to save your change?\n0:No\n1:Yes\n"))
            except:
                print("You input wrong type, please re-enter your selection")
                continue
            if select >1 or select <0:
                print("Your selection is wrong, please re-enter your selection")
                continue
        if select ==1:
            output_link =  input("Please enter output file path:")
            with open(output_link,"w") as output_file:
                temp = self.product_list.head
                while temp is not None:
                    output_file.write(temp.id+","+temp.title+","+str(temp.quantity)+","+str(temp.price)+"\n")
                    temp= temp.next
            print("The file is saved successfully!")      
    #5.Search by ID
    def search_ID(self):
        id = input("Please enter product's ID need to find:")
        product = self.product_list.search(id)
        if product == -1:
            print("ID is not in the product list")
        else:
            print("{:^8}""|{:^16}""|{:^18}""|{:^8}".format("ID","Title","Quantity", "Price"))
            print("{:^8}""|{:^16}""|{:^18}""|{:^8}".format(product.id,product.title,product.quantity, product.price))
            return product
    #6.Delete by ID
    def delete_ID(self):
        del_product =  self.search_ID()
        if del_product is not None:
            self.product_list.delete(del_product)
            print("The product is removed from dataset successfully")        
    #7.Sort by ID
    def sort_ID(self):
        lst = self.product_list
        self.product_list = self.product_list.mergesort(lst)
        self.product_list.print_all()
    #8.Convert to binary
    def covert_binary(self):
        product = self.search_ID()
        if product is not None:
            print("Convert quantity to binary:",product.convert_to_binary(product.quantity))
    #9.Edit Information   
    def edit_infor(self):
        id = input("Please enter product's ID need to find:")
        edit_product = self.product_list.edit(id)
        if edit_product != -1:
            edit_product.print_node(edit_product)
            self.save_to_file()
        else:print("ID is not in Product list")