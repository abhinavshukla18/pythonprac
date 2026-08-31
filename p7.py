#Problem 1
# Print numbers from 1 to 100. Print Fizz if divisible by 3, Buzz if divisible by 5, FizzBuzz if
# divisible by both, otherwise print the number.
# Uses: Loop, if-elif-else, % operator.

#for i in range(0,51):
#    if i%3==0 and i%5==0:
#        print("FIZZBUZZ")
#    elif i%3==0:
#        print("FIZZ")
#    elif i%5==0:
#        print("BUZZ")
#    else:
#        print(i)


#Problem 2
#Sum & Average of a List
#Find the sum and average of a list without using sum() or statistics.mean().
#Uses: Lists, Loop, Variables

#marks = [85, 90, 72, 60, 95]
#sum=0
#for ele in marks:
#    sum=sum+ele
#avg = sum/len(marks)
#print(sum)
#print(avg)



#Problem 3 
# Find the Largest Number
#Find the largest element in a list without using max().
#Uses: Lists, Loop, if.

#nums = [23, 67, 12, 89, 45]
#largest=0
#for i in nums:
#    for j in nums:
#        if i>j:
#            largest = i
#        else:
#            if j>i:
#                largest = j
#
#print("The lagrest number is: ", largest)


#SORTING A LIST:-
nums = [5, 2, 9, 1, 7]
for i in nums:
    for j in nums:
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            continue

print(nums)

#das all