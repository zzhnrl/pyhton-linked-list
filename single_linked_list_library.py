class Node:
    def __init__(self, visitor_name, book_title):
        self.visitor_name = visitor_name
        self.book_title = book_title
        self.next = None


class LibraryRecords:
    def __init__(self):
        self.head = None

    def add_record(self, visitor_name, book_title):
        new_record = Node(visitor_name, book_title)
        if self.head is None:
            self.head = new_record
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_record

    def print_records(self):
        current = self.head
        if current is None:
            print("Tidak ada catatan perpustakaan.")
        else:
            print("Daftar catatan perpustakaan:")
            while current is not None:
                print(
                    f"Pengunjung: {current.visitor_name}, Buku: {current.book_title}")
                current = current.next


# Contoh penggunaan program
library_records = LibraryRecords()

library_records.add_record("John", "Harry Potter")
library_records.add_record("Emily", "To Kill a Mockingbird")
library_records.add_record("David", "The Great Gatsby")
library_records.add_record("Emily", "Pride and Prejudice")

library_records.print_records()
# Output:
# Daftar catatan perpustakaan:
# Pengunjung: John, Buku: Harry Potter
# Pengunjung: Emily, Buku: To Kill a Mockingbird
# Pengunjung: David, Buku: The Great Gatsby
# Pengunjung: Emily, Buku: Pride and Prejudice

# Nurul Azizah-10109042
