 purchase_amount=int(input("Enter the purchase_amount"))
if purchase_amount>500:
    discount=purchase_amount*20%100
    final_amount=purchase_amount-discount
    print(final_amount)
elif purchase_amount>=200 and purchase_amount>=500:
    discount=purchase_amount*10/100
    final_amount=purchase_amount-discount
   print(final_amount)
else:
print("No discount")




