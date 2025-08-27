import math

# Function to calculate area of a circle
def area_circle(radius):
    return math.pi * radius * radius

# Function to calculate area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height


# Main program
def area_calculator():
    print("=== Area Calculator ===")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Choose a shape (1/2/3): ")

    if choice == "1":
        r = float(input("Enter radius of the circle: "))
        print(f"Area of Circle = {area_circle(r):.2f}")

    elif choice == "2":
        l = float(input("Enter length of rectangle: "))
        w = float(input("Enter width of rectangle: "))
        print(f"Area of Rectangle = {area_rectangle(l, w):.2f}")

    elif choice == "3":
        b = float(input("Enter base of triangle: "))
        h = float(input("Enter height of triangle: "))
        print(f"Area of Triangle = {area_triangle(b, h):.2f}")

    else:
        print("Invalid choice!")

# Run the program
if __name__ == "__main__":
    area_calculator()
