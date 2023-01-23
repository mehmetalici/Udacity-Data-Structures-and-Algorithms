from os import path
from typing import Tuple
from problem_7 import PathError, Router, HTTPRequestHandler


def test_edge_inputs():
    print("Testing edge inputs...")
    # Case 1: Creating a default router and adding no additional handlers
    router = _create_default_router()
    print(router.lookup("/home"))  # should print "not found handler"

    # Case 2: Adding an erroneous handler
    try:
        router.add_handler(0, HTTPRequestHandler("new root handler"))
    except PathError:
        print("Pass")  # should print "pass"
    
    # Case 3: lookup an erroneous handler
    try:
        print(router.lookup(123))
    except PathError:
        print("Pass")  # should print "pass"


def test_regular_inputs():
    print("Testing regular inputs...")
    router = _create_default_router()
    router.add_handler("/home/about", HTTPRequestHandler("about handler"))   

    print(router.lookup("/"))  # should print "root handler"
    print(router.lookup("/home"))  # should print 'not found handler' 
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' 
    print(router.lookup("/home/about/me"))  # should print 'not found handler'


def test_huge_inputs():
    print("Testing huge inputs...")
    router = _create_default_router()
    path_handler_pairs = (
        ("/home", HTTPRequestHandler("home handler")),
        ("/home/about", HTTPRequestHandler("about handler")),
        ("/home/contact", HTTPRequestHandler("contact handler"))
    )
    huge_path_handler_pairs = _hugify(path_handler_pairs)
    for huge_pair in huge_path_handler_pairs:
        router.add_handler(huge_pair[0], huge_pair[1])  

    print(router.lookup(_get_huge("/home/about")))  # should print 'about handler'


def _create_default_router():
    return Router(root_handler=HTTPRequestHandler("root handler"), not_found_handler=HTTPRequestHandler("not found handler")) 


def _hugify(path_handler_pairs: Tuple[tuple]) -> Tuple[tuple]:
    return tuple((_get_huge(pair[0]), pair[1]) for pair in path_handler_pairs)


def _get_huge(string):
    hugify_factor = 10 ** 5
    return string * hugify_factor


if __name__ == "__main__":
    # You may wish to highlight "should print" strings throughout the file on your code editor for a fast evaluation. 
    test_regular_inputs()
    test_huge_inputs()
    test_edge_inputs()