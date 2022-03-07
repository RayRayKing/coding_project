def add(*args):
    result = 0
    for arg in args:
        result += arg

    return result


class Car:
  def __init__(self,**kw):
        # self.model = kw["model"]
        self.make = kw["make"]


my_car = Car(model="Nissan", make="GT-R")


print(my_car.model)

