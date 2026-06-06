import django_setup

from app.models import *

print("Виберіть команду:")
print("1. Додавання предмету")
print("2. Додавання вчителя")
print("3. Додавання класу")
print("4. Додавання учня")
print("5. Додавання заняття в розклад")
print("6. Додавання оцінки")


choice = input("Введіть номер дії: ")

if choice == "1":
    name = input("Введіть назву предмету: ")
    subject = Subject.objects.create(name=name)
    print(f"Створено предмет: {subject}")

elif choice == "2":
    firstname = input("Введіть ім'я вчителя: ") 
    lastname = input("Введіть прізвище вчителя: ") 
    middlename = input("Введіть по-батькові вчителя: ") 
    subject_id = int(input("Введіть id предмета: "))
    subject = Subject.objects.get(id=subject_id)
    
    teacher = Teacher.objects.create(firstname=firstname, lastname=lastname, middlename=middlename, subject=subject)
    print(f"Створено вчителя: {teacher}")    

elif choice == "3":
    year = input("Введіть рік навчання: ")
    name = input("Введіть назву класу: ")
    
    classes = Class.objects.filter(name=name, year=year).all()
    if len(classes) > 0:
        print("Такий клас вже існує!")
    else:
        class1 = Class.objects.create(name=name, year=year)
        print(f"Створено клас: {class1}")
