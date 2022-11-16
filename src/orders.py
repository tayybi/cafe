
class Orders:
    order_list = []
    def __init__(self,list):
        self.order_list = list

    def add_order(self, list_item):
        self.order_list.append(list_item)

    def update_order_status(self,indx,status):
        self.order_list[indx].update({"status": status})
    
    def update_existing_order(self,indx,data):
        self.order_list[indx] = data
        
    def is_order_exist(self,index):
        for indx, l in enumerate(self.order_list):
            if index == index:
                return indx
            else:
                return "none"

    def del_order(self,indx):
        self.order_list.pop(indx)
        

    def display_order(self):
        print("Indx  Name  Status  Courier  Items  Address")
        for index , lst in enumerate(self.order_list):
            name=dict(lst)
            print(f"{index})   {name['customer_name']}   {name['status']}  {name['courier']}  {name['items']}  {name['customer_address']}" )

    def get_order(self):
        return self.order_list
    
