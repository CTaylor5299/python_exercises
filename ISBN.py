digit = list(str(input("Please enter the first 12 digits of your ISBN code without hyphens: ")))
digitsum = 0


while(len(digit) != 12):
    print("You did not enter 12 integer digits.")
    digit = list(str(input("Please enter the first 12 digits of your ISBN code without hyphens: ")))


if len(digit) == 12:
    for i in range(0,len(digit)):
        if i % 2 == 0:
            digitsum += int(digit[i])
        else:
            digitsum += 3 * int(digit[i])

    digit_12 = str(10 - (digitsum % 10))
    digit.append(digit_12)
    ISBNCode = [digit[0], digit[1], digit[2], '-', digit[3], '-', digit[4], digit[5], digit[6], '-', digit[7], digit[8], digit[9], digit[10], digit[11], '-', digit[12]]
    print('Your 13 digit ISBN code is: ',''.join(ISBNCode))