import random
class SwapList:
    def swap(self, list):
        for i in range(0, len(list)-1):
            randNum = random.randint(0, len(list)-1)
            temp = list[i]
            list[i] = list[randNum]
            list[randNum] = temp


sl = SwapList()
l = []
for i in range(0, 100):
    l.append(i)
print(l)
sl.swap(l)
print(l)