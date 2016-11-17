class Flight:

    def __init__(self, 
                 start_time, 
                 end_time, 
                 passengers, 
                 max_passengers, 
                 from_dest,
                 to_dest, 
                 terminal,
                 declined):
        self.start_time = start_time
        self.end_time = end_time
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined

    def __repr__(self):
        return 'Flight from {0} to {1}'.format(self.from_dest, self.to_dest)

class Date:

    def __init__(self, day, month, year, hour):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
    
    def return_date(self):
        return '{0}, {1}, {2}'.format(self.day, 
                                      self.month, 
                                      self.year)

    def __repr__(self):
        return '{0}, {1}, {2}, {3}'.format(self.day, 
                                      self.month, 
                                      self.year,
                                      self.hour)

class Terminal:

    def __init__(self, number, max_flights):
        self.number = number
        self.max_flights = max_flights
        self.occupation = 0

    def terminal_availabilty(self):
        if self.occupation <= self.max_flights:
            return True
        return False

class Passenger:

    def __init__(self, first_name, last_name, flight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.flight = flight
        self.age = age

class Reservation:

    def __init__(self, flight, passenger, accepted):
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted


class Airlines:

    def __init__(self, flights):
        self.all_flights = [i for i in flights]

    def get_flights_for(self, date):
        result = []
        for flight in self.all_flights:
            if flight.start_time.return_date() == date:
                result.append(flight)
        return result

    def get_flight_before(self, date, hour): # '2, 11, 2016', '11:20'
        result = []
        hour = [int(i) for i in hour.split(':')] # hour, minute [11, 20]
        for flight in self.get_flights_for(date):
            if hour >= [int(i) for i in flight.start_time.hour.split(':')]:
                result.append(flight)
        return result

    def get_flight_from(self, destination, *argv): # argv = date, hour
        result = []
        for flight in self.all_flights:
            if flight.from_dest == destination:
                if argv:
                    if flight.end_time.return_date() == argv[0] and flight.end_time.hour == argv[1]:
                        result.append(flight)
                else:
                    result.append(flight)
        return result
        #return [flight for flight in self.all_flights if flight.from_dest == destination]

    def get_flight_to(self, destination, *argv): # argv = date, hour
        result = []
        for flight in self.all_flights:
            if flight.to_dest == destination:
                if argv:
                    if flight.start_time.return_date() == argv[0] and flight.start_time.hour == argv[1]:
                        result.append(flight)
                else:
                    result.append(flight)
        return result






#f = Flight(start_time=Date(29, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'), passengers=100, max_passengers=120, from_dest="Sofia", to_dest="London", terminal=Terminal(2, 30), declined=False)



