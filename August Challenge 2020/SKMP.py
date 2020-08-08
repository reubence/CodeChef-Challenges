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
        if str2[0] not in new_str:

            try:
                for i in range(len(new_str)):
                    # print(i)
                    if ord(new_str[i])<=ord(str2[0]) and ord(new_str[i+1])>ord(str2[0]):
                        return(print(new_str[:i+1] + str2 + new_str[i+1:]))
                        break
            except:
                return(print(new_str + str2))
        else:
            yos = new_str[:new_str.index(str2[0])] + str2 + new_str[new_str.index(str2[0]):]
            try:
                for i in range(len(new_str)):
                    # print(i)
                    if ord(new_str[i])<=ord(str2[0]) and ord(new_str[i+1])>ord(str2[0]):
                        return(print(min(new_str[:i+1] + str2 + new_str[i+1:],yos)))
                        break
            except:
                return(print(new_str + str2))
for i,x in zip(string,substring):
    isAnagram(i,x)




#
# from copy import deepcopy
#
# for _ in range(int(input())):
#     s = list(input())
#     p = list(input())
#     for i in p:
#         s.remove(i)
#     s.sort()
#     ne = deepcopy(s)
#     ne.append(p[0])
#     ne = sorted(ne,reverse=True)
#     print(ne)
#     print(s)
#     if p[0] not in s:
#         print(''.join(s[0:len(ne) - ne.index(p[0]) - 1]) +''.join(p) +''.join(s[len(ne) - ne.index(p[0])-1:]))
#     else:
#         air = ''.join(s[0:s.index(p[0])]) + ''.join(p) + ''.join(s[s.index(p[0]):])
#         # print(air)
#         print(min(air,''.join(s[0:len(ne) - ne.index(p[0]) - 1]) +''.join(p) +''.join(s[len(ne) - ne.index(p[0])-1:])))
#
#
