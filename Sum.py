Tuple1=(10,20,30,40,50,60,70)

class Sum:
    def two_sums(self,nums,target):
        dic1={}
        for i,num in enumerate(nums):
            if target-num in dic1:
                return dic1[target-num],i
            dic1[num]=i
value=int(input("Enter the sum of for which you want to search for this value"))

print(Sum.two_sums(Tuple1,value))



        
