# Fraction Reduction Routine through GCD

def gcd_finder(n,d):
    while (n != d):
        if (n > d):
            n = (n-d)
        else:
            d = (d-n)
    return n

def frac_red(n,d):
    print("The original fraction is: ")
    print("\t",n)
    print("\t----")
    print("\t",d)
    gcd = gcd_finder(n,d)
    n = int(n/gcd)
    d = int(d/gcd)
    return n,d

def main():
    n = int(input("Please enter an integer value for the numerator: "))
    d = int(input("Please enter an integer value for the denominator: "))
    new_n, new_d = frac_red(n,d)
    print("The REDUCED fraction is: ")
    print("\t",new_n)
    print("\t----")
    print("\t",new_d)

main()