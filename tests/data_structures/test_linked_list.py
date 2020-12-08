from data_structures_and_algorithms.data_structures.linked_list.linked_list import  Node, LinkedList
import pytest

def test_list_creation():
  actual = LinkedList()
  assert actual.head == None

def test_insert_method():
  lst_one = LinkedList()
  lst_one.insert(1)
  lst_one.insert(2)
  lst_one.insert(3)

  assert lst_one.head.value == 3
  assert lst_one.head.next.value == 2
  assert lst_one.head.next.next.value == 1

def test_includes_method():
  lst_two = LinkedList()
  lst_two.insert('apples')
  lst_two.insert('pickles')
  lst_two.insert('chips')

  assert lst_two.includes('pickles') == True
  assert lst_two.includes('whales') == False


  

def test_to_string_method():
  lst_three = LinkedList()
  lst_three.insert(1)
  lst_three.append(2)
  lst_three.append(3)
  lst_three.append(4)
  lst_three.append(5)

  actual = lst_three.__str__()
  expected = 'Node: 1 Node: 2 Node: 3 Node: 4 Node: 5 '
  assert actual == expected

def test_append():
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  assert lst_four.head.next.value == 'banana'

def test_insert_before():
  lst_five = LinkedList()
  lst_five.insert(1)
  lst_five.append(2)
  lst_five.append(3)
  lst_five.append(5)
  lst_five.insertBefore(5, 4)

  assert lst_five.head.next.next.value == 3
  assert lst_five.head.next.next.next.value == 4
  assert lst_five.head.next.next.next.next.value == 5

def test_insert_after():
  lst_six = LinkedList()
  lst_six.insert(1)
  lst_six.append(2)
  lst_six.append(3)
  lst_six.append(4)
  lst_six.append(6)
  lst_six.insertAfter(4, 5)

  assert lst_six.head.next.next.value == 3
  assert lst_six.head.next.next.next.value == 4
  assert lst_six.head.next.next.next.next.value == 5
  assert lst_six.head.next.next.next.next.next.value == 6



def test_nth_greater_than():
 list = LinkedList()
 list.append(1)
 list.append(2)
 list.append(3)
 with pytest.raises(Exception):
    assert list.nthFromEnd(8)
# 	initialList = LinkedList([5,6,7,8])
# 	assert initialList.nthFromEnd(4) == 5

def test_nth_negative():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    with pytest.raises(Exception):
        assert list.nthFromEnd(-30)


def test_nth_list_of_one():
    list = LinkedList()
    list.append(1)
    assert list.nthFromEnd(0) == 1

def test_nth_average_use():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    assert list.nthFromEnd(1) == 2