import csv
from someprop import db


class RentProperty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), unique=True, nullable=False)
    postcode = db.Column(db.String(10), unique=False, nullable=False)
    prop_type = db.Column(db.String(60), nullable=False)
    asking_rent = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(100), nullable=False)


    def __str__(self):
        return f'{self.address}, {self.postcode}, {self.prop_type}, {self.asking_rent}, {self.url}'
db.create_all()

