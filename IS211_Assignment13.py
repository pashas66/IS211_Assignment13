
#Week 14 Assignment ­ Recursion:
#main function for this program

def main(): 

    print("--Fibonnaci--") #print the header
    number = int(input("Enter Number : ")) #prompt the user to enter a number

    for i in range(number): #loop through the number
        result = fibonnaci(i) #call the fibonnaci function
    print(result) #print out the result

    print("--GCD--") #print the header for GCD
    a = int(input("Enter first number: ")) #prompt the user to enter the first number
    b = int(input("Enter second number: ")) #prompt the user to enter the second number
    print(gcd(a,b)) #print out the gcd


    print("--Compare String--") #print the header
    s1 = input("Enter first string :") #prompt the user to enter the first string 
    s2 = input("Enter second string :") #prompt the user to enter the second string 
    print(compareTo(s1, s2)) #pring out the results

#Part I -­ Implement the Fibonnaci Sequence
def fibonnaci(number): #creating a Fibonnaci function 
    if number <= 1: #if the number is less than or equal 1 then return the number
        return number
    else:    
        return fibonnaci(number-1) + fibonnaci(number-2) #else use the Fibonnaci sequence formula


# Part II -­ Implement Euclid’s GCD Algorithm
def gcd(a,b): #creating a function for gcd
    if b==0: 
        return a
    else:
        return gcd(b, a%b) #to check for remainder using %


#Part III ­- String Comparison:
def compareTo(s1, s2): #creating a function for string comparision 

        #a negative number if s1 < s2,
        #0 if s1 == s2, and
        #a positive number if s1 > s2

    if s1 == s2: #using the = operator to compare
        return 0
    elif (len(s1) == 1 and len(s2) > 1):
        return  -ord(s2[0])
    elif (len(s1) > 1 and len(s2) == 1):
        return  ord(s1[0]) 
    elif ord(s1[0]) > ord(s2[0]):
        return ord(s1[0])
    elif ord(s1[0]) < ord(s2[0]):
        return -ord(s2[0])
    else:
        return compareTo(s1[1:], s2[1:])    


if __name__ == "__main__":
    main() #calling the main function

    #end of the code!