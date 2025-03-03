from marshmallow import Schema, fields, post_load


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} is {self.age} years old'


class PersonSchema(Schema):
    name = fields.String()
    age = fields.Integer()

    @post_load
    def create_person(self, data, **kwargs):
        return Person(**data)


input_data = {
    "name": input("What Is Your Name? :"),
    "age": input("Your Age: ")
}

person_schema = PersonSchema()
person_obj = person_schema.load(input_data)
print(person_obj)

input_data = {
    "name": input("What Is Your Name? :"),
    "age": input("Your Age: ")
}
another_person = person_schema.load(input_data)
simplified_obj = person_schema.dump(another_person)
print(simplified_obj)
