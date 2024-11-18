print('''
For pressure press A
For speed press B
For density press C
For impulse press D
For force press E
''')

def calculate_pressure():
    force=float(input('Enter force'))
    area=float(input('Enter area'))
    pressure = force*area
    print(f"Pressure: {pressure} units")

def calculate_speed():
    distance=float(input('Enter distance'))
    time=float(input('Enter time'))
    speed=distance/time
    print(f"speed: {speed} units")


def calculate_density():
    mass=float(input('Enter mass'))
    volume=float(input('Enter volume'))
    density=mass/volume
    print(f"density: {density} units")

def calculate_impulse():
    force=float(input('Enter force'))
    time=float(input('Enter time'))
    impulse=force/time
    print(f"impulse: {impulse} units")

def calculate_force():
    mass=float(input('Enter mass'))
    acceleration=float(input('Enter acceleration'))
    force=mass*acceleration
    print(f"force: {force} N")

choice = input(" What do you need (A/B/C/D/E)? ").strip().upper()

if choice =='A':
    calculate_pressure()
elif choice == 'B':
    calculate_speed()
elif choice == 'C':
    calculate_density()
elif choice == 'D':
    calculate_impulse()
elif choice == 'E':
    calculate_force()
else:
    print('Invalid choice. Please enter an alphabet between A to E')


