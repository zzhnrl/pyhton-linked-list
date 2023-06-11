class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Node(description, priority)
        if self.head is None:
            self.head = new_task
        elif priority < self.head.priority:
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next is not None and priority >= current.next.priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task

    def remove_task(self, description):
        if self.head is None:
            return
        if self.head.description == description:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.description != description:
            current = current.next
        if current.next is not None:
            current.next = current.next.next

    def print_tasks(self):
        current = self.head
        if current is None:
            print("Daftar tugas kosong.")
        else:
            print("Daftar tugas:")
            while current is not None:
                print(
                    f"Deskripsi: {current.description}, Prioritas: {current.priority}")
                current = current.next


task_list = TaskList()

task_list.add_task("Mengerjakan tugas matematika", 2)
task_list.add_task("Menulis laporan proyek", 1)
task_list.add_task("Belajar bahasa Python", 3)

task_list.print_tasks()

task_list.remove_task("Mengerjakan tugas matematika")

task_list.print_tasks()

# Nurul Azizah-10109042
