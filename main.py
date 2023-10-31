def bid_process(bid, price):
  for _ in range(num_items): 
    price = item_list.items[_].price
    bid = 0
    while bid < price:
      answer = input(f"Would you like to bid on {item_list.items[_].name}?\n"
            f"Current price is ${item_list.items[_].price}.\nY/N ")
      if answer == "N":
        print("\nYou chose not to bid.\n")
        break
      else:
        bid = float(input("\nHow much would you like to bid?\n"))
        if (bid >= price):
          print("Congratulations, you won the bid!\nPlease pay for your item " 
          "within 24 hours.\n\n")
        else:
          print("You have lost the bid.\n\n")

#Declare Class Item
class Item:
  def __init__(self, name, price):
      self.name = name
      self.price = price
  
  def __str__(self):
      return f"Item: {self.name}, Price: ${self.price:.2f}"

#Declare Class ItemList
class ItemList:
  def __init__(self):
      self.items = []

  def add_item(self, item):
      self.items.append(item)
#For testing if the loop works  
  def display_items(self):
      for item in self.items:
          print(item)
  
#Declare Variables
item_list = ItemList()
num_items = int(input("How many items do you want to add? "))

for _ in range(num_items):
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    item_list.add_item(Item(name, price))

#For testing if the loop works 
print("\nItems in the list:")
item_list.display_items()

#initalize variables so that bid starts lower than price
bid = 0
price = 1
bid_process(bid, price)