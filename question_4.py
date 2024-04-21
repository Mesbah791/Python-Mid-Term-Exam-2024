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

        # Allocate seats using a 2D list initially set to 'Free'
        self.seats[show_id] = self.create_seats()

    def book_seats(self, show_id, seat_booked):
        if show_id in self.seats:
            for seat in seat_booked:
                row, col = seat
                if 1 <= row <= self.rows and 1 <= col <= self.cols:
                    if self.seats[show_id][row - 1][col - 1] == 'Free':
                        self.seats[show_id][row - 1][col - 1] = 'Booked'
     

