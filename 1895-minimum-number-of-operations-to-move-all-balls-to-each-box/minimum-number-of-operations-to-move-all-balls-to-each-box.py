class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0 for _ in range(len(boxes))]
        ones = set()
        for i in range(len(boxes)):
            if boxes[i]=='1':
                ones.add(i)
        def calculate(index):
            sum = 0
            for value in ones:
                sum+=abs(value-index)
            return sum
        for i,num in enumerate(boxes):
            ans[i] = calculate(i)
        return ans
        