def checkAngle(num):
    if num == 0:
        print("Zero Angle");
    elif num < 90:
        print("Acute Angle")
    elif num == 90:
        print("Right Angle")
    elif num > 90 and num < 180:
        print("Obtuse Angle")
    elif num == 180:
        print("Straight Angle")
    elif num > 180 and num < 360:
        print("Reflex Angle")
    elif num > 360:
        print("Unidentified angle, try a lower number!")
        
check = float(input("What will your number be to check?"))

if checkAngle(check):
    print(checkAngle(check))
