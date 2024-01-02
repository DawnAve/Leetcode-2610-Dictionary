class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        answer = []
        temp = []
        for i in dic:
            if dic[i] >0:
                temp.append(i)
                dic[i] -=1
        answer.append(temp)
        temp = []
        while any(dic.values()):
            for i in dic:
                if dic[i] >0:
                    temp.append(i)
                    dic[i] -=1
            answer.append(temp)
            temp = []
        return answer
