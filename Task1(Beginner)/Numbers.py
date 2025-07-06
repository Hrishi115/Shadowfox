def formatfunc(num, srt):
    return format(num, srt)

result = formatfunc(145, 'o')
print(result)

# output : 221
# Here, the format() function used within formatfunc() has 2 arguments; 
# num, takes the number input which needs to be formatted and srt, which takes input about which formatting to be used.
# For example, 'o' is octal conversion, 'b' is binary coversion, 'x' for hexadecimal coversion.
# The format() function here, converts 145 into octal format which becomes 221.