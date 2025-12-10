Temp = int(input("Enter A Temperature: "))

if Temp > 30:
    print("Hot")
elif Temp >= 20 and Temp <= 30:
    print("Warm")
elif Temp > 10 and Temp <= 19:
    print("Cool")
elif Temp <= 10:
    print("Cold")