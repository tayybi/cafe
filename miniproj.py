import imp


import os
from re import T
product_list = []
first_input = 1

while first_input !=0:
    
    print("Welcome to London Cafe \n0 to Exit")
    print("1 to Menu")

    first_input = int(input(""))
    if first_input ==1:
        second_input = 1

        while second_input !=0:
            print("0 Main Menue \n1 All products \n2 Add new product \n3 update an Existing product \n4 Delete a product")
            second_input = int(input(""))

            if second_input == 1:
                print("All products List\n")
                for l in product_list:
                    print(l)
                    
            elif second_input == 2:
                new_product = input("Enter the name of new product: ")
                product_list.append(new_product)
                print("New List Added")

            elif second_input == 3:
                flag = False
                while flag != True:
                    update_product = input("Enter the name of product:  ")
                    for indx, l  in enumerate(product_list):
                        if update_product == l:
                            product_list[indx] = input("Enter new product:  ")
                            print("product updated")
                            flag = True
                        elif update_product == '0':
                            flag = True
                    print("product not exist try again / 0 for back")

            elif second_input == 4:
                flag = False
                while flag != True:
                    del_product = input("Enter the name of product: ")
                    if del_product in product_list:
                            product_list.remove(del_product)
                            print("product Deleted")
                            flag = True
                    elif del_product == '0':
                        flag = True
                    print("product not exist try again / 0 for back")
                

            
print("Thank you very much by by")
