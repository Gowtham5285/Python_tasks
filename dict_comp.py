# result = ""

# def allVowels(ch):
#     global result      
#     result += ch       
#     return result      

# a = {"name1": "vamsi", "name2": "ravi"}

# res = {allVowels(j) for i in a for j in a[i] if j in "aeiouAEIOU"}

# print(result)
def evenNum(eN):
    print(eN,"is even number")
nums=[1,2,3,4,5]
res=[evenNum(i) for i in nums if i%2==0]