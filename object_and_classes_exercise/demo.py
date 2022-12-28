class Family:
    for_all = []

    def __init__(self, family_name, number_of_people, has_tv = True):
        self.family_name = family_name
        self.number_of_people = number_of_people
        self.has_tv = has_tv



    def change_name(self):
        print('Dimitrovi')


new_object = Family('Georgievi', 4)
new_object1 = Family('Petrovi', 5, False)
Family.for_all.append(new_object.family_name)
Family.for_all.append(new_object1.family_name)
print(Family.for_all)
print(new_object1.has_tv)
new_object.change_name()
print(new_object.__dict__)

