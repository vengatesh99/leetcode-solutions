# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    
    def findCelebrity(self, n: int) -> int:
        candidate_celeb = 0
        for i in range(1,n):
            if i!=candidate_celeb:
                if knows(candidate_celeb,i):
                    candidate_celeb = i
        for i in range(0,n):
            if i != candidate_celeb:
                if knows(candidate_celeb,i) or not knows(i,candidate_celeb):
                    return -1
        return candidate_celeb