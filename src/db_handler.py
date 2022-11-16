import csv
class DBhandler:
    
    
    def write_into_prod(prod_list):
        fieldnames = ['name', 'price']
        with open('data/product.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(prod_list)

    def read_from_prod(self):
        prod_list = []
        fieldnames = ['name', 'price']
        with open('data/product.csv', encoding="utf8") as f:
            csv_reader = csv.DictReader(f, fieldnames)
            next(csv_reader) # skip first line
            for dic_line in csv_reader:
                prod_list.append(dic_line)
            return prod_list

    def write_into_courier(courier_list):
        fieldnames = ['name', 'phone']
        with open('data/couriers.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(courier_list)

    def read_from_courier(self):
        courier_list = []
        fieldnames = ['name', 'phone']
        with open('data/couriers.csv', encoding="utf8") as f:
            csv_reader = csv.DictReader(f, fieldnames)
            next(csv_reader) # skip first line
            for dic_line in csv_reader:
                courier_list.append(dic_line)
            return courier_list