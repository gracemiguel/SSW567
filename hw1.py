#Grace Miguel 
#2/6/2021
#I pledge my honor that I've abided by the Stevens Honor System.
import math

def classify_triangle(a, b, c):
    output = ""
    if(a is b and a is c):
        output+= "The triangle is equilateral"
    elif(a is b or a is c or b is c):
        output+= "The triangle is isosceles"
    
    elif(a !=b and  a != c and b != c):
        output+= "The triangle is scalene"
    if(a*a +b*b == c*c):
        output+=" and right"
    return output


