import json
from datetime import datetime, timedelta

class TicketBookingSystem:
    def __init__(self, filename='events.json'):
        self.filename = filename
        self.events = self.load_events()

    def load_events(self):
        try:
            with open(self.filename, 'r') as file:
                events = json.load(file)
                return {key: {'date': datetime.strptime(events[key]['date'], "%Y-%m-%d %H:%M"),
                              'available_tickets': events[key]['available_tickets']} for key in events}
        except FileNotFoundError:
            return {}

    def save_events(self):
        with open(self.filename, 'w') as file:
            events = {key: {'date': self.events[key]['date'].strftime("%Y-%m-%d %H:%M"),
                            'available_tickets': self.events[key]['available_tickets']} for key in self.events}
            json.dump(events, file, indent=4)

    def list_events(self):
        if not self.events:
            print("No events found.")
            return
        for event, details in self.events.items():
            print(f"Event: {event}, Date: {details['date'].strftime('%Y-%m-%d %H:%M')}, Available Tickets: {details['available_tickets']}")

    def search_events(self, name):
        found = False
        for event, details in self.events.items():
            if name.lower() in event.lower():
                print(f"Event: {event}, Date: {details['date'].strftime('%Y-%m-%d %H:%M')}, Available Tickets: {details['available_tickets']}")
                found = True
        if not found:
            print("No matching events found.")

    def book_ticket(self, event_name):
        if event_name in self.events and self.events[event_name]['available_tickets'] > 0:
            self.events[event_name]['available_tickets'] -= 1
            self.save_events()
            print(f"Ticket booked for {event_name}.")
            return True
        else:
            print("Ticket not available or event does not exist.")
            return False

    def cancel_ticket(self, event_name):
        if event_name in self.events:
            self.events[event_name]['available_tickets'] += 1
            self.save_events()
            print(f"Ticket booking cancelled for {event_name}.")
            return True
        else:
            print("Event does not exist.")
            return False
    
    def create_event(self, event_name, event_date, available_tickets):
        if event_name not in self.events:
            self.events[event_name] = {'date': event_date, 'available_tickets': available_tickets}
            self.save_events()
            print(f"Event '{event_name}' created successfully.")
            return True
        else:
            print("Event already exists.")
            return False
    
    def delete_event(self, event_name):
        if event_name in self.events:
            del self.events[event_name]
            self.save_events()
            print(f"Event '{event_name}' deleted successfully.")
            return True
        else:
            print("Event does not exist.")
            return False

    def check_ticket_availability(self, event_name):
        if event_name in self.events:
            print(f"Available tickets for {event_name}: {self.events[event_name]['available_tickets']}")
        else:
            print("Event does not exist.")

def main():
    system = TicketBookingSystem()
    while True:
        print("\nTicket Booking System Options:")
        print("1. List All Events")
        print("2. Search for an Event")
        print("3. Book Ticket")
        print("4. Cancel Ticket")
        print("5. Create Event")
        print("6. Delete Event")
        print("7. Check Ticket Availability")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            system.list_events()
        elif choice == '2':
            event_name = input("Enter the name or part of the event name to search: ")
            system.search_events(event_name)
        elif choice == '3':
            event_name = input("Enter the event name to book a ticket for: ")
            system.book_ticket(event_name)
        elif choice == '4':
            event_name = input("Enter the event name to cancel the ticket for: ")
            system.cancel_ticket(event_name)
        elif choice == '5':
            event_name = input("Enter the name of the event: ")
            event_date = input("Enter the date and time of the event (YYYY-MM-DD HH:MM): ")
            available_tickets = int(input("Enter the number of available tickets: "))
            system.create_event(event_name, datetime.strptime(event_date, "%Y-%m-%d %H:%M"), available_tickets)
        elif choice == '6':
            event_name = input("Enter the name of the event to delete: ")
            system.delete_event(event_name)
        elif choice == '7':
            event_name = input("Enter the name of the event to check ticket availability: ")
            system.check_ticket_availability(event_name)
        elif choice == '8':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
