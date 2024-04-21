class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = self.create_seats()
        self.show_list = []
    
    def create_seats(self):
        seats = [['Free' for _ in range (self.cols)] for _ in range(self.rows)]
        return seats        
    

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name,  show_time)
        self.show_list.append(show_info)


        self.seats[show_id] = self.create_seats()

class Star_Cinema:
    hall_list = []

    def __init__(self, hall) -> None:
        self.entry_hall(hall)

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)