from asyncio.taskgroups import TaskGroup
from multiprocessing.sharedctypes import Value
from typing import override


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        str_container = ""
        for key, value in self.props.items():
            str_container +=  f' {key}="{value}"'
        return str_container

    def __repr__(self):
       return f"{self.tag}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    @override
    def to_html(self):
        if self.value is None:
            raise ValueError("Node don't exist")
        if self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.props}"
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    @override
    def to_html(self):
        if self.tag is None:
            raise ValueError("No value")
        if self.children is None:
            raise ValueError("No children")
        else:
            empty_string = ""
            for child in self.children:
                empty_string += child.to_html()

            return f"<{self.tag}{self.props_to_html()}>{empty_string}</{self.tag}>"
