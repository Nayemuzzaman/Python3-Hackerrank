def output_value(size):
    print(val)
    if 90 <= val <= 65:
        print("Alphabets")

if __name__ == '__main__':
    n = input()
    val = int(ord(n))
    if 90 <= int(val) <= 65:
        print("Alphabets")
    output_value(val)

