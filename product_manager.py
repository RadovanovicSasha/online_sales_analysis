from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        print("\n--- Lista svih proizvoda ---")
        for product in self.products:
            product.display_info()

    def total_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        return total
    
    #Dodavanje metoda za uklanjanje proizvoda prema imenu.

    def remove_product_by_name(self, product_name):
    original_count = len(self.products)
    self.products = [p for p in self.products if p.name.lower() != product_name.lower()]
    if len(self.products) < original_count:
        print(f"Proizvod '{product_name}' je uklonjen.")
    else:
        print(f"Proizvod '{product_name}' nije pronađen.")