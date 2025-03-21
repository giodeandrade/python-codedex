
# Planet Weights

print('===============')
print('  Mercury = 1')
print('   Venus = 2')
print('    Mars = 3')
print('  Jupiter = 4')
print('   Saturn = 5')
print('   Uranus = 6')
print('  Neptune = 7')
print('===============')

earth_weight = float(input("What's your Earth weight? "))
planet = int(input("Enter a planet number: "))

# Initialize planet_weight
planet_weight = None

if planet == 1:   # Mercury
    planet_weight = earth_weight * 0.38
elif planet == 2: # Venus
    planet_weight = earth_weight * 0.91
elif planet == 3: # Mars
    planet_weight = earth_weight * 0.38
elif planet == 4: # Jupiter
    planet_weight = earth_weight * 2.53
elif planet == 5: # Saturn
    planet_weight = earth_weight * 1.07
elif planet == 6: # Uranus
    planet_weight = earth_weight * 0.89
elif planet == 7: # Neptune
    planet_weight = earth_weight * 1.14
else:
    print('Invalid planet number')

if planet_weight is not None:
    print(f"Your weight on planet {planet} is: {planet_weight}")