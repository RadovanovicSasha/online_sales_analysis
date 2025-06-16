from product_manager import ProductManager
from product import Product

# Kreiranje menadžera
manager = ProductManager()

# Dodavanje proizvoda
p1 = Product("Laptop", 120000, 5)
p2 = Product("Miš", 1500, 10)
p3 = Product("Tastatura", 3000, 8)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz
manager.show_all_products()

# Ukupna vrednost
print(f"\nUkupna vrednost inventara: {manager.total_value()} RSD")