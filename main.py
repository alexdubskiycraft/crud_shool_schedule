import django_setup

from app.models import *

print("Виберіть дію:")
print("1. Додавання предмету")
print("2. Додавання вчителя")
print("3. Додавання класу")
print("4. Додавання учня")
print("5. Додавання заняття в розклад")
print("6. Додавання оцінки")


choice = input("Введіть номер дії: ")
