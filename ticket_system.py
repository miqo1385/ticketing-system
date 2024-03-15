import queue
import threading
import time
import random


class Ticket:
    def __init__(self, number):
        self.number = number
        self.timestamp = time.time()


class TicketingSystem:
    def __init__(self):
        self.ticket_queue = queue.Queue()

    def generate_ticket(self):
        ticket_number = self.ticket_queue.qsize() + 1
        ticket = Ticket(ticket_number)
        self.ticket_queue.put(ticket)
        print(f"Ticket {ticket.number} generated at {time.strftime('%H:%M:%S', time.localtime(ticket.timestamp))}")

    def process_tickets(self):
        while True:
            if not self.ticket_queue.empty():
                ticket = self.ticket_queue.get()
                print(f"Ticket {ticket.number} is being served...")
                time.sleep(random.uniform(2, 5))  # Simulate processing time
                print(f"Ticket {ticket.number} served.")
            else:
                print("No tickets in the queue.")
                time.sleep(1)

    def start_simulation(self):
        generator_thread = threading.Thread(target=self.generate_tickets)
        processor_thread = threading.Thread(target=self.process_tickets)

        generator_thread.start()
        processor_thread.start()

        generator_thread.join()
        processor_thread.join()

    def generate_tickets(self):
        while True:
            self.generate_ticket()
            time.sleep(random.uniform(1, 4))  # Simulate random intervals between ticket generation


if __name__ == "__main__":
    ticketing_system = TicketingSystem()
    ticketing_system.start_simulation()
