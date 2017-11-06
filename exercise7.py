"""
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""
def find_missing_letter(chars):
    alf = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
    alf = alf.split(',')
    new_list = alf[alf.index(chars[0]): alf.index(chars[-1]) + 1]
    later = list(set(new_list) - set(chars))
    return later[0]


#print(find_missing_letter(['O','Q','R','S']))

def find_missing_letter2(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

print(find_missing_letter(['O','Q','R','S']))