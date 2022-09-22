class Node(object):
    def __init__(self, item, pointer):
        self.item = item
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def empty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    def pop(self):
        if self.empty():
            raise IndexError('stack is empty')
        item = self.head.item
        self.head = self.head.pointer
        self.size -= 1
        return item

    def peek(self):
        if self.empty():
            raise IndexError('stack is empty')
        return self.head.item

    def __len__(self):
        return self.size



if __name__ == '__main__':
    stack = Stack()
    stack.push(7)
    stack.push(5)
    stack.push(4)
    stack.pop()
    stack.push(6)
    stack.pop()
    while(stack.empty() != True):
        print(stack.peek())
        stack.pop()


'''
1. 노드
class Node(object):
    def __init__(self, item, pointer):
        self.item = item
        self.pointer = pointer

2. 스택
class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

1) empty()
def empty(self):
    return not bool(self.head)

2) push(item)
def push(self, item):
    self.head = Node(item, self.head)
    self.size += 1

3) pop()
def pop(self):
    if self.empty():
        raise IndexError('stack is empty')
    item = self.head.item
    self.head = self.head.pointer
    self.size -= 1
    return item

4) peek()
def peek(self):
    if self.empty():
        raise IndexError('stack is empty')
    return self.head.item

5) __len__()
def __len__(self):
    return self.size


다른 방법
class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
    """빈 스택 하나를 생성합니다"""
        self._data = []
    def __len__(self):
    """스택에 저장된 요소의 개수를 반환합니다"""
        return len(self._data)

    def push(self, e):
    """스택에 요소를 추가합니다"""
        self._data.append(e)

    def is_empty(self):
    """스택이 비어있으면 True를 반환합니다.""" 
      return len(self._data) == 0
    def pop(self):
    """가장 마지막에 들어온 요소를 반환하고 제거합니다"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
    """가장 마지막에 들어온 요소를 제거하지 않고 반환합니다"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
'''