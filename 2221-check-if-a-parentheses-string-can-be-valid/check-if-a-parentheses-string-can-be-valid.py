class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        lock, unlock = [],[]

        for i,ch in enumerate(s):
            if locked[i] == '1':
                if ch == ')':
                    if len(lock) == 0:
                        if len(unlock) == 0:
                            return False
                        unlock.pop()
                    else:
                        lock.pop()
                else:
                    lock.append(i)
            else:
                unlock.append(i)
        j = len(unlock)-1
        i = len(lock)-1
        while len(lock)>0:
            if len(unlock) == 0:
                return False
            if lock[-1] < unlock[-1]:
                unlock.pop()
                lock.pop()
            else:
                return False
        return len(unlock)%2 == 0
        
            