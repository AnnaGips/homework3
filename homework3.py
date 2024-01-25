# from datetime import datetime
# def get_days_from_today(date):
#     while True:
#         try:
#             converted_date = datetime.strptime(date, "%Y-%m-%d")
#             current_date = datetime.today()
#             difference = converted_date - current_date
#             return difference.days
#         except ValueError:
#             print("Неправильний формат вводу")
#             date = input("Введіть дату у форматі РРРР-ММ-ДД: ")
#             continue
#         else:
#             break
# user = input('Введіть дату у форматі РРРР-ММ-ДД: ')
# result = get_days_from_today(user)
# print(result)




# import random
# def get_numbers_ticket(min, max, quantity):
#     for num in [min, max, quantity]:
#         if not (1 <= num <= 1000):
#             return []
#         unique_numbers = random.sample(range(min, max + 1), quantity)
#         return sorted(unique_numbers)
# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print('Ваші лотерейні чісла:', lottery_numbers)




# import re
# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]
# def normalize_phone(phone_number):
#     p1=r"[\d\+]+"
#     phone_number=''.join(re.findall(p1,phone_number))
#     if len(phone_number)==10:
#         phone_number='+38'+phone_number
#     elif len(phone_number)==12:
#         phone_number='+'+phone_number
#     return phone_number
# for phone in raw_numbers:
#     print(normalize_phone(phone))


# import datetime as dt
# from datetime import datetime as dtdt
# users = [

#     {"name": "John Doe", "birthday": "1985.01.23"},

#     {"name": "Jane Smith", "birthday": "1990.01.27"}

# ]
# def get_upcoming_birthdays(users=None):
#     tdate=dtdt.today().date()
#     birthdays=[]
#     for user in users:
#         bdate=user["birthday"]
#         bdate=str(tdate.year)+bdate[4:]
#         bdate=dtdt.strptime(bdate, "%Y.%m.%d").date()
#         week_day=bdate.isoweekday()
#         days_between=(bdate-tdate).days
#         if 0<=days_between<7:
#             if week_day<6:
#                 birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")})
#             else:
#                 if (bdate+dt.timedelta(days=1)).weekday()==0:
#                     birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
#                 elif (bdate+dt.timedelta(days=2)).weekday()==0:
#                     birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
#                     return birthdays
# print(get_upcoming_birthdays(users))

