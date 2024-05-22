from planet import Planet

f = open("planets.txt", "r")

planets = []

for line in f.readlines():
    planet_data = line.strip().split(",")
    try:
        planets.append(Planet(float(planet_data[0]),
                        float(planet_data[1]),
                        float(planet_data[2]),
                        float(planet_data[3]),
                        float(planet_data[4])))
    except ValueError:
        corrected_data = []
        for value in planet_data:
            try:
                float(value)
                corrected_data.append(value)
            except ValueError:
                corrected_value = ''
                for char in range(len(value)):
                    if value[char] == 'O':
                        corrected_value = corrected_value + '0'
                    else:
                        corrected_value = corrected_value + value[char]
                corrected_data.append((corrected_value))
        planets.append(Planet(float(corrected_data[0]),
                              float(corrected_data[1]),
                              float(corrected_data[2]),
                              float(corrected_data[3]),
                              float(corrected_data[4])))



sun = planets[3]
del planets[3]

t_total = 0.0
dt = 25000.0
t = 157788000

while t_total < t:
    for planet in planets:
        dx = sun.px - planet.px
        dy = sun.py - planet.py
      
        r = sun.radius(planet)

        F = sun.force(planet, r)

        fx = F * dx/r
        fy = F * dy/r

        ax = fx/planet.m
        ay = fy/planet.m
    
        planet.vx = planet.vx + ax*dt
        planet.vy = planet.vy + ay*dt

        planet.px = planet.px + planet.vx*dt
        planet.py = planet.py + planet.vy*dt

    t_total += dt

planets.insert(3, sun)

for planet in planets:
    print(f"{planet.px:.4e} {planet.py:.4e} {planet.vx:.4e} {planet.vy:.4e} {planet.m:.4e}")