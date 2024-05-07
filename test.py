import unittest
from ticket_booking import TicketBookingSystem
from datetime import datetime

class TestTicketBookingSystem(unittest.TestCase):
    def setUp(self):
        self.system = TicketBookingSystem(filename='events.json')
        
    def tearDown(self):
        del self.system

    def test_load_events(self):
        self.assertEqual(self.system.load_events(), {})

    def test_save_events(self):
        event_name = "Test Event"
        event_date = datetime.now()
        available_tickets = 10
        self.system.events[event_name] = {'date': event_date, 'available_tickets': available_tickets}
        self.system.save_events()
        loaded_events = self.system.load_events()
        self.assertIn(event_name, loaded_events)
        self.assertEqual(loaded_events[event_name]['available_tickets'], available_tickets)

    def test_book_ticket(self):
        event_name = "Test Event"
        self.system.events[event_name] = {'date': datetime.now(), 'available_tickets': 1}
        self.assertTrue(self.system.book_ticket(event_name))

    def test_cancel_ticket(self):
        event_name = "Test Event"
        self.system.events[event_name] = {'date': datetime.now(), 'available_tickets': 0}
        self.assertTrue(self.system.cancel_ticket(event_name))

    def test_create_event(self):
        event_name = "New Event"
        event_date = datetime.now()
        available_tickets = 20
        self.assertTrue(self.system.create_event(event_name, event_date, available_tickets))

    def test_delete_event(self):
        event_name = "Test Event"
        self.system.events[event_name] = {'date': datetime.now(), 'available_tickets': 10}
        self.assertTrue(self.system.delete_event(event_name))

    def test_check_ticket_availability(self):
        event_name = "Test Event"
        self.system.events[event_name] = {'date': datetime.now(), 'available_tickets': 5}
        self.system.check_ticket_availability(event_name)

if __name__ == '__main__':
    unittest.main()
