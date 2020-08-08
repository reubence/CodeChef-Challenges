n = int(input().strip())
string = []
substring = []
for i in range(n):
    string.append(str(input().strip()).lower())
    substring.append(str(input().strip()).lower())

def isAnagram(str1, str2):
    if len(str1) == 1:
        return(print(str1))
    else:
        for char in str2:
            str1 = str1.replace(char,'',1)
        new_str = ''.join(sorted((str1)))
        try:
            for i in range(len(new_str)):
                # print(i)
                if ord(new_str[i])<=ord(str2[0]) and ord(new_str[i+1])>ord(str2[0]):
                    return(print(new_str[:i+1] + str2 + new_str[i+1:]))
                    break
        except:
            return(print(new_str + str2))

for i,x in zip(string,substring):
    isAnagram(i,x)




