# Check input character is alphabet, digit or special character
# All characters whether alphabet, digit or special character have ASCII value. Input character from the user will determine if it’s Alphabet, Number or Special character.
#
# ASCII value ranges-
#
# For capital alphabets 65 – 90
# For small alphabets 97 – 122
# For digits 48 – 57
# All other cases are Special Characters.


def output_value(yu):
    if (65 <= ord(n) <= 90 or 97 <= ord(n) <= 122):
        print("Alphabets")
    elif (48 <= ord(n) <= 97):
        print("Digit")
    else:
        print("Special Characters")


if __name__ == '__main__':
    n = input()
    val = ord(n)
    output_value(val)

