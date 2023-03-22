# Functions to convert temperature from Fahrenheit to Celsius and vice versa
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

# Function to calculate force given mass and acceleration
def get_force(mass, acceleration):
    return mass * acceleration

# Function to calculate energy given mass and speed of light
def get_energy(mass, c=3*10**8):
    return mass * c**2

# Function to calculate work done given mass, acceleration, and distance
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

# Constants for train mass, acceleration, and distance
train_mass = 22680
train_acceleration = 10
train_distance = 100

# Constants for bomb mass
bomb_mass = 1

# Calculate temperature conversions
f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

# Calculate force of train
train_force = get_force(train_mass, train_acceleration)

# Calculate energy of bomb
bomb_energy = get_energy(bomb_mass)

# Calculate work done by train
train_work = get_work(train_mass, train_acceleration, train_distance)

# Print results
print("Temperature Conversions:")
print(f"100 degrees Fahrenheit is {f100_in_celsius:.1f} degrees Celsius.")
print(f"0 degrees Celsius is {c0_in_fahrenheit:.1f} degrees Fahrenheit.\n")

print("Train Physics:")
print(f"The GE train supplies {train_force:.1f} Newtons of force.")
print(f"The work done by the train is {train_work:.1f} Joules over {train_distance} meters.\n")

print("Bomb Physics:")
print(f"A 1kg bomb supplies {bomb_energy:.1f} Joules.")
