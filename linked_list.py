# Реализовать структуру данных связный список

class ListNode:
  #code

class LinkedList:
  #code

node1 = ListNode(2)
node2 = ListNode(5)
node1.next = node2

list = LinkedList(node1)

print(list.head.next.value) # -> 5
list.size() # -> list length: 2
list.clear() # -> None
list.get_last() # -> { value: 5, next: None }
list.get_first() # -> { value: 2, next: { value: 5, next: None } }
