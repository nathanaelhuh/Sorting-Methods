import random
class SwapList:
    def swap(self, list):
        for i in range(0, len(list)-1):
            randNum = random.randint(0, len(list)-1)
            temp = list[i]
            list[i] = list[randNum]
            list[randNum] = temp