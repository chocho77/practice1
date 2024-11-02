# calculate area triangle
# h_a height of triangle
# side_a base side oposit height h_a

def triangle_area(side_a:float, height_a:float) -> float:
    result = side_a * height_a / 2.0
    return result

if __name__ == '__main__':
    side_a = 3.0
    height_a = 4.5
    result = triangle_area(side_a,height_a)
    print(f"Triangle area : side_a = {side_a}, height_a = {height_a} Area = {result}")
    side_a = 245.7
    height_a = 134.5
    result = triangle_area(side_a, height_a)
    print(f"Triangle area : side_a = {side_a}, height_a = {height_a} Area = {result}")

