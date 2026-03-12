class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __str__(self):
    return f"Produto: {self.name}, Preço: R${self.price:.2f}"

  def discount(self, percent_discount):
    valorDiscount = (self.price/100) * percent_discount
    finalPrice = self.price - valorDiscount
    return int(finalPrice)

xbox = Product("Xbox Series X", 4500.00)
iphone = Product("iPhone 14 Pro Max", 7500.00)

print(xbox)
print(iphone)
print(xbox.discount(10))
print(iphone.discount(15))
