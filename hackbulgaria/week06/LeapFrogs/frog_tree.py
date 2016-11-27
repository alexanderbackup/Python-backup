from collections import deque
import re


def frog_string(n):
    return '>'*n + '_' + '<'*n, '<'*n + '_' + '>'*n


class Node: # Node == Move
    def __init__(self, data):
        self.data = data
        self.next = []
        self.prev = None

class LeapFrogs:

    def __init__(self, frogs_quantity):
        start_end_result = frog_string(frogs_quantity)
        self.frogs_start = start_end_result[0] # '>>>_<<<' Example
        self.frogs_end = start_end_result[1] # '<<<_>>>' Example
        self.root = None
        self.stop_iter = False
        
    def add_move(self, root=None):
        if not root:
            self.root = Node(self.frogs_start)
            cur = self.root
        else:
            cur = root
        prev = cur.prev
        smth = self.valid_positions(cur)
        cur.next = [Node(i) for i in smth]
        while cur.next:
            for _node in cur.next:
                prev = cur
                cur = _node
                cur.prev = prev
                if self.frogs_end == _node.data:
                    break
                self.add_move(cur)


    def valid_positions(self, cur_position):
        res = set()
        pos = cur_position.data
        val = pos.index('_') # validator
        if pos[val] != pos[0]:
            if pos[val-1] and pos[val-1] == '>':
                res.add(re.sub('>_', '_>', pos))
        if pos[val] != pos[0] and pos[val] != pos[1]:
            if pos[val-2] and pos[val-2] == '>':
                temp = pos[val-1]
                res.add(re.sub('>'+temp+'_', '_'+temp+'>', pos))
        if pos[val] != pos[-1]:
            if pos[val+1] and pos[val+1] == '<':
                res.add(re.sub('_<', '<_', pos))
        if pos[val] != pos[-1] and pos[val] != pos[-2]:
            if pos[val+2] and pos[val+2] == '<': 
                temp = pos[val+1]
                res.add(re.sub('_'+temp+'<', '<'+temp+'_', pos))
        return res
    
    def find_answer(self, current_node, answer):
        self.result = []
        self.stop_iter = False
        return self._find_answer(current_node, answer)
        
    def _find_answer(self, current_node, answer):
        if self.stop_iter:
            return True
        prev = current_node
        for cur in current_node.next:
            cur.prev = prev
            if cur.data == answer:
                self.stop_iter = True
                temp = cur
                while temp.prev:
                    self.result.append(temp.data)
                    temp = temp.prev
                self.result.append(temp.data)
                return True
            check = self._find_answer(cur, answer)
            if check:
                return check


foo = LeapFrogs(10)
foo.add_move(foo.root)
foo.find_answer(foo.root, foo.frogs_end)
















