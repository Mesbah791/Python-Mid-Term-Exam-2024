class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = self.create_seats()
        self.show_list = []
    
    def create_seats(self):
        seats = {}
        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                seats[(row,col)] = {'occupied': False, 'reserved':False}
        return seats        
    
class Star_Cinema:
    hall_list = []

    def __init__(self, hall) -> None:
        self.entry_hall(hall)

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)