
# Challenge Description
A function called multi_bracket_validation(input) Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : () Square Brackets : [] Curly Brackets : {}
# Approach & Efficiency

# Solution

# problem Domain
 write a function that takes string as an argument . Return a boolean. True if the brackets (),{},[] are balanced , False if the bracketsare not balanced.

### Algorithm🥇
- iterate through the array to check for brackets 
- ([{ increment a counter 
- }]) decrement a counter 

### Pseudo Code 
- Algorithm MultiBracketValidation(argument)
- Input : string
- Output : boolean
- Declare
         "(" counter = 0
         "{" counter = 0 
         "[" counter = 0
- Declare 
         list : split string
         for i in list do 
           if i is "("
               "(" counter ++ 
            
           if i is "{"
               "{" counter ++ 

           if i  is "["
               "[" counter ++

           if i is ")"
               ")" counter -- 
            
           if i is "}"
               "}" counter -- 
           if i  is "]"
               "]" counter --
        final counter = "(" counter + "{" counter + "["
        if final counter == 0 
            return true
        else 
           return false 

### Big O 
   Time O(n)
   space O(n)