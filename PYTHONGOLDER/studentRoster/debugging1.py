import random

def calculate_area(shape):
    if shape == "circle":
        radius = float(input("enter radius: "))
        area = 3.14 * radius * radius
    elif shape == "rectangle":
        width = float(input("enter width: "))
        height = float(input("enter height: "))
        area = width * height
    elif shape == "triangle":
        base = float(input("enter base: "))
        height = float(input("enter height: "))
        area = 0.5 * base * height
    else:
        print("invalid")
        return 
    return area

def get_random_shape():
    shapes = ["circle", "rectangle", "triangle"]
    return random.choice(shapes)

results = {}

while True:
    print()
    print("1. calculate area")
    print("2. random shape")
    print("3. show all results")
    print("4. quit")

    choice = int(input("choose: "))

    if choice == 1:
        shape = input("enter shape (circle/rectangle/triangle): ").lower().strip()
        area = calculate_area(shape)
        if area is not None:
            results[shape] = area
            print("area is: " + str(area))
    elif choice == 2:
        shape = get_random_shape()
        print("random shape: " + shape)
        area = calculate_area(shape)
        results[shape] = area
        print("area is: " + str(area))
    elif choice == 3:
        for shape, area in results.items():
            print(">> " + str(shape))
            print(area)
    elif choice == 4:
        break
    else:
        print("invalid")