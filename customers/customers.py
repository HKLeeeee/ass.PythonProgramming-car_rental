import car_rental.cars as c
import datetime as dt
import car_rental.rental_shop as rs

class Customer :
    def __init__(self, name:str) :
        self.name=name
        self.d=dt.timedelta(days=0)
        ##d는 빌리는 기간
        ##8일간 빌리면 d=8
        
    def __del__(self):
        return
    def get_name(self) :
        return self.name
    
    def rent(self, car:c.Car, d:int, where:rs.Rental) :
        self.car=car
        self.rental_shop = where
        self.rental_shop.renting(self.car, self.name, d)
        
    def give_back(self) :
        self.rental_shop.get_back(self.car)
        
    def fill_up(self) :
        self.car.fill_up()
        self.rental_shop.agg_recent_fill(self.car.get_recent_fill())
        
    def fill(self, x) :
        self.car.fill(x)
        self.rental_shop.agg_recent_fill(self.car.get_recent_fill())
        
    def ride_passenger(self, x):
        self.car.ride(x)
    def get_off_passenger(self, x):
        self.car.get_off(x)
    def loading(self, x):
        self.car.loading(x)
    def unloading(self, x):
        self.car.unloaing(self,x)
    def driving(self, x):
        self.car.move(x)
        self.rental_shop.agg_recent_mileage(self.car.get_recent_mileage())
    def retrieve_dash(self) :
        self.car.show_dash()
        
    def ask(self, ask, where:rs.Rental) :
        where.recommendation(ask)