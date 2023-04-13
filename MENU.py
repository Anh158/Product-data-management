import FUNCTION as manage
class main():
    def __init__(self):
        self.product_data = manage.productEngine()
    def operation(self):
        while 1==1:
            print("+----------------Menu----------------+")
            print("1. Load data from file and display")
            print("2. Input and add to the end")
            print("3. Display")
            print("4. Save product list to file")
            print("5. Search by ID")
            print("6. Delete by ID")
            print("7. Sort by ID")
            print("9.Edit product's information")
            print("0. Exit")
            print("+-----------------------------------+")        
            #enter selection
            selection = -1
            while selection <=-1:
                try: selection =  int(input("Please enter your selection: "))
                except:
                    #print(selection)
                    print("You input wrong data type, please input number")
                    continue
                if selection <=-1:
                    #print(selection)
                    print("You have input minus value, please re-input your selection")
                #elif selection > 11:
                    #print("Your selection is not vailable, please re-select")
                    #selection = -1
                    #continue
            #stat run
            #__init__ to load data from file
            #proceed selection 1
            if selection == 1:
                self.product_data.load_data()
            #proceed selection 2
            elif selection ==2:
                self.product_data.add_newproduct()
            #procedd selection 3:
            elif selection == 3:
                self.product_data.display()
            #proceed selection 4:
            elif selection == 4:
                self.product_data.save_to_file()
            #proceed selection 5
            elif selection ==5:
                self.product_data.search_ID()
            #proceed selection 6
            elif selection == 6:
                self.product_data.delete_ID()
            #proceed selection 7
            elif selection == 7:
                self.product_data.sort_ID()
            #proceed selection 8
            elif selection == 8:
                self.product_data.covert_binary()
            #proceed selection 9
            elif selection ==9:
                self.product_data.edit_infor()
            elif selection == 0:
                break
a=main()
a.operation()
