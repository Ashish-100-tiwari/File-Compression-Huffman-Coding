import heapq #default inbuild heap

class BinaryTree:
  def __init__(self,value,freq):
    self.value = value
    self.freq = freq
    self.left = None
    self.right = None

class Huffmancode:

  def __init__(self,path) #path of the file
      self.path = path
      self.__heap = []
      self.__code = {}

  def __leftfunc__(self,other):
    return self.freq < other.freq #checking & comparing on frequency and elemnet have min freq we're picking up that
  
  def __equalfunc__(self,other):
    return self.freq == other.freq

  def __frequency_from_text(self,text):
      freq_dict = {}
      for char in text:
        if char not in freq_dict:
          freq_dict[char] = 0
        freq_dict[char] += 1
      return freq_dict  




  def __Build_heap(self,frequency_dict):
      for key in frequency_dict

      frequency = frequency_dict[key]
      binary_tree_node = BinaryTree(key,frequency)
      heapq.push(self.__heap,binary_tree_node)

  def __Build_Binary_Tree(self):
    while(self.__heap) > 1:
    binaryTree_Node_1 = heapq.heappop(self.__heap)
    binaryTree_Node_2 = heapq.heappop(self.__heap)
    sum_of_freq = binaryTree_Node_1.freq + binaryTree_Node_2.freq
    newNode = BinaryTree(None,sum_of_freq)

    newNode.left = binaryTree_Node_1
    newNode.right = binaryTree_Node_2
    return

  def __Build_Tree_Code_Helper(self,root,curr_bits):
    if root is None:
      return
      if root.value is not None:
        self.__code[root.value] = curr_bits
        return
      self.__Build_Tree_Code_Helper(root.left,curr_bits+'0')
      self.__Build_Tree_Code_Helper(root.rigth,curr_bits+'1')

  def __Build_Tree_Code(self.__heap):
    root = heapq.heappop(self.__heap)
    self.__Build_Tree_Code_Helper(root,'')


  def __Build_Encoded_Text(self,text):
    encoded_text = ''
    for char in text:
      encoded_text += self.__code[char]

    return encoded_text


  def compression(self):

    #To access the file and extarct text from that file


    text = 'fbvjbvjbjcjdjsdnjdsjdsjsfjn'
    frequency_dict = self.__frequency_from_text(text)

    #calculate frequency of each text and store in the frequency dicionary

    build_heap = self.__Build_heap(frequency_dict)


    #we need minimum 2characters having minimum frequency , so we have to construct a min heap
    
    #Min heap for two minimum frequency
    #so after this we've to create the binary tree using the heap

  self.__Build_Binary_Tree()

    #with the hellp of binary tree , we've to construct the code and code will store in the heap or you can say hashmap or dictionary

    self.__Build_Tree_Code()


    #construct the encoded text.
    encoded_text = self.__Build_Encoded_Text(text)
    #we have to return that binary file as output containing encoded text which is given by compression function