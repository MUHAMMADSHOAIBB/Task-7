print('==============task7.1==========')
print('hello welcome to ATM machine')
Amount = 5000
print('select the option 1,2,3')
option = int(input('1 is for check balnce ,2 is for withdraw your amount,and 3 is for deposit amount'))
a = int(input('enter the amount you withdraw'))
if option==1:
    print('your current balance is:',Amount)
elif a>Amount:
    print("insufficient balance")
else:
    print("your amount withdrawn ")
    if option ==3:
        b = int(input('enter the amount you want to deposit'))
        Amount +=b
        print('Amount deposited')
    else:
        print("soory please take your card")

print('=====================TAsk7.2================')
print('welcome to gamexone oofice')
gamexone = int(input('please tell us about your experience years in game development '))
if gamexone > 4:
    print('you are selected welcome to gamexone')
else:
    print('you are short listed for management')
print('========================Task7.3=======================')
print('1:if u select 1 then these subjects are included arts,drawing,management')
print('2:if uh select 2 then your interest are logical,'
      ' having expertise and interest in programming ,' 'problem solving ,technologies ')
print('3:if your interest in these then you select the 3'
      'included  bio , science , discipline and development of humanity')
a = int(str(input('select the number by your interest:')))
if a==1:
    print('i suggest you to study arts')
elif a==2:
    print('i suggest you to study engineering')
elif a==3:
    print('i suggest you to chhose medical field ')
else:
    print('error')



