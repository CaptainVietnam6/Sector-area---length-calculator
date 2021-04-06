calc_start = False
start = input("Start? (y/n): ")
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

def arc_calculator():
    radius = float(input("Enter the circle's radius: "))
    angle = float(input("Enter the angle of the arc: "))
    arc_length = 2 * pi * radius * angle / 360
    print(f"\nArc length is {arc_length}\n")

if start == "y" or start == "Y":
    calc_start = True
    while calc_start is True:
        arc_calculator()

elif start == "n" or start == "N":
    exit()

else:
    print("Please enter only y/n next time")
    exit()
