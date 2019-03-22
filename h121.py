def longestPalindrome(abi):
        amu = ""
        for i in range(len(abi)):
            for j in range(len(abi)-1,i-1,-1):
                if(abi[i]==abi[j]):
                    m=abi[i:j+1]
                    if(m ==m[::-1]):
                        if(len(amu) <= len(m)):
                            amu = m
        return amu
abi=str(raw_input())
print(longestPalindrome(abi))
