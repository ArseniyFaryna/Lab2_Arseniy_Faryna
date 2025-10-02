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

    @phone_number.setter
    def phone_number(self, new_phone):
        if Person.validate_phone(new_phone):
            self._phone_number = new_phone
            print(f"Phone number updated to {new_phone}")
        else:
            print("Invalid phone number format")

    @property
    def email(self):
        return self._email

    def show_information(self):
        print(f"Name: {self._first_name} {self._last_name}, "
              f"Phone: {self._phone_number}, Email: {self._email}")

    @staticmethod
    def validate_phone(phone):
        return phone.startswith("+380") and len(phone) == 13


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


class Client(Person, RentalManager):
    def __init__(self, first_name, last_name, phone_number, email, client_id):
        Person.__init__(self, first_name, last_name, phone_number, email)
        RentalManager.__init__(self)
        self._client_id = client_id

    def show_information(self):
        print(f"Client ID: {self._client_id}, Name: {self.first_name} {self.last_name}, "
              f"Phone: {self.phone_number}, Email: {self.email}")

    def rent_property(self, property_address, start_date, end_date, monthly_price):
        self.add_rental(self, property_address, start_date, end_date, monthly_price)


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
    print("Phone validation:", Person.validate_phone("+380123456789"))

    client1 = Client("Arseniy", "Faryna", "+380123456789", "farynaarseniy@gmail.com", 1)
    client2 = Client("Demyan", "Vorobets", "+380765432198", "demyanvorobets@gmail.com", 2)
    agent1 = Agent("Danylo", "Siatetskiy", "+380987654321", "danylosiatetskiy@gmail.com", 101)

    client1.rent_property("Stryi, Shevchenko St, 45", "2025-10-01", "2026-03-01", 1200)
    client2.rent_property("Lviv, Naukova St, 67", "2025-09-15", "2025-12-15", 800)

    print("\nAll rentals before approval:")
    agent1.show_all_rentals(client1)
    agent1.show_all_rentals(client2)

    agent1.approve_rental(client1, 0)

    print("\nAll rentals after approval:")
    agent1.show_all_rentals(client1)
    agent1.show_all_rentals(client2)

    print("\nChanging phone number with setter")
    client1.phone_number = "+380111111111"
    client2.phone_number = "12345"

    client1.show_information()
    agent1.show_information()
