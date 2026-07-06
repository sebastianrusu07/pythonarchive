price = int(input())

p150 = price//150
price%=150
p30 = price//30
price%=30
p15 = price//15
price%=15
p5 = price//5
price%=5
p1 = price

print (p1,p5,p15,p30,p150,sep=" ")