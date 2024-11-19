author:Nikkita Anna George
created on:16/11/24
program to print stock value

inventory=[
    ("laptop",2,5000.00),
    ("headphones",3,2000.00),
    ("mouse",4,2000.00),
    ("monitor",6,4000.00)
]
highest_stock_value=0
item_with_highest_stock_value=None

for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    total_value=quantity*unit_price
    print(f"Item Name:{item_name},the total_value is:{total_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f'Highest stock value is:{highest_stock_value}')
print(f'Item with highest stock value is:{item_with_highest_stock_value}')



