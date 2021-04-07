import time
import os

calc_start = False
start = input("Start? (y/n): ")

if start == "y" or start == "Y":
    calc_start = True
    DIGITS = int(input("Enter your accuracy (# digits of pi): "))

    def pi_digits(x):
        k, a, b, a1, b1 = 2, 4, 1, 12, 4
        while x > 0:
            p, q, k = k * k, 2 * k + 1, k + 1
            a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
            d, d1 = a/b, a1/b1
            while d == d1 and x > 0:
                yield int(d)
                x -= 1
                a, a1 = 10*(a % b), 10*(a1 % b1)
                d, d1 = a/b, a1/b1

    digits = [str(n) for n in list(pi_digits(DIGITS))]
    pi = float("%s.%s\n" % (digits.pop(0), "".join(digits)))

    while calc_start is True:

        def sector_parameter_input():
            global radius
            global angle
            radius = float(input("Enter the circle's radius: "))
            angle = float(input("Enter the angle of the arc: "))

        def sector_length_calc(radius, angle, pi):
            global arc_length
            arc_length = 2 * pi * radius * angle / 360
            rounded_arc_length = round(arc_length, 2)
            print(f"\n\nSector arc length is {arc_length} (rounded to {rounded_arc_length})")

        def sector_area_calc(radius, angle, pi):
            global sector_area
            sector_area = angle / 360 * pi * radius * radius
            rounded_sector_area = round(sector_area, 2)
            print(f"Sector area is {sector_area} (rounded to {rounded_sector_area})\n")

        def circle_circumference_calc(radius, pi):
            global circle_circumference
            circle_circumference = 2 * pi * radius
            rounded_circle_circumference = round(circle_circumference, 2)
            print(f"The circle's circumference is {circle_circumference} (rounded to {rounded_circle_circumference})")

        def circle_area_calc(radius, pi):
            global circle_area
            circle_area = pi * radius * radius
            rounded_circle_area = round(circle_area, 2)
            print(f"The circle's area is {circle_area} (rounded to {rounded_circle_area})\n")

        def length_percentage_calc(arc_length, circle_circumference):
            length_percentage = arc_length / circle_circumference * 100
            rounded_length_percentage = round(length_percentage, 2)
            print(f"The arc length is {length_percentage}% of the circle's circumference (rounded to {rounded_length_percentage}%)")

        def sector_area_percentage_calc(sector_area, circle_area):
            sector_area_percentage = sector_area / circle_area * 100
            rounded_sector_area_percentage = round(sector_area_percentage, 2)
            print(f"The sector's area is {sector_area_percentage}% that of the circle's area (rounded to {rounded_sector_area_percentage}%)\n\n")

        sector_parameter_input()
        os.system("cls||clear")

        sector_length_calc(radius, angle, pi)
        sector_area_calc(radius, angle, pi)

        circle_circumference_calc(radius, pi)
        circle_area_calc(radius, pi)

        length_percentage_calc(arc_length, circle_circumference)
        sector_area_percentage_calc(sector_area, circle_area)

elif start == "n" or start == "N":
    print("Exiting...")
    time.sleep(float(0.5))
    exit()

else:
    print("Please enter only y/n next time")
    print("Exiting...")
    time.sleep(float(0.5))
    exit()
