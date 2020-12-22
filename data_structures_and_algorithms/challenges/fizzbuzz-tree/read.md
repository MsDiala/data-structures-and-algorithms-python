# problrm Domain 

write a function called FizzBuzzTree which takes BST as an argument of valur of node divisble by 3 , change it to fizz , and by 5 change it to buzz 

# Algorithm 
if a node vakue div by 3 and 5 return fizzbuzz

if divisble by 3 return fizz

if div by 5 return buzz

return BST

# Pusodu Code 

Input : BST
Output : BST

Declre isDiv(Node val)
if node.val%15=0
    Node.val=FizzBizz
elif Node.val%3 =0
    Node.val=Fizz
elif Node.val%5=0
    Node.val='Buzz'

BST.inorder(isDiv)

return bst

# Big O
log(n)