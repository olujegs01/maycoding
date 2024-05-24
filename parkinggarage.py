class ParkingGarage:
    def __init__(self):
        self.tickets = [i for i in range(1, 101)]  # 100 tickets available initially
        self.parkingSpaces = [i for i in range(1, 101)]  # 100 parking spaces available initially
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            self.currentTicket[ticket] = False  # False indicates that the ticket has not been paid
            self.parkingSpaces.pop(0)
            print(f"Ticket number {ticket} has been issued.")
        else:
            print("Sorry, the parking garage is full.")

    def payForParking(self):
        ticket = int(input("Please enter your ticket number: "))
        if ticket in self.currentTicket:
            payment = float(input("Please enter the payment amount: "))
            if payment:
                self.currentTicket[ticket] = True  # True indicates that the ticket has been paid
                print("Your ticket has been paid. You have 15 minutes to leave.")
            else:
                print("Invalid payment amount.")
        else:
            print("Invalid ticket number.")

    def leaveGarage(self):
        ticket = int(input("Please enter your ticket number: "))
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]:  # If the ticket has been paid
                print("Thank you, have a nice day!")
                del self.currentTicket[ticket]
                self.tickets.append(ticket)
                self.parkingSpaces.append(ticket)
            else:
                print("Your ticket has not been paid. Please pay for parking.")
        else:
            print("Invalid ticket number.")
