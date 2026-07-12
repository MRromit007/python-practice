# Electrostatics Calculator
# By Romit Ghosh

import math

K = 9e9           # Coulomb's constant (N m²/C²)
EPSILON = 8.854e-12

while True:
    print("\n==============================")
    print("      ELECTROSTATICS CALCULATOR")
    print("==============================")
    print("1. Coulomb's Law")
    print("2. Electric Field")
    print("3. Electric Potential")
    print("4. Force on a Charge")
    print("5. Capacitance of Parallel Plate Capacitor")
    print("6. Energy Stored in Capacitor")
    print("7. Exit")

    choice = int(input("\nEnter your choice: "))

    # ---------------------------------------------------
    # 1. Coulomb's Law
    # ---------------------------------------------------
    if choice == 1:
        print("\nCoulomb's Law")
        q1 = float(input("Enter q1 (C): "))
        q2 = float(input("Enter q2 (C): "))
        r = float(input("Enter distance between charges (m): "))

        F = K * q1 * q2 / (r ** 2)

        print(f"\nElectrostatic Force = {F:.3e} N")

    # ---------------------------------------------------
    # 2. Electric Field
    # ---------------------------------------------------
    elif choice == 2:
        print("\nElectric Field due to a Point Charge")
        q = float(input("Enter charge (C): "))
        r = float(input("Enter distance (m): "))

        E = K * q / (r ** 2)

        print(f"\nElectric Field = {E:.3e} N/C")

    # ---------------------------------------------------
    # 3. Electric Potential
    # ---------------------------------------------------
    elif choice == 3:
        print("\nElectric Potential")
        q = float(input("Enter charge (C): "))
        r = float(input("Enter distance (m): "))

        V = K * q / r

        print(f"\nElectric Potential = {V:.3e} V")

    # ---------------------------------------------------
    # 4. Force on a Charge
    # ---------------------------------------------------
    elif choice == 4:
        print("\nForce on a Charge")
        q = float(input("Enter charge (C): "))
        E = float(input("Enter electric field (N/C): "))

        F = q * E

        print(f"\nForce = {F:.3e} N")

    # ---------------------------------------------------
    # 5. Parallel Plate Capacitor
    # ---------------------------------------------------
    elif choice == 5:
        print("\nParallel Plate Capacitor")

        A = float(input("Enter plate area (m²): "))
        d = float(input("Enter separation between plates (m): "))

        C = EPSILON * A / d

        print(f"\nCapacitance = {C:.3e} F")

    # ---------------------------------------------------
    # 6. Energy Stored
    # ---------------------------------------------------
    elif choice == 6:
        print("\nEnergy Stored in Capacitor")
        C = float(input("Enter capacitance (F): "))
        V = float(input("Enter potential difference (V): "))

        U = 0.5 * C * (V ** 2)

        print(f"\nEnergy Stored = {U:.3e} J")

    # ---------------------------------------------------
    # 7. Exit
    # ---------------------------------------------------
    elif choice == 7:
        print("\nThank you for using the calculator!")
        break

    else:
        print("\nInvalid choice. Please try again.")
