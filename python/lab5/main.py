import datetime
from pattern import *
with db:
    db.create_tables([Vehicle, Price]) #генерация объектов на основе классов
    helicopter = Vehicle.create(name='Ка-50')
    vehicles = Vehicle.select()
