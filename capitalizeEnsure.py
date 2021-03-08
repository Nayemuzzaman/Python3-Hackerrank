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

