##import rental_shop as rs
import car_rental.cars as c
import datetime as dt

class Garage:
    def __init__(self) :
        self.garage_list={}
        ##garage_list={car.get_name() :[car, 0 or 1] 
        
    def __del__(self) :
         return
        
    def add_car (self, car:c.Car) :
        name = car.get_name()
        if name in self.garage_list :
            print("같은 이름의 차가 이미 있습니다.")
            return
        self.garage_list[name]=[car, 1]
        ##1: this car is in the garage , 0: this car is not in the garage
        
          
    def remove_car (self, car:c.Car) :
        name=car.get_name()
        if self.garage_list[name][1] == 0 :
            print("현재 대여중인 차입니다. 반납 후 폐차가 가능합니다.")
        else :
            if name in self.garage_list :
                del self.garage_list[name]
                print(name,"을 폐차했습니다.")
            else :
                print(name,"이 차고에 없습니다.")
                
    def renting (self, car:c.Car) :
        name=car.get_name()
        if self.garage_list[name][1] == 0 :
            print("현재 대여중인 차입니다.")
        else :
            self.garage_list[name][1]=0
            print("대여되었습니다.")
            
    def get_back(self, car:c.Car) :
        name=car.get_name()
        if self.garage_list[name][1] != 0 :
            print("입력을 확인하십시오.")
            return
        
        self.garage_list[name][1] = 1
        print("반납되었습니다.")

    def available_list(self):
        for i in self.garage_list :
            if self.garage_list[i][1]==1 :
                print(i)
                
    ##garage_list={car.get_name() :[car, 0 or 1]             
    def retrieve(self) :
        print('현재 자동차 현황')
        for i in self.garage_list :
            t = '대여가능' if self.garage_list[i][1]==1 else '대여중'
            print('{:<10} {:<10} : {}'.format(self.garage_list[i][0].get_cartype(), i, t))
    
    def search(self, ask):
        print('요청사항에서 대여가능한 차 목록')
        for i in self.garage_list :
            if self.garage_list[i][0].get_cartype()==ask and self.garage_list[i][1]==1 :
                print('{:<10} {:<10}'.format(self.garage_list[i][0].get_cartype(), i))