from smartphone import Smartphone

catalog = [
    Smartphone("Sony", "Xperia", "+79999999999"),
    Smartphone("Aple", "Iphone", "+79888888888"),
    Smartphone("Motorolla", "50", "+79777777777"),
    Smartphone("Nokia", "2100", "+79666666666"),
    Smartphone("Huawei", "90", "+79555555555"),
]

for phone in catalog:
    print(f"{phone.marka}, {phone.model}, {phone.number}")
