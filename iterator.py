class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

it = MyIterator(5)
for num in it:
    print(num)
#In this example, the MyIterator class implements the iterator protocol by defining the __iter__()
# and __next__() methods. The __iter__() method returns the iterator object itself, 
# and the __next__() method produces the next value in the sequence, 
# or raises a StopIteration exception if there are no more values.

#When the MyIterator object is used in a for loop, 
# Python calls the __iter__() method to get the iterator object, 
# and then calls the __next__() method repeatedly to get each value in the sequence.