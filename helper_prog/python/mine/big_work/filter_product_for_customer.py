from product_data import product

def filter_by_price_works_names(works_name, product_price):
    filtered_data = []
    for i in product.values():
        if i["price"] <= product_price and works_name in i["to_who"]:
            filtered_data.append(i)
    return filtered_data