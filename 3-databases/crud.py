from dbcreate import db,Puppy

# Creating
my_puppy = Puppy("Rufus",5)

db.session.add(my_puppy)
db.session.commit()

all_puppies = Puppy.query.all() # returns every object held in database

print(all_puppies)


#Select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#Select by name

# Filter_by returns a list
puppy_frankies = Puppy.query.filter_by(name="Frankie")
print(puppy_frankies.all())

# UPDATE

first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# Delete

second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
