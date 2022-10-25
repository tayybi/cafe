import os

product_list = []
couriers_list = []

def read_from_file():
    f = open("couriers.txt", "r")
    f1 = f.readlines()
    for x in f1:
        couriers_list.append(x[:-1])
    f.close

    f = open("products.txt", "r")
    f1 = f.readlines()
    for x in f1:
        product_list.append(x[:-1])
    f.close

def write_into_file():
    f = open("couriers.txt", "w")
    for x in couriers_list:
        f.write(x+"\n")
    f.close()
    
    f = open("products.txt", "w")
    for x in product_list:
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

read_from_file()
# main menue
first_input = 1
while first_input != 0:
    os.system("cls")
    print("******* Welcome to POP-UP CAFE *******\n")
    first_input = int(input("0 To Exit \n1 Product Menue \n2 Couriers Menue: "))
    try:
        if first_input <3:
            if first_input == 1:
                os.system("cls")
                product_menue()

            elif first_input == 2:
                os.system("cls")
                courioure_menue()

    except ValueError as r:
        print(r)

write_into_file()
print("Thank you very much")
