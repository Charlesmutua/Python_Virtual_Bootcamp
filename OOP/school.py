class School:
    def __init__(self, name, population, location, students, fees):
        self.name = name
        self.population = population
        self.location = location
        self.fees = fees
        

    def set_name(self, name):
        return name

    def set_fees(self, fees):
        return fees

    def set_population(self, pop):
        return pop
    
    def enroll(self, s_name):
        return f"{s_name} Enrolled Succesfully"


    


#Student = level, Enroll
#Gurdian, Fees.
# newstu = input()
#Class.method(enroll - newstude)


school1 = School("Nairobi", 600, "Kenya", 4, 1700)


print(school1.enroll(input("Enter New Students Name :")))