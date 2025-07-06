# subtask 1
pi = 22/7
print(type(pi))
# output = <class 'float'>

# subtask 2
# for = 4
# output : error raised as for is a keyword used to initialize a for loop. The string 'for' cannot be used as a variable name.

# subtask 3
principle = int(input("Enter Principle amount: "))
roi = float(input("Enter Rate of Interest: "))
time = int(input("Enter Number of Years(time): "))
si = (principle*roi*time)/100
print(f"Simple Interst: {int(si)}")