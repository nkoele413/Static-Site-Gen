import unittest
from inline_markdown import (
    split_nodes_delimeter,

)

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is  text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This is  text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimeter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
    


if __name__ == "__main__":
    unittest.main()