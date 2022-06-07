 #!/usr/bin/python
"""
Python  Functions
"""

# Write a function unique_list() that takes a list and returns a new list with unique elements of the first list.
# unique_list: (1,2,3,3,3,3,4,4,5)
def unique_list(list):
   unique =[]
   for i in list:
     if i not in unique:
       unique.append(i)
   #counts =list.count()
   
   return(unique)
   


#Write a function multiply() to multiply all giving numbers in a list.
#Sample List : (9, 2, 3, -6, 7)
#Expected Output : -2268
def multiply(list):
  prod = 1
  for i in list:
    prod = prod * i

  return(prod)


# Write a function get_average() that takes an arbitrary number of arguments and returns the average of them
# Number of arguments : (5,6,8,10,31)
# Expected Output : 12
def get_average(*args):
  l =len(args)
  sum = 0
  for i in args:
    sum = sum + i
  avg = sum / len(args)
  return(avg)

