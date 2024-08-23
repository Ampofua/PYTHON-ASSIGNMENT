def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
  else:
    final_price = price

  return final_price
    

def main():
  original_price = float(input("What's the price of the item please? "))
  discount_percent = float(input("Enter the discount percentage the item please "))


  final_price = calculate_discount(original_price, discount_percent)

  print(f"The final price after applying discount is : {final_price}")


if __name__ == "__main__":
  main()