from customer import filter_workers
from filter_product_for_customer import filter_by_price_works_names

works_names = ["Front end", "Back end", "Mobile dev", "Designer", "UI/IX", "QI"]


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


def filter_product():
    selected_customers = customers_list_visualization("choose customer: \n")
    product_list = filter_by_price_works_names(
        selected_customers["field"], selected_customers["balance"]
    )
    return [selected_customers, product_list]


def product_list_vizualization(double_data):
    selected_customers = double_data[0]
    product_list = double_data[1]
    selected_customers.update({"products": []})
    check_customer_balance = []
    if type(product_list) != list:
        print(product_list, "\nRestart the program")
        exit(0)
    else:
        while True:
            for i in range(len(product_list)):
                if product_list[i]['price'] <= selected_customers["balance"]:
                    check_customer_balance.append(product_list[i])
            if len(check_customer_balance) > 0:
                for i in range(len(check_customer_balance)):
                    print(f"{i + 1} - {check_customer_balance[i]['name']} / {check_customer_balance[i]['price']} / {check_customer_balance[i]['to_who']}")
                else:
                    print("if 0 salling stopped\n\n")
                    print(f"{selected_customers['name']}'s balance : {selected_customers['balance']}"   )
                while True:
                    product_id = int(input(f"Choose product ID: from 1 to {len(check_customer_balance)}:\n"))
                    if product_id == 0:
                        print(
                            f'customer name: {selected_customers["name"]}\ncustomer balance: {selected_customers["balance"]}\ncustomer\'s products: {selected_customers["products"]}'
                        )
                        print("\n\n\nSalling stopped\n\n\n")
                        exit(0)
                    elif selected_customers['balance'] >= check_customer_balance[product_id - 1]['price']:
                        selected_customers['balance'] -= check_customer_balance[i]['price']
                        selected_customers["products"].append(check_customer_balance[product_id - 1]['name'])
                        print("Product successfully added")
                        check_customer_balance.clear()
                        break
                    else:
                        print("wrong number try again !!!\n")
                        continue
            else:
                print(f"No products for customer {selected_customers['name']}")
                break
        print(
            f'customer name: {selected_customers["name"]}\ncustomer balance: {selected_customers["balance"]}\ncustomer\'s products: {selected_customers["products"]}'
        )
product_list_vizualization(filter_product())