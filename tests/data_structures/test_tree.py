  
import pytest
from data_structures_and_algorithms.data_structures.tree.tree import Ktree 
from data_structures_and_algorithms.data_structures.tree.tree import Node as nd


@pytest.fixture
def empty_Ktree():
    """make empty Ktree"""
    return Ktree()


@pytest.fixture
def node():
    """make node"""
    return nd(5)
 

@pytest.fixture
def small_Ktree():
    return Ktree([4, 3, 3.5, 2, 5, 6, 7])


def test_constractor(empty_Ktree):
    """test constarctor"""
    assert empty_Ktree.root is None


def test_node(node):
    """test node object"""
    assert node.right is None
    assert node.left is None


def test_value_of_node(node):
    """test repr and str of node"""
    assert node.val == 5


def test_insert_empty(empty_Ktree):
    """insert in empty Ktree"""
    empty_Ktree.insert(5)
    assert empty_Ktree.root.val == 5


def test_insert_empty_two(empty_Ktree):
    """insert two items"""
    empty_Ktree.insert(3)
    empty_Ktree.insert(10)
    assert empty_Ktree.root.val == 3
    assert empty_Ktree.root.right.val == 10
    assert empty_Ktree.root.left is None


def test_repr_small_Ktree(small_Ktree):
    """test repr of small Ktree"""
    assert small_Ktree.root.val == 4
    assert small_Ktree.root.right.val == 5


def test_insert_for_small_Ktree(small_Ktree):
    """test insert in small Ktree"""
    small_Ktree.insert(1)
    small_Ktree.insert(1.5)
    assert small_Ktree.root.left.val == 3
    assert small_Ktree.root.right.val == 5


def test_inorder_traverse(small_Ktree):
    """test in order tarversal"""
    a = []
    small_Ktree.in_order(a.append)
    assert a == [2, 3, 3.5, 4, 5, 6, 7]


def test_pre_order(small_Ktree):
    """test preorder traversal"""
    a = []
    small_Ktree.pre_order(a.append)
    assert a == [4, 3, 2, 3.5, 5, 6, 7]


def test_post_order(small_Ktree):
    """test preorder"""
    a = []
    small_Ktree.post_order(a.append)
    assert a == [2, 3.5, 3, 7, 6, 5, 4]