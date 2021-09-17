class Car() : 
    ###생성자
    def __init__(self, name, isnew, max_fuel, fuel_economy, max_passenger=0, max_load=0) :
        self.max_fuel = max_fuel
        self.fuel_economy = fuel_economy
        self.max_passenger = max_passenger
        self.max_load=max_load
        self.passenger = 0
        self.load = 0
        self.economy = self.fuel_economy
        self.m_record = [0 for _ in range(100)]
        self.r_index=0
        self.name = name
        self.isnew=isnew
        if self.isnew : ##신차이면
            self.mileage = 0
            self.fuel = self.max_fuel
        else: ##신차가 아니면
            self.mileage = 50000
            self.fuel = self.max_fuel*0.3
        self.recent_quantity=0          
    ##소멸자    
    def __del__(self) :
        print("폐차")
        
    ###메소드
    def get_name(self):
        return self.name
    def get_fuel(self) :
        return self.fuel
    def get_max_fuel(self) :
        return self.max_fuel
    def fill_up(self) :
        quantity = self.max_fuel - self.fuel
        Car.set_recent_fill(self, quantity)
        self.fuel = self.max_fuel
        print("{}L 주유했습니다.".format(quantity))
        
    def fill(self, x) :
        if self.fuel+x <= self.max_fuel :
            self.fuel += x
            Car.set_recent_fill(self, x)
            print("{}L 주유했습니다.".format(x))
        else : 
            print("최대용량을 초과할 수 없어 최대용량까지 {}L만 주유합니다.".format(self.max_fuel-self.fuel))
            quantity = self.max_fuel - self.fuel
            Car.set_recent_fill(self, quantity)
            self.fuel=self.max_fuel
            
    def set_recent_fill(self, quantity) :
        self.recent_quantity
        
    def get_recent_fill(self):
        return self.recent_quantity
    
    def ride(self, x) :
        if self.max_passenger == 0 :
            print('이 차에는 탑승할 수 없습니다.')
            return
        if x<0 :
            print('탑승 인원이 음수일 수 없습니다.')
        else :
            if self.passenger == self.max_passenger :
                print("현재 탑승가능한 최대 인원이 탑승하고 있습니다.")
            elif self.passenger+x > self.max_passenger :
                print("탑승가능 인원을 초과하여 탑승할 수 없습니다.")
                print("현재 추가 탑승가능 인원은 {}명 입니다.".format(self.max_passenger - self.passenger))
            else :
                self.passenger += x
                Car.update_economy(self, passenger=self.passenger)
                
    def get_off(self, x) :
        if x<0 :
            print('하차 인원이 음수일 수 없습니다.')
        else :
            if x>self.passenger :
                print('하차인원이 현재 탑승인원보다 많을 수 없습니다.')
            else :
                self.passenger -= x
                Car.update_economy(self, passenger=self.passenger)
                
    def loading(self, x) : 
        if self.max_load == 0 :
            print('이 차에는 짐을 실을 수 없습니다.')
            return
        if x<0 :
            print('무게가 음수일 수 없습니다.')
        else :
            if self.load == self.max_load  :
                print("현재 최대 적재량입니다. 추가 적재가 불가능합니다.")
            elif self.load + x > self.max_load :
                print("최대적재량을 초과하여 적재할 수 없습니다.")
                print("현재 추가 적재 가능 용량은 {}kg 입니다.".format(self.max_load - self.load))
            else :
                self.load += x
                Car.update_economy(self, load=self.load)
                
    def unloading(self, x) :
        if x<0 :
            print('무게가 음수일 수 없습니다.')
        else :
            if x>self.load :
                print('하차량이 현재 적재량보다 많을 수 없습니다.')
            else : 
                self.load -= x
                Car.update_economy(self, load=self.load)
                
    def get_range(self) : ##주행가능거리
        return self.economy*self.fuel
    
    def update_economy(self, passenger=0, load=0) :
        if self.max_passenger != 0 and self.max_load != 0 :
            self.economy = self.fuel_economy*(1 - self.passenger/self.max_passenger*0.1 - self.load/self.max_load*0.1)
        elif self.max_passenger == 0 and self.max_load != 0:
            self.economy = self.fuel_economy*(1 - self.load/self.max_load*0.1)
        elif self.max_passenger != 0 and self.max_load == 0:
            self.economy = self.fuel_economy*(1 - self.passenger/self.max_passenger*0.1)
        else :
            print('이럴리없어....')
            
    def move(self, x:float) :
        if self.fuel==0:
            print("현재 연료가 없어 주행이 불가능합니다.")
        elif x<=Car.get_range(self) :
            print("{}km 이동".format(x))
            self.fuel -= x/self.economy
            self.mileage += x
            Car.move_record(self, x, self.economy)
            Car.set_recent_mileage(self, x)
        else :
            print("현재 연료가 부족해 {}만큼 갈 수 없습니다. 현재 주행가능 거리는 {:.2f}입니다.".format(x, Car.get_range(self)))
            Car.move(self, Car.get_range(self))
            print("주행가능 거리를 모두 운행했습니다. 연료가 부족해 주행을 중지합니다.")               
            
    def set_recent_mileage(self, quantity) :
        self.recent_quantity=quantity
    def get_recent_mileage(self) :
        return self.recent_quantity
    
    def get_mileage(self) :
        return self.mileage
    
    def move_record(self, x, economy) :
        if x>100 : x=100
        for i in range(x) :
            self.m_record[self.r_index%100]=float(economy)
            self.r_index+=1
            
    def fuel_economy_100(self) :
        ##최근 100km 주행간 연비
        if self.mileage <100 : return self.economy
        else :
            return sum(self.m_record)/len(self.m_record)
        
    def show_dash(self) :
        pass

