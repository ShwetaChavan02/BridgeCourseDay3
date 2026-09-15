#write a program to calculate the avergae of a given list
l = [10, 20, 30, 40, 50]
sum = 0
for n in l:
    sum += n  
average = sum / len(l)
print("The average of the given list is:", average)
