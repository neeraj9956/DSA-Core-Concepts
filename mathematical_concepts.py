class Count:
    def __init__(self):
        pass
    
    def cnt_digits(self,digit):
        digit=abs(digit)
        if digit == 0:
            return 1
        cnt = 0
        while digit >0:
            digit//=10
            cnt+=1
        return cnt
    
    def reverse_number(self,digit):
        digit=abs(digit)
        if digit==0:
            return 0
        reverse_digit =0
        while digit >0:
            last_rem = digit %10
            reverse_digit=reverse_digit * 10 + last_rem
            digit=digit//10
        return reverse_digit
        
    def checkpalindrome(self,digit):
        digits = abs(digit)
        reverse_digit =0
        while digits >0:
            last_digit = digits %10
            reverse_digit=reverse_digit * 10 + last_digit
            digits=digits//10
        if reverse_digit == digit:
            return True
        else:
            return False
    def check_number_is_armstrong(self,digit):
        digits = abs(digit)
        armstrong_number =0
        while digits >0:
            last_digit = digits %10
            armstrong_number= armstrong_number * 1 + last_digit*last_digit*last_digit
            digits=digits//10
        if armstrong_number == digit:
            return True
        else:
            return False
  
   def check_prime_number(self, digit):
    if digit <= 1:
        return False
    for i in range(2, int(digit**0.5) + 1):
        if digit % i == 0:
            return False
    return True





                
cnt = Count()
print("Count Digits------->",cnt.cnt_digits(321))
print("Reverse a Digit---------->",cnt.reverse_number(321))
if cnt.checkpalindrome(121):
    print("Number is Palindrome")
else:
    print("Number is Not palindrom")

if cnt.check_number_is_armstrong(153):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
if cnt.check_prime_number(13):
    print("Number is Prime")
else:
    print("Number is not Prime")
