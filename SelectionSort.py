from SwapList import *
from BaseSort import *
class SelectionSort(BaseSort):
    #Add in your bubble sorting method here
    def selectionSort(self, list):
        print(list)
#Empty list
l = []

selection = SelectionSort()
selection.populate(l)
sl = SwapList()
sl.swap(l)

selection.selectionSort(l)

print(l)