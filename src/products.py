class Products:
    prod_list = []
    def __init__(self,list):
        self.prod_list = list

    def add_product(self, list_item):
        if type(list_item) == 'list':
            return 'null'
        else:
            self.prod_list.append(list_item)

    def update_product(self,indx,name,price):
        self.prod_list[indx] = {'name':name,'price':price}

    def is_product_exist(self,index):
        for indx, l in enumerate(self.prod_list):
            if index == index:
                return indx
            else:
                return "none"

    def del_product(self,indx):
        self.prod_list.remove(indx)
        

    def display_products(self):
        print("Indx  Name  Price")
        for index , lst in enumerate(self.prod_list):
            name=dict(lst)
            print(f"{index})   {name['name']}   {name['price']}" )

    def get_products(self):
        return self.prod_list
    
