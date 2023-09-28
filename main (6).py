radius = input("Enter the radius of a circle: ")
area = int(radius)**2*22/7
print("The area is ",area)
question = input("Perform another calculation? ")
while question.lower().startswith("y") :
    radius = input("Enter the radius of a circle: ")
    area = int(radius)**2*22/7
    print("The area is ",area)
    question = input("Perform another calculation? ")