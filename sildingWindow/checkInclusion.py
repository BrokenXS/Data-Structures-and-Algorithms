def checkInclusion(s1: str, s2: str) -> bool:
        # s1 = sorted(s1)
        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         subStr = s2[i : j + 1]
        #         subStr = sorted(subStr)
        #         print(subStr)
        #         if subStr == s1:
        #             return True
        # return False

        if len(s1) > len(s2):
            return False
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                print(f"i={i}, j={j}, count2={count2}")
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    print(f"Found permutation at s2[{i}:{j+1}] = {s2[i:j+1]}")
                    return True
        return False


        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        print('s2Count 1', s2Count)
        print('s1Count 1', s1Count)
        print('origin matches', matches)
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            
            s2Count[index] += 1
            print('right', r)
            print('index right', index)
            print('s2Count right', s2Count)
            print('s1Count right', s1Count)
            if s2Count[index] == s1Count[index]:
                print('s2Count right', s2Count[index])
                print('s1Count right', s1Count[index])
                matches += 1
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1
            print('matches right', matches)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            print('left', l)
            print('index left', index)
            print('s2Count left', s2Count)
            print('s1Count left', s1Count)
            if s2Count[index] == s1Count[index]:
                print('s2Count left', s2Count[index])
                print('s1Count left', s1Count[index])
                matches += 1
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1
            print('matches 2', matches)
            l += 1

        return matches == 26

checkInclusion("ab", "eidbaooo")