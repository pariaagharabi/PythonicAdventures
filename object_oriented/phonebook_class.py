import os
"""
    Create A Python Class Phonebook That Should Keep A List Of Contacts. Derive The Class Contact From Two Base Classes Person And Address And Use Their Methods To Print Out The Contact Information. The Structure Of The Module Is Given Below. Complete The Code And Add Functions To Search And Sort Addresses. Test The Code By Creating A Phone Book With At-Least 10 Addresses And Display The Same.
"""


class Person:
    def __init__(self, name, email, phone_number):
        self._name = name
        self._email = email
        self._phone_number = phone_number

    # Protected Attributes starts with _
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    def display(self):
        print(
            f"\nPerson information:\n\t Name: {self._name} \n\t Email address: {self._email} \n\t Phone number: {self._phone_number}")


class Address:
    def __init__(self, street, city):
        self._street = street
        self._city = city

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street):
        self._street = street

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    def display(self):
        print(
            f"\nAddress of person:\n\tStreet: {self._street}\n\tCity: {self._city}")


class Contact(Person, Address):
    # constructor to initialize the person and Address class variables
    def __init__(self, name, email, phone_number, street, city):
        Person.__init__(self, name, email, phone_number)
        Address.__init__(self, street, city)

    def display(self):
        Person.display(self)
        Address.display(self)


class Phonebook:
    def __init__(self):
        self.__contacts = []

    def add(self, contact):
        self.__contacts.append(contact)

    def show(self):
        for contact in self.__contacts:
            contact.display()


c1 = Contact('Hans Hanson', 'hans@hanshanson.com',
             "1234567890", "plymouth", "Montreal")
c2 = Contact('Paria', 'paria@gmail.com',
             "5146772141", "brittany", "mont-royal")

phonebook = Phonebook()
phonebook.add(c1)
phonebook.add(c2)
phonebook.show()
