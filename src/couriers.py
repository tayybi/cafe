
class Couriers:
    courior_list = []
    def __init__(self,list):
        self.courior_list = list

    def add_courior(self, list_item):
        # if type(list_item) != 'list':
        #     return 'null'
        # else:
        self.courior_list.append(list_item)

    def update_courier(self,indx,name,phone):
        self.courior_list[indx] = {'name':name,'phone':phone}

    def is_cour_exist(self,index):
        for indx, l in enumerate(self.courior_list):
            if index == index:
                return indx
            else:
                return "none"

    def del_courier(self,indx):
        self.courior_list.pop(indx)
        

    def display_couriour(self):
        print("Indx  Name  Phone")
        for index , lst in enumerate(self.courior_list):
            name=dict(lst)
            print(f"{index})   {name['name']}   {name['phone']}" )

    def get_courier(self):
        return self.courior_list
    
