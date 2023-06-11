class Node:
    def __init__(self, item_name, importance_level):
        self.item_name = item_name
        self.importance_level = importance_level
        self.next = None


class PlayerInventory:
    def __init__(self):
        self.head = None

    def add_item(self, item_name, importance_level):
        new_item = Node(item_name, importance_level)
        if self.head is None:
            self.head = new_item
        elif importance_level < self.head.importance_level:
            new_item.next = self.head
            self.head = new_item
        else:
            current = self.head
            while current.next is not None and importance_level >= current.next.importance_level:
                current = current.next
            new_item.next = current.next
            current.next = new_item

    def remove_item(self, item_name):
        if self.head is None:
            return
        if self.head.item_name == item_name:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.item_name != item_name:
            current = current.next
        if current.next is not None:
            current.next = current.next.next

    def print_inventory(self):
        current = self.head
        if current is None:
            print("Tas pemain kosong.")
        else:
            print("Daftar item dalam tas:")
            while current is not None:
                print(
                    f"Nama: {current.item_name}, Tingkat Kepentingan: {current.importance_level}")
                current = current.next


inventory = PlayerInventory()

inventory.add_item("Pedang Legendaris", 5)
inventory.add_item("Potion Kesembuhan", 3)
inventory.add_item("Panah Sihir", 4)
inventory.add_item("Buku Sihir", 2)

inventory.print_inventory()

inventory.remove_item("Potion Kesembuhan")

inventory.print_inventory()

# Nurul Azizah-10109042
