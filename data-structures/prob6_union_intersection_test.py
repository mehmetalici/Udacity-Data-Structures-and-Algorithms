from prob6_union_intersection import LinkedList, union, intersection


def test_usual_operation():
    print("Testing usual operation...")
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1,linked_list_2))
    print(intersection(linked_list_1,linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3,linked_list_4))
    print(intersection(linked_list_3,linked_list_4))


def test_big_lists():
    print("Testing big lists...")
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    expected_soln_union = LinkedList()
    expected_soln_intersection = LinkedList()

    element_1 = [i for i in range(10 ** 2)]
    element_2 = [i for i in range(10 ** 4)]
    expected_soln_intersection_lst = element_1
    expected_soln_union_lst = element_2


    # In Problem's boilerplate code, append is given as O(n), so it takes time for big lists. 
    for i in element_1:
        linked_list_1.append(i)  

    for i in element_2:
        linked_list_2.append(i)

    for i in expected_soln_intersection_lst:
        expected_soln_intersection.append(i)

    for i in expected_soln_union_lst:
        expected_soln_union.append(i)
    
    print("Append is complete. Checking now...")
    print(union(linked_list_1,linked_list_2).get_as_list() == expected_soln_union.get_as_list())  
    # Return True
    print(intersection(linked_list_1,linked_list_2).get_as_list() == expected_soln_intersection.get_as_list())  
    # Return True


def test_empty_lists():
    print("Testing empty lists...")
    # Test two empty lists 
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    expected_soln_union = LinkedList()
    expected_soln_intersection = LinkedList()
   
    # Return True
    print(union(linked_list_1,linked_list_2).get_as_list() == expected_soln_union.get_as_list())  
    # Return True
    print(intersection(linked_list_1,linked_list_2).get_as_list() == expected_soln_intersection.get_as_list())  
    
    # Test one empty list
    for i in range(5):
        linked_list_1.append(i)

    expected_soln_union = linked_list_1
    expected_soln_intersection = LinkedList()
    
    # Return True
    print(union(linked_list_1, linked_list_2).get_as_list() == expected_soln_union.get_as_list())
    # Return True
    print(intersection(linked_list_1, linked_list_2).get_as_list() == expected_soln_intersection.get_as_list())



if __name__ == "__main__":
    test_usual_operation()
    test_big_lists()
    test_empty_lists()