from customer import filter_workers
from filter_product_for_customer import filter_by_price_works_names
works_names = ["Front end", "back end", "Mobile dev", "designer", "UI/IX", "QI", "lead"]
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
    selected_customer = filter_customers[incoming_number]
    print(f"selected customer:\n{selected_customer}\n")
    return selected_customer


def main_function_visualization():
    selected_customers = customers_list_visualization("choose customer: \n")
    product_list = filter_by_price_works_names(
        selected_customers["field"], selected_customers["balance"]
    )
    return product_list
print(main_function_visualization())
