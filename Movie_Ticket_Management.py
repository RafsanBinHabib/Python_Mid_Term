class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().entry_hall(self)
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__show_list = []
        self.__seats = {}


    def entry_show(self, show_id, movie_name, time):
        self.__show_list.append((show_id, movie_name, time))
        seat_allocation = [["0 " for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seat_allocation


    def view_show_list(self):
        print(f"Shows running in Hall {self.__hall_no}:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")


    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print(f"Show ID '{show_id}' not found!")
            return

        print(f"\nAvailable seats for Show ID '{show_id}':")
        for row_idx, row in enumerate(self.__seats[show_id]):
            seat_row = ''.join(row)
            print(f"Row {row_idx}: {seat_row}")


    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print(f"Show ID '{show_id}' not found!")
            return

        for seat in seat_list:
            row, col = seat
            if not (0 <= row < self.__rows and 0 <= col < self.__cols):
                print(f"Invalid seat position: ({row}, {col})")
                continue

            if self.__seats[show_id][row][col] == "1":
                print(f"Seat ({row}, {col}) is already booked!")
            else:
                self.__seats[show_id][row][col] = "1 "
                print(f"Seat ({row}, {col}) booked successfully!")


class Replica:
    @staticmethod
    def view_all_shows():
        if not Star_Cinema._hall_list:
            print("No halls or shows available!")
            return

        print("\n--- All Shows Running Today ---")
        for hall in Star_Cinema._hall_list:
            hall.view_show_list()


    @staticmethod
    def view_available_seats_for_show():
        show_id = input("\nEnter the Show ID to view available seats: ").strip()
        found = False
        
        for hall in Star_Cinema._hall_list:
            if show_id in hall._Hall__seats:
                hall.view_available_seats(show_id)
                found = True
        if not found:
            print(f"Show ID '{show_id}' not found in any hall.")


    @staticmethod
    def book_ticket():
        show_id = input("\nEnter the Show ID to book tickets: ").strip()
        found = False
        
        for hall in Star_Cinema._hall_list:
            if show_id in hall._Hall__seats:
                found = True
                
                num_tickets = input("Enter the number of tickets: ").strip()
                if not num_tickets.isdigit() or int(num_tickets) <= 0:
                    print("Invalid number of tickets!")
                    return

                num_tickets = int(num_tickets)
                seat_list = []
                for i in range(num_tickets):
                    seat_pos = input(f"Enter seat position for ticket {i + 1} (row, col): ").strip()
                    if ',' not in seat_pos:
                        print(f"Invalid format for seat {i + 1}. Use row,col format.")
                        continue
                    
                    row_col = seat_pos.split(',')
                    
                    if len(row_col) != 2 or not row_col[0].isdigit() or not row_col[1].isdigit():
                        print(f"Invalid seat position for ticket {i + 1}.")
                        continue

                    row, col = map(int, row_col)
                    seat_list.append((row, col))
                hall.book_seats(show_id, seat_list)
                
        if not found:
            print(f"Show ID '{show_id}' not found!")

    @staticmethod
    def menu():
        while True:
            print("\n--- Star Cinema Booking System ---")
            print("1. View All Shows Today")
            print("2. View Available Seats")
            print("3. Book Ticket")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()
            
            if not choice.isdigit() or int(choice) not in [1, 2, 3, 4]:
                print("Invalid choice! Please enter a valid option.")
                continue

            choice = int(choice)
            if choice == 1:
                Replica.view_all_shows()
            elif choice == 2:
                Replica.view_available_seats_for_show()
            elif choice == 3:
                Replica.book_ticket()
            elif choice == 4:
                print("Exiting the system. Thank you!")
                break



hall1 = Hall(5, 5, 101)
hall1.entry_show("S1", "Avengers: Endgame", "5:00 PM")
hall1.entry_show("S2", "Inception", "8:00 PM")

hall2 = Hall(4, 4, 102)
hall2.entry_show("S3", "Titanic", "6:00 PM")
hall2.entry_show("S4", "The Dark Knight", "9:00 PM")

Replica.menu()