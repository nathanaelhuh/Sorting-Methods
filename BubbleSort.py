from SwapList import *
from BaseSort import *
class BubbleSort(BaseSort):
    #Add in your bubble sorting method here
    def bubbleSort(self, list):
        for j in list:
            for i in list:
                if i < len(list)-1:
                    if list[i] > list[i+1]:
                        temp = list[i]
                        list[i] = list[i+1]
                        list[i+1] = temp


#Empty list
l = []
print(l)

bubble = BubbleSort()
bubble.populate(l)
print(l)

swap = SwapList()
swap.swap(l)
print(l)
bubble.bubbleSort(l)
print(l)