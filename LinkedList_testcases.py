from LinkedList import *

#Test insert at a given position

#Initialize Linked List
LL = LinkedList()

#Insert values into linked lists
LL.insert(100)
LL.insert(-13)
LL.insert(153)
LL.insert(77)

# print(LL.get_size())
# print(LL.get_tail().val)


# Test insert at position
LL.insert_at_position(5,2)
LL.insert_at_position(3,5)
print(LL.head.val)
print(LL.get_size())
#LL.insert_at_position(-46, LL.get_size())



print(LL.head.next.next.next.next.next.val)
#print(LL.head.next.next.val)
#print(LL.head.val)

# print(LL.get_size())

# LL.remove_at_position(2)
# print(LL.head.next.next.val)

#print(remove_at_position)

