# Challenge Summary
<!-- Short summary or background information -->

.append(value) which adds a new node with the given value to the end of the list
## Challenge Description
<!-- Description of the challenge -->
.append(value) which adds a new node with the given value to the end of the list
.insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
.insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
1. Can successfully instantiate an empty linked list.
    * list = LinkedList() -> None
2. Can properly insert into the linked list.
    * list.insert(2) -> { 2 } -> NULL
3. The head property will properly point to the first node in the linked list.
    * print (list.head.value) -> 2
4. Can properly insert multiple nodes into the linked list.
    * list.insert(4)
    * list.insert(5)
    * list.insert(6)
5. Will return true when finding a value within the linked list that exists.
    * list.includes(5) -> True
6. Will return false when searching for a value in the linked list that does not exist.
    * list.includes(20) -> False
7. Can properly return a collection of all the values that exist in the linked list.
    * print(list) -> "{ 6 } -> { 5 } -> { 4 } -> { 2 } -> NULL"


## Solution
<!-- Embedded whiteboard image -->
![Getting Started](IMG_20201207_011706.jpg./2/to/img.jpg)
