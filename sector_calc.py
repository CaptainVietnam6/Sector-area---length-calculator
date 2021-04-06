import time

calc_start = False
start = input("Start? (y/n): ")

if start == "y" or start == "Y":
    calc_start = True
    while calc_start is True:
        DIGITS = int(input("Enter your accuracy (# digits of pi): "))

        def sector_parameter_input():
            global radius
            global angle
            radius = float(input("Enter the circle's radius: "))
            angle = float(input("Enter the angle of the arc: "))

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

        def sector_length_calc(radius, angle, pi):
            arc_length = 2 * pi * radius * angle / 360
            rounded_arc_length = round(arc_length, 2)
            print(f"\nSector arc length is {arc_length} (rounded to {rounded_arc_length})")

        def sector_area_calc(radius, angle, pi):
            arc_area = angle / 360 * pi * radius * radius
            rounded_arc_area = round(arc_area, 2)
            print(f"Sector area is {arc_area} (rounded to {rounded_arc_area})\n")

        sector_parameter_input()
        sector_length_calc(radius, angle, pi)
        sector_area_calc(radius, angle, pi)

elif start == "n" or start == "N":
    print("Exiting...")
    time.sleep(float(0.5))
    exit()

else:
    print("Please enter only y/n next time")
    print("Exiting...")
    time.sleep(float(0.5))
    exit()
