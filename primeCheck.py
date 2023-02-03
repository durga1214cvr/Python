f=True;
num=7;
for i in num-1:
    if num%2==0: f=False; break;
    num-=1;
    if(num==1): break;

    if f: print("prime");

    else: print("not prime");
