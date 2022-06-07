"""
Python Functions and Recursions
"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""
def generateParenthesis(n): 
    return(genP(n))
def genP(n,l=0,r=0,cur="",result=[]): 
        if(n==0):
            #result.append(cur)
            #return(result);
            return([''])
        #print([''])
        else:
            if (l == n & r == n):
                result.append(cur);
                return;

            if (l < n):
                newCurrent = cur + "(";
                genP(n, l + 1, r, newCurrent, result)
        
            if ((r < n) & (l > r)):
                newCurrent = cur + ")";
                genP(n, l, r + 1, newCurrent, result)
            return(result)
        
generateParenthesis(2)
"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""
def isPalindrome(st):
    
    st = st.lower()
    st = ''.join(char for char in st if char.isalnum())
    f=True
    m= len(st)//2
    
    for i in range(m):
        if(st[i] != st[len(st)-i-1]):
            f = False;  
            break; 
    
    if(f):
        return(f)
    else:
        return(f)

isPalindrome("race a car")
