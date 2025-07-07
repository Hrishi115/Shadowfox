#Subtask 1
def formatfunc(num, srt):
    return format(num, srt)

result = formatfunc(145, 'o')
print(result)

# output : 221
# Here, the format() function used within formatfunc() has 2 arguments; 
# num, takes the number input which needs to be formatted and srt, which takes input about which formatting to be used.
# For example, 'o' is octal conversion, 'b' is binary coversion, 'x' for hexadecimal coversion.
# The format() function here, converts 145 into octal format which becomes 221.

#subtask 2
pi = 3.14
radius = 84 
area = pi*radius*radius
# print(f"The Area of the pond: {area}")
water_per_square_meter = 1.4
Total_water_in_pond = int(water_per_square_meter*area)
print(f"The total water present in the pond: {Total_water_in_pond} Litres")

#subtask 3
Distance = 490 #in meters
time = 7*60
print(f"Speed: {int(Distance/time)} m/s")