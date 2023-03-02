

class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'phone': self.phone,
            'address': self.address
        }

    def call(self, phone_number):
        print(f'{self.phone} вызывает абонента {phone_number}')



chel1 = Human('Ihor', 'Igorovich', 32, '+380976741313' , 'city.Odessa,street.Taiti')
chel2 = Human('Egor', 'Egorovich' , 46 , '+380971234567' , 'city.Kyiv,street.Obolon')
chel3 = Human('Y' , 'Ygrikovich' , 24 , '+380977654321', 'city.Zhmerinka,street.Lesi Ykrainki')

