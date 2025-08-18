import unittest
from inline_markdown import (
    split_nodes_delimiter,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is a **bold** text", TextType.TEXT),
            TextNode("This is an *italic* text", TextType.TEXT),
        ]
        delimiter = "**"
        text_type = TextType.BOLD

        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text, " text")

    def test_split_nodes_invalid_markdown(self):
        old_nodes = [TextNode("This is an **unclosed bold text", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD

        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(old_nodes, delimiter, text_type)
        
        self.assertTrue("invalid markdown, formatted section not closed" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
