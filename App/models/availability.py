# Availability wie: od kiedy pracownik może pracować.
# ScheduleService decyduje: którego pracownika wybrać.
#w bardziej sensownym modelu dyspozycyjność jest osobnym faktem biznesowym, który ma referencję do pracownika.
class Availability: #obiekt domenowy, pojedyncza deklaracaj dostępności pracownika
    def __init__(self, employee_id, date, start_time, end_time = None):
        self.employee_id = employee_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def can_close(self):
        if self.end_time is not None:
            return False
        if self.end_time is None:
            return True
#mówi nam CZYM JEST DYSPOZYCJA
# potrzebujemy tego obiektu aby móc go przypisac do kazdego dnia jako osobna dyspozycja danego pracownika na dany dzien
# dzieki temu dyspozycja przestaje byc surowymi danymi a staje sie bardziej funkcjonalnym obiektem
# który może powiedzieć np. praconik może zostać do zamknięcia. 