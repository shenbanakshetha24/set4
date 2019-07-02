c=input()
f=0
for i in range(len(c)):
 if(c[i].isdigit() or c[i].isalpha() or c[i]==(" ")):
  continue
 else:
  f+=1
print(f)
