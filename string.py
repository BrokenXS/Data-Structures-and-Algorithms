from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    # for i in range(len(strs[0])):
    #     for s in strs:
    #         if i == len(s) or s[i] != strs[0][i]:
    #             return s[:i]
    #     print(strs[0])
        
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                print(i)
                print(s[:i])
                return s[:i]
    print(strs)
    return strs[0]    
    
strs = ["dance","dag","danger","damage"]

longestCommonPrefix(strs)