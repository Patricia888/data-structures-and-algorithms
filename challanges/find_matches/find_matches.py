from .k_tree import KTree, Node


def find_matches(ktree_input, target_val):
    """
    Traverse through a tree and return a collection of node which have the
    matching target value.
    """
    try:
        output_list = []
        ktree_input.breadth_first_traversal(
            lambda x: check_if_matches(target_val, x, output_list))
        return output_list
    except AttributeError:
        print('Arguments must be 1. ktree and 2. value of any datatype')
        return False


def check_if_matches(target_val, node, output_list):
    """
    Check to see if input node's val matches target val and appends if so.
    """
    if node.val == target_val:
        output_list.append(node)
