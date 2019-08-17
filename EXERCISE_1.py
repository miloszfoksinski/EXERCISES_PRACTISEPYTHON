import datetime


name = input('Write Your name: ')
age = int(input('Write how old are You: '))

today = datetime.datetime.now()
today_year = today.year
age_100 = today_year + (100-age)

print(name,', You will be 100 years old in ',age_100)
