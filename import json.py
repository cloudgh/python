import json

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)

address_obj = Address(street="Street", city="City", zip_code="12345")

person_obj = Person(name="John", age=30, address=address_obj)

address_json = address_obj.to_json()
print("Address JSON:")
print(address_json)

person_json = person_obj.to_json()
print("\nPerson JSON:")
print(person_json)

new_address_obj = Address(**json.loads(address_json))

new_person_obj = Person(**json.loads(person_json, object_hook=lambda d: Address(**d) if 'street' in d else d))

print("\nNew Address Object:")
print(new_address_obj.to_json())

print("\nNew Person Object:")
print(new_person_obj.to_json())
