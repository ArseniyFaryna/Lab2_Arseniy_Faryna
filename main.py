class Person:
    def __init__(self, first_name, last_name, phone_number, email):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def email(self):
        return self._email

    def show_information(self):
        print(f"Name: {self._first_name} {self._last_name}, "
                f"Phone: {self._phone_number}, Email: {self._email}")


class RentalManager:
    def __init__(self):
        self._rentals = []

    def add_rental(self, client, property_address, start_date, end_date, monthly_price):
        rental = {
            "client": client,
            "property_address": property_address,
            "start_date": start_date,
            "end_date": end_date,
            "monthly_price": monthly_price,
            "status": "pending"
        }
        self._rentals.append(rental)
        print(f"Rental added: {property_address} from {start_date} to {end_date} for ${monthly_price} per month")

    def get_rentals(self):
        return list(self._rentals)


class Client(Person):
    def __init__(self, first_name, last_name, phone_number, email, client_id):
        super().__init__(first_name, last_name, phone_number, email)
        self._client_id = client_id

    def show_information(self):
        print(f"Client ID: {self._client_id}, Name: {self.first_name} {self.last_name}, "
              f"Phone: {self.phone_number}, Email: {self.email}")

    def rent_property(self, rental_manager, property_address, start_date, end_date, monthly_price):
        rental_manager.add_rental(self, property_address, start_date, end_date, monthly_price)


class Agent(Person):
    def __init__(self, first_name, last_name, phone_number, email, agent_id):
        super().__init__(first_name, last_name, phone_number, email)
        self._agent_id = agent_id

    def show_information(self):
        print(f"Agent ID: {self._agent_id}, Name: {self.first_name} {self.last_name}, "
              f"Phone: {self.phone_number}, Email: {self.email}")

    def approve_rental(self, rental_manager, rental_index):
        try:
            rental = rental_manager.get_rentals()[rental_index]
            rental["status"] = "approved"
            print(f"Rental for {rental['property_address']} approved by Agent {self.first_name} {self.last_name} (ID: {self._agent_id})")
        except IndexError:
            print("Invalid rental index")

    def show_all_rentals(self, rental_manager):
        for i, r in enumerate(rental_manager.get_rentals()):
            print(f"[{i}] Client {r['client'].first_name} {r['client'].last_name}: "
                  f"{r['property_address']} from {r['start_date']} to {r['end_date']}, "
                  f"${r['monthly_price']}/month | Status: {r['status']}")


if __name__ == "__main__":
    rentals = RentalManager()

    client1 = Client("Arseniy", "Faryna", "+3801234567", "farynaarseniy@gmail.com", 1)
    client2 = Client("Demyan", "Vorobets", "+3807654321", "demyanvorobets@gmail.com", 2)
    agent1 = Agent("Danylo", "Siatetskiy", "+3809876543", "danylosiatetskiy@gmail.com", 101)

    client1.rent_property(rentals, "Stryi, Shevchenko St, 45", "2025-10-01", "2026-03-01", 1200)
    client2.rent_property(rentals, "Lviv, Naukova St, 67", "2025-09-15", "2025-12-15", 800)

    print("\nAll rentals before approval:")
    agent1.show_all_rentals(rentals)


    agent1.approve_rental(rentals, 0)

    print("\nAll rentals after approval:")
    agent1.show_all_rentals(rentals)

    client1.show_information()