class Hotel:
    def __init__(self, name, address, rating, continent, country):
        self.name = name
        self.address = address
        self.rating = rating
        self.continent = continent
        self.country = country

    def pay_employees(self):
        print(f"{self.name}'s employees have received their paychecks!")

    def advertise(self):
        print(f"The advertisements for {self.name} have been sent to all platforms!")

    def pay_taxes(self):
        print(f"{self.name} has filed its returns for this year!")

    def clean(self):
        print(f"{self.name} has deployed its cleaning staff for the day!")

    def restock(self):
        print(f"The hotel supplies have been restocked!")

    def give_offer(self):
        print(f"{self.name} has opened the offer season for our clients! Enjoy!!")


class IntercontinentalHotel(Hotel):
    def __init__(self, name, address, rating, continent, country):
        super().__init__(name, address, rating, continent, country)

    def hire_translators(self):
        print(f"The recruitment has been opened to hire translators for {self.name}")

    def cuisine_update(self):
        print(f"{self.name}'s chefs are hunting for new exotic dishes!")

    def book_guests(self):
        print(f"The guests have been booked into {self.name}'s facilities.")


hotel1 = IntercontinentalHotel("Dine and Dance Hotel", "24D-Oakshire", 5.0, "Eutopia", "Barbon")
hotel2 = IntercontinentalHotel("Global Stay", "123 World Ave", 4.9, "Icya", "Patonia")
hotel3 = Hotel("Feed and Eat", "69 Pipeway", 4.5, "Khuka", "Rippit")

#examples of method implememntation
print(hotel1.address)
hotel2.hire_translators()
hotel3.clean()
