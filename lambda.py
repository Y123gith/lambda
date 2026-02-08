#1
adder = lambda a,b:a+b

# 2
divider_2 = lambda a: True if a%2==0 else False
#3
absolute = lambda a,b: abs(a-b)
#4
max_value = lambda a,b,c: max(a,b,c)
#5
grade_pass = lambda score: "PASS" if score >= 60 else "FAIL"
#6
def square(x):
    return x*x
# 7
def full_name(first,last):
    return first+" "+last
#8
def is_positive(n):
    return True if n > 0 else False

#9
def discount_price(price):
    return price*0.9 if price>100 else price

#10
def last_char(s):
    return s[-1]
#11
add_ten = lambda a:a+10
#12
rectangle_space = lambda width,height:width*height
#13
get_age = lambda age: age if age >17 and age < 65 else False
#14
length= lambda word: (len(word.upper()),word.upper())
#15
number = lambda num: num*num if num >0 else abs(num)
#16
score = lambda grade: "A" if grade >=90 else "B" if grade >=80 else "C" if grade >=70 else "F"
#17
smallest_and = lambda a,b,c: min(a,b,c)-max(a,b,c)
#18
div = lambda a,b: "cannot divide by zero" if b == 0 else a/b
#19
find_div = lambda num: "fizzbuzz" if (num%3==0 and num%5==0) else "fizz"if num%3==0 else "buzz" if num%5==0 else num
#20
the_price = lambda price,member: price*0.85 if member else price*0.95 if price > 200 else price 