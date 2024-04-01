import main
import product_data
work_name = ["front end", "back end", "design", "ui/ux"]
main_data = main.works(work_name)
full_data = {}
customer = {}
for i in main_data.keys():
    for k , v in main_data[i].items():
        full_data.update({k:{"balance":sum(v['salary']) , "field":i , "name":k}})
    else:
        customer.update({i: full_data})
        full_data = {}
print(product_data)
