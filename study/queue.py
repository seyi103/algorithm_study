from LinkedList import DoubleLinkedList


class Queue(object):
    def __init__(self):
        self.queue = DoubleLinkedList()

    def empty(self):
        return self.queue.empty()

    def enqueue(self, item):
        self.queue.append(item)

    def deque(self):
        return self.queue.popleft()

    def __str__(self):
        return self.queue.__str__()

    def __len__(self):
        return len(self.queue)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(7)
    q.enqueue(5)
    q.enqueue(4)
    q.deque()
    q.enqueue(6)
    q.deque()

    while (q.empty() != True):
        print(q)
        q.deque()