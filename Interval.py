#  File: Interval.py

#  Description: A basic interval class.

#  Student Name: Carla Gonzalez

#  Student UT EID: cig588

#  Course Name: CS 313E

#  Unique Number:

import sys

class IntegerInterval (object):
    # constructor with default values
    def __init__(self, beginning = 0, end = 0):
        self.beginning = beginning
        self.end = end

    # creates a string representation of an Interval
    # returns a string in the form "Beginning: startTime, End: endTime"
    def __str__(self):
        return "Beginning: " +  str(self.beginning) + ", End: " + str(self.end)


    # test for equality between two intervals
    # other is an interval object
    # returns a Boolean
    def __eq__(self, other):
        interval0 = [self.beginning, self.end]
        interval0.sort()
        other_interval = [other.beginning, other.end]
        other_interval.sort()
        
        if interval0 == other_interval:
            return True
        else:
            return False


    # returns the length of this interval
    # returns an integer 
    def __len__(self):
        return (self.end - self.beginning)


    # determine if this interval overlaps with another
    # other is an interval object
    # returns a Boolean
    def overlap(self, other):
        my_list = []
        for i in range(self.beginning, self.end):
            for j in range(other.beginning, other.end):
                if i == j:
                    my_list.append(i)
        if len(my_list) > 0:
            return True
        else:
            return False
            
        
    # determine the time in the intersection of this interval with another
    # other is an interval object
    # returns an Integer
    def intersection(self, other):
        overlapi=[]
        if IntegerInterval.overlap(self, other)  == True:
            for i in range(self.beginning, self.end):
                for j in range(other.beginning, other.end):
                    if i == j:
                        overlapi.append(i)
            return len(overlapi)
        else:
            return 0
            
    # determine the time in the union of this interval with another
    # other is an interval object
    # returns an Integer
    def union(self, other):
        return ((self.end - self.beginning) + (other.end - other.beginning) - IntegerInterval.intersection(self, other))


# do NOT change main, it has been fully completed for you
def main():
    # read the two intervals
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    line1 = line1.split(" ")
    line2 = line2.split(" ")

    interval1 = IntegerInterval(int(line1[0]), int(line1[1]))
    interval2 = IntegerInterval(int(line2[0]), int(line2[1]))

    # print the output
    print(interval1)
    print(interval2)
    print(len(interval1))
    print(len(interval2))
    print(interval1 == interval2)
    print(interval1.overlap(interval2))
    print(interval2.overlap(interval1))
    print(interval1.intersection(interval2))
    print(interval2.intersection(interval1))
    print(interval1.union(interval2))
    print(interval2.union(interval1))

if __name__ == "__main__":
    main()
