name = 'Zed A. Shaw'
age = 35 #not a lie
height =  74 # inches
#converts height from inches to centimeters
height_in_centimeters = round(height / .39, 2)

weight = 180 # pounds
#converts weight in lbs to kilograms
weight_in_kilograms = round(weight * 2.20, 2)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_centimeters} centimeters tall.")
print(f"He's {weight_in_kilograms} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are ususally {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height_in_centimeters + weight_in_kilograms
print(f"If I add {age}, {height_in_centimeters}, and {weight_in_kilograms} I get {total}.")