class Sonata(Car) :
    def __init__(self, name, isnew) :
        self.isnew=isnew
        self.name=name
        Car.__init__(self, name=name, max_fuel=55, fuel_economy=12, max_passenger=4, isnew=isnew)
    def get_cartype(self) :
        return "Sonata"
    def show_dash(self) :
        print('{} DASH'.format(self.get_cartype()))
        dic={'총운행거리(km)':self.mileage, '현재 연료량(L)': self.fuel, '주행가능거리(km)':Car.get_range(self), '최근 100km간 연비':Car.fuel_economy_100(self), '탑승인원(명)':self.passenger}
        for i in dic :
            print('{} : {}'.format(i, dic[i]))
            
class Tucson(Car) :
    def __init__(self, name, isnew) :
        self.isnew=isnew
        self.name=name
        Car.__init__(self, name=name, max_fuel=60, fuel_economy=10, max_passenger=5, max_load=500, isnew=isnew)
    def get_cartype(self) :
        return "Tucson"
    def show_dash(self) :
        print('{} DASH'.format(self.get_cartype()))
        dic={'총운행거리(km)':self.mileage, '현재 연료량(L)': self.fuel, '주행가능거리(km)':Car.get_range(self), '최근 100km간 연비':Car.fuel_economy_100(self), '탑승인원(명)':self.passenger,'적재량(kg)':self.load}
        for i in dic :
            print('{} : {}'.format(i, dic[i])) 
        
class Bongo(Car) :
    def __init__(self, name, isnew) :
        self.isnew=isnew
        self.name=name
        Car.__init__(self, name=name, max_fuel=55, fuel_economy=10, max_load=700, isnew=isnew)
    def get_cartype(self) :
        return "Bongo"
    def show_dash(self) :
        print('{} DASH'.format(self.get_cartype()))
        dic={'총운행거리(km)':self.mileage, '현재 연료량(L)': self.fuel, '주행가능거리(km)':Car.get_range(self), '최근 100km간 연비':Car.fuel_economy_100(self), '적재량(kg)':self.load}
        for i in dic :
            print('{} : {}'.format(i, dic[i])) 
        
class Tesla_s(Car) :
    def __init__(self, name, isnew) :
        self.isnew=isnew
        self.name=name
        Car.__init__(self, name=name, max_fuel=450, fuel_economy=1, max_passenger=5, isnew=isnew)
    def get_cartype(self) :
        return "Tesla_s"
    
    def fill_up(self) :
        quantity = self.max_fuel - self.fuel
        Car.set_recent_fill(self, quantity)
        self.fuel = self.max_fuel
        print("{}kwh 충전했습니다.".format(quantity))
        
    def fill(self, x) :
        if self.fuel+x <= self.max_fuel :
            self.fuel += x
            Car.set_recent_fill(self, x)
            print("{}kwh 충전했습니다.".format(x))
        else : 
            print("최대용량을 초과할 수 없어 최대용량까지 {}kwh만 충전합니다.".format(self.max_fuel-self.fuel))
            quantity = self.max_fuel - self.fuel
            Car.set_recent_fill(self, quantity)
            self.fuel=self.max_fuel
            
    def show_dash(self) :
        print('{} DASH'.format(self.get_cartype()))
        dic={'총운행거리(km)':self.mileage, '현재 연료량(kwh)': self.fuel, '주행가능거리(km)':Car.get_range(self), '최근 100km간 연비':Car.fuel_economy_100(self), '탑승인원(명)':self.passenger}
        for i in dic :
            print('{} : {}'.format(i, dic[i]))

