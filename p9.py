#Q1. Use set comprehension to build the set of all distinct name lengths:- 
#names = ["Ravi", "Amit", "Sara", "Neha", "Ram"]
#len_set = {len(ele) for ele in names}
#print(len_set)


#Q2. Create a dictionary for numbers 1-6 as key with the values as squares of the numbers:-
#sq = {n:n*n for n in range(1,7,1)}
#print(sq)


#Q3. use list comp to build sq of no. 1-10. then make a second version with only even no.

#num = {n:n*n for n in range(1,11,1)}
#even_num = {m:m*m for m in range(1,11,1) if m%2==0}
#print(num)
#print(even_num)


#Q4. use dict comp to build cubes for no. 1-6, then print cube of 4

#tab = {n:n*n*n for n in range(1,7,1)}
#print(tab[4])
#print(tab)


#word = input("Enter a word: ")
#vowels = {char for char in word.lower() if char in "aeiou"}
#print("Unique Vowels: ", vowels)