import car_rental.cars as c
import datetime as dt
import car_rental.garage as g
import customers.customers as cu

class Rental :
    def __init__(self, start_y, start_m, start_d) :
        self.opening = dt.datetime(year=start_y, month=start_m, day=start_d)
        self.rent_list={}
        self.garage=g.Garage()
        self.recent_fill={}
        self.recent_mileage={}
        
    def __del__(self) :
        print("폐업")
        
    def buy_car (self, car:c.Car) :
        ##garage에 넣음
        self.garage.add_car(car)
        
    def remove_car(self, car:c.Car):
        ##garage에서 제거
        self.garage.remove_car(car)
        
    def renting(self, car:c.Car, who:str, howlong:int) :
        self.garage.renting(car)
        if car.get_fuel() < 0.5*car.get_max_fuel() :
            car.fill(0.5*car.get_max_fuel()-car.get_fuel())
        print('반납시 연료는 50%이상이어야 합니다.')
        return_date = dt.date.today()+dt.timedelta(days=howlong)
        self.rent_list[car.get_name()]=[who, return_date]
        
    def get_back(self, car:c.Car) :
        if car.get_fuel() < 0.5*car.get_max_fuel() :
            print('연료를 50%이상으로 채우고 반납해야합니다.')
            return
        today=dt.date.today()
        if today>self.rent_list[car.get_name()][1] :
            print('반납일이 지나 추가요금이 발생되었습니다.')
        self.garage.get_back(car)
        del self.rent_list[car.get_name()]
        
    def monitor(self) :
        self.garage.retrieve()    
        
    def agg_recent_fill(self,x) :
        ##일주일간 주유량 집계
        today=dt.date.today()
        if today in self.recent_fill :
            self.recent_fill[today]+=x
        else :
            self.recent_fill[today]=x        
            
    def week_fill(self):
        ##일주일간 주유량 조회
        today=dt.date.today()
        week=today-dt.timedelta(days=7)
        d=today-dt.timedelta(days=1)
        quantity=0
        while d>=week :
            if d in self.recent_fill :
                quantity += self.recent_fill[d]
            d=d-dt.timedelta(days=1)
        print("일주일간({}~{}) 주유량 : {}".format(week, today-dt.timedelta(days=1), quantity))
    
    def agg_recent_mileage(self,x):
        ##일주일간 운행량 집계
        today=dt.date.today()
        if today in self.recent_fill :
            self.recent_mileage[today]+=x
        else :
            self.recent_mileage[today]=x      
            
    def week_mileage(self):
        ##일주일간 운행량 조회
        today=dt.date.today()
        week=today-dt.timedelta(days=7)
        d=today-dt.timedelta(days=1)
        quantity=0
        while d>=week :
            if d in self.recent_mileage :
                quantity += self.recent_mileage[d]
            d=d-dt.timedelta(days=1)
        print("일주일간({}~{}) 운행량 : {} km".format(week, today-dt.timedelta(days=1), quantity))
    
    def recommendation(self, ask):
        answer=""
        if ask=="Passenger car" : answer = "Sonata"
        elif ask=="SUV" : answer = "Tucson"
        elif ask=="Truck" : answer = "Bongo"
        elif ask=="Electric" : answer = "Tesla_s"
        print(answer)
        self.garage.search(answer)
