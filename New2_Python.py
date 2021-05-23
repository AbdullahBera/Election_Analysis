countries_dic = {'Islamabad': 45, 'Paris': 300, 'Berlin': 450}
for city, value in countries_dic.items():
    print(city , "city has" , value , "registered voters" )
for city, value in countries_dic.items():
    print(f"{city} city has {value} registered voters.")

hourly_wage = int(input("How much is your hourly wage?"))
total_wage = int(input("How many hours do you work a week?"))
message_to_member = (f"You earn ${hourly_wage} an hour. You earn a total of ${total_wage * hourly_wage}. Your monthly earning is ${total_wage * hourly_wage * 4}")

print(message_to_member)

message_to_collegue = (
    f' You can earn$ {hourly_wage:,} an hour.'
    f' You earn a total of ${total_wage * hourly_wage:,}.'
    f' Your monthly earning is ${total_wage * hourly_wage * 4:,}.')
print(message_to_collegue)