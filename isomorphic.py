s1,s2=raw_input().split(' ')
c=0
d=0
i=0
if(len(s1)==len(s2)):
        if(s1[i]==s1[i+1]):
            c=c+1
        if(s2[i]==s2[i+1]):
            d=d+1
        if(c!=d):
            print('no')
        if c==d:
            print('yes')
        
