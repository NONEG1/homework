# my_sentence = "aa {} bb {} cc{}".format("xx", "yy", "zz")
# print(my_sentence)
#
# my_sentence1 = "Hello, {} name is {}, I'm {} years {}".format("my", "Giorge", "19", "old.")
# print(my_sentence1)
#
# my_name ="giorge"
# my_surname = "tchanturidze"
# my_age = "20"
# my_sentence2 = "name: {} surname: {} age: {}".format(my_name, my_surname, my_age)
# print(my_sentence2)

# my_name = input("enter your name: ")
#
# print("My name is " + my_name)

# my_age = 22
# my_age += 3
# print(my_age)

#შემოვატანინოთ მომხმარებელს სახელი, გვარი, ასაკი. გავიდეს 3 წელი და გაზარდეთ ასაკი, დაპრინტეთ ახალი წინადადება:
# გავიდა 3 წელი და მე გავხდი რაღაცა წლის"

# my_name = input("Enter your name: ") #input-ით ყოველთვის შემოდის სტრინგი!
# my_surname = input("Enter your surname: ")
# my_age = input("Enter your age: ")
#
# print("My name is {}, My surname is {}, My age is {}.".format(my_name, my_surname, my_age))


# new_age = int(my_age) + 3
# print("After 3 years, i'm {} old".format(new_age))
# year = input("enter years: ")
# new_age = int(my_age) + int(year)
# print("After {} years, i'll be {} years old.".format(year, new_age))

# my_age = 20
# my_age += 3
# print("გავიდა 3 წელი და მე გავხდი 23 წლის")

#მომხმარებელს შემოატანინეთ ორი რიცხვი და დაპრინტეთ მათი ნამრავლი თუ ის 100-ზე მეტია. თუ არადა დაპრინტეთ, რომ მან წააგო.

# number_one = int(input("enter your number1: "))
# number_two = int(input("enter your number2: "))
#
# product = number_one * number_two
#
# if product > 100:
#     print(product)
# else:
#     print("YOU LOSE")



## HOMEWORK!!!
#input, %, if, +=
#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი და აქედან მხოლოდ კენტები შეკრიბოს და დაპრინტოს ჯამი.

num1 = int(input("NUM1: "))
num2 = int(input("NUM2: "))
num3 = int(input("NUM3: "))
#საინკრემენტაციო ცვლადი
my_sum = 0

if num1 % 2 == 1:
    my_sum += num1
if num2 % 2 == 1:
    my_sum += num2
if num3 % 2 == 1:
    my_sum += num3
print(my_sum)
