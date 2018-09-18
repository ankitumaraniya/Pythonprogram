a=(input())
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up=[x.upper() for x in (alphabet)]
if(a in alphabet or a in up):
    print("Alphabet")
else:
    print("No")
