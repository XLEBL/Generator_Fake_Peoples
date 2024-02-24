import random
import datetime
from russian_names import RussianNames
datalist = ["14.06", "4.09", "5.02", "16.03", "13.05", "9.04", "5.01", "31.03", "14.04", "15.12", "17.11", "13.03", "5.12", "1.04"]
def gen_name():
    return RussianNames().get_person()
def age():
    random_age = random.randint(18, 40)
    current_year = datetime.datetime.now().year
    date_of_birth = random.choice(datalist)
    year_of_birth = int(current_year - int(random_age))
    return f"{random_age} / {date_of_birth} {year_of_birth}"
def credit_card():
    service_card = random.choice(["2", "4", "5"])
    if service_card == 2:
        card_service = "MIR"
    elif service_card == 4:
        card_service = "Visa"
    else:
        card_service = "Mastercard"
    credit_card_number = random.randint(1000000000000000, 9999999999999999)
    credit_card_cvv = random.randint(100, 999)
    credit_card_expiry = f"{random.randint(1, 30)}/{random.randint(1, 12)}"
    return f"{card_service} {service_card}{credit_card_number} {credit_card_cvv} {credit_card_expiry}"
def generate_phone_number():
     area_code = str(random.randint(12, 99))
     phone_number = str(random.randint(1000000, 9999999))
     return f"+7{area_code}{phone_number}"   
