class car:
   def __init__(self,make,model,year):
      self.make=make
      self.model=model 
      self.year=year
   def start(self):
    print(f"the {self.year} {self.make} {self.model} is starting.")
   def stop(self):
      print(f"the {self.year} {self.make} {self.model} is stopping.")
car1=car("toyato","camry",2022)
car2=car("toyato","camry",2045)
car1.start()
car2.stop()