def complete_divisibility(number,divisor):
    if number%divisor==0:
        print("The number {} is exactly divisible by {}".format(number, divisor))
    else:
        print("The number {} is not divisible by {}".format(number,divisor))
number,divisor=int(input("Enter number: ")),int(input("Enter divisor: "))
complete_divisibility(number, divisor)