import unittest
from airlines import *


class TestFlight(unittest.TestCase):

    def setUp(self):
        self.flight = Flight(start_time=Date(29, 11, 2016, hour='12:20'), 
                             end_time=Date(29, 11, 2016, hour='15:30'), 
                             passengers=100, 
                             max_passengers=120, 
                             from_dest="Sofia", 
                             to_dest="London", 
                             terminal=Terminal(2, 30), 
                             declined=False)

    def test_smth(self):
        pass


class TestDate(unittest.TestCase):

    def setUp(self):
        self.date = Date(29, 11, 2016, hour='15:30')

    def test_repr(self):
        self.assertEqual(repr(self.date), '29, 11, 2016, 15:30')

    def test_return_date(self):
        self.assertEqual(self.date.return_date(), '29, 11, 2016')


class TestTerminal(unittest.TestCase):

    def setUp(self):
        self.terminal = Terminal(number=1, max_flights=20)

    def test_terminal_availabilty(self):
        self.terminal.occupation = 10
        self.assertTrue(self.terminal.terminal_availabilty(), self.terminal.occupation)
        self.terminal.occupation = 21 
        self.assertFalse(self.terminal.terminal_availabilty(), self.terminal.occupation)
        

class TestPassengers(unittest.TestCase):

    def setUp(self):
        self.passenger = Passenger(first_name="Rositsa",
                                   last_name="Zlateva",
                                   flight=Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                                 end_time=Date(29, 11, 2016, hour='15:30'), 
                                                 passengers=100, 
                                                 max_passengers=120, 
                                                 from_dest="Sofia", 
                                                 to_dest="London", 
                                                 terminal=Terminal(2, 30), 
                                                 declined=False),
                                   age=22)


    def test_smth(self):
        pass


class TestReservation(unittest.TestCase):
    
    def setUp(self):
        self.reservation = Reservation(flight=Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                                 end_time=Date(29, 11, 2016, hour='15:30'), 
                                                 passengers=100, 
                                                 max_passengers=120, 
                                                 from_dest="Sofia", 
                                                 to_dest="London", 
                                                 terminal=Terminal(2, 30), 
                                                 declined=False), 
                                       passenger=Passenger(first_name="Rositsa", 
                                                           last_name="Zlateva", 
                                                           flight=Flight(start_time=Date(29, 11, 2016, hour='12:20'),
                                                                         end_time=Date(29, 11, 2016, hour='15:30'), 
                                                                         passengers=100, 
                                                                         max_passengers=120, 
                                                                         from_dest="Sofia", 
                                                                         to_dest="London", 
                                                                         terminal=Terminal(2, 30), 
                                                                         declined=False), age=22), 
                                       accepted=True)

    def test_smth(self):
        pass


class TestAirlines(unittest.TestCase):

    def setUp(self):
        self.flight1 = Flight(start_time=Date(30, 11, 2016, hour='12:20'), 
                             end_time=Date(30, 11, 2016, hour='15:30'), 
                             passengers=100, max_passengers=120, 
                             from_dest="Sofia", 
                             to_dest="London", 
                             terminal=Terminal(2, 30), 
                             declined=False)
        self.flight2 = Flight(start_time=Date(2, 11, 2016, hour='11:20'), 
                             end_time=Date(2, 11, 2016, hour='14:30'), 
                             passengers=90, max_passengers=111, 
                             from_dest="Somewhere", 
                             to_dest="Nowhere", 
                             terminal=Terminal(1, 15), 
                             declined=False)
        self.flight3 = Flight(start_time=Date(2, 11, 2016, hour='9:50'), 
                             end_time=Date(2, 11, 2016, hour='12:30'), 
                             passengers=90, max_passengers=111, 
                             from_dest="Closet", 
                             to_dest="Narnia", 
                             terminal=Terminal(2, 15), 
                             declined=False)
        self.flight4 = Flight(start_time=Date(2, 12, 2016, hour='12:50'), 
                             end_time=Date(2, 12, 2016, hour='15:30'), 
                             passengers=90, max_passengers=111, 
                             from_dest="Closet", 
                             to_dest="Narnia", 
                             terminal=Terminal(3, 15), 
                             declined=False)
        self.airlines = Airlines([self.flight1, 
                                  self.flight2, 
                                  self.flight3, 
                                  self.flight4])

    def test_get_flights_for(self):
        self.assertEqual(self.airlines.get_flights_for('2, 11, 2016'), 
                         [self.flight2, self.flight3])

    def test_get_flight_before(self):
        self.assertEqual(self.airlines.get_flight_before('2, 11, 2016', '11:20'), 
                         [self.flight2, self.flight3])

    def test_get_flight_from(self):
        self.assertEqual(self.airlines.get_flight_from('Somewhere'),
                         [self.flight2])
        self.assertEqual(self.airlines.get_flight_from('Somewhere', 
                                                       '2, 11, 2016', 
                                                       '14:30'), 
                                                       [self.flight2])

    def test_get_flight_to(self):
        self.assertEqual(self.airlines.get_flight_to('Narnia'),
                         [self.flight3, self.flight4])
        self.assertEqual(self.airlines.get_flight_to('Narnia', 
                                                       '2, 11, 2016', 
                                                       '9:50'), 
                                                       [self.flight3])

    def test_get_terminal_flights(self):
        pass










if __name__ == '__main__':
    unittest.main()
