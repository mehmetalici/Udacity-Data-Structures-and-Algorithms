# Project 2: Show Me The Data Structures

Answers for the Project 2 Show Me the Data Structures of the Data Structures and Algorithms Course offered by Udacity.

## Performance Analysis
The analysis for each answer is provided in the following sections. 

It does not include a detailed walk-through of the code, but provides a reasoning behind the decisions taken. For example, reasons for choosing a data structure as well as the efficiencies of the solutions.

## Problem 1: Least Recently Used (LRU) Cache
The entries to the cache are given as key-value pairs. Therefore, these entries are cached, i.e kept, using a dictionary which provides get and set operations in constant time, i.e O(1). 

If the LRU Cache hits its capacity when adding a new entry, it is specified to remove the LRU entry and replace it with the new one. To satisfy this specification in constant time, a `UniqueEltQueue` is used.


### UniqueEltQueue
In UniqueEltQueue, the built-in Deque was employed as its underlying data structure. The enqueue operation is trivially enqueuing from left to Deque, and therefore O(1). 

On the other hand, the dequeue operation, however, does not directly dequeue the element at the end of the queue. Instead, starting from the right end, it checks how many times the elements appear in the queue. 

If an element is found to appear more than once, it removes the element from the queue and continues until it hits a unique element. The unique element is, then, dequeued and returned from the function. 

In similar fashion to enqueue, the dequeue operation is also designed to be O(1) using a Counter to keep track of the repeated elements.


### Space Complexity
At the worst case, where we perform `get_value` every time, the corresponding value will be added to the `UniqueEltQueue`. Therefore, the space complexity is O(n), where n is the number of values, on each of which we use `get_value` method. 

## Problem 2: File Recursion
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with a suffix, such as ".c".

Since there is no limit to the depth of the subdirectories, recursion technique was employed to solve this problem efficiently and elegantly. According to that, a linear search was implemented in the function `find_files` to find all elements in one directory. The function recurs for all elements that are found and the recursion stops, i.e base case is reached, when the element to be searched is actually a file. The suffix check was implemented in the base case.   

All files and directories are visited only once. Therefore, the time complexity is O(n), when n is the total number of files. The time complexity can also be modeled as O(n+m), with n being the total number of directories and m is the total number of files.

The recursion should usually be avoided because it does not scale to big input sizes.  More specifically, in each recursion call, a new block is allocated in the stack for function's local variables. For huge inputs, this might cause the stack to overflow after a certain recursion depth. For security reasons, Python throws the RecursionException when the recursion depth is exceeds as default 1000.

In the problem space, however, it is very unlikely that the directory depth exceeds 1000 and therefore the recursion was employed over loop-based techniques.


### Space Complexity
Since files with a desired suffix are added to the `all_files` list, the solution is O(n) in space.  

## Problem 3: Huffman Coding
In this problem, Huffman data compression technique is implemented. The solution consists of two parts, namely Huffman Encoding and Huffman Decoding. We will walk through each part, focusing on the efficiency. 

### Huffman Encoding
In this section, a Huffman tree is built in a bottom-up approach and the steps are enumerated below:

#### Phase 1: Build the Hoffman Tree
1. The frequency of each character was determined in a given message. This is implemented using a Counter with O(n) time complexity for creation.

2. In this step, we store the frequency-character pairs under Node data structure. It is specified that the least frequency elements to be constantly popped out. To compare frequencies, `__lt__` method was implemented for Node class to compare two nodes based on their frequencies. To pop out least frequency efficiently, a priority queue was implemented to store the nodes.  

    A priority queue can be implemented with a variety of data structures. For efficiency, we use min heaps as underlying data structure, which gives O(logn) performance for both the find-min and insert operations.   

    ![pq](images/pq.png)
3. The minimum frequency pairs are popped out of the priority queue. 
4. A new node was created with a frequency being the sum of the popped out nodes. 
5. #3 and #4 are repeated until there is a single element left in the priority queue.A binary tree data structure is implemented to generate the Huffman Tree. For this purpose, the popped out nodes are connected as left and right child and parented by the created new node.  
6. For each node in the Hufmann Tree, bits are assigned. To do this, a bit property is introduced to Node class.

    ![huffmann-tree](images/hf_tree.png)
#### Phase 2: Generate the Encoded Data
7. The Hoffman tree was traversed to generate unique binary code for each character. The traversal was implemented as pre-order DFS because the bit in parent node is used to create the bits for children nodes. 

    Moreover, the pre-order DFS was implemented using recursion. This is safe as long as the tree depth would not exceed 1000.

### Huffman Decoding 
Once we have the encoded string as well as the corresponding Huffman tree, the string was decoded via a traversal from root to each leaf. 

### Size of Strings 
| Message              | Size (byte)* | Encoded Size (byte)* | Difference (%) |
|----------------------|-------------|---------------------|----------------|
| "The bird is the word" | 69          | 36                  | 47.82          |

*: sys.sizeof() was used to determine the sizes. This function does not determine the size of the data types that hold the messages, like in C, but instead the objects that hold additional overhead.  

### Space Complexity
Since there is one node for each individual character in the Huffmann Tree, the space complexity is O(n).  

## Problem 4: Active Directory
This problem was solved through recursion because a group can consist of group(s). There are two subsequent base cases in the function. First one checks if the user is in the current group. Subsequent base case checks if there are no subgroups in the current group. As long as the base cases are not reached, we do a linear search for subgroups and recur for each of them.

The time complexity of the solution is O(n+m) = O(n), with n, m being the total number of users and groups, respectively. 

### Space Complexity
Since the groups and users are traversed without allocating a memory block, for example, by creating an extra array, and a variable of Boolean type is returned regardless of the input size, the algorithm takes constant space. Therefore, the space complexity is O(1). 

## Problem 5: Blockchain
The Blockchain is implemented by a Blockchain class with its internal "chain" structure represented by a List. Adding a Block to the list is, therefore, O(1). Furthermore, a hash function is implemented that hashes whole the object.    

### Space Complexity
Since every block is hashed and then stored in a List, the space complexity is O(n).


## Problem 6: Union & Intersection
Union and intersection operations for linked lists are realized by converting them to sets, which is O(n). Furthermore, the intersection and union operations are performed on the sets. The resulting set is converted back to a linkedlist before returning. 

Converting from sets to LinkedLists, and vica versa, is O(n). Moreover, Python provides | operator for union and & for intersection on sets, with time complexities O(n+m) and O(min(m, n)), respectively. Therefore the overall time complexity is O(n) for both operations.

### Space Complexity
First, a LinkedList is created out of the input list. Then, in a similar fashion, a set is created out of the LinkedList to perform union and intersection operations. All creations take O(n) space, and therefore, the overall space complexity is O(n).

## Acknowledgements
Images at the Huffman Coding section are obtained from udacity.com. 


 