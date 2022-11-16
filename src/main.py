import os
import products
import couriers
import orders
import db_handler

prod_list = db_handler.DBhandler().read_from_prod()
courier_list = db_handler.DBhandler().read_from_courier()

# main menue
def main_menu():
    
    first_input = 1
    while first_input != 0:
        os.system("cls")
        print("******* Welcome to POP-UP CAFE *******\n")
        first_input = int(input("""
        0) To Exit \n
        1) Product Menue \n
        2) Couriers Menue \n
        3) Order Menue: """))
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
                
    db_handler.DBhandler.write_into_prod(prod_list)
    db_handler.DBhandler.write_into_courier(courier_list)
    print("Thank you very much")

# product menue
def product_menue():
    prod_obj = products.Products(prod_list)
    prod_menue_input = 1
    while prod_menue_input != 0:
        print("\n******* PRODUCT MENUE *******\n")
        prod_menue_input = int(input('''
        0 Main Menue \n
        1 All products \n
        2 Add new product \n
        3 update an Existing product \n
        4 Delete a product: '''))
       
        #List of all products
        if prod_menue_input == 1:
            os.system('cls')
            print("\n******* All products *******\n")
            prod_obj.display_products()

        #adding new products
        elif prod_menue_input == 2:
            os.system('cls')
            print("\n******* Adding New Product *******\n")
            new_product_name = input("\nEnter the name of product: ")
            new_product_price = input("\nEnter the Price: ")
            prod_obj.add_product({'name':new_product_name,'price':new_product_price})
            print("\nNew Product Added...")

        # Updating existing product
        elif prod_menue_input == 3:
            temp = 'y'
            while not temp == 'n':
                os.system('cls')
                print("\n******* Updating Existing Product *******\n")
                prod_obj.display_products()
                prod_indx = int(input("\nChoose the index for update:  "))

                prod_check = prod_obj.get_products()[prod_indx]
                if prod_check != "":
                    new_prod_name = input("\nEnter new product Name:  ")
                    new_prod_price = float(input("\nEnter new product price:  "))
                    prod_obj.update_product(prod_indx,new_prod_name,new_prod_price)
                    print("\nProduct Updated...")
                    break
                else:
                     temp = input("\nProduct not exist try again y/n: ")
       
        #Deleting a product
        elif prod_menue_input == 4:
            temp = 'y'
            while not temp == 'n':
                os.system('cls')
                print("\n******* Delete a Product *******\n")
                prod_obj.display_products()
                prod_indx = int(input("\nChoose the index for delete:  "))
                prod_check = prod_obj.get_products()[prod_indx]
                if prod_check != "":
                    prod_obj.del_product(prod_indx)
                    print("\nProduct Deleted...")
                    break
                else:                    
                    temp = input("\nProduct not exist try again y/n")


# couriour menue
def courioure_menue():
    cour_obj = couriers.Couriers(courier_list)
    cour_menue_input = 1
    while cour_menue_input != 0:
        print("\n******* COURIER MENUE *******\n")
        cour_menue_input = int(input("""
        0 Main Menue \n
        1 All Couriers \n
        2 Add new Couriers \n
        3 Update an Existing Couriers \n
        4 Delete a Couriers: """))

        # All couriers
        if cour_menue_input == 1:
            os.system('cls')
            print("******* All Couriers *******\n")
            cour_obj.display_couriour()
        
        # Addidng new Courier
        elif cour_menue_input == 2:
            os.system('cls')
            print("\n******* Adding New Courier *******\n")
            new_name = input("\nEnter the name of courier: ")
            new_phone = input("\nEnter the phone number: ")
            cour_obj.add_courior({'name':new_name,'phone':new_phone})
            print("\nNew Courier Added")
        
        #Update an Existing courier
        elif cour_menue_input == 3:
            temp = 'y'
            while not temp == 'n':
                os.system('cls')
                print("\n******* Updating Existing Courier *******\n")
                cour_obj.display_couriour()
                indx = int(input("\nChoose the index for update:  "))

                prod_check = cour_obj.get_courier()[indx]
                if prod_check != "":
                    new_name = input("\nEnter new product Name:  ")
                    new_phone = float(input("\nEnter new product phone:  "))
                    cour_obj.update_courier(indx,new_name,new_phone)
                    print("\nProduct Updated...")
                    break
                else:
                     temp = input("\nCourier not exist try again y/n: ")
        
        #Delete a Courier
        elif cour_menue_input == 4:
            temp = 'y'
            while not temp == 'n':
                os.system('cls')
                print("\n******* Delete a Courier *******\n")
                cour_obj.display_couriour()
                indx = int(input("\nChoose the index for delete:  "))
                cour_check = cour_obj.get_courier()[indx]
                if cour_check != "":
                    cour_obj.del_courier(indx)
                    print("\nProduct Deleted...")
                    break
                else:
                    temp = input("\Courier not exist try again y/n")


