import queue
import time
import random


class Ticket:
    def __init__(self, ticket_number, timestamp):
        self.ticket_number = ticket_number
        self.timestamp = timestamp


def main():
    ticket_queue = queue.Queue()
    ticket_number = 1

    while True:
        current_time = time.time()
        new_ticket = Ticket(ticket_number, current_time)
        ticket_number += 1
        ticket_queue.put(new_ticket)
        print(f"Ticket #{new_ticket.ticket_number} issued at {new_ticket.timestamp}")

        time.sleep(random.random() * 5)

        if not ticket_queue.empty():
            current_ticket = ticket_queue.get()
            print(f"Ticket #{current_ticket.ticket_number} is being served.")

        time.sleep(random.random() * 3)


if __name__ == "__main__":
    main()
