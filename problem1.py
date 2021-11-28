import math

def get_coordinate():
    x = int(input("X>"))
    y = int(input("Y>"))

    return [x,y]

def get_distance(a,b):
    return math.sqrt(math.pow((a[0] - a[1]),2) + math.pow((b[0] - b[1]),2))

if __name__ == "__main__":
    print("Enter coordinates of A: ")
    a = get_coordinate()
    print("Enter coordinates of B: ")
    b = get_coordinate()

    print(get_distance(a,b))