# Order Menue
def order_menue():

    cour_menue_input = 1
    order_data = orders.Orders()
    while cour_menue_input != 0:
        print("\n******* ORDER MENUE *******\n")
        cour_menue_input = int(input("0 Main Menue \n1 All Orders \n2 Create Order \n3 update Order status \n4 Update Existing order \n5 Delete order : "))
        
        # All orders list
        if cour_menue_input == 1:
            os.system("cls")
            print("******* All Orders *******\n")
            order_data.display_order()

        #create new order
        elif cour_menue_input == 2:
            os.system("cls")
            print("\n******* Create New Order *******\n")
            c_name = input("Customer name: ")
            c_address = input("Customer Address: ")
            c_phone = input("Customer Phone: ")
            o_status = "PREPARING"
            new_order = {"customer_name":c_name,"customer_address":c_address,"customer_phone":c_phone,"status":o_status}
            order_data.add_ordert(new_order)
            print("\nNew Order Added...")
        
        #update order status
        elif cour_menue_input == 3:
            temp = 'y'   
            while temp != 'n':
                os.system("cls")
                order_data.display_order()
                print("\n******* Update Order Status *******\n")
                order_no = int(input("Enter Order number: "))
                ord_lst = order_data.is_order_exist(order_no)
                if ord_lst != "none":
                    print("Current order status is:"+ ord_lst.get("status"))
                    temp = input("\nDo you want update status? y/n")
                    if temp == 'y':
                        get_status = int(input("\n0 'PPREPARING'\n1 'READY'\n2 'COMPLETED' "))
                        if get_status == 0:
                            ord_lst.update({"status":"PPREPARING"})
                            order_data.update_order(order_no,ord_lst)
                            break
                        elif get_status == 1:
                            ord_lst.update({"status":"READY"})
                            order_data.update_order(order_no,ord_lst)
                            break
                        elif get_status == 2:
                            ord_lst.update({"status":"COMPLETED"})
                            order_data.update_order(order_no,ord_lst)
                            break
                else:
                    temp = input("\nOrder not exist try again y/n: ")
        #update an existing order
        elif cour_menue_input == 4:
            temp = 'y'   
            while temp != 'n':
                os.system("cls")
                order_data.display_order()
                print("\n******* Update Order *******\n")
                order_no = int(input("Enter Order number: "))
                ord_lst = order_data.is_order_exist(order_no)
                if ord_lst != "none":
                    name = input("\nEnter new name: ")
                    add = input("\nEnter new address: ")
                    ph = input("\nEnter newphone : ")
                    ord_lst.update({"customer_name":name,"customer_address":add,"customer_phone":ph})
                    order_data.update_order(order_no,ord_lst)
                    print("Order Updated")
                    break
                else:
                    temp = input("\nOrder not exist try again y/n: ")

        #Delete an order
        elif cour_menue_input == 5:
            temp = 'y'   
            while temp != 'n':
                os.system("cls")
                order_data.display_order()
                print("\n******* Update Order *******\n")
                order_no = int(input("Enter Order number: "))
                ord_lst = order_data.is_order_exist(order_no)
                if ord_lst != "none":
                    ord_lst.update({"customer_name":name,"customer_address":add,"customer_phone":ph})
                    order_data.del_order(order_no)
                    print("Order Deleted")
                    break
                else:
                    temp = input("\nOrder not exist try again y/n: ")
    order_data.write_into_file()
            
main_menu()