n = int(input("Enter The Value of n: ")) #for taking input
c = 0 #for variable
num = 11 #palindrome number starts form a least 2 digit
ans = 0 #for variable

while c != n: #run loop if n is not 0
    a = False
    for i in range(2, num):
        if (num % i) == 0:
            a = True #will asign composite so that prime remains in false or a

    if a== False:
        k = num
        t = k
        rev = 0 #reverse variable
        while (k > 0):
            digit = k % 10 #get lastdigit Eg.123 last is 3
            rev = rev*10+digit #will store the rev. digit
            k = k//10
        if (t == rev): #if rev and num is same its palindrome
            ans = t
            c = c + 1 #will increase value of c by 1
    num = num + 1
print("The Answer is : ",ans)