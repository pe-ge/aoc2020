from math import inf


class MyLinkedList:

    class MyLinkedNode:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, data):
        self._list = None
        self._nodes = {}
        self.length = 0
        node = None
        max_value = -inf
        for value in map(int, list(str(data))):
            node = self.insert_cup(value, node)
            max_value = max(max_value, value)
        for value in range(max_value+1, 1000000+1):
            node = self.insert_cup(value, node)
        node.next = self._list
        self._list.prev = node

        self.current_cup = self._list

    def insert_cup(self, value, prev):
        self.length += 1
        node = MyLinkedList.MyLinkedNode(value)
        self._nodes[value] = node
        if self._list is None:
            self._list = node
        else:
            prev.next = node
            node.prev = prev

        return node

    def remove_cups(self, num=3):
        cup = self.current_cup
        cups = []
        for _ in range(num):
            cup = cup.next
            cups.append(cup)

        cup.next.prev = self.current_cup
        self.current_cup.next = cup.next

        return cups

    def contains_value(self, removed_cups, value):
        for removed_cup in removed_cups:
            if removed_cup.value == value:
                return True

        return False

    def select_destination_cup(self, removed_cups):
        destination_cup_value = self.current_cup.value - 1
        if destination_cup_value == 0:
            destination_cup_value = self.length
        while self.contains_value(removed_cups, destination_cup_value):
            destination_cup_value -= 1
            if destination_cup_value == 0:
                destination_cup_value = self.length

        return self._nodes[destination_cup_value]

    def mix(self):
        removed_cups = cups.remove_cups()
        destination_cup = self.select_destination_cup(removed_cups)

        destination_cup.next.prev = removed_cups[-1]
        removed_cups[-1].next = destination_cup.next
        destination_cup.next = removed_cups[0]
        removed_cups[0].prev = destination_cup

        self.current_cup = self.current_cup.next

    def get_answer(self):
        current_cup = self.current_cup
        while current_cup.value != 1:
            current_cup = current_cup.next

        return current_cup.next.value * current_cup.next.next.value


cups = MyLinkedList(653427918)
for idx in range(10000000):
    cups.mix()

print(cups.get_answer())
