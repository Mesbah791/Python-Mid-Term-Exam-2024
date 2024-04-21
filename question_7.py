class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def create_seats(self):
        seats = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]
        return seats

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self.show_list.append(show_info)


        self.seats[show_id] = self.create_seats()

    def book_seats(self, show_id, seats_to_book):
        if show_id in self.seats:
            for seat in seats_to_book:
                row, col = seat
                if 1 <= row <= self.rows and 1 <= col <= self.cols:
                    if self.seats[show_id][row - 1][col - 1] == 'Free':
                        self.seats[show_id][row - 1][col - 1] = 'Booked'
                        print(f"Seat {row}{chr(64 + col)} booked successfully.")
                    

    

    def view_show_list(self):
        print("The shows which are running now:")
        for show_info in self.show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")



    def view_available_seats(self, show_id):
        if show_id in self.seats:   
            print(f"available seats of show id =  {show_id}:")
            
            for row in range (self.rows):
                for col in range(self.cols):
                    if self.seats[show_id][row][col] == 'Free':
                        print (f"Row {row + 1}, Seat {chr(65 + col)}")


class CounterReplica:
    def __init__(self, hall):
        self.hall = hall
    
    def view_all_shows(self):
        self.hall.view_show_list()
    
    def view_available_seats(self, show_id):
        self.hall.view_available_seats(show_id) 
    
    def book_tickets(self, show_id, seats_to_book):
        self.hall.book_seats(show_id, seats_to_book)


hall1 = Hall(10, 10, 1)

hall1.entry_show("S1", "Rajkumar", "6:00 PM")
hall1.entry_show("S2", "Hawa", "9:00 PM")


counter = CounterReplica(hall1)

print("\nAll shows running:")
counter.view_all_shows()

print("\nViewing available seats :")
counter.view_available_seats("S1")

print("\nBooking tickets :")
counter.book_tickets("S1", [(1, 1), (2, 2), (3, 3)])

        
