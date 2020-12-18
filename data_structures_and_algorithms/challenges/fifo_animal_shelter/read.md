
'''
Required Features:
- [x] Create a class called AnimalShelter which holds only dogs and cats.
- [x] The shelter operates using a first-in, first-out approach.
- [x] Implement the following methods:
- [x] enqueue(animal): adds animal to the shelter.
- [x] animal can be either a dog or a cat object.
- [x] dequeue(pref): returns either a dog or a cat.
- [x] If pref is not "dog" or "cat" then return null.
- [x] Stretch: If a cat or dog isn’t preferred, return whichever animal has been waiting in the shelter the longest.
'''


# Animal Shelter (Code Challenge 12)
Come get a new dog or cat at our First In - First Out Animal Shelter!

## Challenge
Create a First In - First Out animal shelter making use of queues, classes, and objects.  Handle cats and dogs seperately and see who has been there the longest.

## Approach & Efficiency
A class was defined for the shelter.  It contained methods for adding animals of either dog or cat class to the shelter.  The shelter returns users their preference of cat or dog based on a first in, first out approach.  Two seperate queues are used to keep the cats and dogs in order and to prevent any dogs from chasing the cats.  Both cats and dogs are a subclass of the animal class.  If a visitor requests an animal and does not provide a preference, they are given the animal that has been in the shelter the longest.

## Solution
[Picture of Whiteboard Exercise](https://raw.githubusercontent.com/MsDiala/data-structures-and-algorithms-python/fifo-animal-shelter/data_structures_and_algorithms/challenges/fifo_animal_shelter/whiteboard.png)

-----------------------------------------------------------------



https://github.com/MsDiala/data-structures-and-algorithms-python/pull/13
