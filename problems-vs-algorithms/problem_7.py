from typing import List


class HTTPRequestHandler:
    def __init__(self, representation) -> None:
        self.representation = representation

    def __repr__(self) -> str:
        return self.representation


class _RouteTrie:
    def __init__(self, root_handler: HTTPRequestHandler):
        self.root = _RouteTrieNode(root_handler)

    def insert(self, path: List[str], handler: HTTPRequestHandler):
        node = self.root
        for path_part in path:
            node = node.insert(path_part)
        node.handler = handler

    def find(self, path: List[str]) -> HTTPRequestHandler:
        node = self.root
        for path_part in path:
            try:
                node = node.children[path_part]
            except KeyError:
                return
        return node.handler


class _RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, path_part: str, handler=None):
        return self.children.setdefault(path_part, _RouteTrieNode(handler))


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.route_trie = _RouteTrie(root_handler)
        self.not_found_handler = not_found_handler
        self.root_handler = root_handler

    def add_handler(self, path: str, handler: str):
        if not _is_valid_path(path):
            raise PathError
        path = _split_path(path)
        self.route_trie.insert(path, handler)

    def lookup(self, path: str) -> HTTPRequestHandler:
        if not _is_valid_path(path):
            raise PathError
        path = _split_path(path)
        handler = self.route_trie.find(path)
        if handler is not None:
            return handler
        return self.not_found_handler


def _is_valid_path(path):
    return isinstance(path, str)


def _split_path(path: str) -> filter:
    return filter(lambda elt: elt != "", path.split("/"))


class PathError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)