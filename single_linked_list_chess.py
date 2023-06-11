class Node:
    def __init__(self, player_name, ranking):
        self.player_name = player_name
        self.ranking = ranking
        self.next = None


class ChessTournament:
    def __init__(self):
        self.head = None

    def register_player(self, player_name, ranking):
        new_player = Node(player_name, ranking)
        if self.head is None:
            self.head = new_player
        elif ranking < self.head.ranking:
            new_player.next = self.head
            self.head = new_player
        else:
            current = self.head
            while current.next is not None and ranking >= current.next.ranking:
                current = current.next
            new_player.next = current.next
            current.next = new_player

    def eliminate_player(self, player_name):
        if self.head is None:
            return
        if self.head.player_name == player_name:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.player_name != player_name:
            current = current.next
        if current.next is not None:
            current.next = current.next.next

    def print_players(self):
        current = self.head
        if current is None:
            print("Tidak ada peserta terdaftar.")
        else:
            print("Daftar peserta turnamen:")
            while current is not None:
                print(
                    f"Nama: {current.player_name}, Peringkat: {current.ranking}")
                current = current.next


tournament = ChessTournament()

tournament.register_player("John", 1200)
tournament.register_player("Emily", 1500)
tournament.register_player("David", 1100)
tournament.register_player("Sarah", 1400)

tournament.print_players()

tournament.eliminate_player("David")

tournament.print_players()

# Nurul Azizah-10109042
