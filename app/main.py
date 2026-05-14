from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from typing import List, Dict


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner_name: str,
                 movie_name: str) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_staff = Cleaner(name=cleaner_name)
    cinema_bar = CinemaBar()
    guests = []
    for customer_data in customers:
        customer_inst = Customer(
            name=customer_data["name"],
            food=customer_data["food"])
        cinema_bar.sell_product(
            customer_inst,
            product=customer_data["food"]
        )
        guests.append(customer_inst)
    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=guests,
        cleaning_staff=cleaner_staff)
