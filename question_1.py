class Hall:
    def __init__(self, hall_name) -> None:
        self.hall_name = hall_name

class Star_Cinema:
    hall_list = []
    

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

moinamoti_hall = Hall("moinamoti hall")
shompura_hall = Hall("shompura hall")

Star_Cinema.entry_hall(moinamoti_hall)
Star_Cinema.entry_hall(shompura_hall)