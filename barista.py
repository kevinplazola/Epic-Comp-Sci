class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, receipt):
        self.receipt = receipt

    def add_item(self, item):
        self.receipt.append(item)

    def calculate_taxes(self):
        total = sum(item.price for item in self.receipt)
        return total * 0.07

    def calculate_total(self):
       return sum(item.price for item in self.receipt)

    def print_receipt(self):
        print("CROSSROAD'S CAFE\n-----------------")
        for item in self.receipt:
            print(f" {item.name}: ${item.price:.2f}")
        print(f"Subtotal: ${self.calculate_total()}")
        print(f"Tax: ${self.calculate_taxes():.2f}")
        print(f"Total: ${self.calculate_total() + self.calculate_taxes():.2f}")
        print(f"----------------\nEND OF RECEIPT")

def main():
   
   menu = [
       MenuItem("bagel", 3.00),
       MenuItem("burrito", 5.00),
       MenuItem("ramen", 1.50),
       MenuItem("gum", 0.50)
   ]
     
   order1 = Order([])
   order1.add_item(menu[1])
   order1.add_item(menu[1])
   order1.add_item(menu[3])

   total = order1.calculate_total() + order1.calculate_taxes()
   print(f"The total due is {total:.2f}")

   order1.print_receipt()
   

if __name__ == '__main__':
    main()
