import datetime
Name=input("Enter your Name")
Age=int(input("Enter your Age"))
nyear=datetime.datetime.now()
print(nyear.year)
year=(nyear.year-Age)+100
print(Name+"will turn 100 years old in",year)




