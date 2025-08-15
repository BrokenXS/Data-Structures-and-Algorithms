from typing import List

temperatures = [30,38,30,36,35,40,28]
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []  # Monotonic decreasing stack to store indices

    for i, temp in enumerate(temperatures):
        # While the current temperature is warmer than the temperature at the stack's top index
        while stack and temperatures[stack[-1]] < temp:
            print(stack[-1])
            print(temperatures[stack[-1]])
            print(temp)
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
            print(result)
        stack.append(i)
        
    return result
#dailyTemperatures(temperatures) 

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = [[p,s] for p,s in zip(position, speed)]
    stack = []  # Monotonic decreasing stack to store indices
    
    pair.sort(reverse = True)
    for p,s in pair:
        stack.append((target - p)/s)
        if len(stack) >=2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
carFleet(target, position, speed)


def calPoints(operations: List[str]) -> int:
    stack = []
    for op in operations:
        if op == "+":
            if len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        elif op == "D":
            if stack:
                stack.append(2 * stack[-1])
        elif op == "C":
            if stack:
                stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)