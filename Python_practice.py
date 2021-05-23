print("Hello World!")          
print((5 + 2) * 3)
print(5 + (2*3))
print((8//5)-3)
print(8+(22*(2-4)))
print(16 - 3 /(2+7)-1)
print(3**(3%5))
print(5 + (9*3/2-4))
print(5+ (9*3/(2-4)))

countries = ["Istanbul", "San Francisco", "Dubai"]
countries.append("Paris")
print(countries)

print(len(countries))
countries_dic = {"Istanbul: 45", "Jerusalam: 300", "San Francisco: 450"}
print(countries_dic)
countries_dic = {}
countries_dic ["Istabul"] = 34
countries_dic["Ankara"] = 6
countries_dic["Izmit"] = 41
print(countries_dic)
print(len(countries_dic))
countries = ["Istanbul", "Paris", "Jerusalam"]




money = int(input("How much money do you have?"))

if money >=10000: 
    print("Buy all you need!")
else: 
    if money >= 8000:
        print("Don't spend much on luxury!")
    else: 
        if money >= 6000: 
            print("Buy your basic needs")
        else: 
            if money >= 5000: 
                print("Buy only your basic needs")
            else: 
                print("Save your money as much as possible")

score = int(input("What is your test score?"))

if score >= 90: 
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60: 
    print("Your grade is D")
else: 
    print("Your grade is F")

countries_ve = ["Turkey", "USA", "Palestine"]

if "China" in countries_ve:
    print("China is in the countries list")
else: 
    print("China is not in the countries list")

if "Turkey" and "France" in countries_ve: 
    print("Go to both countries")
else: 
    print("Go somewhere local!")

if "Turkey" or "USA" in countries_ve: 
    print("You can work in either country")
else: 
    print("It is hard for you to find a job eslewhere!")