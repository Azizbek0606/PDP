import main
from product_data import product

def filter_workers(works_names_list):
    main_data = main.works(works_names_list)
    full_data = {}
    result_customer = {}
    for i in main_data.keys():
        for k, v in main_data[i].items():
            full_data.update({k: {"balance": sum(v["salary"]), "field": i, "name": k}})
        else:
            result_customer.update({i: full_data})
            full_data = {}
    return result_customer