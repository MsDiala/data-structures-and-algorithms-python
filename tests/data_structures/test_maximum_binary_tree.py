import pytest
from data_structures_and_algorithms.data_structures.tree.tree import Ktree
from data_structures_and_algorithms.data_structures.BinaryTree.maximum_binary_tree  import find_maximum_value

def test_invalid_arg():
    '''Test invalid parameter'''
    with pytest.raises(TypeError):
        find_maximum_value(4)

def test_empty_Ktree():
    '''Test an empty Ktree has no max value'''
    assert find_maximum_value(Ktree()) is None

def test_single_Ktree():
    '''Test single valued Ktree'''
    assert find_maximum_value(Ktree([1])) == 1

def test_multi_Ktree():
    '''Test multi-valued non-balanced Ktree'''
    l = [5,2,15,33,1,8,7,4,2,66,5,1,0,-2]
    b = Ktree(l)
    assert find_maximum_value(b) == 66