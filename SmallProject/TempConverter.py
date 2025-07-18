# Unit Converter

def FtC(temp):
    return (temp - 32) / 1.8

def CtF(temp):
    return (temp * 1.8) + 32

def CtK(temp):
    return (temp + 273.15)

def FtK(temp):
    return (FtC(temp) + 273.15)

def KtC(temp):
    return (temp - 273.15)

def KtF(temp):
    return ((KtC(temp) * 1.8) + 32)

while True:
    item_list = [
        ("------------------------"),
        ("0. Quit"),
        ("1. Fahrenheit => Celcius"),
        ("2. Celcius => Fahrenheit"),
        ("3. Celcius => Kelvin"),
        ("4. Fahrenheit => Kelvin"),
        ("5. Kelvin => Celcius"),
        ("6. Kelvin => Fahrenheit\n")
    ]

    for item in item_list:
        print(item)
    
    unit = int(input("Select the unit to convert: "))
    temp = float(input("Select Temperature number: "))

    if unit == 0:
        break

    elif unit == 1:
        print(FtC(temp),"C")

    elif unit == 2:
        print(CtF(temp),"F")
    
    elif unit == 3:
        print(CtK(temp),"K")

    elif unit == 4:
        print(FtK(temp),"K")

    elif unit == 5:
        print(KtC(temp),"C")

    elif unit == 6:
        print(KtF(temp),"F")

    else:
        print("Invalid. Please choose the number above!")