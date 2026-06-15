class India():
    def capital(self):
        print("New Delhi is the capital of india")
    def language(self):
        print("Hindi is the most widly spoken language in india")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington, D.c. is the capital of the USA")
    def language(self):
        print("English is the most widely spoken language in the Usa")
    def type(self):
        print("THe USA is a developed country")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()