from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Optional


class ParkingSpot(ABC):
    def __init__(self, id: int, is_free: bool = True):
        self.id = id
        self.is_free = is_free

    def get_is_free(self) -> bool:
        return self.is_free


class Payment(ABC):
    def __init__(
        self, amount: float, status: str = "Pending", timestamp: datetime = None
    ):
        self.amount = amount
        self.status = status
        self.timestamp = timestamp or datetime.now()

    @abstractmethod
    def initiate_transaction(self) -> None:
        pass

    @abstractmethod
    def validate_ticket(self) -> bool:
        pass


class Account(ABC):
    def __init__(self, username: str, password: str, status: str = "Active"):
        self.username = username
        self.password = password
        self.status = status

    @abstractmethod
    def reset_password(self) -> bool:
        pass


class Large(ParkingSpot):
    def __init__(self, id: int, is_free: bool = True):
        super().__init__(id, is_free)


class Motorcycle(ParkingSpot):
    def __init__(self, id: int, is_free: bool = True):
        super().__init__(id, is_free)


class Compact(ParkingSpot):
    def __init__(self, id: int, is_free: bool = True):
        super().__init__(id, is_free)


class Handicapped(ParkingSpot):
    def __init__(self, id: int, is_free: bool = True):
        super().__init__(id, is_free)


class Car(ParkingSpot):
    def __init__(self, id: int, is_free: bool = True):
        super().__init__(id, is_free)


class Truck(ParkingSpot):
    def __init__(self, id: int, is_free: bool = True):
        super().__init__(id, is_free)


class Van(ParkingSpot):
    def __init__(self, id: int, is_free: bool = True):
        super().__init__(id, is_free)


class CreditCard(Payment):
    def __init__(self, amount: float, card_number: str, status: str = "Pending"):
        super().__init__(amount, status)
        self.card_number = card_number

    def initiate_transaction(self) -> None:
        self.status = "Completed"
        self.timestamp = datetime.now()
        print(f"Transaction of ${self.amount} with card {self.card_number} completed.")

    def validate_ticket(self) -> bool:
        return self.status == "Completed"


class Cash(Payment):
    def __init__(self, amount: float, status: str = "Pending"):
        super().__init__(amount, status)

    def initiate_transaction(self) -> None:
        self.status = "Completed"
        self.timestamp = datetime.now()
        print(f"Cash payment of ${self.amount} completed.")

    def validate_ticket(self) -> bool:
        return self.status == "Completed"


class ParkingTicket:
    def __init__(self, ticket_id: int, entry_time: datetime):
        self.ticket_id = ticket_id
        self.entry_time = entry_time
        self.exit_time = None
        self.amount = 0

    def calculate_amount(self, rate: float, hours: float) -> None:
        self.amount = rate * hours

    def set_exit_time(self, exit_time: datetime) -> None:
        self.exit_time = exit_time


class Entrance:
    def __init__(self, id: int):
        self.id = id

    def get_ticket(self) -> ParkingTicket:
        return ParkingTicket(self.id, datetime.now())


class ParkingLot:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.is_full = False
        self.spots: List[ParkingSpot] = []

    def get_parking_ticket(self) -> ParkingTicket:
        if not self.is_full:
            return Entrance(1).get_ticket()
        return None

    def is_full(self) -> bool:
        return self.is_full


class ParkingRate:
    def __init__(self, hours: float, rate: float):
        self.hours = hours
        self.rate = rate

    def calculate(self) -> float:
        return self.hours * self.rate


class DisplayBoard:
    def __init__(self, id: int):
        self.id = id
        self.parking_spot: Dict[int, List[ParkingSpot]] = {}

    def add_parking_spot(self, spot_type: str, spot: ParkingSpot) -> None:
        if spot_type not in self.parking_spot:
            self.parking_spot[spot_type] = []
        self.parking_spot[spot_type].append(spot)

    def show_free_slot(self) -> None:
        for spot_type, spots in self.parking_spot.items():
            free_spots = [spot.id for spot in spots if spot.get_is_free()]
            print(f"Free {spot_type} spots: {free_spots}")


class Admin:
    def __init__(self):
        self.parking_agent = ParkingAgent()

    def add_parking_spot(self, parking_spot: ParkingSpot) -> bool:

        return True

    def add_entrance(self, entrance: Entrance) -> bool:

        return True

    def add_exit(self, exit: Entrance) -> bool:

        return True

    def process_ticket(self, ticket: ParkingTicket) -> bool:

        return True


class ParkingAgent:
    def __init__(self):
        self.preferred_spots = []

    def process_ticket(self, ticket: ParkingTicket) -> bool:

        return True


class AccountImpl(Account):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)

    def reset_password(self) -> bool:
        self.password = "newpassword123"
        return True


if __name__ == "__main__":
    parking_lot = ParkingLot(1, "City Parking")
    ticket = parking_lot.get_parking_ticket()
    payment = CreditCard(5.0, "1234-5678-9012-3456")
    payment.initiate_transaction()
    display = DisplayBoard(1)
    spot = Compact(1)
    display.add_parking_spot("Compact", spot)
    display.show_free_slot()
