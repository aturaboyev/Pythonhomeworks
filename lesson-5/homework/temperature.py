def covert_cel_to_far(c):
    return c * 9/5 + 32

def covert_far_to_cel(f):
    return (f - 32) * 5/9

f = float(input("Enter a temperature in degrees F: "))
print(f"{f} degrees F = {covert_far_to_cel(f)} degrees C")

c = float(input("Enter a temperature in degrees C: "))
print(f"{c} degrees C = {covert_cel_to_far(c)} degrees F")

