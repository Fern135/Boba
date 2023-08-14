import math

class Search:
    def __init__(self, lys=None, val=None):
        if lys is not None and val is not None:
            self.lys = lys #  where we're searching
            self.val = val #  what's being searched

    def __del__(self) -> None:
        if self.lys is not None and self.val is not None:
            self.lys = None
            self.val = None
    

    def setList(self, lys): # where we're searching
        self.lys = lys

    
    def setVal(self, val): #  what's being searched
        self.val = val


    def getList(self): # getting the list being searched
        return self.lys

    
    def getVal(self): # getting the value being searched
        return self.val


    def Linear_Search(self):
        for i in range(len(self.lys)):
            if self.lys[i] == self.val:
                return i
        return -1


    def Binary_Search(self):
        first = 0
        last = len(self.lys) - 1
        index = -1
        while first <= last and index == -1:
            mid = (first + last) // 2
            if self.lys[mid] == self.val:
                index = mid
            else:
                if self.val < self.lys[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return index


    def Jump_Search (self):# self.val it's what's being searched in the self.lys
        length = len(self.lys)
        jump = int(math.sqrt(length))
        left, right = 0, 0
        while left < length and self.lys[left] <= self.val:
            right = min(length - 1, left + jump)
            if self.lys[left] <= self.val and self.lys[right] >= self.val:
                break
            left += jump
        if left >= length or self.lys[left] > self.val:
            return -1
        right = min(length - 1, right)
        i = left
        while i <= right and self.lys[i] <= self.val:
            if self.lys[i] == self.val:
                return i
            i += 1
        return -1


    def Fibonacci_Search(self):# self.val it's what's being searched in the self.lys
        fibM_minus_2 = 0
        fibM_minus_1 = 1
        fibM = fibM_minus_1 + fibM_minus_2

        while (fibM < len(self.lys)):
            fibM_minus_2 = fibM_minus_1
            fibM_minus_1 = fibM
            fibM = fibM_minus_1 + fibM_minus_2

        index = -1

        while (fibM > 1):
            i = min(index + fibM_minus_2, (len(self.lys)-1))
            if (self.lys[i] < self.val):
                fibM = fibM_minus_1
                fibM_minus_1 = fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
                index = i
            elif (self.lys[i] > self.val):
                fibM = fibM_minus_2
                fibM_minus_1 = fibM_minus_1 - fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
            else :
                return i

        if(fibM_minus_1 and index < (len(self.lys)-1) and self.lys[index+1] == self.val):
            return index+1

        return -1


    def Exponential_Search(self):
        if self.lys[0] == self.val:
            return 0
        
        index = 1
        while index < len(self.lys) and self.lys[index] <= self.val:
            index = index * 2
            
        return self.Binary_Search()  # Call Binary_Search without arguments



    def Interpolation_Search(self):# self.val it's what's being searched in the self.lys
    # self.val = 6,
    # low = 0,
    # high = 7,
    # self.lys[low] = 1,
    # self.lys[high] = 8,
    # index = 0 + [(6-1)*(7-0)/(8-1)] = 5

        low = 0
        high = (len(self.lys) - 1)
        while low <= high and self.val >= self.lys[low] and self.val <= self.lys[high]:
            index = low + int(((float(high - low) / ( self.lys[high] - self.lys[low])) * ( self.val - self.lys[low])))
            if self.lys[index] == self.val:
                return index
            if self.lys[index] < self.val:
                low = index + 1
            else:
                high = index - 1
        return -1
