# 🧾 Online Sales Analysis – GitHub Projekat

## 📌 Opis
Ovaj projekat simulira jednostavan sistem za upravljanje prodajom i korpom kupca. Implementiran je u Pythonu korišćenjem OOP principa, uz upotrebu Gita i GitHub-a za verzionisanje.

## 📦 Funkcionalnosti

### ✅ Klasa `Product`
- Atributi: `name`, `price`, `quantity`
- Metodi:
  - `display_info()`: prikazuje informacije o proizvodu
  - `update_quantity()`: ažurira količinu

### ✅ Klasa `ProductManager`
- Atribut: lista svih proizvoda
- Metodi:
  - `add_product()`
  - `show_all_products()`
  - `total_value()`
  - `remove_product_by_name()`

### ✅ Klasa `Cart`
- Atribut: `cart_items` – lista proizvoda koje kupac dodaje
- Metodi:
  - `add_to_cart(proizvod, količina)`
  - `total_cart_value()`
  - `show_cart()`

## 🔀 Verzije i grane

- `main`: osnovna grana sa stabilnim kodom
- `add-cart-functionality`: posebna grana za razvoj funkcije korpe
- Merge je izvršen u fazama 5 i 7, uključujući rešavanje konflikta u `main.py`.

## 🔐 Ignorisani fajlovi

Sledeći fajlovi i folderi su isključeni iz verzionisanja preko `.gitignore`:

Snimci ekrana se nalaze u folderu `Screenshots/`, ali nisu deo verzionisanog repozitorijuma.

## 👤 Autor

Aleksandar Radovanović  
Projekat za GitHub vežbu u okviru ITAcademy kursa