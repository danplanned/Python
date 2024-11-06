import datetime as dt
import decimal 
import random
import custom_module

DateToday = dt.date.today()
CurrentYear = DateToday.year
TimeNow = dt.datetime.now().time()
print(DateToday)
print(CurrentYear)

RandomYear = random.randint(0,10000)
print(RandomYear)

TravelDestinations = ["France", "Spain", "England", "Thailand", "Vietnam", "Canada"]
Destination = random.choice(TravelDestinations)
print(Destination)

BaseCost = decimal.Decimal('1000.00')

yearDifference = abs(CurrentYear - RandomYear)
CostMultiplier = decimal.Decimal(1+(yearDifference/10))

FinalCost = round(BaseCost * CostMultiplier,2)

print(FinalCost)
print("\n")

custom_module.generate_time_travel_message(RandomYear, Destination, FinalCost)