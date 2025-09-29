if __name__ == "__main__":
    m = int(input("Enter the marks of Maths: "))
    p = int(input("Enter the marks of Physics: "))
    c = int(input("Enter the marks of Chemistry: "))
    e = int(input("Enter the marks of English: "))
    g = int(input("Enter the marks of Gujarati: "))

    percentage = (m + p + c + e + g) / 5

    if percentage >= 33 and percentage < 50:
        print("Grade F")
    elif percentage >= 50 and percentage < 60:
        print("Grade E")
    elif percentage >= 60 and percentage < 70:
        print("Grade D")
    elif percentage >= 70 and percentage < 80:
        print("Grade C")
    elif percentage >= 80 and percentage <= 100:
        print("Grade A")
    else:
        print("Enter a valid value")

def add(x,y):
    return x+y
