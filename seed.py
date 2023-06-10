from models import db, Pet
from app import app


db.drop_all()
db.create_all()

Pet.query.delete()

Remy = Pet(name="Remy", species="Dog", photo_url="https://www.science.org/do/10.1126/science.aaw5856/abs/dog_16x9_3.jpg",
           age="10", notes="Good boy")
Tom = Pet(name="Tom", species="Cat", age=5, notes="cat", avaliable=False)


db.session.add(Remy)
db.session.add(Tom)
db.session.commit()