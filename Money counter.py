#Kavilan Naidoo
#19-09-2014
#Money counter

value=int(input("please enter an amount of money: "))
twenty=value//20
remainder= value%20
ten=remainder//10
remainder=remainder%10
five=remainder//5
remainder=remainder%5
two=remainder//2
remainder=remainder%2
one=remainder//1
remainder=remainder%1
print("""you will need:
{0} twenty pound note(s),
{1} ten pound note(s),
{2} five pound note(s),
{3} two pound coin(s),
{4} one pound coin(s).""".format(twenty,ten,five,two,one))
