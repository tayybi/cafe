import os
from tabnanny import check

product_list = []
couriers_list = []
orders_list = []

# reading data of courior and products from file
#adding into list 
def read_from_file():
    f = open("data/couriers.txt", "r")
    f1 = f.readlines()
    for x in f1:
        couriers_list.append(x.strip("\n"))
    f.close

    f = open("data/products.txt", "r")
    f1 = f.readlines()
    for x in f1:
        product_list.append(x[:-1])
    f.close

    f = open("data/orders.txt", "r")
    f1 = f.readlines()
    for x in f1:
        orders_list.append(x[:-1])
    f.close

# reading data of courior and products from file
#adding into list 
def write_into_file():
    f = open("data/couriers.txt", "w")
    for x in couriers_list:
        f.write(x+"\n")
    f.close()
    
    f = open("data/products.txt", "w")
    for x in product_list:
        f.write(x+"\n")
    f.close()  

    f = open("data/orders.txt", "w")
    for x in orders_list:
        f.write(x+"\n")
    f.close()    

# product menue
def product_menue():

    second_input = 1
    while second_input != 0:
        print("\n******* PRODUCT MENUE *******\n")
        print("0 Main Menue \n1 All products \n2 Add new product \n3 update an Existing product \n4 Delete a product")
        second_input = int(input(""))

        if second_input == 1:
            print("\nAll products List\n")
            for l in product_list:
                print(l)

        elif second_input == 2:
            new_product = input("\nEnter the name of new product: ")
            product_list.append(new_product)
            print("\nNew List Added")

        elif second_input == 3:
            flag = False
            while flag != True:
                update_product = input("\nEnter the name of product:  ")
                for indx, l in enumerate(product_list):
                    if update_product == l:
                        product_list[indx] = input("\nEnter new product:  ")
                        print("\nproduct updated")
                        flag = True
                    elif update_product == '0':
                        flag = True
                print("\nproduct not exist try again / 0 for back")

        elif second_input == 4:
            flag = False
            while flag != True:
                del_product = input("\nEnter the name of product: ")
                if del_product in product_list:
                    product_list.remove(del_product)
                    print("\nproduct Deleted")
                    flag = True
                elif del_product == '0':
                    flag = True
                print("\nproduct not exist try again / 0 for back")

# couriour menue
def courioure_menue():

    second_input = 1
    while second_input != 0:
        print("\n******* PRODUCT MENUE *******\n")
        print("0 Main Menue \n1 All Couriers \n2 Add new Couriers \n3 update an Existing Couriers \n4 Delete a Couriers")
        second_input = int(input(""))

        if second_input == 1:
            print("All Couriers List\n")
            for l in couriers_list:
                print(l)

        elif second_input == 2:
            new_courier = input("Enter the name of new Courier: ")
            couriers_list.append(new_courier)
            print("New Courier Added")

        elif second_input == 3:
            flag = False
            while flag != True:
                update_courier = input("Enter the name of courier:  ")
                for indx, l in enumerate(couriers_list):
                    if update_courier == l:
                        couriers_list[indx] = input("Enter new courier:  ")
                        print("courier updated")
                        flag = True
                    elif update_courier == '0':
                        flag = True
                print("courier not exist try again / 0 for back")

        elif second_input == 4:
            flag = False
            while flag != True:
                del_courier = input("Enter the name of courier: ")
                if del_courier in couriers_list:
                    product_list.remove(del_courier)
                    print("courier Deleted")
                    flag = True
                elif del_courier == '0':
                    flag = True
                print("courier not exist try again / 0 for back")


# Order Menue
def order_menue():

    second_input = 1
    while second_input != 0:
        print("\n******* ORDER MENUE *******\n")
        second_input = int(input("0 Main Menue \n1 All Orders \n2 Create Order \n3 update Order status \n4 Update Existing order \n5 Delete order : "))
        
        if second_input == 1:
            #print all order
            print("All Orders \n")
            for l in orders_list:
                print(l)

        elif second_input == 2:
            #create new order
            c_name = input("Customer name: ")
            c_address = input("Customer Address: ")
            c_phone = input("Customer Phone: ")
            o_status = "PREPARING"
            new_order = {"customer_name":c_name,"customer_address":c_address,"customer_phone":c_phone,"status":o_status}
            orders_list.append(new_order)
            print("New Order Added")

        elif second_input == 3:
            #update order status
            for index,name in enumerate(orders_list):
                print(f"{index}   "+name["customer_name"])
            flag=""   
            while flag != 'no':
                order_no = input("Enter Order number for status change or 'no' for back:  ")
                if order_no == 'no':
                    flag = 'no'
                else:
                    for indx, l in enumerate(orders_list):
                        if int(order_no) == indx:
                            print("Current order status is:"+ l.get("status"))
                            check_update = input("\nDo you want update status? y/n")
                            if check_update == 'y':
                                get_status = int(input("\n0 'PPREPARING'\n1 'READY'\n2 'COMPLETED'"))
                                if get_status == 0:
                                    l.update({"status":"PPREPARING"})
                                    flag = 'no'
                                elif get_status == 1:
                                    l.update({"status":"READY"})
                                    flag = 'no'
                                elif get_status == 1:
                                    l.update({"status":"COMPLETED"})
                                    flag = 'no'

                        else:
                            print("Order not exist")

        elif second_input == 4:
            #update existing order
            for index,name in enumerate(orders_list):
                print(f"{index}   "+name["customer_name"])
            flag=""   
            while flag != 'no':
                order_no = input("Enter Order number for updation or 'no' for back:  ")
                if order_no == 'no':
                    flag = 'no'
                else:
                    for indx, l in enumerate(orders_list):
                        if int(order_no) == indx:
                            name = input("\nEnter new name: ")
                            add = input("\nEnter new address: ")
                            ph = input("\nEnter newphone : ")
                            l.update({"customer_name":name,"customer_address":add,"customer_phone":ph})
                            print("Order Updated")
                            flag="no"
                        else:
                            print("Order not exist")
        
        elif second_input == 5:
            #Delete order
            for index,name in enumerate(orders_list):
                print(f"{index}   "+name["customer_name"])
            flag=""   
            while flag != 'no':
                order_no = input("Enter Order number for Deletion or 'no' for back:  ")
                if order_no == 'no':
                    flag = 'no'
                else:
                    for indx, l in enumerate(orders_list):
                        if int(order_no) == indx:
                            orders_list.pop(indx)
                            print("Order Deleted")
                            flag="no"
                        else:
                            print("Order not exist")



# main menue

read_from_file()
first_input = 1
while first_input != 0:
    os.system("cls")
    print("******* Welcome to POP-UP CAFE *******\n")
    first_input = int(input("0 To Exit \n1 Product Menue \n2 Couriers Menue \n3 Order Menue: "))
    try:
        if first_input <4:
            if first_input == 1:
                os.system("cls")
                product_menue()

            elif first_input == 2:
                os.system("cls")
                courioure_menue()
            elif first_input == 3:
                os.system("cls")
                order_menue()

    except ValueError as r:
        print(r)

write_into_file()
print("Thank you very much")
