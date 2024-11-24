def convert_far_to_cel():
    far = float(input("Enter a temperature in degrees F: "))
    cel = round((far - 32) * 5 / 9, 2)
    print(f"{far} degrees F = {cel:.2f} degrees C")

def convert_cel_to_far():
    cel = float(input("Enter a temperature in degrees C: "))
    far = round(cel * 9 / 5 + 32, 2)  
    print(f"{cel} degrees C = {far:.2f} degrees F")
convert_far_to_cel()
convert_cel_to_far()
