commands = """
                    SHOPPING CART COMMANDS
Hello 👋. The following commands will guide you on managing your shopping cart. Type:

   • HIGHEST ~ Shows the most expensive item in your cart
   • CHEAPEST ~ Shows the least expensive item in our cart
   • TOTAL ~ For total amount of items in cart
   • CHECKOUT ~ For proceeding to payment gateway
   
               © https://github.com/jeniOko/Simplified
"""
print(commands)

prices = [100.01, 25.10, 300.75, 75, 19.99]
total = 0
request = ""
for item in prices:
    total += item
    request = input('Check cart : ')
    if request.upper() == 'TOTAL':
        print(f' The total amount of goods in cart is: ${total}')
    elif request.upper() == 'HIGHEST':
        print(f' The most expensive item costs : ${max(prices)}')
    elif request.upper() == 'CHEAPEST':
        print(f' The cheapest item costs : ${min(prices)}')
    elif request.upper() == 'CHECKOUT':
        print(f'Proceeding to checkout............')
        break
    else:
        print('unknown request. Kindly use the listed commands')
