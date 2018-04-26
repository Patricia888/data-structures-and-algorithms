from .queue import Queue


def print_level_order(tree):
    '''print values of all nodes in level order of K-ary tree'''
    queue = Queue()
    next_queue = Queue()
    list_of_all_values = ''

    queue.enqueue(tree.root)

    while queue or next_queue:
        if not queue:
            queue, next_queue = next_queue, queue
            list_of_all_values += '\n'

        current = queue.dequeue()
        list_of_all_values += f'{current.val} '
        for child in current.children:
            next_queue.enqueue(child)

    return list_of_all_values
