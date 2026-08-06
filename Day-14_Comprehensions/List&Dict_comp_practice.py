# #Reverse each word in a list
# list1=['rohit','sanjay','rahul','ravi']
# list1=[i[::-1] for i in list1]
# print(list1)

# # extract vovel from a string
# string="hello world"
# list2=[ch for ch in string if ch in 'aeiou']
# print(list2)

# # i>j pair from 1-10
# list3=[(i,j) for i in range(10) for j in range(10) if i>j]
# print(list3)
# # i==j pair from 1-10
# list4=[(i,j) for i in range(10) for j in range(10) if i==j]
# print(list4)

# #when a dice or a coin is tossed 10 times, the possible outcomes are
# coin=['H','T']
# dice=[1,2,3,4,5,6]
# result=[(i,j) for i in coin for j in dice]
# result1=[(i,j) for i in coin for j in dice if i=="H"] # it prints only the Head is appeared in the outcome
# result2=[(i,j) for i in coin for j in dice if i=="H" and j==5] # it returns only the Head and 5  appeared in the outcome
# result3=[(i,j) for i in coin for j in dice if i=="H" or j==5] # it returns only the Head or 5  appeared in the outcome
# result4=[(i,j) for i in coin for j in dice if i=="H" and i=='T' or j==5] # it returns when Head and Tail or 5  appeared in the outcome
# print(result)
# print(len(result))
# print(result1)
# print(len(result1))
# print(result2)
# print(len(result2))
# print(result3)
# print(len(result3))
# print(result4)
# print(len(result4))

# #Matrix transpose -- make rows as columns and columns as rows
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# list5=[]
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         list5.append(matrix[i][j])
# print(list5)

matrix = [[1,2,3],[4,5,6]]
transpose = [j for i in matrix for j in i]
new=[[i for i in range(len(transpose))]]
print(transpose)
print(new)
