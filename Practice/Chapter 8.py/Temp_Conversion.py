#Write a python program using function to convert Celsius to Fahrenheit and vice versa.


#Temperature conversion

def f_to_c(f):
    return (f-32)*5/9 #c/5 = (f-32)/9 => c = (f-32)*5/9

f = (int(input( "Enter the temperature in Fahrenheit: ")))
c = f_to_c(f)
print(f"{round(c, 2)}° C")#f"{f_to_c(f)}° C" is a formatted string




def c_to_f(c):
    return (c/5)*9 +32 #c/5 = (f-32)/9 => f = (c/5)*9 +32

c = (int(input( "Enter the temperature in celcius: ")))
f = c_to_f(c)
print(f"{round(f, 2)}° F")#f"{c_to_f(c)}° F" is a formatted string