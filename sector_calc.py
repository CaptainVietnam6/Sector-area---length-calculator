'''
Copyright (©) 2021 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#7932
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itz_kietttttttttt
Program Status: ACTIVE - FINALISED
'''

import time
import os

os.system("cls||clear")
calc_start = False
start = input("Start? (y/n): ")
os.system("cls||clear")

if start == "y" or start == "Y":
    calc_start = True
    DIGITS = int(input("Enter your accuracy (# digits of pi): ")) #asks the user the precision or how many digits of pi the algorithm will generate
    if DIGITS <= 0 or DIGITS > 25000:
        print("Sorry, but for caculation time reasons, this calculator will only accept under 25000 digits of pi")
        exit()

    #algorithm to generate requested digits of pi
    def pi_digits(x):
        k, a, b, a1, b1 = 2, 4, 1, 12, 4
        while x > 0:
            p, q, k = k * k, 2 * k + 1, k + 1
            a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
            d, d1 = a/b, a1/b1
            while d == d1 and x > 0:
                yield int(d)
                x -= 1
                a, a1 = 10 * (a % b), 10 * (a1 % b1)
                d, d1 = a/b, a1/b1

    digits = [str(n) for n in list(pi_digits(DIGITS))]
    pi = float("%s.%s\n" % (digits.pop(0), "".join(digits)))

    while calc_start is True:
        #defines all the calculation/operations

        #asks the user their circle's parameters
        def sector_parameter_input():
            global radius
            global angle
            radius = float(input("Enter the circle's radius: "))
            if radius <= 0 or radius >= 25000:
                print("The calculator only excepts numbers between 1-25000 for the radius, please restart the calculator")
                exit()

            angle = float(input("Enter the angle of the arc: "))
            if angle <= 0 or angle > 360:
                print("Sorry, but the input angle can only be between  1-360, please restart the calculator")
                exit()


        #calculates the length of an arc from radius and angle
        def sector_length_calc(radius, angle, pi):
            global arc_length
            arc_length = 2 * pi * radius * angle / 360
            rounded_arc_length = round(arc_length, 2)
            print(f"\n\nSector arc length is {arc_length} (rounded to {rounded_arc_length})")


        #calculates area of the sector from radius and angle
        def sector_area_calc(radius, angle, pi):
            global sector_area
            sector_area = angle / 360 * pi * radius * radius
            rounded_sector_area = round(sector_area, 2)
            print(f"Sector area is {sector_area} (rounded to {rounded_sector_area})\n")


        #calculates the circle's circumference from radius
        def circle_circumference_calc(radius, pi):
            global circle_circumference
            circle_circumference = 2 * pi * radius
            rounded_circle_circumference = round(circle_circumference, 2)
            print(f"The circle's circumference is {circle_circumference} (rounded to {rounded_circle_circumference})")


        #calculates the circle's area from radius
        def circle_area_calc(radius, pi):
            global circle_area
            circle_area = pi * radius * radius
            rounded_circle_area = round(circle_area, 2)
            print(f"The circle's area is {circle_area} (rounded to {rounded_circle_area})\n")
            

        #calculates what percentage is the arc's length in relation to the circle's circumference
        def length_percentage_calc(arc_length, circle_circumference):
            length_percentage = arc_length / circle_circumference * 100
            rounded_length_percentage = round(length_percentage, 2)
            print(f"The arc length is {length_percentage}% of the circle's circumference (rounded to {rounded_length_percentage}%)")


        #calculates what percentage is the sector's area in relation to the circle's area
        def sector_area_percentage_calc(sector_area, circle_area):
            sector_area_percentage = sector_area / circle_area * 100
            rounded_sector_area_percentage = round(sector_area_percentage, 2)
            print(f"The sector's area is {sector_area_percentage}% that of the circle's area (rounded to {rounded_sector_area_percentage}%)\n\n")


        sector_parameter_input()
        os.system("cls||clear") #clears the terminal

        sector_length_calc(radius, angle, pi)
        sector_area_calc(radius, angle, pi)

        circle_circumference_calc(radius, pi)
        circle_area_calc(radius, pi)

        length_percentage_calc(arc_length, circle_circumference)
        sector_area_percentage_calc(sector_area, circle_area)


elif start == "n" or start == "N": #if the user responses with "n" it'll exit
    print("Exiting...")
    time.sleep(float(0.5))
    exit()

else: #if the user responds with anything that is not "y" or "n", it'll warn them and exit
    print("Please enter only y/n next time")
    print("Exiting...")
    time.sleep(float(0.5))
    exit()
