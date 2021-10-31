from dbcreate import db,Puppy

# Creates all the tables
db.create_all()

sam = Puppy("Sammy",3)
frank = Puppy("Frankie",4)

print(sam.id) # None
print(frank.id) #None

db.session.add_all([sam,frank])

db.session.commit()
# db.session.add(object) -> This code adds individually, and the one above add one by one seperately

print(sam.id)
print(frank.id)

print(sam.__repr__)