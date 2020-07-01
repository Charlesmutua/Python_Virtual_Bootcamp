#Class name always start with caps
#Defining the Attributes ==> no. of wheels, seat capacity, engine type, Max Velocity


class Vehicle:
    #create constructor
    def __init__(self, number_of_wheels, seating_capacity, number_of_doors, engine_type, max_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.number_of_doors = number_of_doors
        self.engine_type = engine_type
        self.max_velocity = max_velocity
    
    # Set the number of wheels

    def number_of_wheels(self):
        return self.number_of_wheels

    #Make Noise
    def make_noise(self):
        return "**vrruuum**"

    # Stop
    def stop(self):
        return "**Stop**"


#Create an instance of the class(Object)
tesla_model_s = Vehicle(4, 5, 4, "Electric", 250)

#Use dot annotation to access the attributes of the object

print(tesla_model_s.engine_type)
#print(tesla_model_s.number_of_wheels)

#Accessing the varoius methods / Behaviours

tesla_model_s.number_of_wheels = 2
print(tesla_model_s.number_of_wheels)

print(tesla_model_s.make_noise())