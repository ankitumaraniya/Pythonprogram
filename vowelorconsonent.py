a=(input())
vowel=['a','e','i','o','u']
vow=[x.upper() for x in (vowel)]
consonent=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
const=[y.upper() for y in (consonent)]
if(a in vowel or a in vow):
    print("Vowel")
elif(a in consonent or a in const):
    print("Consonent")
else:
    print("invalid")
