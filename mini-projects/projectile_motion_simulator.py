import math

print("=" * 55)
print("        ADVANCED PROJECTILE MOTION SIMULATOR")
print("=" * 55)

while True:

    print("\nChoose the planet:")
    print("1. Earth")
    print("2. Moon")
    print("3. Mars")
    print("4. Jupiter")
    print("5. Custom g")

    planet = int(input("Enter choice: "))

    if planet == 1:
        g = 9.8
        planet_name = "Earth"

    elif planet == 2:
        g = 1.62
        planet_name = "Moon"

    elif planet == 3:
        g = 3.71
        planet_name = "Mars"

    elif planet == 4:
        g = 24.79
        planet_name = "Jupiter"

    elif planet == 5:
        g = float(input("Enter g (m/s²): "))
        planet_name = "Custom Planet"

    else:
        print("Invalid choice!")
        continue

    print(f"\nSimulation on {planet_name}")
    print("-" * 40)

    u = float(input("Initial velocity (m/s): "))
    theta = float(input("Angle of projection (degrees): "))
    h = float(input("Initial height above ground (m): "))

    theta_rad = math.radians(theta)

    ux = u * math.cos(theta_rad)
    uy = u * math.sin(theta_rad)

    # Time of flight (works for elevated launches)
    T = (uy + math.sqrt(uy**2 + 2 * g * h)) / g

    # Maximum height
    H = h + (uy**2) / (2 * g)

    # Horizontal range
    R = ux * T

    # Final velocity components
    vy_final = uy - g * T
    vx_final = ux

    final_speed = math.sqrt(vx_final**2 + vy_final**2)

    # Angle of impact
    impact_angle = math.degrees(
        math.atan(abs(vy_final) / abs(vx_final))
    )

    print("\n" + "=" * 40)
    print("RESULTS")
    print("=" * 40)

    print(f"Planet                 : {planet_name}")
    print(f"Acceleration due to g  : {g:.2f} m/s²")
    print(f"Horizontal velocity    : {ux:.2f} m/s")
    print(f"Vertical velocity      : {uy:.2f} m/s")
    print(f"Time of flight         : {T:.2f} s")
    print(f"Maximum height         : {H:.2f} m")
    print(f"Horizontal range       : {R:.2f} m")
    print(f"Impact speed           : {final_speed:.2f} m/s")
    print(f"Impact angle           : {impact_angle:.2f}°")

    # ---------------------------------------------------
    # Position at any time
    # ---------------------------------------------------

    while True:

        choice = input(
            "\nFind position at a specific time? (y/n): "
        ).lower()

        if choice == "n":
            break

        t = float(input("Enter time (s): "))

        if t < 0 or t > T:
            print("Projectile is not in air at this time.")
            continue

        x = ux * t
        y = h + uy * t - 0.5 * g * t**2

        vx = ux
        vy = uy - g * t

        speed = math.sqrt(vx**2 + vy**2)

        print("\nPosition Details")
        print("----------------")
        print(f"x = {x:.2f} m")
        print(f"y = {y:.2f} m")
        print(f"vx = {vx:.2f} m/s")
        print(f"vy = {vy:.2f} m/s")
        print(f"speed = {speed:.2f} m/s")

    # ---------------------------------------------------
    # Trajectory Table
    # ---------------------------------------------------

    choice = input(
        "\nGenerate trajectory table? (y/n): "
    ).lower()

    if choice == "y":

        n = int(input("Number of intervals: "))

        dt = T / n

        print("\n")
        print("Time(s)\tX(m)\tY(m)")
        print("-" * 35)

        t = 0

        while t <= T + 0.001:

            x = ux * t
            y = h + uy * t - 0.5 * g * t**2

            if y < 0:
                y = 0

            print(
                f"{t:.2f}\t{x:.2f}\t{y:.2f}"
            )

            t += dt

    # ---------------------------------------------------
    # Repeat simulation
    # ---------------------------------------------------

    again = input(
        "\nRun another simulation? (y/n): "
    ).lower()

    if again != "y":
        print("\nThank you for using the simulator!")
        break
