from ikea.models import BaseModel
from ikea.fields import PKColumn, IntegerColumn, TextColumn


class User(BaseModel):
    __tablename__ = 'users'

    id = PKColumn()
    name = TextColumn(max_length=100)
    age = IntegerColumn(number=20)
         
class Student(User):
    __tablename__ = 'Students'
    email = TextColumn()
    shirt_size = IntegerColumn(number=1)


# Creating all tables from BaseModel class
BaseModel.create_all_tables()

# Create record in table
User.create_obj(name="Rosi", age=22)

# Return dict with object
User.filter(name = "Panda")

