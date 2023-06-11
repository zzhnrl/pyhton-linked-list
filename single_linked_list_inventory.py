class Node:
    def __init__(self, product_name, product_code, stock):
        self.product_name = product_name
        self.product_code = product_code
        self.stock = stock
        self.next = None


class InventoryManagement:
    def __init__(self):
        self.head = None

    def add_product(self, product_name, product_code, stock):
        new_product = Node(product_name, product_code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_product

    def remove_product(self, product_code):
        if self.head is None:
            return
        if self.head.product_code == product_code:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.product_code != product_code:
            current = current.next
        if current.next is not None:
            current.next = current.next.next

    def print_inventory(self):
        current = self.head
        if current is None:
            print("Inventaris kosong.")
        else:
            print("Daftar produk di inventaris:")
            while current is not None:
                print(
                    f"Nama Produk: {current.product_name}, Kode Produk: {current.product_code}, Jumlah Stok: {current.stock}")
                current = current.next


inventory = InventoryManagement()

inventory.add_product("Keyboard", "KB001", 10)
inventory.add_product("Mouse", "MS001", 15)
inventory.add_product("Monitor", "MN001", 5)

inventory.print_inventory()

inventory.remove_product("MS001")

inventory.print_inventory()

# Nurul Azizah_10109042
