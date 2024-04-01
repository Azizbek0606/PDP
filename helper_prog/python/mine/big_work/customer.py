import main
from product_data import product

works_names = ["front end", "back end", "design", "ui/ux"]


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


def filter_by_price_works_names(works_name, product_price):
    filtered_data = []
    for i in product.values():
        if i["price"] <= product_price and works_name in i["to_who"]:
            filtered_data.append(i)
    return filtered_data


def customers_list_visualization(incoming_text):
    customers_list = filter_workers(works_names)
    filter_customers = []
    counter = 0
    print(incoming_text)
    for i in customers_list.keys():
        for k in customers_list[i].values():
            filter_customers.append(k)
            counter += 1
            print(f"{counter} - {k['name']} / {k['balance'] } / {k['field']}")
    incoming_number = 0
    while True:
        customer_index = int(
            input(f"enter number of customers\nfrom 1 to {counter}:\n")
        )
        if customer_index <= counter and customer_index >= 1:
            incoming_number = customer_index - 1
            break
        else:
            print("wrong number try again !!!\n")
            continue
    selected_customer = filter_customers[incoming_number].items()

customers_list_visualization("choose customer:\n")
