import time
from faker import Faker
fake = Faker('pl_PL')

# BaseContact


class BaseContact:
    def __init__(self, number, first_name, last_name, privat_number, e_mail):
        self.next_number = number
        self.first_name = first_name
        self.last_name = last_name
        self.privat_number = privat_number
        self.e_mail = e_mail

    def __repr__(self):
        return f'  \n{self.next_number} / {self.first_name} / {self.last_name} / {self.privat_number} / {self.e_mail}'

    def contact(self):
        return f'Wybieram numer {self.privat_number}...\ndzwonię do {self.first_name} {self.last_name}'

    @property
    def number_of_letters(self):
        sum = len(self.first_name) + len(self.last_name) + 1
        return sum


def create_base_contact():
    cards_list.append(BaseContact(
        number=number, first_name=fake.first_name(), last_name=fake.last_name(),
        privat_number=fake.phone_number(), e_mail=fake.email()))

# businessContact


class BusinessContact(BaseContact):
    def __init__(self, position, company, work_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_number = work_number

    def contact(self):
        return f'Wybieram numer {self.work_number}...\ndzwonię do {self.first_name} {self.last_name}'

    def __repr__(self):
        return f'  \n{self.next_number} / {self.first_name} / {self.last_name} / {self.company} / {self.position} / {self.work_number} / {self.e_mail}'


def create_busines_contact():
    cards_list.append(BusinessContact(number=number, first_name=fake.first_name(), last_name=fake.last_name(
    ), privat_number=None, work_number=fake.phone_number(), e_mail=fake.company_email(), position=fake.job(), company=fake.company(),))


# Variables
cards_list = []
number = 0
choose = 0

choose = int(input(
    "Wybierz czy mam wyświetlić wizytówki prywatne czy słubowe.Dla prywatnej wybiez 1 dla słubowej 2\n"))
if choose == 1:
    for i in range(int(input('Jaką Liczbę kontatków wygenerować?"\n'))):
        create_base_contact()
        number += 1
else:
    for i in range(int(input('Jaką Liczbę kontatków wygenerować?"\n'))):
        create_busines_contact()
        number += 1

print(cards_list)

flag = input("Czy chcesz poznać liczbę liter w którymś kontakcie [T/N]\n")
while flag == "T":
    list_letters = cards_list[int(
        input("Podaj nr kontaktu którego chcesz poznać liczbę liter\n"))]
    print(
        f'W imieniu i nazwisku {list_letters.first_name} {list_letters.last_name} jest {list_letters.number_of_letters} liter do liczby została dodana równiez spacja')
    flag = input("Czy chcesz poznać liczbę liter w innym kontakcie ? [T/N]\n")
ring = str(input('Czy chcesz się skontaktować z ktorymś kontaktem? [T/N]\n'))
if ring == "T":
    phone = cards_list[int(
        input('Podaj nr kontaktu z którym chcesz się skontaktować\n'))]
    print(phone.contact())
else:
    print('Nie został wybrany zaden kontakt w celu wybrania nr..')
