class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node


   

  def swap_nodes(self,val1, val2):
        
      node1_prev = None
      node2_prev = None
      node1 = self.head_node
      node2 = self.head_node

      if val1 == val2:
          print("Elements are the same - no swap needed")
          return

      while node1 is not None:
          if node1.get_value() == val1:
              break
          node1_prev = node1
          node1 = node1.get_next_node()

      while node2 is not None:
          if node2.get_value() == val2:
              break
          node2_prev = node2
          node2 = node2.get_next_node()

      if (node1 is None or node2 is None):
          print("Swap not possible - one or more element is not in the list")
          return

      if node1_prev is None:
          self.head_node = node2
      else:
          node1_prev.set_next_node(node2)

      if node2_prev is None:
          self.head_node = node1
      else:
          node2_prev.set_next_node(node1)

      temp = node1.get_next_node()
      node1.set_next_node(node2.get_next_node())
      node2.set_next_node(temp)




#count=1
#nmb = int(input ('Enter list length: '))
value = input('Create a linked list enter value: ')
my_list = LinkedList(int(value))




#while count<int(nmb):
    
    
    #new_value = input('Enter value: ')
    #count = count + 1 
    #my_list.insert_beginning(int(new_value))

#print('The list is :' '\n' + my_list.stringify_list())


while True:
    print('Select 0 to see list')
    print('Select 1 if remove value')
    print('Select 2 if head node')
    print('Select 3 if add to list')
    print('Select 4 to swap values')
    print('Select 5 to exit')
    to_do = input('I want to do: ')


    if int(to_do) == 1:
        node_to_remove = input('Remove a value: ')
        my_list.remove_node(int(node_to_remove))
        print('The list after :' '\n' + my_list.stringify_list())

    elif int(to_do) == 2:
     
        print('The head node : ' + str(my_list.get_head_node().get_value()))

    elif int(to_do) == 3:
        new_value = input('Enter new value: ')
        my_list.insert_beginning(int(new_value))
        

    elif int(to_do) == 0:
        print('The list is :' '\n' + my_list.stringify_list())

    elif int(to_do) == 4:
        val1 = input('Value 1: ')
        val2 = input('value 2: ')
        my_list.swap_nodes(int(val1),int(val2))
        

   
        
    else:
        print('Bye')
        break
        

