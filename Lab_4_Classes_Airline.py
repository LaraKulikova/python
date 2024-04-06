'''Kласс Airline: Пункт назначения, Номер рейса,
Тип самолета, Время вылета, Дни недели.
Функции- члены реализуют запись и считывание полей (проверка корректности).
Создать список объектов. Вывести:
a)	список рейсов для заданного пункта назначения;
б) список рейсов для заданного дня недели;.
'''


class Airline:
    def __init__(self, destination, flightNum, airplaneType, departureTime, dayOfWeek):
        self.destination = destination
        self.flightNum = flightNum
        self.airplaneType = airplaneType
        self.departureTime = departureTime
        self.dayOfWeek = dayOfWeek

    @classmethod
    def createListPlane(cls, destination_list, flightNum_list, airplaneType_list,
                        departureTime_list, dayOfWeek_list):

        planes = []
        for i in range(len(destination_list)):
            plane = Airline(destination_list[i], flightNum_list[i], airplaneType_list[i],
                            departureTime_list[i], dayOfWeek_list[i])
            planes.append(plane)
        return planes

    @staticmethod
    def printPlanes(planes):
        for i, plane in enumerate(planes):
            print(f"{i + 1}. Город: {plane.destination}, Номер: {plane.flightNum}, "
                  f"Модель: {plane.airplaneType}, "
                  f"Время вылета: {plane.departureTime}, День: {plane.dayOfWeek}")


    @staticmethod
    def listFlightsByDestination(planes, destination):
        matching_flights = [plane for plane in planes if plane.destination == destination]
        return matching_flights


    @staticmethod
    def listFlightsByDay(planes, dayOfWeek):
        matching_flights = [plane for plane in planes if plane.dayOfWeek == dayOfWeek]
        return matching_flights



planes = Airline.createListPlane(
    ['Москва', 'Санкт-Петербург', 'Москва'],
    ['2B2', '3A3', '4D4'],
    ['Боинг', 'ТУ-34', 'Ковер-самолет'],
    ['12.00', '14.13', '00.12'],
    ['Понедельник', 'Понедельник', 'Среда']
)
print('Вывожу весь список рейсов:')
Airline.printPlanes(planes)

print('Вывожу список рейсов в Москву:')
flight_to_moscow = Airline.listFlightsByDestination(planes, 'Москва')
Airline.printPlanes(flight_to_moscow)

print('Вывожу список рейсов по Понедельникам:')
flights_on_monday = Airline.listFlightsByDay(planes, 'Понедельник')
Airline.printPlanes(flights_on_monday)







