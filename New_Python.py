from sys import pycache_prefix


countries = ["Istanbul", "San Francisco", "Dubai"]
for city in countries: 
    print(city)
numbers = [0,1,2,3,4,5]
for num in numbers: 
    print(num)
for num in range(6):
    print(num)

for i in range(len(countries)):
    print(countries[0])

countries_dic = {'Islamabad': 45, 'Paris': 300, 'Berlin': 450}

for city in countries_dic:
    print(city)
for city in countries_dic.values():
    print(city)

for city in countries_dic:
    print(countries_dic[city])

for city in countries_dic:
    print(countries_dic.get(city))

for key, value in countries_dic.items():
    print(key,value)

for city, value in countries_dic.items():
    print(city, "city has", value, "registered voters")

city_dic = [{"city":"Islamabad", "population": 888192},
            {"city":"Paris", "population": 718181},
            {"city":"Berlin", "population": 616161}]

for city in city_dic:
    print(city) 
for i in range(len(city_dic)):
    print(city_dic[i])

for countries_dic in city_dic:
    for value in countries_dic.values():
        print(value)

for countries_dic in city_dic:
    print(countries_dic["city"])

amount = 899

print("Your payment this years is $" + str(amount))

ques_age = int(input("How old are you?"))
ques_income = int(input("What is your weekly income?"))
average_mean = (ques_age + ques_income) * 88
print("I was born to have $" + str(average_mean) + " at the age of five")

countries_dic = {'Islamabad': 45, 'Paris': 300, 'Berlin': 450}
for city, value in countries_dic.items():
    print(city , "city has" , value , "registered voters" )