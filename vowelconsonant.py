number=input()
if(number=='a'or number=='e' or number=='i' or number=='o' or number=='u' or number=='A'or number=='E' or number=='I' or number=='O' or number=='U'):
    print("vowel")
elif(number>='A' and number<='Z' or number>='a' and number<='z'):
    print("consonant")
else:
    print("invalid")
