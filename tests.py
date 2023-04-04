"""
Project 5
CSE 331 S21 (Onsay)
Andrew McDonald & Bank Premsri
Inspired by Brandon Field and Anna DeBiasi's implementation
tests.py
"""
import math
import unittest
import random
import types
from math import log2
from solution import Node, AVLTree, is_avl_tree
from solution import Node, AVLTree as AVLTreeSolution, is_avl_tree, AVLDatabase, Table
from xml.dom import minidom

NAMES = {0: 'Aaron', 1: 'Abigail', 2: 'Adam', 3: 'Alan', 4: 'Albert', 5: 'Alexander', 6: 'Alexis', 7: 'Alice',
         8: 'Amanda', 9: 'Amber', 10: 'Amy', 11: 'Andrea', 12: 'Andrew', 13: 'Angela', 14: 'Ann', 15: 'Anna',
         16: 'Anthony', 17: 'Arthur', 18: 'Ashley', 19: 'Austin', 20: 'Barbara', 21: 'Benjamin', 22: 'Betty',
         23: 'Beverly', 24: 'Billy', 25: 'Bobby', 26: 'Brandon', 27: 'Brenda', 28: 'Brian', 29: 'Brittany', 30: 'Bruce',
         31: 'Bryan', 32: 'Carl', 33: 'Carol', 34: 'Carolyn', 35: 'Catherine', 36: 'Charles', 37: 'Charlotte',
         38: 'Cheryl', 39: 'Christian', 40: 'Christina', 41: 'Christine', 42: 'Christopher', 43: 'Cynthia',
         44: 'Daniel', 45: 'Danielle', 46: 'David', 47: 'Deborah', 48: 'Debra', 49: 'Denise', 50: 'Dennis', 51: 'Diana',
         52: 'Diane', 53: 'Donald', 54: 'Donna', 55: 'Doris', 56: 'Dorothy', 57: 'Douglas', 58: 'Dylan', 59: 'Edward',
         60: 'Elijah', 61: 'Elizabeth', 62: 'Emily', 63: 'Emma', 64: 'Eric', 65: 'Ethan', 66: 'Eugene', 67: 'Evelyn',
         68: 'Frances', 69: 'Frank', 70: 'Gabriel', 71: 'Gary', 72: 'George', 73: 'Gerald', 74: 'Gloria', 75: 'Grace',
         76: 'Gregory', 77: 'Hannah', 78: 'Harold', 79: 'Heather', 80: 'Helen', 81: 'Henry', 82: 'Isabella', 83: 'Jack',
         84: 'Jacob', 85: 'Jacqueline', 86: 'James', 87: 'Janet', 88: 'Janice', 89: 'Jason', 90: 'Jean', 91: 'Jeffrey',
         92: 'Jennifer', 93: 'Jeremy', 94: 'Jerry', 95: 'Jesse', 96: 'Jessica', 97: 'Joan', 98: 'Joe', 99: 'John',
         100: 'Johnny', 101: 'Jonathan', 102: 'Jordan', 103: 'Jose', 104: 'Joseph', 105: 'Joshua', 106: 'Joyce',
         107: 'Juan', 108: 'Judith', 109: 'Judy', 110: 'Julia', 111: 'Julie', 112: 'Justin', 113: 'Karen',
         114: 'Katherine', 115: 'Kathleen', 116: 'Kathryn', 117: 'Kayla', 118: 'Keith', 119: 'Kelly', 120: 'Kenneth',
         121: 'Kevin', 122: 'Kimberly', 123: 'Kyle', 124: 'Larry', 125: 'Laura', 126: 'Lauren', 127: 'Lawrence',
         128: 'Linda', 129: 'Lisa', 130: 'Logan', 131: 'Louis', 132: 'Madison', 133: 'Margaret', 134: 'Maria',
         135: 'Marie', 136: 'Marilyn', 137: 'Mark', 138: 'Martha', 139: 'Mary', 140: 'Matthew', 141: 'Megan',
         142: 'Melissa', 143: 'Michael', 144: 'Michelle', 145: 'Nancy', 146: 'Natalie', 147: 'Nathan', 148: 'Nicholas',
         149: 'Nicole', 150: 'Noah', 151: 'Olivia', 152: 'Pamela', 153: 'Patricia', 154: 'Patrick', 155: 'Paul',
         156: 'Peter', 157: 'Philip', 158: 'Rachel', 159: 'Ralph', 160: 'Randy', 161: 'Raymond', 162: 'Rebecca',
         163: 'Richard', 164: 'Robert', 165: 'Roger', 166: 'Ronald', 167: 'Rose', 168: 'Roy', 169: 'Russell',
         170: 'Ruth', 171: 'Ryan', 172: 'Samantha', 173: 'Samuel', 174: 'Sandra', 175: 'Sara', 176: 'Sarah',
         177: 'Scott', 178: 'Sean', 179: 'Sharon', 180: 'Shirley', 181: 'Sophia', 182: 'Stephanie', 183: 'Stephen',
         184: 'Steven', 185: 'Susan', 186: 'Teresa', 187: 'Terry', 188: 'Theresa', 189: 'Thomas', 190: 'Timothy',
         191: 'Tyler', 192: 'Victoria', 193: 'Vincent', 194: 'Virginia', 195: 'Walter', 196: 'Wayne', 197: 'William',
         198: 'Willie', 199: 'Zachary'}


class AVLTreeTests(unittest.TestCase):

    def test_rotate(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.right_rotate(avl.origin))
        self.assertIsNone(avl.left_rotate(avl.origin))

        """
        (1) test basic right
        initial structure:
            3
           /
          2
         /
        1
        final structure:
          2
         / \
        1   3
        """
        avl.origin = Node(3)
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.size = 3

        node = avl.right_rotate(avl.origin)

        self.assertIsInstance(node, Node)

        self.assertEqual( avl.origin.value, 2)
        self.assertIsNone(avl.origin.parent)  # root value and parent
        # root left value and parent
        self.assertEqual( avl.origin.left.value, 1)
        self.assertEqual(avl.origin.left.parent, avl.origin)
        # shouldn't have children
        self.assertFalse( (avl.origin.left.left or avl.origin.left.right))
        # root right value and parent
        self.assertEqual( avl.origin.right.value, 3)
        self.assertEqual(avl.origin.right.parent, avl.origin)
        # shouldn't have children
        self.assertFalse(avl.origin.right.right or avl.origin.right.left)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (2) test basic left
        initial structure:
        1
         \
          2
           \
            3
        final structure:
          2
         / \
        1   3
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.right = Node(2, parent=avl.origin)
        avl.origin.right.right = Node(3, parent=avl.origin.right)
        avl.size = 3

        node = avl.left_rotate(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual( avl.origin.value,2)
        self.assertIsNone(avl.origin.parent)  # root value and parent
        # root left value and parent
        self.assertEqual( avl.origin.left.value, 1)
        self.assertEqual(avl.origin.left.parent, avl.origin)
        # shouldn't have any children
        self.assertFalse(avl.origin.left.left or avl.origin.left.right)
        # root right value and parent
        self.assertEqual(avl.origin.right.value, 3)
        self.assertEqual(avl.origin.right.parent, avl.origin)
        # shouldn't have any children
        self.assertFalse(avl.origin.right.right or avl.origin.right.left)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (3) test intermediate right, rotating at origin
        initial structure:
              7
             / \
            3   10
           / \
          2   4
         /
        1 
        final structure:
            3
           / \
          2   7
         /   / \
        1   4   10
        """
        avl = AVLTree()
        avl.origin = Node(7)
        avl.origin.left = Node(3, parent=avl.origin)
        avl.origin.left.left = Node(2, parent=avl.origin.left)
        avl.origin.left.left.left = Node(1, parent=avl.origin.left.left)
        avl.origin.left.right = Node(4, parent=avl.origin.left)
        avl.origin.right = Node(10, parent=avl.origin)

        node = avl.right_rotate(avl.origin)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node3 = avl.origin
        node2 = avl.origin.left
        node1 = avl.origin.left.left
        node7 = avl.origin.right
        node4 = avl.origin.right.left
        node10 = avl.origin.right.right

        self.assertEqual( node3.value, 3)
        self.assertIsNone(node3.parent)
        self.assertEqual( node2.value, 2)
        self.assertEqual(node2.parent, node3)
        self.assertIsNone(node2.right)
        self.assertEqual( node1.value, 1)
        self.assertEqual(node1.parent, node2)
        self.assertFalse(node1.left or node1.right)
        self.assertEqual(node7.value, 7)
        self.assertEqual(node7.parent, node3)
        self.assertEqual(node7.left, node4)
        self.assertEqual(node7.right, node10)
        self.assertEqual( node4.value, 4)
        self.assertEqual(node4.parent, node7)
        self.assertFalse(node4.left or node4.right)
        self.assertEqual( node10.value, 10)
        self.assertEqual(node10.parent, node7)
        self.assertFalse(node10.left or node10.right)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (4) test intermediate left, rotating at origin
        initial structure:
          7
         /  \
        3   10
           /   \
          9    11
                 \
                  12
        final structure:
        	10
           /  \
          7   11
         / \    \
        3   9    12
        """
        avl = AVLTree()
        avl.origin = Node(7)
        avl.origin.left = Node(3, parent=avl.origin)
        avl.origin.right = Node(10, parent=avl.origin)
        avl.origin.right.left = Node(9, parent=avl.origin.right)
        avl.origin.right.right = Node(11, parent=avl.origin.right)
        avl.origin.right.right.right = Node(12, parent=avl.origin.right.right)

        node = avl.left_rotate(avl.origin)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node10 = avl.origin
        node7 = avl.origin.left
        node3 = avl.origin.left.left
        node9 = avl.origin.left.right
        node11 = avl.origin.right
        node12 = avl.origin.right.right

        self.assertEqual( node10.value, 10)
        self.assertIsNone(node10.parent)
        self.assertEqual( node7.value, 7)
        self.assertEqual(node7.parent, node10)
        self.assertEqual( node3.value, 3)
        self.assertEqual(node3.parent, node7)
        self.assertFalse(node3.left or node3.right)
        self.assertEqual( node9.value, 9)
        self.assertEqual(node9.parent, node7)
        self.assertFalse(node9.left or node9.right)
        self.assertEqual( node11.value, 11)
        self.assertEqual(node11.parent, node10)
        self.assertIsNone(node11.left)
        self.assertEqual( node12.value, 12)
        self.assertEqual(node12.parent, node11)
        self.assertFalse(node12.left or node12.right)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (5) test advanced right, rotating not at origin
        initial structure:
        		10
        	   /  \
        	  5	   11
        	 / \     \
        	3	7    12
           / \
          2   4
         /
        1
        final structure:
              10
             /  \
            3    11
           / \     \
          2   5     12
         /   / \
        1   4   7
        """
        avl = AVLTree()
        avl.origin = Node(10)
        avl.origin.right = Node(11, parent=avl.origin)
        avl.origin.right.right = Node(12, parent=avl.origin.right)
        avl.origin.left = Node(5, parent=avl.origin)
        avl.origin.left.right = Node(7, parent=avl.origin.left)
        avl.origin.left.left = Node(3, parent=avl.origin.left)
        avl.origin.left.left.right = Node(4, parent=avl.origin.left.left)
        avl.origin.left.left.left = Node(2, parent=avl.origin.left.left)
        avl.origin.left.left.left.left = Node(
            1, parent=avl.origin.left.left.left)

        node = avl.right_rotate(avl.origin.left)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node10 = avl.origin
        node11 = avl.origin.right
        node12 = avl.origin.right.right
        node3 = avl.origin.left
        node2 = avl.origin.left.left
        node1 = avl.origin.left.left.left
        node5 = avl.origin.left.right
        node4 = avl.origin.left.right.left
        node7 = avl.origin.left.right.right

        self.assertEqual( node10.value, 10)
        self.assertIsNone(node10.parent)
        self.assertEqual( node3.value, 3)
        self.assertEqual(node3.parent, node10)
        self.assertEqual( node2.value, 2)
        self.assertEqual(node2.parent, node3)
        self.assertIsNone(node2.right)
        self.assertEqual( node1.value, 1)
        self.assertEqual(node1.parent, node2)
        self.assertFalse(node1.left or node1.right)
        self.assertEqual( node5.value, 5)
        self.assertEqual(node5.parent, node3)
        self.assertEqual( node4.value, 4)
        self.assertEqual(node4.parent, node5)
        self.assertFalse(node4.left or node4.right)
        self.assertEqual( node7.value, 7)
        self.assertEqual(node7.parent, node5)
        self.assertFalse(node7.left or node7.right)
        self.assertEqual( node11.value, 11)
        self.assertEqual(node11.parent, node10)
        self.assertIsNone(node11.left)
        self.assertEqual( node12.value, 12)
        self.assertEqual(node12.parent, node11)
        self.assertFalse(node12.left or node12.right)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (6) test advanced left, rotating not at origin
        initial structure:
        	3
           / \
          2   10
         /   /  \
        1   5   12
               /  \
              11   13
                     \
                      14
        final structure:
        	3
           / \
          2   12
         /   /  \
        1   10   13
           /  \    \
          5   11   14
        """
        avl = AVLTree()
        avl.origin = Node(3)
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.right = Node(10, parent=avl.origin)
        avl.origin.right.left = Node(5, parent=avl.origin.right)
        avl.origin.right.right = Node(12, parent=avl.origin.right)
        avl.origin.right.right.left = Node(11, parent=avl.origin.right.right)
        avl.origin.right.right.right = Node(13, parent=avl.origin.right.right)
        avl.origin.right.right.right.right = Node(
            14, parent=avl.origin.right.right.right)

        node = avl.left_rotate(avl.origin.right)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node3 = avl.origin
        node2 = avl.origin.left
        node1 = avl.origin.left.left
        node12 = avl.origin.right
        node10 = avl.origin.right.left
        node5 = avl.origin.right.left.left
        node11 = avl.origin.right.left.right
        node13 = avl.origin.right.right
        node14 = avl.origin.right.right.right

        self.assertEqual( node3.value, 3)
        self.assertIsNone(node3.parent)
        self.assertEqual( node2.value, 2)
        self.assertEqual(node2.parent, node3)
        self.assertIsNone(node2.right)
        self.assertEqual( node1.value, 1)
        self.assertEqual(node1.parent, node2)
        self.assertFalse(node1.left or node1.right)
        self.assertEqual( node12.value, 12)
        self.assertEqual(node12.parent, node3)
        self.assertEqual( node10.value, 10)
        self.assertEqual(node10.parent, node12)
        self.assertEqual( node5.value, 5)
        self.assertEqual(node5.parent, node10)
        self.assertFalse(node5.left or node5.right)
        self.assertEqual( node11.value, 11)
        self.assertEqual(node11.parent, node10)
        self.assertFalse(node11.left or node11.right)
        self.assertEqual( node13.value, 13)
        self.assertEqual(node13.parent, node12)
        self.assertIsNone(node13.left)
        self.assertEqual( node14.value, 14)
        self.assertEqual(node14.parent, node13)
        self.assertFalse(node14.left or node14.right)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

    def test_balance_factor(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertEqual(0, avl.balance_factor(avl.origin))

        """
        (1) test on balanced tree
        structure:
          2
         / \
        1   3
        """
        avl.origin = Node(2)
        avl.origin.height = 1
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 0
        avl.size = 3

        self.assertEqual(0, avl.balance_factor(avl.origin))
        self.assertEqual(0, avl.balance_factor(avl.origin.left))
        self.assertEqual(0, avl.balance_factor(avl.origin.right))

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (2a) test on unbalanced left
        structure:
            3
           /
          2
         /
        1
        """
        avl = AVLTree()
        avl.origin = Node(3)
        avl.origin.height = 2
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 1
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.size = 3

        self.assertEqual(2, avl.balance_factor(avl.origin))
        self.assertEqual(1, avl.balance_factor(avl.origin.left))
        self.assertEqual(0, avl.balance_factor(avl.origin.left.left))

        """
        (2b) test on unbalanced right
        structure:
        1
         \
          2
           \
            3
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.height = 2
        avl.origin.right = Node(2, parent=avl.origin)
        avl.origin.right.height = 1
        avl.origin.right.right = Node(3, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.size = 3

        self.assertEqual(-2, avl.balance_factor(avl.origin))
        self.assertEqual(-1, avl.balance_factor(avl.origin.right))
        self.assertEqual(0, avl.balance_factor(avl.origin.right.right))

    def test_rebalance(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.rebalance(avl.origin))

        """
        (1) test balanced tree (do nothing)
        initial and final structure:
          2
         / \
        1   3
        since pointers are already tested in rotation testcase, only check values and heights
        """
        avl.origin = Node(2)
        avl.origin.height = 1
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 0
        avl.size = 3

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(2, node.value)
        self.assertEqual(2, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (2a) test left-left rebalance
        initial structure:
            4
           /
          2
         / \
        1   3
        final structure:
          2
         / \
        1   4
           /
          3
        """
        avl = AVLTree()
        avl.origin = Node(4)
        avl.origin.height = 2
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 1
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.origin.left.right = Node(3, parent=avl.origin.left)
        avl.origin.left.right.height = 0
        avl.size = 4

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(2, node.value)  # make sure to return the new root
        self.assertEqual(2, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(3, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (2b) test right-right rebalance
        initial structure:
        1
         \
          3
         /  \
        2    4
        final structure:
          3
         / \
        1   4
         \
          2
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.height = 2
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 1
        avl.origin.right.right = Node(4, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.origin.right.left = Node(2, parent=avl.origin.right)
        avl.origin.right.left.height = 0
        avl.size = 4

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(3, node.value)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.assertEqual(2, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (3) test left-right rebalance
        initial structure:
            5
           / \
          2   6
         / \
        1   3
             \
              4
        intermediate structure:
              5
             / \
            3   6
           / \
          2   4
         /
        1
        final structure:
            3 
           / \
          2   5
         /   / \
        1   4   6
        """
        avl = AVLTree()
        avl.origin = Node(5)
        avl.origin.height = 3
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 2
        avl.origin.right = Node(6, parent=avl.origin)
        avl.origin.right.height = 0
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.origin.left.right = Node(3, parent=avl.origin.left)
        avl.origin.left.right.height = 1
        avl.origin.left.right.right = Node(4, parent=avl.origin.left.right)
        avl.origin.left.right.right.height = 0

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(3, node.value)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (4) test right-left rebalance
        initial structure:
          2
         / \
        1   5
           / \
          4   6
         /
        3
        intermediate structure:
          2
         / \
        1   4
           / \
          3   5
               \
                6
        final structure:
            4 
           / \
          2   5
         / \   \
        1   3   6
        """
        avl = AVLTree()
        avl.origin = Node(2)
        avl.origin.height = 3
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(5, parent=avl.origin)
        avl.origin.right.height = 2
        avl.origin.right.left = Node(4, parent=avl.origin.right)
        avl.origin.right.left.height = 1
        avl.origin.right.right = Node(6, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.origin.right.left.left = Node(3, parent=avl.origin.right.left)
        avl.origin.right.left.left.height = 0

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(4, node.value)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

    def test_insert(self):

        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        avl = AVLTree()
        """
        (1) test insertion causing right-right rotation
        final structure
          1
         / \
        0   3
           / \
          2   4
        """
        for i in range(5):
            node = avl.insert(avl.origin, i, i)
            self.assertIsInstance(node, Node)

        self.assertEqual(5, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(1, avl.origin.data)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(0, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.data)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(3, avl.origin.right.data)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(2, avl.origin.right.left.value)
        self.assertEqual(2, avl.origin.right.left.data)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(4, avl.origin.right.right.value)
        self.assertEqual(4, avl.origin.right.right.data)
        self.assertEqual(0, avl.origin.right.right.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (2) test insertion causing left-left rotation
        final structure
            3
           / \
          1   4
         / \
        0   2
        """
        avl = AVLTree()
        for i in range(4, -1, -1):
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)
        self.assertEqual(5, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(2, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (3) test insertion (with duplicates) causing left-right rotation
        initial structure:
            5
           / \
          2   6
         / \
        1   3
             \
              4
        final structure:
            3 
           / \
          2   5
         /   / \
        1   4   6
        """
        avl = AVLTree()
        for i in [5, 2, 6, 1, 3] * 2 + [4]:
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """
        (4) test insertion (with duplicates) causing right-left rotation
        initial structure:
          2
         / \
        1   5
           / \
          4   6
         /
        3
        final structure:
            4 
           / \
          2   5
         / \   \
        1   3   6
        """
        avl = AVLTree()
        for i in [2, 1, 5, 4, 6] * 2 + [3]:
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

    def test_min(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.min(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        min_node = avl.min(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertEqual(0, min_node.value)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        min_node = avl.min(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertEqual(-100, min_node.value)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """(3) large random tree"""
        random.seed(331)
        avl = AVLTree()
        numbers = [random.randint(-1000, 1000) for _ in range(1000)]
        for num in numbers:
            avl.insert(avl.origin, num)
        min_node = avl.min(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertEqual(min(numbers), min_node.value)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

    def test_max(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.max(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        max_node = avl.max(avl.origin)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(9, max_node.value)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        max_node = avl.max(avl.origin)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(100, max_node.value)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """(3) large random tree"""
        random.seed(331)
        avl = AVLTree()
        numbers = [random.randint(-1000, 1000) for _ in range(1000)]
        for num in numbers:
            avl.insert(avl.origin, num)
        max_node = avl.max(avl.origin)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(max(numbers), max_node.value)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

    def test_search(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.search(avl.origin, 0))

        """
        (1) search small basic tree
        tree structure
          1
         / \
        0   3
           / \
          2   4
        """
        avl = AVLTree()
        numbers = [1, 0, 3, 2, 4]
        for num in numbers:
            avl.insert(avl.origin, num)
        # search existing numbers
        for num in numbers:
            node = avl.search(avl.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        # search non-existing numbers and ensure parent of where value would go is returned
        pairs = [(-1, 0), (0.5, 0), (5, 4), (2.5, 2),
                 (3.5, 4), (-1e5, 0), (1e5, 4)]
        for target, closest in pairs:
            node = avl.search(avl.origin, target)
            self.assertIsInstance(node, Node)
            self.assertEqual(closest, node.value)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

        """(2) search large random tree"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(1000)}
        for num in numbers:
            avl.insert(avl.origin, num)
        for num in numbers:
            # search existing number
            node = avl.search(avl.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)

            # if this node is a leaf, search non-existing numbers around it
            # to ensure it is returned as the parent of where new insertions would go
            if node.left is None and node.right is None:
                node = avl.search(avl.origin, num + 0.1)
                self.assertIsInstance(node, Node)
                self.assertEqual(num, node.value)
                node = avl.search(avl.origin, num - 0.1)
                self.assertIsInstance(node, Node)
                self.assertEqual(num, node.value)

        self.assertTrue(is_avl_tree(avl.origin))  # sanity check for valid AVL tree

    def test_inorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.inorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(10))
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(-100, 101))
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(80)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = sorted(numbers)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(4) Testing tree is iterable. Hint: Implement the __iter__ function."""
        for expected_val, actual in zip(expected, avl):
            self.assertEqual(expected_val, actual.value)

    def test_preorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.preorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [3, 1, 0, 2, 7, 5, 4, 6, 8, 9]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 21):
            avl.insert(avl.origin, i)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-5, -13, -17, -19, -20, -18, -15, -16, -14, -9, -11,
                    -12, -10, -7, -8, -6, 11, 3, -1, -3, -4, -2, 1, 0, 2,
                    7, 5, 4, 6, 9, 8, 10, 15, 13, 12, 14, 17, 16, 19, 18,
                    20]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(80)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [527, 33, -493, -834, -933, -954, -918, -655, -720,
                    -789, -705, -650, -529, -165, -343, -422, -434,
                    -359, -312, -324, -269, -113, -142, -148, -116, -43,
                    -89, -26, 327, 220, 108, 77, 44, 101, 193, 113,
                    194, 274, 251, 224, 268, 294, 283, 316, 454, 362, 358,
                    333, 360, 431, 411, 446, 486, 485, 498, 503,
                    711, 574, 565, 529, 571, 675, 641, 687, 832, 776, 733,
                    720, 775, 784, 782, 802, 914, 860, 843, 888,
                    966, 944, 975]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_postorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.postorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [0, 2, 1, 4, 6, 5, 9, 8, 7, 3]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 20):
            avl.insert(avl.origin, i)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-20, -18, -19, -16, -14, -15, -17, -12, -10, -11, -8, -6, -7, -9,
                    -13, -4, -2, -3, 0, 2, 1, -1, 4, 6, 5, 8, 10, 9, 7, 3, 12, 14, 13,
                    16, 19, 18, 17, 15, 11, -5]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(80)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-954, -918, -933, -789, -705, -720, -529, -650, -655, -834, -434, -359, -422, -324, -269, -312,
                    -343, -148, -116, -142, -89, -26, -43, -113, -165, -493, 44, 101, 77, 113, 194, 193, 108, 224,
                    268, 251, 283, 316, 294, 274, 220, 333, 360, 358, 411, 446, 431, 362, 485, 503, 498, 486, 454,
                    327, 33, 529, 571, 565, 641, 687, 675, 574, 720, 775, 733, 782, 802, 784, 776, 843, 888, 860,
                    944, 975, 966, 914, 832, 711, 527]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_levelorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.levelorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [3, 1, 7, 0, 2, 5, 8, 4, 6, 9]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-20, 20):
            avl.insert(avl.origin, i)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-5, -13, 11, -17, -9, 3, 15, -19, -15, -11, -7, -1, 7, 13, 17, -20, -18,
                    -16, -14, -12, -10, -8, -6, -3, 1, 5, 9, 12, 14, 16, 18, -4, -2, 0, 2,
                    4, 6, 8, 10, 19]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(80)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [527, 33, 711, -493, 327, 574, 832, -834, -165, 220, 454,
                    565, 675, 776, 914, -933, -655, -343, -113, 108, 274,
                    362, 486, 529, 571, 641, 687, 733, 784, 860, 966, -954,
                    -918, -720, -650, -422, -312, -142, -43, 77, 193, 251,
                    294, 358, 431, 485, 498, 720, 775, 782, 802, 843, 888,
                    944, 975, -789, -705, -529, -434, -359, -324, -269, -148,
                    -116, -89, -26, 44, 101, 113, 194, 224, 268, 283, 316, 333,
                    360, 411, 446, 503]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_remove(self):

        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.remove(avl.origin, 0))

        """
        (1) test removal causing right-right rotation
        initial structure:
            2
           / \
          1   3
         /     \
        0       4
        final structure (removing 1, 0):
          3 
         / \
        2   4
        """
        avl = AVLTree()
        for i in [2, 1, 3, 4, 0]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 1)  # one child removal
        avl.remove(avl.origin, 0)  # zero child removal, will need rebalancing
        self.assertEqual(3, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (2) test removal causing left-left rotation
        initial structure:
            3
           / \
          2   4
         /     \
        1       5
        final structure (removing 4, 5):
          2 
         / \
        1   3
        """
        avl = AVLTree()
        for i in [3, 2, 4, 1, 5]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 4)  # one child removal
        avl.remove(avl.origin, 5)  # zero child removal, will need rebalancing
        self.assertEqual(3, avl.size)
        self.assertEqual(2, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (3) test removal causing left-right rotation
        initial structure:
              5
             / \
            2   6
           / \   \
          1   3   7
         /     \
        0       4
        final structure (removing 1, 6):
            3 
           / \
          2   5
         /   / \
        0   4   7
        """
        avl = AVLTree()
        for i in [5, 2, 6, 1, 3, 7, 0, 4]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 1)  # one child removal
        avl.remove(avl.origin, 6)  # one child removal, will need rebalancing
        self.assertEqual(6, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (4) test removal causing right-left rotation
        initial structure:
            2
           / \
          1   5
         /   / \
        0   4   6
           /     \
          3       7
        final structure (removing 6, 1):
            4 
           / \
          2   5
         / \   \
        0   3   7
        """
        avl = AVLTree()
        for i in [2, 1, 5, 0, 4, 6, 3, 7]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 6)  # one child removal
        avl.remove(avl.origin, 1)  # one child removal, will need rebalancing
        self.assertEqual(6, avl.size)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        """
        (5) test simple 2-child removal
        initial structure:
          2
         / \
        1   3
        final structure (removing 2):
         1 
          \
           3
        """
        avl = AVLTree()
        for i in [2, 1, 3]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 2)  # two child removal
        self.assertEqual(2, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (5) test compounded 2-child removal
        initial structure:
              4
           /     \
          2       6
         / \     / \
        1   3   5   7
        intermediate structure (removing 2, 6):
            4
           / \
          1   5
           \   \
            3   7
        final structure (removing 4)
            3
           / \
          1   5
               \
                7        
        """
        avl = AVLTree()
        for i in [4, 2, 6, 1, 3, 5, 7]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 2)  # two child removal
        avl.remove(avl.origin, 6)  # two child removal
        avl.remove(avl.origin, 4)  # two child removal
        self.assertEqual(4, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

    # def test_AVL_comprehensive(self):
    #
    #     # visualize some of test in this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
    #     # ensure empty tree is properly handled
    #     """
    #     First part, inserting and removing without rotation
    #
    #     insert without any rotation (inserting 5, 0, 10):
    #       5
    #      / \
    #     1   10
    #     """
    #
    #     def check_node_properties(current: Node, value: int = 0, height: int = 0, balance: int = 0):
    #         if value is None:
    #             self.assertIsNone(current)
    #             return
    #         self.assertEqual(value, current.value)
    #         self.assertEqual(height, current.height)
    #         self.assertEqual(balance, avl.balance_factor(current))
    #
    #     avl = AVLTree()
    #     avl.insert(avl.origin, 5)
    #     avl.insert(avl.origin, 1)
    #     avl.insert(avl.origin, 10)
    #     self.assertEqual(3, avl.size)
    #     self.assertEqual(1, avl.min(avl.origin).value)
    #     self.assertEqual(10, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=5, height=1, balance=0)
    #     check_node_properties(avl.origin.left, value=1, height=0, balance=0)
    #     check_node_properties(avl.origin.right, value=10, height=0, balance=0)
    #     """
    #     Current AVL tree:
    #       5
    #      / \
    #     1   10
    #     After Removing 5:
    #       1
    #        \
    #         10
    #     """
    #     avl.remove(avl.origin, 5)
    #     self.assertEqual(2, avl.size)
    #     self.assertEqual(1, avl.min(avl.origin).value)
    #     self.assertEqual(10, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=1, height=1, balance=-1)
    #     check_node_properties(avl.origin.left, value=None)
    #     check_node_properties(avl.origin.right, value=10, height=0, balance=0)
    #     """
    #     Current AVL tree:
    #       1
    #         \
    #         10
    #     After inserting 0, 20:
    #       1
    #      /  \
    #     0   10
    #           \
    #            20
    #     """
    #     avl.insert(avl.origin, 0)
    #     avl.insert(avl.origin, 20)
    #     self.assertEqual(4, avl.size)
    #     self.assertEqual(0, avl.min(avl.origin).value)
    #     self.assertEqual(20, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=1, height=2, balance=-1)
    #     check_node_properties(avl.origin.left, value=0, height=0, balance=0)
    #     check_node_properties(avl.origin.right, value=10, height=1, balance=-1)
    #     check_node_properties(avl.origin.right.right,
    #                           value=20, height=0, balance=0)
    #
    #     """
    #     Current AVL tree:
    #       1
    #      /  \
    #     0   10
    #           \
    #            20
    #     After removing 20, inserting -20 and inserting 5
    #          1
    #         /  \
    #        0   10
    #       /   /
    #     -20  5
    #     """
    #     avl.remove(avl.origin, 20)
    #     avl.insert(avl.origin, -20)
    #     avl.insert(avl.origin, 5)
    #     self.assertEqual(5, avl.size)
    #     self.assertEqual(-20, avl.min(avl.origin).value)
    #     self.assertEqual(10, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=1, height=2, balance=0)
    #     check_node_properties(avl.origin.left, value=0, height=1, balance=1)
    #     check_node_properties(avl.origin.left.left,
    #                           value=-20, height=0, balance=0)
    #     check_node_properties(avl.origin.right, value=10, height=1, balance=1)
    #     check_node_properties(avl.origin.right.left,
    #                           value=5, height=0, balance=0)
    #
    #     """
    #     Second part, inserting and removing with rotation
    #
    #     inserting 5, 10:
    #       5
    #        \
    #         10
    #     """
    #     avl = AVLTree()
    #     avl.insert(avl.origin, 5)
    #     avl.insert(avl.origin, 10)
    #     self.assertEqual(2, avl.size)
    #     self.assertEqual(5, avl.min(avl.origin).value)
    #     self.assertEqual(10, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=5, height=1, balance=-1)
    #     check_node_properties(avl.origin.right, value=10, height=0, balance=0)
    #     """
    #     Current AVL tree:
    #       5
    #        \
    #         10
    #     After inserting 8, 9, 12
    #        8
    #      /   \
    #     5    10
    #         /  \
    #        9   12
    #     """
    #     avl.insert(avl.origin, 8)
    #     avl.insert(avl.origin, 9)
    #     avl.insert(avl.origin, 12)
    #     self.assertEqual(5, avl.size)
    #     self.assertEqual(5, avl.min(avl.origin).value)
    #     self.assertEqual(12, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=8, height=2, balance=-1)
    #     check_node_properties(avl.origin.right, value=10, height=1, balance=0)
    #     check_node_properties(avl.origin.right.left,
    #                           value=9, height=0, balance=0)
    #     check_node_properties(avl.origin.right.right,
    #                           value=12, height=0, balance=0)
    #     check_node_properties(avl.origin.left, value=5, height=0, balance=0)
    #
    #     """
    #     Current AVL tree:
    #        8
    #      /   \
    #     5    10
    #         /  \
    #        9   12
    #     After inserting 3, 1, 2
    #            8
    #        /       \
    #       3        10
    #      /  \     /   \
    #     1    5   9    12
    #       \
    #        2
    #     """
    #     avl.insert(avl.origin, 3)
    #     avl.insert(avl.origin, 1)
    #     avl.insert(avl.origin, 2)
    #     self.assertEqual(8, avl.size)
    #     self.assertEqual(1, avl.min(avl.origin).value)
    #     self.assertEqual(12, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=8, height=3, balance=1)
    #     check_node_properties(avl.origin.right, value=10, height=1, balance=0)
    #     check_node_properties(avl.origin.right.left,
    #                           value=9, height=0, balance=0)
    #     check_node_properties(avl.origin.right.right,
    #                           value=12, height=0, balance=0)
    #     check_node_properties(avl.origin.left, value=3, height=2, balance=1)
    #     check_node_properties(avl.origin.left.left,
    #                           value=1, height=1, balance=-1)
    #     check_node_properties(avl.origin.left.left.right,
    #                           value=2, height=0, balance=0)
    #     check_node_properties(avl.origin.left.right,
    #                           value=5, height=0, balance=0)
    #     """
    #     Current AVL tree:
    #            8
    #        /       \
    #       3        10
    #      /  \     /   \
    #     1    5   9    12
    #       \
    #        2
    #     After removing 5
    #            8
    #        /       \
    #       2        10
    #      /  \     /   \
    #     1    3   9    12
    #     """
    #     avl.remove(avl.origin, 5)
    #     self.assertEqual(7, avl.size)
    #     self.assertEqual(1, avl.min(avl.origin).value)
    #     self.assertEqual(12, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=8, height=2, balance=0)
    #     check_node_properties(avl.origin.right, value=10, height=1, balance=0)
    #     check_node_properties(avl.origin.right.left,
    #                           value=9, height=0, balance=0)
    #     check_node_properties(avl.origin.right.right,
    #                           value=12, height=0, balance=0)
    #     check_node_properties(avl.origin.left, value=2, height=1, balance=0)
    #     check_node_properties(avl.origin.left.left,
    #                           value=1, height=0, balance=0)
    #     check_node_properties(avl.origin.left.right,
    #                           value=3, height=0, balance=0)
    #     """
    #     Current AVL tree:
    #           8
    #        /     \
    #       2      10
    #      /  \   /   \
    #     1    3 9    12
    #     After inserting 5, 13, 0, 7, 20
    #            8
    #         /       \
    #        2         10
    #       /  \      /   \
    #      1    5     9    13
    #     /    / \        /  \
    #     0   3   7     12    20
    #     """
    #     avl.insert(avl.origin, 5)
    #     avl.insert(avl.origin, 13)
    #     avl.insert(avl.origin, 0)
    #     avl.insert(avl.origin, 7)
    #     avl.insert(avl.origin, 20)
    #     self.assertEqual(12, avl.size)
    #     self.assertEqual(0, avl.min(avl.origin).value)
    #     self.assertEqual(20, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=8, height=3, balance=0)
    #
    #     check_node_properties(avl.origin.right, value=10, height=2, balance=-1)
    #     check_node_properties(avl.origin.right.left,
    #                           value=9, height=0, balance=0)
    #     check_node_properties(avl.origin.right.right,
    #                           value=13, height=1, balance=0)
    #     check_node_properties(avl.origin.right.right.right,
    #                           value=20, height=0, balance=0)
    #     check_node_properties(avl.origin.right.right.left,
    #                           value=12, height=0, balance=0)
    #
    #     check_node_properties(avl.origin.left, value=2, height=2, balance=0)
    #     check_node_properties(avl.origin.left.left,
    #                           value=1, height=1, balance=1)
    #     check_node_properties(avl.origin.left.left.left,
    #                           value=0, height=0, balance=0)
    #     check_node_properties(avl.origin.left.right,
    #                           value=5, height=1, balance=-0)
    #     check_node_properties(avl.origin.left.right.right,
    #                           value=7, height=0, balance=0)
    #     check_node_properties(avl.origin.left.right.left,
    #                           value=3, height=0, balance=0)
    #
    #     """
    #     Current AVL tree:
    #            8
    #         /       \
    #        2         10
    #       /  \      /   \
    #      1    5     9    13
    #     /    / \        /  \
    #     0   3   7     12    20
    #     After removing 1, 9
    #            8
    #         /       \
    #        2         13
    #       /  \      /   \
    #      0    5   10     20
    #          / \     \
    #          3   7    12
    #     """
    #     avl.remove(avl.origin, 1)
    #     avl.remove(avl.origin, 9)
    #     self.assertEqual(10, avl.size)
    #     self.assertEqual(0, avl.min(avl.origin).value)
    #     self.assertEqual(20, avl.max(avl.origin).value)
    #     # Properties of all nodes
    #     check_node_properties(avl.origin, value=8, height=3, balance=0)
    #
    #     check_node_properties(avl.origin.right, value=13, height=2, balance=1)
    #     check_node_properties(avl.origin.right.left,
    #                           value=10, height=1, balance=-1)
    #     check_node_properties(avl.origin.right.left.right,
    #                           value=12, height=0, balance=0)
    #     check_node_properties(avl.origin.right.right,
    #                           value=20, height=0, balance=0)
    #
    #     check_node_properties(avl.origin.left, value=2, height=2, balance=-1)
    #     check_node_properties(avl.origin.left.left,
    #                           value=0, height=0, balance=0)
    #     check_node_properties(avl.origin.left.right,
    #                           value=5, height=1, balance=-0)
    #     check_node_properties(avl.origin.left.right.right,
    #                           value=7, height=0, balance=0)
    #     check_node_properties(avl.origin.left.right.left,
    #                           value=3, height=0, balance=0)
    #
    #     """
    #     Part Three
    #     Everything but random, checking properties of tree only
    #     """
    #     random.seed(331)
    #     """
    #     randomly insert, and remove alphabet to avl tree
    #     """
    #
    #     def random_order_1(character=True):
    #         order = random.randint(0, 2)
    #         if not len(existing_value) or (order and (not character or avl.size < 26)):
    #             if character:
    #                 inserted = chr(ord('a') + random.randint(0, 25))
    #                 while inserted in existing_value:
    #                     inserted = chr(ord('a') + random.randint(0, 25))
    #             else:
    #                 inserted = random.randint(0, 100000)
    #             avl.insert(avl.origin, inserted)
    #             existing_value[inserted] = 1
    #         else:
    #             removed = random.choice(list(existing_value.keys()))
    #             avl.remove(avl.origin, removed)
    #             existing_value.pop(removed)
    #
    #     existing_value = {}
    #     avl = AVLTree()
    #     for _ in range(30):
    #         random_order_1()
    #     self.assertEqual('a', avl.min(avl.origin).value)
    #     self.assertEqual('y', avl.max(avl.origin).value)
    #     # inorder test
    #     expected = ['a', 'b', 'd', 'f', 'g', 'i', 'k',
    #                 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y']
    #     generator = avl.inorder(avl.origin)
    #     self.assertIsInstance(generator, types.GeneratorType)
    #     for num in expected:
    #         node = next(generator)
    #         self.assertIsInstance(node, Node)
    #         self.assertEqual(num, node.value)
    #     with self.assertRaises(StopIteration):
    #         next(generator)
    #
    #     expected = ['p', 'f', 'b', 'a', 'd', 'k', 'i',
    #                 'g', 'o', 't', 'r', 'q', 's', 'w', 'v', 'y']
    #     generator = avl.preorder(avl.origin)
    #     self.assertIsInstance(generator, types.GeneratorType)
    #     for num in expected:
    #         node = next(generator)
    #         self.assertIsInstance(node, Node)
    #         self.assertEqual(num, node.value)
    #     with self.assertRaises(StopIteration):
    #         next(generator)
    #
    #     expected = ['a', 'd', 'b', 'g', 'i', 'o', 'k',
    #                 'f', 'q', 's', 'r', 'v', 'y', 'w', 't', 'p']
    #     generator = avl.postorder(avl.origin)
    #     self.assertIsInstance(generator, types.GeneratorType)
    #     for num in expected:
    #         node = next(generator)
    #         self.assertIsInstance(node, Node)
    #         self.assertEqual(num, node.value)
    #     with self.assertRaises(StopIteration):
    #         next(generator)
    #
    #     existing_value.clear()
    #     avl = AVLTree()
    #     for _ in range(150):
    #         random_order_1(character=False)
    #     self.assertEqual(3113, avl.min(avl.origin).value)
    #     self.assertEqual(99254, avl.max(avl.origin).value)
    #     # inorder test
    #     expected = [3113, 4842, 8476, 9661, 9691, 9849, 12004, 13818, 16748, 19125,
    #                 20633, 20815, 20930, 25633, 25790, 28476, 29509, 30303, 30522,
    #                 32151, 32253, 35293, 35691, 36623, 37047, 40980, 41185, 42559,
    #                 43298, 44521, 44698, 45027, 46070, 46204, 46876, 49122, 51761,
    #                 51864, 54480, 55579, 56007, 56230, 58594, 59094, 59240, 59245,
    #                 61029, 61837, 63796, 66866, 69402, 69498, 70575, 70733, 74185,
    #                 74291, 74893, 76608, 76840, 77762, 78162, 78215, 80089, 80883,
    #                 85118, 86927, 88662, 91673, 94661, 94848, 98575, 99254]
    #
    #     generator = avl.inorder(avl.origin)
    #     self.assertIsInstance(generator, types.GeneratorType)
    #     for num in expected:
    #         node = next(generator)
    #         self.assertIsInstance(node, Node)
    #         self.assertEqual(num, node.value)
    #     with self.assertRaises(StopIteration):
    #         next(generator)
    #
    #     expected = [49122, 35691, 20815, 9849, 4842, 3113, 9661, 8476, 9691, 19125,
    #                 13818, 12004, 16748, 20633, 30303, 25790, 20930, 25633, 29509,
    #                 28476, 32253, 30522, 32151, 35293, 43298, 37047, 36623, 41185,
    #                 40980, 42559, 46070, 44698, 44521, 45027, 46204, 46876, 69498,
    #                 58594, 54480, 51761, 51864, 56007, 55579, 56230, 59245, 59240,
    #                 59094, 61837, 61029, 66866, 63796, 69402, 80883, 76840, 74185,
    #                 70575, 70733, 74893, 74291, 76608, 78162, 77762, 80089, 78215,
    #                 91673, 86927, 85118, 88662, 94848, 94661, 99254, 98575]
    #
    #     generator = avl.preorder(avl.origin)
    #     self.assertIsInstance(generator, types.GeneratorType)
    #     for num in expected:
    #         node = next(generator)
    #         self.assertIsInstance(node, Node)
    #         self.assertEqual(num, node.value)
    #     with self.assertRaises(StopIteration):
    #         next(generator)
    #
    #     expected = [3113, 8476, 9691, 9661, 4842, 12004, 16748, 13818,
    #                 20633, 19125, 9849, 25633, 20930, 28476, 29509,
    #                 25790, 32151, 30522, 35293, 32253, 30303, 20815,
    #                 36623, 40980, 42559, 41185, 37047, 44521, 45027,
    #                 44698, 46876, 46204, 46070, 43298, 35691, 51864,
    #                 51761, 55579, 56230, 56007, 54480, 59094, 59240,
    #                 61029, 63796, 69402, 66866, 61837, 59245, 58594,
    #                 70733, 70575, 74291, 76608, 74893, 74185, 77762,
    #                 78215, 80089, 78162, 76840, 85118, 88662, 86927,
    #                 94661, 98575, 99254, 94848, 91673, 80883, 69498, 49122]
    #
    #     generator = avl.postorder(avl.origin)
    #     self.assertIsInstance(generator, types.GeneratorType)
    #     for num in expected:
    #         node = next(generator)
    #         self.assertIsInstance(node, Node)
    #         self.assertEqual(num, node.value)
    #     with self.assertRaises(StopIteration):
    #         next(generator)

    def test_application(self):
        db = AVLDatabase()

        # (1) Empty table case
        db.query("Create for me an awesome table thingy or whatever, table1, "
                 "and give it the attributes length, width, height, mass, temperature. Make it snappy!")

        actual = db.query("Show me from the table, table1, like, everything.")
        expected = [['index', 'length', 'width', 'height', 'mass', 'temperature']]
        self.assertEqual(actual, expected)

        actual = db.query("Show me from the table, table1, the latest row, okay?")
        self.assertEqual(actual, expected)

        actual = db.query("Show me the oldest row from the table, table1, got it?")
        self.assertEqual(actual, expected)

        # (2) Multiple tables + single row case
        db.query("create, table2, attributes annual revenue, annual expenses, account type.")

        db.query("INSERT INTO MY LOVELY NEW TABLE, TABLE2, THESE HERE VALUES: 100306, 64023, SAVINGS "
                 "WITH CORRESPONDING ATTRIBUTES ANNUAL REVENUE, ANNUAL EXPENSES, ACCOUNT TYPE.")

        actual = db.query("Show me, table2, everything.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [0, '100306', '64023', 'savings']]
        self.assertEqual(actual, expected)

        actual = db.query("Show me, table2, latest.")
        self.assertEqual(actual, expected)

        actual = db.query("Show me, table2, oldest.")
        self.assertEqual(actual, expected)

        # (3) Insertion but with different attribute order than at creation
        db.query("insert into, table2, values: checking, 57821, 130012 "
                 "with attributes account type, annual revenue, annual expenses.")
        actual = db.query("Show me, table2, everything.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [0, '100306', '64023', 'savings'],
                    [1, '57821', '130012', 'checking']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, latest.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [1, '57821', '130012', 'checking']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, oldest.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [0, '100306', '64023', 'savings']]
        self.assertEqual(actual, expected)

        # (4a) Test removal
        db.query("Remove from the table that I call, table2, those dang indices 1.")
        actual = db.query("show me, table2, everything.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [0, '100306', '64023', 'savings']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, latest.")
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, oldest.")
        self.assertEqual(actual, expected)

        # (4b) Test emptying removals
        db.query("remove, table2, indices 0.")
        actual = db.query("show me, table2, everything.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, latest.")
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, oldest.")
        self.assertEqual(actual, expected)

        # (5a) Test index after removals + multiple insertions/removals with one query
        # insertions
        db.query("insert into, table2, values: checking, 40000, 64000; savings, 500, 625; checking, 1230023, 512348 "
                 "with attributes account type, annual expenses, annual revenue.")
        actual = db.query("show me, table2, everything.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [2, '64000', '40000', 'checking'],
                    [3, '625', '500', 'savings'],
                    [4, '512348', '1230023', 'checking']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, latest.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [4, '512348', '1230023', 'checking']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, oldest.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [2, '64000', '40000', 'checking']]
        self.assertEqual(actual, expected)

        # removals
        db.query("remove, table2, indices 4, 2.")
        actual = db.query("show me, table2, everything.")
        expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
                    [3, '625', '500', 'savings']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, latest.")
        self.assertEqual(actual, expected)

        actual = db.query("show me, table2, oldest.")
        self.assertEqual(actual, expected)

        # (5b) Test multiple removals + removals on empty table
        # removing nonexistent indices shouldn't throw an exception
        db.query("Remove from the table, table1, like, the indices 5, 3, 2, 6, 1.")  # this uses table1, not table2!

        # (6) Large comprehensive test case using table1
        random.seed(331)

        # insertions
        query_start = "insert into, table1, values: "
        query_end = " with attributes height, length, mass, temperature, width."
        row_values = ""
        for i in range(1000):
            row_values += ', '.join([str(random.randint(1, 1000)) for j in range(5)]) + '; '
        row_values = row_values[:-2]
        query = query_start + row_values + query_end
        db.query(query)

        actual = db.query("show me, table1, everything.")
        # IMPORTANT!
        # click the little down arrow thing on the left of this line to collapse the list in PyCharm!
        expected = [['index', 'length', 'width', 'height', 'mass', 'temperature'],
                    [0, '750', '176', '856', '329', '893'], [1, '892', '106', '254', '861', '648'],
                    [2, '488', '988', '664', '479', '638'], [3, '680', '743', '958', '345', '598'],
                    [4, '764', '682', '888', '427', '889'], [5, '443', '728', '838', '786', '867'],
                    [6, '626', '444', '902', '430', '42'], [7, '290', '744', '557', '922', '539'],
                    [8, '788', '418', '613', '339', '821'], [9, '973', '236', '555', '844', '681'],
                    [10, '148', '635', '765', '321', '783'], [11, '173', '597', '611', '84', '706'],
                    [12, '984', '284', '642', '366', '752'], [13, '917', '716', '551', '523', '945'],
                    [14, '517', '659', '931', '42', '24'], [15, '456', '141', '724', '34', '667'],
                    [16, '521', '759', '485', '555', '543'], [17, '820', '902', '195', '105', '317'],
                    [18, '938', '37', '701', '494', '796'], [19, '36', '978', '345', '583', '698'],
                    [20, '201', '884', '38', '623', '704'], [21, '877', '281', '727', '323', '354'],
                    [22, '992', '787', '106', '214', '177'], [23, '51', '215', '513', '150', '380'],
                    [24, '133', '715', '778', '854', '176'], [25, '38', '851', '249', '778', '826'],
                    [26, '292', '297', '24', '822', '973'], [27, '537', '517', '164', '156', '698'],
                    [28, '47', '634', '206', '35', '466'], [29, '782', '683', '677', '132', '747'],
                    [30, '666', '572', '964', '32', '258'], [31, '334', '667', '202', '41', '509'],
                    [32, '109', '117', '518', '573', '149'], [33, '997', '38', '756', '880', '831'],
                    [34, '468', '601', '545', '286', '531'], [35, '42', '268', '518', '530', '303'],
                    [36, '628', '279', '462', '608', '354'], [37, '392', '91', '882', '444', '332'],
                    [38, '983', '951', '418', '632', '651'], [39, '343', '611', '444', '535', '449'],
                    [40, '277', '737', '430', '141', '241'], [41, '480', '989', '172', '940', '315'],
                    [42, '360', '339', '910', '148', '263'], [43, '37', '357', '484', '583', '67'],
                    [44, '170', '629', '394', '578', '30'], [45, '752', '33', '799', '484', '250'],
                    [46, '218', '517', '760', '456', '543'], [47, '410', '843', '717', '454', '603'],
                    [48, '266', '886', '239', '463', '725'], [49, '463', '417', '974', '125', '142'],
                    [50, '576', '461', '581', '523', '918'], [51, '871', '71', '438', '70', '407'],
                    [52, '903', '10', '162', '322', '328'], [53, '121', '786', '354', '954', '946'],
                    [54, '603', '445', '393', '791', '81'], [55, '742', '384', '354', '975', '686'],
                    [56, '287', '381', '750', '452', '371'], [57, '321', '217', '231', '616', '447'],
                    [58, '606', '39', '889', '907', '562'], [59, '95', '956', '54', '864', '632'],
                    [60, '578', '143', '752', '621', '506'], [61, '808', '779', '295', '607', '84'],
                    [62, '419', '316', '48', '761', '440'], [63, '301', '783', '580', '874', '955'],
                    [64, '213', '676', '458', '826', '866'], [65, '986', '578', '498', '540', '350'],
                    [66, '996', '986', '78', '951', '631'], [67, '251', '501', '626', '493', '58'],
                    [68, '552', '131', '373', '10', '945'], [69, '163', '21', '717', '615', '568'],
                    [70, '604', '59', '472', '322', '892'], [71, '351', '665', '116', '162', '595'],
                    [72, '693', '628', '386', '529', '290'], [73, '301', '986', '150', '776', '25'],
                    [74, '515', '301', '176', '426', '896'], [75, '807', '834', '405', '501', '361'],
                    [76, '435', '406', '521', '790', '638'], [77, '586', '711', '580', '597', '38'],
                    [78, '793', '682', '360', '363', '333'], [79, '738', '974', '237', '25', '959'],
                    [80, '612', '793', '480', '985', '523'], [81, '277', '710', '477', '740', '310'],
                    [82, '680', '69', '274', '299', '77'], [83, '471', '198', '916', '252', '907'],
                    [84, '390', '116', '71', '367', '963'], [85, '907', '381', '173', '180', '121'],
                    [86, '56', '932', '276', '514', '641'], [87, '929', '36', '815', '462', '16'],
                    [88, '579', '437', '942', '543', '60'], [89, '348', '893', '486', '866', '731'],
                    [90, '756', '713', '252', '76', '929'], [91, '870', '474', '499', '306', '108'],
                    [92, '150', '928', '321', '962', '75'], [93, '553', '359', '628', '559', '131'],
                    [94, '277', '482', '94', '76', '968'], [95, '350', '223', '599', '854', '887'],
                    [96, '632', '201', '865', '352', '655'], [97, '771', '362', '395', '616', '950'],
                    [98, '714', '208', '65', '910', '800'], [99, '215', '119', '979', '437', '173'],
                    [100, '322', '735', '618', '642', '139'], [101, '129', '667', '536', '552', '787'],
                    [102, '423', '187', '51', '291', '959'], [103, '496', '701', '559', '505', '712'],
                    [104, '350', '102', '744', '350', '31'], [105, '417', '341', '489', '723', '97'],
                    [106, '487', '722', '178', '640', '756'], [107, '589', '393', '129', '859', '513'],
                    [108, '120', '371', '147', '482', '23'], [109, '491', '617', '699', '651', '247'],
                    [110, '90', '955', '803', '598', '8'], [111, '211', '523', '186', '316', '437'],
                    [112, '881', '492', '460', '498', '300'], [113, '762', '975', '145', '89', '971'],
                    [114, '5', '190', '393', '639', '383'], [115, '871', '794', '11', '678', '182'],
                    [116, '110', '162', '988', '752', '564'], [117, '919', '585', '975', '178', '197'],
                    [118, '190', '674', '608', '589', '902'], [119, '32', '519', '232', '508', '148'],
                    [120, '216', '583', '173', '638', '605'], [121, '464', '840', '43', '480', '851'],
                    [122, '559', '811', '276', '619', '171'], [123, '410', '612', '787', '677', '323'],
                    [124, '885', '805', '557', '300', '347'], [125, '413', '355', '403', '617', '29'],
                    [126, '94', '433', '621', '419', '870'], [127, '277', '248', '304', '665', '779'],
                    [128, '799', '14', '744', '920', '226'], [129, '745', '893', '480', '740', '635'],
                    [130, '657', '489', '4', '499', '440'], [131, '760', '865', '283', '872', '798'],
                    [132, '441', '109', '779', '122', '138'], [133, '835', '751', '783', '470', '276'],
                    [134, '34', '629', '189', '165', '999'], [135, '849', '285', '7', '870', '969'],
                    [136, '574', '305', '496', '326', '196'], [137, '696', '68', '558', '995', '192'],
                    [138, '249', '594', '41', '311', '109'], [139, '947', '373', '283', '495', '121'],
                    [140, '523', '520', '589', '730', '386'], [141, '500', '898', '989', '125', '791'],
                    [142, '272', '995', '99', '525', '294'], [143, '36', '63', '300', '213', '924'],
                    [144, '530', '875', '394', '290', '156'], [145, '17', '690', '975', '882', '440'],
                    [146, '624', '829', '422', '121', '397'], [147, '854', '499', '6', '857', '406'],
                    [148, '581', '728', '737', '178', '911'], [149, '278', '544', '73', '488', '120'],
                    [150, '702', '238', '83', '225', '691'], [151, '348', '165', '696', '705', '981'],
                    [152, '756', '293', '384', '534', '475'], [153, '760', '918', '318', '969', '428'],
                    [154, '866', '311', '357', '308', '654'], [155, '874', '270', '366', '654', '240'],
                    [156, '257', '223', '638', '276', '850'], [157, '347', '678', '696', '671', '647'],
                    [158, '263', '793', '904', '563', '941'], [159, '60', '384', '734', '909', '601'],
                    [160, '612', '456', '777', '548', '851'], [161, '656', '277', '30', '397', '564'],
                    [162, '13', '696', '287', '824', '473'], [163, '239', '83', '323', '889', '306'],
                    [164, '279', '27', '641', '199', '870'], [165, '809', '125', '228', '369', '971'],
                    [166, '569', '354', '835', '754', '602'], [167, '147', '344', '370', '851', '667'],
                    [168, '229', '93', '806', '950', '954'], [169, '400', '114', '280', '789', '79'],
                    [170, '136', '467', '64', '585', '840'], [171, '872', '645', '492', '999', '480'],
                    [172, '761', '14', '895', '428', '63'], [173, '305', '63', '206', '526', '397'],
                    [174, '165', '266', '565', '62', '336'], [175, '274', '818', '870', '346', '366'],
                    [176, '696', '607', '9', '131', '415'], [177, '338', '388', '94', '24', '407'],
                    [178, '852', '378', '278', '92', '19'], [179, '347', '919', '515', '982', '827'],
                    [180, '964', '231', '780', '987', '277'], [181, '300', '251', '352', '699', '352'],
                    [182, '283', '84', '178', '746', '880'], [183, '220', '593', '190', '278', '525'],
                    [184, '553', '572', '790', '125', '312'], [185, '674', '251', '414', '712', '212'],
                    [186, '136', '442', '899', '260', '474'], [187, '420', '993', '761', '707', '419'],
                    [188, '456', '775', '45', '570', '9'], [189, '3', '377', '646', '676', '879'],
                    [190, '163', '1000', '997', '213', '806'], [191, '44', '18', '877', '736', '880'],
                    [192, '181', '976', '117', '43', '377'], [193, '3', '559', '931', '312', '158'],
                    [194, '880', '856', '578', '627', '129'], [195, '248', '672', '697', '425', '145'],
                    [196, '819', '672', '815', '742', '751'], [197, '985', '519', '991', '126', '472'],
                    [198, '244', '108', '923', '535', '56'], [199, '453', '63', '233', '871', '141'],
                    [200, '110', '716', '536', '593', '51'], [201, '841', '952', '886', '295', '770'],
                    [202, '483', '35', '98', '682', '694'], [203, '147', '921', '368', '268', '962'],
                    [204, '407', '947', '431', '831', '958'], [205, '101', '73', '415', '682', '520'],
                    [206, '639', '673', '167', '74', '337'], [207, '9', '64', '870', '230', '77'],
                    [208, '930', '116', '632', '54', '945'], [209, '179', '340', '726', '626', '35'],
                    [210, '459', '769', '974', '399', '585'], [211, '851', '413', '842', '127', '604'],
                    [212, '653', '817', '482', '280', '507'], [213, '795', '693', '551', '185', '504'],
                    [214, '498', '209', '438', '995', '978'], [215, '213', '42', '218', '141', '658'],
                    [216, '78', '134', '327', '734', '113'], [217, '430', '747', '972', '155', '329'],
                    [218, '394', '54', '246', '428', '72'], [219, '318', '371', '359', '639', '46'],
                    [220, '671', '312', '178', '913', '998'], [221, '409', '383', '390', '570', '719'],
                    [222, '102', '672', '632', '630', '535'], [223, '623', '887', '724', '823', '787'],
                    [224, '360', '8', '369', '727', '153'], [225, '64', '574', '867', '186', '105'],
                    [226, '90', '885', '203', '224', '68'], [227, '645', '436', '405', '509', '90'],
                    [228, '295', '701', '388', '866', '53'], [229, '775', '951', '697', '50', '131'],
                    [230, '235', '535', '371', '518', '466'], [231, '696', '964', '750', '14', '242'],
                    [232, '942', '527', '575', '344', '880'], [233, '377', '182', '847', '632', '104'],
                    [234, '637', '428', '488', '805', '484'], [235, '432', '563', '241', '324', '79'],
                    [236, '779', '19', '550', '172', '967'], [237, '129', '797', '554', '230', '475'],
                    [238, '375', '116', '928', '456', '673'], [239, '616', '75', '885', '69', '824'],
                    [240, '842', '105', '632', '310', '998'], [241, '624', '87', '292', '357', '151'],
                    [242, '644', '735', '514', '681', '837'], [243, '115', '47', '138', '899', '809'],
                    [244, '989', '224', '157', '408', '10'], [245, '209', '314', '305', '729', '324'],
                    [246, '761', '375', '28', '421', '777'], [247, '779', '281', '979', '116', '350'],
                    [248, '363', '12', '937', '15', '626'], [249, '230', '246', '746', '665', '757'],
                    [250, '949', '66', '752', '46', '687'], [251, '1', '833', '989', '692', '648'],
                    [252, '626', '289', '648', '142', '441'], [253, '29', '239', '564', '162', '965'],
                    [254, '187', '650', '886', '732', '822'], [255, '87', '289', '934', '720', '222'],
                    [256, '583', '316', '52', '171', '581'], [257, '692', '215', '578', '979', '560'],
                    [258, '475', '608', '8', '632', '754'], [259, '866', '7', '592', '141', '984'],
                    [260, '600', '703', '280', '424', '893'], [261, '46', '707', '567', '739', '63'],
                    [262, '19', '244', '608', '707', '574'], [263, '103', '158', '86', '87', '584'],
                    [264, '959', '307', '302', '695', '157'], [265, '980', '617', '860', '738', '550'],
                    [266, '101', '772', '826', '165', '207'], [267, '367', '277', '962', '406', '571'],
                    [268, '533', '546', '760', '440', '257'], [269, '432', '681', '397', '457', '744'],
                    [270, '146', '772', '641', '780', '503'], [271, '906', '999', '507', '995', '453'],
                    [272, '587', '362', '772', '236', '70'], [273, '335', '773', '236', '709', '506'],
                    [274, '351', '703', '556', '568', '521'], [275, '219', '789', '337', '296', '915'],
                    [276, '309', '727', '787', '423', '205'], [277, '470', '103', '312', '447', '416'],
                    [278, '538', '154', '660', '518', '615'], [279, '884', '92', '122', '547', '109'],
                    [280, '200', '530', '115', '193', '12'], [281, '839', '325', '295', '919', '338'],
                    [282, '292', '34', '196', '258', '143'], [283, '13', '148', '70', '292', '751'],
                    [284, '2', '240', '656', '213', '439'], [285, '443', '334', '180', '631', '149'],
                    [286, '719', '487', '521', '90', '250'], [287, '106', '146', '986', '875', '573'],
                    [288, '705', '17', '402', '24', '572'], [289, '322', '854', '38', '616', '300'],
                    [290, '391', '414', '886', '917', '289'], [291, '18', '277', '228', '744', '695'],
                    [292, '472', '252', '905', '931', '543'], [293, '300', '477', '461', '332', '79'],
                    [294, '125', '521', '984', '687', '820'], [295, '771', '686', '912', '174', '317'],
                    [296, '828', '740', '65', '908', '615'], [297, '93', '647', '972', '197', '249'],
                    [298, '278', '89', '567', '426', '233'], [299, '724', '938', '16', '158', '173'],
                    [300, '105', '460', '981', '169', '528'], [301, '791', '168', '411', '283', '934'],
                    [302, '801', '114', '581', '964', '447'], [303, '661', '372', '276', '949', '281'],
                    [304, '663', '592', '705', '660', '831'], [305, '96', '754', '409', '146', '456'],
                    [306, '754', '38', '84', '504', '431'], [307, '508', '272', '105', '655', '546'],
                    [308, '69', '231', '278', '245', '91'], [309, '258', '643', '13', '125', '589'],
                    [310, '906', '683', '868', '510', '433'], [311, '606', '634', '554', '631', '294'],
                    [312, '808', '275', '837', '279', '160'], [313, '656', '477', '481', '417', '679'],
                    [314, '555', '718', '211', '846', '116'], [315, '549', '960', '786', '891', '281'],
                    [316, '991', '367', '48', '223', '246'], [317, '946', '444', '414', '228', '716'],
                    [318, '872', '73', '226', '866', '991'], [319, '48', '567', '406', '45', '237'],
                    [320, '978', '721', '328', '797', '469'], [321, '563', '242', '281', '173', '131'],
                    [322, '123', '534', '522', '337', '282'], [323, '46', '113', '956', '172', '867'],
                    [324, '920', '831', '364', '357', '252'], [325, '168', '816', '156', '509', '597'],
                    [326, '82', '824', '873', '681', '274'], [327, '481', '429', '817', '750', '563'],
                    [328, '932', '678', '154', '107', '788'], [329, '69', '449', '386', '906', '716'],
                    [330, '657', '101', '57', '689', '501'], [331, '86', '832', '205', '902', '164'],
                    [332, '805', '183', '11', '284', '827'], [333, '572', '267', '461', '159', '140'],
                    [334, '499', '753', '166', '99', '952'], [335, '226', '946', '236', '989', '264'],
                    [336, '96', '693', '588', '766', '34'], [337, '5', '749', '439', '168', '21'],
                    [338, '230', '605', '682', '904', '347'], [339, '159', '237', '6', '814', '362'],
                    [340, '333', '237', '4', '462', '794'], [341, '49', '853', '676', '544', '646'],
                    [342, '968', '120', '905', '923', '72'], [343, '174', '29', '598', '830', '960'],
                    [344, '585', '486', '23', '388', '444'], [345, '854', '16', '376', '700', '79'],
                    [346, '420', '91', '670', '892', '875'], [347, '429', '131', '221', '276', '840'],
                    [348, '542', '638', '648', '977', '400'], [349, '282', '644', '730', '781', '671'],
                    [350, '612', '162', '747', '301', '355'], [351, '138', '955', '632', '372', '664'],
                    [352, '601', '388', '771', '954', '55'], [353, '771', '503', '26', '117', '142'],
                    [354, '823', '651', '20', '151', '812'], [355, '248', '91', '186', '505', '515'],
                    [356, '14', '21', '726', '213', '667'], [357, '91', '281', '731', '445', '607'],
                    [358, '798', '518', '78', '840', '178'], [359, '498', '570', '74', '152', '269'],
                    [360, '126', '657', '710', '454', '947'], [361, '893', '748', '432', '656', '579'],
                    [362, '708', '638', '861', '733', '573'], [363, '482', '931', '860', '54', '443'],
                    [364, '307', '930', '341', '158', '512'], [365, '341', '213', '877', '641', '364'],
                    [366, '233', '762', '648', '331', '174'], [367, '256', '942', '905', '603', '663'],
                    [368, '664', '277', '443', '699', '345'], [369, '503', '195', '888', '203', '344'],
                    [370, '985', '926', '381', '538', '430'], [371, '553', '479', '126', '200', '230'],
                    [372, '357', '902', '75', '847', '47'], [373, '888', '999', '826', '881', '702'],
                    [374, '472', '435', '747', '153', '279'], [375, '994', '966', '333', '260', '310'],
                    [376, '21', '296', '156', '359', '925'], [377, '366', '886', '823', '170', '747'],
                    [378, '175', '416', '342', '448', '89'], [379, '545', '877', '988', '795', '579'],
                    [380, '589', '47', '692', '218', '162'], [381, '239', '314', '939', '159', '699'],
                    [382, '369', '223', '640', '463', '29'], [383, '348', '282', '758', '425', '288'],
                    [384, '626', '182', '513', '123', '682'], [385, '403', '156', '815', '575', '213'],
                    [386, '75', '841', '923', '422', '507'], [387, '870', '241', '556', '951', '502'],
                    [388, '723', '933', '973', '844', '328'], [389, '127', '549', '323', '826', '654'],
                    [390, '543', '989', '900', '599', '464'], [391, '796', '282', '478', '86', '924'],
                    [392, '823', '620', '647', '293', '34'], [393, '273', '603', '213', '553', '975'],
                    [394, '891', '361', '229', '417', '407'], [395, '744', '137', '333', '893', '963'],
                    [396, '157', '8', '19', '742', '77'], [397, '45', '92', '679', '917', '22'],
                    [398, '446', '947', '293', '445', '604'], [399, '865', '651', '162', '114', '33'],
                    [400, '586', '670', '714', '177', '494'], [401, '395', '563', '676', '987', '251'],
                    [402, '613', '666', '969', '230', '634'], [403, '555', '839', '205', '204', '588'],
                    [404, '853', '238', '757', '917', '30'], [405, '314', '627', '240', '462', '131'],
                    [406, '942', '942', '157', '206', '597'], [407, '769', '471', '55', '442', '320'],
                    [408, '339', '81', '861', '169', '482'], [409, '418', '740', '445', '864', '365'],
                    [410, '314', '341', '396', '595', '990'], [411, '829', '346', '825', '485', '434'],
                    [412, '781', '792', '189', '854', '671'], [413, '684', '427', '513', '129', '229'],
                    [414, '165', '483', '29', '451', '996'], [415, '59', '685', '359', '834', '285'],
                    [416, '393', '753', '527', '34', '509'], [417, '296', '225', '542', '974', '816'],
                    [418, '149', '649', '8', '485', '421'], [419, '333', '460', '615', '150', '552'],
                    [420, '897', '277', '36', '447', '683'], [421, '449', '272', '16', '611', '447'],
                    [422, '170', '973', '796', '158', '812'], [423, '763', '568', '461', '239', '530'],
                    [424, '709', '785', '194', '574', '156'], [425, '774', '313', '767', '153', '32'],
                    [426, '706', '260', '408', '268', '876'], [427, '768', '493', '458', '268', '557'],
                    [428, '352', '962', '342', '828', '968'], [429, '54', '254', '810', '507', '599'],
                    [430, '947', '285', '204', '860', '500'], [431, '28', '437', '511', '188', '921'],
                    [432, '515', '355', '29', '804', '153'], [433, '577', '847', '380', '379', '410'],
                    [434, '21', '370', '710', '698', '666'], [435, '671', '755', '331', '703', '168'],
                    [436, '900', '289', '651', '828', '201'], [437, '780', '847', '763', '196', '95'],
                    [438, '207', '133', '431', '380', '761'], [439, '882', '42', '54', '394', '150'],
                    [440, '408', '290', '522', '812', '2'], [441, '38', '818', '281', '195', '569'],
                    [442, '359', '817', '219', '980', '688'], [443, '172', '322', '832', '695', '413'],
                    [444, '482', '797', '860', '716', '803'], [445, '128', '627', '355', '212', '543'],
                    [446, '848', '209', '18', '321', '302'], [447, '644', '307', '629', '711', '444'],
                    [448, '877', '329', '713', '590', '503'], [449, '277', '168', '32', '923', '843'],
                    [450, '885', '339', '553', '70', '289'], [451, '407', '63', '788', '401', '899'],
                    [452, '398', '738', '985', '859', '906'], [453, '341', '480', '264', '488', '277'],
                    [454, '59', '583', '362', '82', '581'], [455, '558', '380', '916', '539', '895'],
                    [456, '936', '246', '478', '996', '957'], [457, '376', '325', '71', '595', '221'],
                    [458, '730', '296', '650', '421', '20'], [459, '839', '41', '111', '27', '219'],
                    [460, '567', '497', '915', '933', '545'], [461, '871', '218', '182', '526', '557'],
                    [462, '296', '767', '900', '159', '198'], [463, '945', '11', '420', '182', '297'],
                    [464, '848', '409', '32', '262', '783'], [465, '223', '291', '120', '250', '754'],
                    [466, '358', '329', '22', '981', '564'], [467, '518', '209', '6', '526', '35'],
                    [468, '742', '90', '811', '322', '808'], [469, '76', '81', '453', '683', '768'],
                    [470, '443', '588', '128', '614', '835'], [471, '651', '848', '753', '853', '334'],
                    [472, '609', '132', '893', '672', '375'], [473, '806', '559', '599', '673', '524'],
                    [474, '380', '953', '930', '273', '38'], [475, '82', '649', '433', '669', '485'],
                    [476, '425', '422', '769', '602', '78'], [477, '632', '181', '44', '397', '44'],
                    [478, '950', '43', '635', '157', '679'], [479, '952', '37', '637', '273', '892'],
                    [480, '838', '750', '268', '997', '243'], [481, '234', '140', '605', '848', '697'],
                    [482, '75', '786', '985', '544', '967'], [483, '668', '605', '515', '675', '517'],
                    [484, '812', '603', '153', '595', '783'], [485, '247', '839', '256', '136', '237'],
                    [486, '986', '93', '666', '704', '696'], [487, '453', '389', '656', '721', '792'],
                    [488, '270', '678', '308', '390', '437'], [489, '147', '388', '746', '296', '785'],
                    [490, '205', '731', '354', '425', '355'], [491, '617', '734', '243', '393', '853'],
                    [492, '736', '508', '397', '762', '934'], [493, '995', '459', '425', '44', '669'],
                    [494, '376', '735', '721', '544', '229'], [495, '279', '211', '410', '403', '403'],
                    [496, '516', '67', '112', '715', '354'], [497, '524', '819', '129', '456', '5'],
                    [498, '396', '110', '792', '385', '410'], [499, '212', '49', '726', '476', '43'],
                    [500, '974', '622', '890', '178', '748'], [501, '401', '402', '236', '242', '144'],
                    [502, '680', '587', '839', '848', '150'], [503, '162', '780', '769', '10', '166'],
                    [504, '575', '461', '865', '644', '732'], [505, '534', '25', '14', '852', '735'],
                    [506, '995', '583', '743', '371', '20'], [507, '998', '509', '237', '990', '281'],
                    [508, '637', '760', '64', '857', '899'], [509, '48', '543', '508', '667', '737'],
                    [510, '719', '757', '966', '311', '311'], [511, '131', '712', '766', '972', '390'],
                    [512, '576', '962', '18', '240', '621'], [513, '880', '129', '787', '388', '193'],
                    [514, '194', '370', '848', '159', '323'], [515, '471', '583', '356', '595', '307'],
                    [516, '256', '911', '120', '526', '816'], [517, '151', '627', '139', '954', '946'],
                    [518, '565', '727', '140', '632', '983'], [519, '764', '260', '788', '90', '830'],
                    [520, '343', '556', '562', '668', '148'], [521, '853', '355', '17', '425', '593'],
                    [522, '981', '123', '718', '948', '246'], [523, '243', '576', '942', '741', '716'],
                    [524, '611', '102', '732', '89', '898'], [525, '751', '16', '576', '366', '938'],
                    [526, '31', '191', '319', '485', '941'], [527, '793', '907', '967', '984', '540'],
                    [528, '56', '557', '435', '216', '814'], [529, '241', '962', '24', '563', '206'],
                    [530, '560', '529', '329', '6', '544'], [531, '374', '25', '734', '364', '363'],
                    [532, '297', '367', '800', '612', '877'], [533, '421', '8', '900', '606', '345'],
                    [534, '325', '649', '706', '459', '895'], [535, '37', '632', '319', '35', '325'],
                    [536, '782', '894', '689', '827', '792'], [537, '342', '858', '820', '200', '999'],
                    [538, '786', '765', '916', '612', '186'], [539, '703', '208', '658', '387', '568'],
                    [540, '296', '742', '876', '966', '724'], [541, '851', '462', '781', '798', '691'],
                    [542, '578', '384', '894', '388', '747'], [543, '53', '591', '952', '457', '131'],
                    [544, '439', '646', '23', '482', '57'], [545, '864', '976', '858', '789', '56'],
                    [546, '10', '132', '124', '570', '686'], [547, '792', '598', '208', '783', '754'],
                    [548, '389', '418', '133', '904', '852'], [549, '394', '156', '575', '681', '580'],
                    [550, '523', '167', '563', '608', '593'], [551, '958', '606', '363', '567', '387'],
                    [552, '246', '722', '639', '374', '140'], [553, '930', '41', '343', '159', '739'],
                    [554, '268', '358', '550', '494', '927'], [555, '111', '606', '609', '410', '702'],
                    [556, '822', '15', '605', '827', '96'], [557, '625', '937', '25', '737', '752'],
                    [558, '921', '578', '730', '989', '681'], [559, '686', '928', '566', '161', '147'],
                    [560, '459', '866', '603', '562', '685'], [561, '330', '808', '685', '332', '431'],
                    [562, '515', '613', '596', '868', '763'], [563, '109', '880', '802', '734', '581'],
                    [564, '400', '133', '817', '768', '912'], [565, '472', '709', '779', '900', '694'],
                    [566, '430', '916', '612', '610', '456'], [567, '290', '715', '61', '175', '101'],
                    [568, '224', '907', '643', '181', '112'], [569, '664', '420', '73', '270', '834'],
                    [570, '257', '912', '173', '733', '782'], [571, '163', '949', '874', '182', '47'],
                    [572, '961', '589', '637', '522', '241'], [573, '221', '397', '723', '106', '447'],
                    [574, '707', '734', '15', '834', '857'], [575, '960', '151', '672', '88', '163'],
                    [576, '800', '336', '953', '960', '82'], [577, '920', '294', '178', '30', '35'],
                    [578, '799', '344', '315', '70', '843'], [579, '341', '61', '420', '637', '992'],
                    [580, '59', '803', '158', '124', '170'], [581, '869', '29', '706', '432', '211'],
                    [582, '360', '110', '599', '713', '8'], [583, '482', '869', '865', '676', '258'],
                    [584, '37', '45', '141', '637', '767'], [585, '614', '210', '657', '997', '671'],
                    [586, '301', '55', '267', '314', '364'], [587, '665', '931', '427', '653', '679'],
                    [588, '800', '299', '508', '426', '615'], [589, '898', '364', '104', '189', '585'],
                    [590, '135', '742', '183', '433', '69'], [591, '433', '101', '102', '601', '697'],
                    [592, '317', '181', '659', '926', '523'], [593, '4', '728', '591', '781', '184'],
                    [594, '994', '10', '54', '345', '282'], [595, '58', '106', '744', '359', '248'],
                    [596, '500', '64', '873', '502', '835'], [597, '764', '419', '320', '213', '299'],
                    [598, '887', '138', '219', '858', '341'], [599, '61', '256', '512', '182', '543'],
                    [600, '547', '817', '558', '167', '353'], [601, '163', '733', '922', '470', '447'],
                    [602, '9', '580', '954', '557', '578'], [603, '11', '818', '896', '74', '552'],
                    [604, '935', '438', '160', '476', '248'], [605, '110', '288', '502', '770', '420'],
                    [606, '636', '671', '832', '562', '497'], [607, '971', '430', '152', '241', '932'],
                    [608, '567', '818', '327', '26', '628'], [609, '88', '865', '539', '624', '778'],
                    [610, '732', '495', '437', '725', '484'], [611, '648', '493', '268', '244', '609'],
                    [612, '796', '559', '987', '222', '503'], [613, '343', '649', '423', '223', '726'],
                    [614, '111', '523', '61', '973', '949'], [615, '767', '235', '732', '564', '522'],
                    [616, '537', '43', '463', '521', '134'], [617, '975', '448', '689', '199', '385'],
                    [618, '272', '943', '839', '635', '560'], [619, '1000', '875', '587', '559', '184'],
                    [620, '903', '946', '250', '713', '939'], [621, '257', '277', '110', '518', '969'],
                    [622, '720', '130', '983', '710', '446'], [623, '374', '382', '196', '953', '121'],
                    [624, '20', '252', '162', '365', '132'], [625, '143', '513', '916', '304', '491'],
                    [626, '383', '787', '353', '877', '262'], [627, '360', '739', '456', '261', '592'],
                    [628, '127', '950', '74', '352', '345'], [629, '650', '306', '88', '720', '818'],
                    [630, '278', '588', '440', '774', '357'], [631, '283', '894', '5', '657', '519'],
                    [632, '131', '117', '690', '628', '900'], [633, '577', '695', '836', '487', '524'],
                    [634, '868', '276', '309', '876', '559'], [635, '505', '562', '603', '416', '641'],
                    [636, '685', '944', '758', '80', '640'], [637, '266', '356', '720', '359', '557'],
                    [638, '365', '359', '364', '66', '213'], [639, '707', '207', '436', '934', '248'],
                    [640, '503', '14', '449', '387', '811'], [641, '584', '452', '782', '28', '514'],
                    [642, '783', '886', '236', '451', '639'], [643, '297', '33', '295', '90', '589'],
                    [644, '212', '121', '783', '659', '347'], [645, '189', '604', '740', '830', '452'],
                    [646, '83', '206', '23', '768', '916'], [647, '356', '924', '424', '407', '509'],
                    [648, '125', '815', '408', '840', '604'], [649, '224', '785', '504', '769', '537'],
                    [650, '239', '45', '665', '801', '818'], [651, '942', '699', '674', '453', '111'],
                    [652, '793', '509', '238', '710', '105'], [653, '363', '609', '517', '898', '54'],
                    [654, '500', '282', '53', '190', '881'], [655, '329', '132', '962', '496', '222'],
                    [656, '128', '972', '254', '248', '975'], [657, '94', '508', '602', '130', '265'],
                    [658, '830', '323', '5', '511', '62'], [659, '503', '343', '185', '650', '454'],
                    [660, '977', '340', '811', '378', '993'], [661, '716', '280', '270', '393', '599'],
                    [662, '856', '826', '429', '324', '357'], [663, '980', '188', '662', '283', '859'],
                    [664, '392', '443', '851', '724', '765'], [665, '688', '197', '786', '220', '449'],
                    [666, '749', '425', '228', '755', '228'], [667, '74', '253', '963', '663', '74'],
                    [668, '776', '77', '439', '358', '335'], [669, '419', '106', '660', '882', '68'],
                    [670, '124', '781', '259', '24', '301'], [671, '734', '497', '678', '313', '153'],
                    [672, '58', '387', '169', '587', '580'], [673, '527', '647', '201', '157', '99'],
                    [674, '24', '706', '271', '918', '207'], [675, '464', '150', '81', '153', '701'],
                    [676, '38', '934', '559', '946', '159'], [677, '404', '638', '558', '361', '169'],
                    [678, '232', '584', '397', '665', '415'], [679, '71', '768', '19', '57', '914'],
                    [680, '39', '782', '515', '664', '543'], [681, '622', '569', '769', '857', '417'],
                    [682, '83', '79', '823', '626', '722'], [683, '773', '988', '794', '453', '841'],
                    [684, '299', '441', '404', '973', '871'], [685, '58', '340', '383', '189', '519'],
                    [686, '908', '681', '897', '229', '341'], [687, '332', '950', '244', '885', '374'],
                    [688, '793', '93', '945', '227', '73'], [689, '396', '147', '370', '240', '692'],
                    [690, '942', '239', '121', '999', '265'], [691, '872', '695', '807', '952', '565'],
                    [692, '65', '665', '522', '689', '108'], [693, '659', '175', '151', '336', '408'],
                    [694, '154', '380', '545', '356', '405'], [695, '365', '944', '110', '707', '263'],
                    [696, '977', '90', '706', '566', '86'], [697, '507', '5', '152', '230', '313'],
                    [698, '388', '715', '885', '806', '489'], [699, '33', '321', '423', '880', '31'],
                    [700, '304', '504', '825', '426', '624'], [701, '92', '198', '819', '241', '147'],
                    [702, '839', '673', '904', '162', '891'], [703, '821', '331', '242', '90', '728'],
                    [704, '550', '11', '401', '351', '273'], [705, '294', '911', '670', '293', '994'],
                    [706, '818', '652', '779', '93', '681'], [707, '306', '193', '998', '506', '734'],
                    [708, '923', '804', '990', '352', '273'], [709, '268', '641', '864', '355', '977'],
                    [710, '966', '286', '465', '474', '765'], [711, '954', '562', '945', '327', '517'],
                    [712, '573', '795', '447', '161', '544'], [713, '88', '971', '593', '680', '237'],
                    [714, '481', '951', '630', '469', '368'], [715, '737', '826', '218', '540', '36'],
                    [716, '604', '967', '661', '886', '691'], [717, '721', '958', '388', '387', '418'],
                    [718, '795', '853', '991', '775', '233'], [719, '733', '836', '540', '549', '179'],
                    [720, '356', '727', '697', '584', '88'], [721, '52', '311', '365', '239', '107'],
                    [722, '523', '515', '369', '812', '733'], [723, '770', '367', '715', '136', '764'],
                    [724, '13', '114', '659', '233', '61'], [725, '871', '757', '152', '598', '324'],
                    [726, '313', '450', '939', '418', '984'], [727, '711', '636', '88', '537', '118'],
                    [728, '133', '478', '807', '162', '107'], [729, '199', '585', '126', '880', '855'],
                    [730, '976', '252', '598', '378', '988'], [731, '213', '971', '292', '345', '482'],
                    [732, '336', '893', '65', '708', '733'], [733, '721', '254', '564', '944', '998'],
                    [734, '140', '853', '192', '690', '954'], [735, '447', '198', '448', '55', '947'],
                    [736, '112', '280', '86', '355', '174'], [737, '251', '875', '930', '181', '324'],
                    [738, '338', '187', '551', '528', '619'], [739, '903', '106', '389', '877', '584'],
                    [740, '125', '809', '489', '705', '780'], [741, '778', '61', '398', '50', '671'],
                    [742, '133', '603', '78', '242', '583'], [743, '570', '630', '608', '591', '633'],
                    [744, '918', '100', '130', '469', '410'], [745, '763', '317', '842', '510', '131'],
                    [746, '483', '668', '251', '80', '364'], [747, '664', '34', '894', '2', '990'],
                    [748, '551', '527', '624', '78', '169'], [749, '846', '73', '737', '631', '691'],
                    [750, '3', '91', '986', '201', '50'], [751, '127', '52', '79', '272', '505'],
                    [752, '264', '653', '147', '990', '937'], [753, '622', '163', '18', '367', '18'],
                    [754, '877', '318', '655', '352', '541'], [755, '716', '863', '401', '336', '339'],
                    [756, '618', '408', '337', '808', '595'], [757, '317', '702', '820', '738', '367'],
                    [758, '310', '219', '929', '317', '120'], [759, '478', '500', '290', '133', '5'],
                    [760, '881', '577', '558', '16', '246'], [761, '378', '222', '265', '355', '588'],
                    [762, '598', '935', '303', '359', '936'], [763, '891', '54', '483', '62', '374'],
                    [764, '972', '167', '577', '873', '130'], [765, '60', '944', '158', '255', '599'],
                    [766, '614', '759', '30', '965', '797'], [767, '671', '552', '994', '37', '231'],
                    [768, '209', '845', '384', '93', '755'], [769, '287', '314', '507', '382', '427'],
                    [770, '339', '469', '948', '520', '529'], [771, '853', '682', '453', '852', '815'],
                    [772, '388', '478', '850', '12', '678'], [773, '748', '257', '450', '81', '683'],
                    [774, '608', '338', '478', '669', '648'], [775, '829', '651', '597', '706', '327'],
                    [776, '912', '338', '190', '484', '154'], [777, '242', '745', '979', '849', '760'],
                    [778, '682', '189', '471', '469', '323'], [779, '545', '503', '885', '484', '304'],
                    [780, '562', '929', '823', '159', '953'], [781, '212', '73', '909', '882', '175'],
                    [782, '862', '859', '537', '213', '643'], [783, '352', '147', '193', '979', '130'],
                    [784, '234', '137', '284', '379', '479'], [785, '340', '633', '14', '615', '863'],
                    [786, '222', '997', '833', '956', '161'], [787, '588', '477', '700', '808', '551'],
                    [788, '521', '664', '356', '730', '629'], [789, '113', '948', '510', '511', '253'],
                    [790, '478', '765', '631', '892', '187'], [791, '213', '205', '592', '714', '834'],
                    [792, '410', '255', '333', '525', '326'], [793, '919', '345', '12', '42', '477'],
                    [794, '658', '773', '5', '196', '478'], [795, '181', '822', '827', '723', '345'],
                    [796, '889', '386', '748', '911', '314'], [797, '998', '850', '216', '607', '914'],
                    [798, '701', '446', '107', '95', '378'], [799, '583', '819', '530', '199', '637'],
                    [800, '902', '460', '344', '683', '104'], [801, '61', '844', '258', '920', '911'],
                    [802, '847', '474', '195', '141', '422'], [803, '2', '545', '103', '53', '441'],
                    [804, '660', '622', '206', '969', '121'], [805, '299', '928', '429', '39', '16'],
                    [806, '677', '266', '164', '160', '433'], [807, '996', '580', '33', '773', '48'],
                    [808, '28', '129', '797', '626', '952'], [809, '271', '792', '949', '816', '272'],
                    [810, '259', '235', '377', '881', '453'], [811, '440', '454', '182', '258', '362'],
                    [812, '841', '687', '432', '191', '908'], [813, '207', '181', '207', '118', '254'],
                    [814, '619', '261', '735', '104', '763'], [815, '798', '776', '826', '999', '190'],
                    [816, '478', '409', '931', '815', '203'], [817, '922', '38', '66', '992', '458'],
                    [818, '255', '592', '612', '890', '610'], [819, '747', '609', '813', '316', '633'],
                    [820, '200', '891', '487', '441', '4'], [821, '277', '549', '86', '416', '538'],
                    [822, '449', '115', '334', '865', '99'], [823, '531', '222', '202', '399', '522'],
                    [824, '473', '900', '706', '387', '598'], [825, '528', '551', '272', '677', '949'],
                    [826, '44', '246', '622', '950', '684'], [827, '712', '50', '449', '888', '381'],
                    [828, '385', '484', '217', '655', '430'], [829, '998', '786', '228', '303', '235'],
                    [830, '248', '517', '628', '159', '820'], [831, '473', '649', '577', '2', '723'],
                    [832, '488', '719', '679', '773', '880'], [833, '581', '135', '266', '183', '108'],
                    [834, '184', '36', '712', '553', '744'], [835, '105', '677', '82', '71', '254'],
                    [836, '705', '374', '949', '116', '460'], [837, '3', '260', '451', '905', '551'],
                    [838, '944', '691', '656', '567', '574'], [839, '600', '159', '488', '52', '309'],
                    [840, '774', '185', '155', '342', '813'], [841, '322', '218', '417', '699', '740'],
                    [842, '614', '649', '763', '434', '880'], [843, '713', '918', '92', '206', '771'],
                    [844, '814', '582', '969', '394', '991'], [845, '409', '119', '941', '18', '738'],
                    [846, '582', '352', '814', '456', '524'], [847, '378', '746', '4', '310', '898'],
                    [848, '507', '559', '117', '637', '413'], [849, '68', '584', '571', '230', '494'],
                    [850, '264', '469', '769', '753', '958'], [851, '581', '659', '51', '620', '638'],
                    [852, '820', '412', '990', '791', '617'], [853, '222', '578', '923', '25', '198'],
                    [854, '13', '275', '556', '328', '275'], [855, '580', '730', '363', '883', '443'],
                    [856, '514', '301', '390', '52', '921'], [857, '655', '819', '653', '990', '715'],
                    [858, '375', '513', '690', '389', '988'], [859, '481', '766', '391', '134', '945'],
                    [860, '249', '702', '755', '852', '695'], [861, '420', '99', '970', '341', '790'],
                    [862, '182', '929', '605', '971', '281'], [863, '37', '249', '284', '377', '307'],
                    [864, '48', '875', '765', '664', '700'], [865, '684', '424', '798', '913', '268'],
                    [866, '84', '811', '231', '190', '76'], [867, '362', '99', '957', '828', '41'],
                    [868, '892', '465', '641', '948', '498'], [869, '745', '231', '106', '574', '869'],
                    [870, '155', '853', '709', '584', '566'], [871, '432', '242', '792', '590', '551'],
                    [872, '118', '27', '85', '756', '652'], [873, '636', '267', '598', '981', '624'],
                    [874, '218', '228', '347', '678', '538'], [875, '137', '351', '738', '888', '576'],
                    [876, '220', '243', '67', '168', '628'], [877, '377', '344', '490', '208', '629'],
                    [878, '293', '712', '898', '558', '261'], [879, '820', '775', '390', '584', '233'],
                    [880, '432', '344', '643', '871', '114'], [881, '74', '952', '146', '221', '330'],
                    [882, '662', '680', '525', '762', '977'], [883, '687', '877', '762', '527', '777'],
                    [884, '295', '722', '383', '600', '216'], [885, '994', '94', '940', '861', '80'],
                    [886, '637', '765', '523', '173', '554'], [887, '596', '290', '490', '787', '557'],
                    [888, '927', '293', '644', '54', '612'], [889, '601', '285', '378', '839', '390'],
                    [890, '478', '41', '252', '837', '831'], [891, '957', '727', '721', '981', '902'],
                    [892, '748', '351', '495', '524', '113'], [893, '543', '845', '732', '700', '454'],
                    [894, '773', '918', '831', '222', '217'], [895, '397', '313', '593', '866', '127'],
                    [896, '523', '187', '35', '814', '504'], [897, '788', '421', '112', '514', '74'],
                    [898, '28', '596', '829', '666', '250'], [899, '942', '232', '644', '180', '935'],
                    [900, '305', '105', '172', '948', '873'], [901, '464', '887', '747', '667', '52'],
                    [902, '346', '371', '862', '930', '776'], [903, '227', '897', '656', '827', '435'],
                    [904, '141', '227', '576', '654', '549'], [905, '513', '548', '124', '374', '505'],
                    [906, '992', '773', '476', '808', '211'], [907, '576', '777', '841', '479', '149'],
                    [908, '18', '610', '446', '80', '697'], [909, '516', '851', '873', '387', '516'],
                    [910, '191', '543', '129', '504', '626'], [911, '276', '809', '343', '131', '773'],
                    [912, '483', '646', '214', '829', '301'], [913, '137', '904', '912', '12', '424'],
                    [914, '853', '569', '806', '976', '96'], [915, '655', '479', '512', '594', '243'],
                    [916, '505', '207', '13', '856', '920'], [917, '159', '175', '312', '156', '342'],
                    [918, '222', '838', '812', '596', '260'], [919, '294', '801', '13', '591', '613'],
                    [920, '793', '651', '979', '717', '857'], [921, '12', '442', '736', '941', '252'],
                    [922, '43', '95', '285', '987', '94'], [923, '499', '375', '129', '31', '857'],
                    [924, '675', '787', '550', '385', '660'], [925, '382', '45', '659', '970', '395'],
                    [926, '850', '240', '41', '957', '382'], [927, '814', '831', '954', '362', '641'],
                    [928, '29', '289', '292', '794', '198'], [929, '712', '809', '621', '361', '305'],
                    [930, '929', '660', '989', '158', '177'], [931, '894', '134', '242', '693', '510'],
                    [932, '306', '968', '140', '449', '829'], [933, '650', '866', '945', '40', '866'],
                    [934, '582', '255', '361', '911', '143'], [935, '174', '82', '172', '902', '471'],
                    [936, '753', '287', '280', '4', '398'], [937, '658', '100', '258', '123', '418'],
                    [938, '983', '10', '915', '349', '235'], [939, '469', '368', '17', '590', '365'],
                    [940, '43', '58', '652', '482', '70'], [941, '928', '511', '339', '368', '364'],
                    [942, '812', '839', '592', '297', '455'], [943, '708', '211', '604', '829', '363'],
                    [944, '627', '378', '467', '847', '746'], [945, '348', '591', '401', '399', '5'],
                    [946, '294', '851', '12', '804', '366'], [947, '626', '25', '819', '877', '390'],
                    [948, '995', '967', '511', '219', '238'], [949, '869', '888', '922', '23', '772'],
                    [950, '494', '385', '936', '247', '198'], [951, '186', '99', '479', '170', '421'],
                    [952, '259', '339', '750', '763', '660'], [953, '475', '878', '705', '691', '308'],
                    [954, '680', '478', '959', '659', '692'], [955, '966', '310', '569', '276', '917'],
                    [956, '377', '272', '797', '808', '292'], [957, '377', '391', '936', '589', '135'],
                    [958, '329', '436', '171', '894', '173'], [959, '227', '280', '118', '962', '37'],
                    [960, '525', '366', '19', '279', '721'], [961, '939', '979', '406', '319', '198'],
                    [962, '542', '660', '702', '943', '664'], [963, '92', '213', '590', '829', '418'],
                    [964, '358', '476', '237', '218', '82'], [965, '686', '34', '101', '520', '248'],
                    [966, '982', '524', '586', '723', '530'], [967, '388', '867', '607', '476', '910'],
                    [968, '102', '171', '898', '652', '903'], [969, '971', '87', '4', '601', '399'],
                    [970, '896', '793', '544', '698', '558'], [971, '859', '776', '770', '12', '496'],
                    [972, '404', '683', '636', '666', '139'], [973, '537', '783', '51', '143', '588'],
                    [974, '251', '298', '753', '482', '26'], [975, '512', '315', '893', '560', '84'],
                    [976, '921', '993', '705', '440', '932'], [977, '392', '565', '159', '577', '118'],
                    [978, '131', '651', '475', '402', '877'], [979, '32', '204', '730', '67', '797'],
                    [980, '190', '377', '837', '892', '220'], [981, '919', '521', '322', '431', '344'],
                    [982, '534', '674', '474', '292', '297'], [983, '908', '12', '258', '284', '404'],
                    [984, '937', '733', '84', '525', '642'], [985, '48', '32', '83', '391', '820'],
                    [986, '144', '981', '549', '262', '755'], [987, '388', '731', '907', '969', '675'],
                    [988, '449', '608', '22', '485', '427'], [989, '834', '522', '278', '403', '411'],
                    [990, '860', '192', '709', '169', '673'], [991, '377', '133', '737', '527', '824'],
                    [992, '332', '320', '666', '948', '121'], [993, '820', '432', '316', '477', '757'],
                    [994, '273', '232', '462', '446', '299'], [995, '113', '330', '192', '328', '434'],
                    [996, '959', '33', '680', '599', '910'], [997, '631', '380', '765', '982', '734'],
                    [998, '401', '326', '127', '152', '958'], [999, '188', '337', '47', '128', '178']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table1, oldest.")
        expected = [['index', 'length', 'width', 'height', 'mass', 'temperature'],
                    [0, '750', '176', '856', '329', '893']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table1, latest.")
        expected = [['index', 'length', 'width', 'height', 'mass', 'temperature'],
                    [999, '188', '337', '47', '128', '178']]
        self.assertEqual(actual, expected)

        # removals + insertions afterwards
        query_start_r = "remove, table1, indices "
        indices = ""
        for i in range(500):
            indices += str(random.randint(0, 499)*2) + ', '  # remove only evens
        indices = indices[:-2]
        indices += '.'
        query = query_start_r + indices
        db.query(query)  # accounting for duplicate indices, this removes 316 entries

        row_values = ""
        for i in range(250):
            row_values += ', '.join([str(random.randint(1, 1000)) for j in range(5)]) + '; '
        row_values = row_values[:-2]
        query = query_start + row_values + query_end
        db.query(query)

        actual = db.query("show me, table1, everything.")
        expected = [['index', 'length', 'width', 'height', 'mass', 'temperature'],
                    [1, '892', '106', '254', '861', '648'], [2, '488', '988', '664', '479', '638'],
                    [3, '680', '743', '958', '345', '598'], [4, '764', '682', '888', '427', '889'],
                    [5, '443', '728', '838', '786', '867'], [6, '626', '444', '902', '430', '42'],
                    [7, '290', '744', '557', '922', '539'], [9, '973', '236', '555', '844', '681'],
                    [10, '148', '635', '765', '321', '783'], [11, '173', '597', '611', '84', '706'],
                    [13, '917', '716', '551', '523', '945'], [15, '456', '141', '724', '34', '667'],
                    [17, '820', '902', '195', '105', '317'], [18, '938', '37', '701', '494', '796'],
                    [19, '36', '978', '345', '583', '698'], [20, '201', '884', '38', '623', '704'],
                    [21, '877', '281', '727', '323', '354'], [23, '51', '215', '513', '150', '380'],
                    [25, '38', '851', '249', '778', '826'], [26, '292', '297', '24', '822', '973'],
                    [27, '537', '517', '164', '156', '698'], [29, '782', '683', '677', '132', '747'],
                    [30, '666', '572', '964', '32', '258'], [31, '334', '667', '202', '41', '509'],
                    [33, '997', '38', '756', '880', '831'], [34, '468', '601', '545', '286', '531'],
                    [35, '42', '268', '518', '530', '303'], [37, '392', '91', '882', '444', '332'],
                    [39, '343', '611', '444', '535', '449'], [41, '480', '989', '172', '940', '315'],
                    [42, '360', '339', '910', '148', '263'], [43, '37', '357', '484', '583', '67'],
                    [45, '752', '33', '799', '484', '250'], [46, '218', '517', '760', '456', '543'],
                    [47, '410', '843', '717', '454', '603'], [48, '266', '886', '239', '463', '725'],
                    [49, '463', '417', '974', '125', '142'], [51, '871', '71', '438', '70', '407'],
                    [53, '121', '786', '354', '954', '946'], [54, '603', '445', '393', '791', '81'],
                    [55, '742', '384', '354', '975', '686'], [57, '321', '217', '231', '616', '447'],
                    [59, '95', '956', '54', '864', '632'], [60, '578', '143', '752', '621', '506'],
                    [61, '808', '779', '295', '607', '84'], [63, '301', '783', '580', '874', '955'],
                    [64, '213', '676', '458', '826', '866'], [65, '986', '578', '498', '540', '350'],
                    [66, '996', '986', '78', '951', '631'], [67, '251', '501', '626', '493', '58'],
                    [68, '552', '131', '373', '10', '945'], [69, '163', '21', '717', '615', '568'],
                    [70, '604', '59', '472', '322', '892'], [71, '351', '665', '116', '162', '595'],
                    [73, '301', '986', '150', '776', '25'], [74, '515', '301', '176', '426', '896'],
                    [75, '807', '834', '405', '501', '361'], [77, '586', '711', '580', '597', '38'],
                    [79, '738', '974', '237', '25', '959'], [80, '612', '793', '480', '985', '523'],
                    [81, '277', '710', '477', '740', '310'], [83, '471', '198', '916', '252', '907'],
                    [85, '907', '381', '173', '180', '121'], [86, '56', '932', '276', '514', '641'],
                    [87, '929', '36', '815', '462', '16'], [89, '348', '893', '486', '866', '731'],
                    [90, '756', '713', '252', '76', '929'], [91, '870', '474', '499', '306', '108'],
                    [93, '553', '359', '628', '559', '131'], [95, '350', '223', '599', '854', '887'],
                    [96, '632', '201', '865', '352', '655'], [97, '771', '362', '395', '616', '950'],
                    [99, '215', '119', '979', '437', '173'], [100, '322', '735', '618', '642', '139'],
                    [101, '129', '667', '536', '552', '787'], [102, '423', '187', '51', '291', '959'],
                    [103, '496', '701', '559', '505', '712'], [105, '417', '341', '489', '723', '97'],
                    [107, '589', '393', '129', '859', '513'], [109, '491', '617', '699', '651', '247'],
                    [111, '211', '523', '186', '316', '437'], [112, '881', '492', '460', '498', '300'],
                    [113, '762', '975', '145', '89', '971'], [115, '871', '794', '11', '678', '182'],
                    [117, '919', '585', '975', '178', '197'], [119, '32', '519', '232', '508', '148'],
                    [120, '216', '583', '173', '638', '605'], [121, '464', '840', '43', '480', '851'],
                    [123, '410', '612', '787', '677', '323'], [124, '885', '805', '557', '300', '347'],
                    [125, '413', '355', '403', '617', '29'], [127, '277', '248', '304', '665', '779'],
                    [129, '745', '893', '480', '740', '635'], [130, '657', '489', '4', '499', '440'],
                    [131, '760', '865', '283', '872', '798'], [133, '835', '751', '783', '470', '276'],
                    [135, '849', '285', '7', '870', '969'], [137, '696', '68', '558', '995', '192'],
                    [139, '947', '373', '283', '495', '121'], [140, '523', '520', '589', '730', '386'],
                    [141, '500', '898', '989', '125', '791'], [143, '36', '63', '300', '213', '924'],
                    [145, '17', '690', '975', '882', '440'], [147, '854', '499', '6', '857', '406'],
                    [148, '581', '728', '737', '178', '911'], [149, '278', '544', '73', '488', '120'],
                    [151, '348', '165', '696', '705', '981'], [153, '760', '918', '318', '969', '428'],
                    [155, '874', '270', '366', '654', '240'], [157, '347', '678', '696', '671', '647'],
                    [158, '263', '793', '904', '563', '941'], [159, '60', '384', '734', '909', '601'],
                    [161, '656', '277', '30', '397', '564'], [162, '13', '696', '287', '824', '473'],
                    [163, '239', '83', '323', '889', '306'], [164, '279', '27', '641', '199', '870'],
                    [165, '809', '125', '228', '369', '971'], [167, '147', '344', '370', '851', '667'],
                    [169, '400', '114', '280', '789', '79'], [171, '872', '645', '492', '999', '480'],
                    [173, '305', '63', '206', '526', '397'], [175, '274', '818', '870', '346', '366'],
                    [176, '696', '607', '9', '131', '415'], [177, '338', '388', '94', '24', '407'],
                    [178, '852', '378', '278', '92', '19'], [179, '347', '919', '515', '982', '827'],
                    [181, '300', '251', '352', '699', '352'], [182, '283', '84', '178', '746', '880'],
                    [183, '220', '593', '190', '278', '525'], [185, '674', '251', '414', '712', '212'],
                    [187, '420', '993', '761', '707', '419'], [189, '3', '377', '646', '676', '879'],
                    [191, '44', '18', '877', '736', '880'], [192, '181', '976', '117', '43', '377'],
                    [193, '3', '559', '931', '312', '158'], [194, '880', '856', '578', '627', '129'],
                    [195, '248', '672', '697', '425', '145'], [196, '819', '672', '815', '742', '751'],
                    [197, '985', '519', '991', '126', '472'], [199, '453', '63', '233', '871', '141'],
                    [200, '110', '716', '536', '593', '51'], [201, '841', '952', '886', '295', '770'],
                    [203, '147', '921', '368', '268', '962'], [205, '101', '73', '415', '682', '520'],
                    [207, '9', '64', '870', '230', '77'], [208, '930', '116', '632', '54', '945'],
                    [209, '179', '340', '726', '626', '35'], [211, '851', '413', '842', '127', '604'],
                    [213, '795', '693', '551', '185', '504'], [215, '213', '42', '218', '141', '658'],
                    [216, '78', '134', '327', '734', '113'], [217, '430', '747', '972', '155', '329'],
                    [219, '318', '371', '359', '639', '46'], [220, '671', '312', '178', '913', '998'],
                    [221, '409', '383', '390', '570', '719'], [222, '102', '672', '632', '630', '535'],
                    [223, '623', '887', '724', '823', '787'], [225, '64', '574', '867', '186', '105'],
                    [226, '90', '885', '203', '224', '68'], [227, '645', '436', '405', '509', '90'],
                    [229, '775', '951', '697', '50', '131'], [231, '696', '964', '750', '14', '242'],
                    [233, '377', '182', '847', '632', '104'], [235, '432', '563', '241', '324', '79'],
                    [237, '129', '797', '554', '230', '475'], [239, '616', '75', '885', '69', '824'],
                    [241, '624', '87', '292', '357', '151'], [243, '115', '47', '138', '899', '809'],
                    [245, '209', '314', '305', '729', '324'], [247, '779', '281', '979', '116', '350'],
                    [248, '363', '12', '937', '15', '626'], [249, '230', '246', '746', '665', '757'],
                    [251, '1', '833', '989', '692', '648'], [252, '626', '289', '648', '142', '441'],
                    [253, '29', '239', '564', '162', '965'], [255, '87', '289', '934', '720', '222'],
                    [256, '583', '316', '52', '171', '581'], [257, '692', '215', '578', '979', '560'],
                    [259, '866', '7', '592', '141', '984'], [261, '46', '707', '567', '739', '63'],
                    [262, '19', '244', '608', '707', '574'], [263, '103', '158', '86', '87', '584'],
                    [265, '980', '617', '860', '738', '550'], [266, '101', '772', '826', '165', '207'],
                    [267, '367', '277', '962', '406', '571'], [268, '533', '546', '760', '440', '257'],
                    [269, '432', '681', '397', '457', '744'], [271, '906', '999', '507', '995', '453'],
                    [273, '335', '773', '236', '709', '506'], [275, '219', '789', '337', '296', '915'],
                    [277, '470', '103', '312', '447', '416'], [279, '884', '92', '122', '547', '109'],
                    [280, '200', '530', '115', '193', '12'], [281, '839', '325', '295', '919', '338'],
                    [283, '13', '148', '70', '292', '751'], [285, '443', '334', '180', '631', '149'],
                    [287, '106', '146', '986', '875', '573'], [289, '322', '854', '38', '616', '300'],
                    [290, '391', '414', '886', '917', '289'], [291, '18', '277', '228', '744', '695'],
                    [293, '300', '477', '461', '332', '79'], [295, '771', '686', '912', '174', '317'],
                    [296, '828', '740', '65', '908', '615'], [297, '93', '647', '972', '197', '249'],
                    [299, '724', '938', '16', '158', '173'], [301, '791', '168', '411', '283', '934'],
                    [303, '661', '372', '276', '949', '281'], [304, '663', '592', '705', '660', '831'],
                    [305, '96', '754', '409', '146', '456'], [306, '754', '38', '84', '504', '431'],
                    [307, '508', '272', '105', '655', '546'], [308, '69', '231', '278', '245', '91'],
                    [309, '258', '643', '13', '125', '589'], [311, '606', '634', '554', '631', '294'],
                    [313, '656', '477', '481', '417', '679'], [315, '549', '960', '786', '891', '281'],
                    [317, '946', '444', '414', '228', '716'], [319, '48', '567', '406', '45', '237'],
                    [320, '978', '721', '328', '797', '469'], [321, '563', '242', '281', '173', '131'],
                    [323, '46', '113', '956', '172', '867'], [324, '920', '831', '364', '357', '252'],
                    [325, '168', '816', '156', '509', '597'], [327, '481', '429', '817', '750', '563'],
                    [329, '69', '449', '386', '906', '716'], [330, '657', '101', '57', '689', '501'],
                    [331, '86', '832', '205', '902', '164'], [333, '572', '267', '461', '159', '140'],
                    [334, '499', '753', '166', '99', '952'], [335, '226', '946', '236', '989', '264'],
                    [337, '5', '749', '439', '168', '21'], [339, '159', '237', '6', '814', '362'],
                    [341, '49', '853', '676', '544', '646'], [342, '968', '120', '905', '923', '72'],
                    [343, '174', '29', '598', '830', '960'], [344, '585', '486', '23', '388', '444'],
                    [345, '854', '16', '376', '700', '79'], [347, '429', '131', '221', '276', '840'],
                    [348, '542', '638', '648', '977', '400'], [349, '282', '644', '730', '781', '671'],
                    [351, '138', '955', '632', '372', '664'], [353, '771', '503', '26', '117', '142'],
                    [355, '248', '91', '186', '505', '515'], [357, '91', '281', '731', '445', '607'],
                    [358, '798', '518', '78', '840', '178'], [359, '498', '570', '74', '152', '269'],
                    [361, '893', '748', '432', '656', '579'], [363, '482', '931', '860', '54', '443'],
                    [365, '341', '213', '877', '641', '364'], [366, '233', '762', '648', '331', '174'],
                    [367, '256', '942', '905', '603', '663'], [369, '503', '195', '888', '203', '344'],
                    [371, '553', '479', '126', '200', '230'], [373, '888', '999', '826', '881', '702'],
                    [375, '994', '966', '333', '260', '310'], [377, '366', '886', '823', '170', '747'],
                    [379, '545', '877', '988', '795', '579'], [380, '589', '47', '692', '218', '162'],
                    [381, '239', '314', '939', '159', '699'], [382, '369', '223', '640', '463', '29'],
                    [383, '348', '282', '758', '425', '288'], [384, '626', '182', '513', '123', '682'],
                    [385, '403', '156', '815', '575', '213'], [387, '870', '241', '556', '951', '502'],
                    [389, '127', '549', '323', '826', '654'], [391, '796', '282', '478', '86', '924'],
                    [392, '823', '620', '647', '293', '34'], [393, '273', '603', '213', '553', '975'],
                    [395, '744', '137', '333', '893', '963'], [396, '157', '8', '19', '742', '77'],
                    [397, '45', '92', '679', '917', '22'], [398, '446', '947', '293', '445', '604'],
                    [399, '865', '651', '162', '114', '33'], [401, '395', '563', '676', '987', '251'],
                    [403, '555', '839', '205', '204', '588'], [405, '314', '627', '240', '462', '131'],
                    [407, '769', '471', '55', '442', '320'], [408, '339', '81', '861', '169', '482'],
                    [409, '418', '740', '445', '864', '365'], [411, '829', '346', '825', '485', '434'],
                    [412, '781', '792', '189', '854', '671'], [413, '684', '427', '513', '129', '229'],
                    [415, '59', '685', '359', '834', '285'], [417, '296', '225', '542', '974', '816'],
                    [418, '149', '649', '8', '485', '421'], [419, '333', '460', '615', '150', '552'],
                    [420, '897', '277', '36', '447', '683'], [421, '449', '272', '16', '611', '447'],
                    [423, '763', '568', '461', '239', '530'], [424, '709', '785', '194', '574', '156'],
                    [425, '774', '313', '767', '153', '32'], [427, '768', '493', '458', '268', '557'],
                    [429, '54', '254', '810', '507', '599'], [431, '28', '437', '511', '188', '921'],
                    [432, '515', '355', '29', '804', '153'], [433, '577', '847', '380', '379', '410'],
                    [435, '671', '755', '331', '703', '168'], [437, '780', '847', '763', '196', '95'],
                    [438, '207', '133', '431', '380', '761'], [439, '882', '42', '54', '394', '150'],
                    [440, '408', '290', '522', '812', '2'], [441, '38', '818', '281', '195', '569'],
                    [442, '359', '817', '219', '980', '688'], [443, '172', '322', '832', '695', '413'],
                    [444, '482', '797', '860', '716', '803'], [445, '128', '627', '355', '212', '543'],
                    [446, '848', '209', '18', '321', '302'], [447, '644', '307', '629', '711', '444'],
                    [449, '277', '168', '32', '923', '843'], [450, '885', '339', '553', '70', '289'],
                    [451, '407', '63', '788', '401', '899'], [452, '398', '738', '985', '859', '906'],
                    [453, '341', '480', '264', '488', '277'], [455, '558', '380', '916', '539', '895'],
                    [456, '936', '246', '478', '996', '957'], [457, '376', '325', '71', '595', '221'],
                    [459, '839', '41', '111', '27', '219'], [461, '871', '218', '182', '526', '557'],
                    [463, '945', '11', '420', '182', '297'], [464, '848', '409', '32', '262', '783'],
                    [465, '223', '291', '120', '250', '754'], [467, '518', '209', '6', '526', '35'],
                    [468, '742', '90', '811', '322', '808'], [469, '76', '81', '453', '683', '768'],
                    [470, '443', '588', '128', '614', '835'], [471, '651', '848', '753', '853', '334'],
                    [473, '806', '559', '599', '673', '524'], [474, '380', '953', '930', '273', '38'],
                    [475, '82', '649', '433', '669', '485'], [476, '425', '422', '769', '602', '78'],
                    [477, '632', '181', '44', '397', '44'], [478, '950', '43', '635', '157', '679'],
                    [479, '952', '37', '637', '273', '892'], [480, '838', '750', '268', '997', '243'],
                    [481, '234', '140', '605', '848', '697'], [483, '668', '605', '515', '675', '517'],
                    [485, '247', '839', '256', '136', '237'], [487, '453', '389', '656', '721', '792'],
                    [489, '147', '388', '746', '296', '785'], [490, '205', '731', '354', '425', '355'],
                    [491, '617', '734', '243', '393', '853'], [492, '736', '508', '397', '762', '934'],
                    [493, '995', '459', '425', '44', '669'], [495, '279', '211', '410', '403', '403'],
                    [497, '524', '819', '129', '456', '5'], [498, '396', '110', '792', '385', '410'],
                    [499, '212', '49', '726', '476', '43'], [501, '401', '402', '236', '242', '144'],
                    [503, '162', '780', '769', '10', '166'], [505, '534', '25', '14', '852', '735'],
                    [507, '998', '509', '237', '990', '281'], [508, '637', '760', '64', '857', '899'],
                    [509, '48', '543', '508', '667', '737'], [510, '719', '757', '966', '311', '311'],
                    [511, '131', '712', '766', '972', '390'], [513, '880', '129', '787', '388', '193'],
                    [514, '194', '370', '848', '159', '323'], [515, '471', '583', '356', '595', '307'],
                    [516, '256', '911', '120', '526', '816'], [517, '151', '627', '139', '954', '946'],
                    [519, '764', '260', '788', '90', '830'], [521, '853', '355', '17', '425', '593'],
                    [523, '243', '576', '942', '741', '716'], [525, '751', '16', '576', '366', '938'],
                    [526, '31', '191', '319', '485', '941'], [527, '793', '907', '967', '984', '540'],
                    [528, '56', '557', '435', '216', '814'], [529, '241', '962', '24', '563', '206'],
                    [531, '374', '25', '734', '364', '363'], [532, '297', '367', '800', '612', '877'],
                    [533, '421', '8', '900', '606', '345'], [535, '37', '632', '319', '35', '325'],
                    [537, '342', '858', '820', '200', '999'], [539, '703', '208', '658', '387', '568'],
                    [540, '296', '742', '876', '966', '724'], [541, '851', '462', '781', '798', '691'],
                    [543, '53', '591', '952', '457', '131'], [544, '439', '646', '23', '482', '57'],
                    [545, '864', '976', '858', '789', '56'], [546, '10', '132', '124', '570', '686'],
                    [547, '792', '598', '208', '783', '754'], [549, '394', '156', '575', '681', '580'],
                    [551, '958', '606', '363', '567', '387'], [553, '930', '41', '343', '159', '739'],
                    [554, '268', '358', '550', '494', '927'], [555, '111', '606', '609', '410', '702'],
                    [557, '625', '937', '25', '737', '752'], [559, '686', '928', '566', '161', '147'],
                    [561, '330', '808', '685', '332', '431'], [563, '109', '880', '802', '734', '581'],
                    [565, '472', '709', '779', '900', '694'], [566, '430', '916', '612', '610', '456'],
                    [567, '290', '715', '61', '175', '101'], [568, '224', '907', '643', '181', '112'],
                    [569, '664', '420', '73', '270', '834'], [570, '257', '912', '173', '733', '782'],
                    [571, '163', '949', '874', '182', '47'], [573, '221', '397', '723', '106', '447'],
                    [575, '960', '151', '672', '88', '163'], [577, '920', '294', '178', '30', '35'],
                    [579, '341', '61', '420', '637', '992'], [581, '869', '29', '706', '432', '211'],
                    [582, '360', '110', '599', '713', '8'], [583, '482', '869', '865', '676', '258'],
                    [585, '614', '210', '657', '997', '671'], [587, '665', '931', '427', '653', '679'],
                    [588, '800', '299', '508', '426', '615'], [589, '898', '364', '104', '189', '585'],
                    [590, '135', '742', '183', '433', '69'], [591, '433', '101', '102', '601', '697'],
                    [593, '4', '728', '591', '781', '184'], [595, '58', '106', '744', '359', '248'],
                    [596, '500', '64', '873', '502', '835'], [597, '764', '419', '320', '213', '299'],
                    [598, '887', '138', '219', '858', '341'], [599, '61', '256', '512', '182', '543'],
                    [600, '547', '817', '558', '167', '353'], [601, '163', '733', '922', '470', '447'],
                    [603, '11', '818', '896', '74', '552'], [605, '110', '288', '502', '770', '420'],
                    [607, '971', '430', '152', '241', '932'], [608, '567', '818', '327', '26', '628'],
                    [609, '88', '865', '539', '624', '778'], [611, '648', '493', '268', '244', '609'],
                    [612, '796', '559', '987', '222', '503'], [613, '343', '649', '423', '223', '726'],
                    [615, '767', '235', '732', '564', '522'], [617, '975', '448', '689', '199', '385'],
                    [618, '272', '943', '839', '635', '560'], [619, '1000', '875', '587', '559', '184'],
                    [621, '257', '277', '110', '518', '969'], [622, '720', '130', '983', '710', '446'],
                    [623, '374', '382', '196', '953', '121'], [625, '143', '513', '916', '304', '491'],
                    [627, '360', '739', '456', '261', '592'], [629, '650', '306', '88', '720', '818'],
                    [631, '283', '894', '5', '657', '519'], [633, '577', '695', '836', '487', '524'],
                    [635, '505', '562', '603', '416', '641'], [637, '266', '356', '720', '359', '557'],
                    [639, '707', '207', '436', '934', '248'], [640, '503', '14', '449', '387', '811'],
                    [641, '584', '452', '782', '28', '514'], [643, '297', '33', '295', '90', '589'],
                    [645, '189', '604', '740', '830', '452'], [647, '356', '924', '424', '407', '509'],
                    [648, '125', '815', '408', '840', '604'], [649, '224', '785', '504', '769', '537'],
                    [651, '942', '699', '674', '453', '111'], [653, '363', '609', '517', '898', '54'],
                    [654, '500', '282', '53', '190', '881'], [655, '329', '132', '962', '496', '222'],
                    [656, '128', '972', '254', '248', '975'], [657, '94', '508', '602', '130', '265'],
                    [659, '503', '343', '185', '650', '454'], [661, '716', '280', '270', '393', '599'],
                    [663, '980', '188', '662', '283', '859'], [664, '392', '443', '851', '724', '765'],
                    [665, '688', '197', '786', '220', '449'], [667, '74', '253', '963', '663', '74'],
                    [668, '776', '77', '439', '358', '335'], [669, '419', '106', '660', '882', '68'],
                    [671, '734', '497', '678', '313', '153'], [672, '58', '387', '169', '587', '580'],
                    [673, '527', '647', '201', '157', '99'], [675, '464', '150', '81', '153', '701'],
                    [676, '38', '934', '559', '946', '159'], [677, '404', '638', '558', '361', '169'],
                    [679, '71', '768', '19', '57', '914'], [681, '622', '569', '769', '857', '417'],
                    [682, '83', '79', '823', '626', '722'], [683, '773', '988', '794', '453', '841'],
                    [685, '58', '340', '383', '189', '519'], [687, '332', '950', '244', '885', '374'],
                    [689, '396', '147', '370', '240', '692'], [691, '872', '695', '807', '952', '565'],
                    [693, '659', '175', '151', '336', '408'], [694, '154', '380', '545', '356', '405'],
                    [695, '365', '944', '110', '707', '263'], [697, '507', '5', '152', '230', '313'],
                    [698, '388', '715', '885', '806', '489'], [699, '33', '321', '423', '880', '31'],
                    [701, '92', '198', '819', '241', '147'], [702, '839', '673', '904', '162', '891'],
                    [703, '821', '331', '242', '90', '728'], [704, '550', '11', '401', '351', '273'],
                    [705, '294', '911', '670', '293', '994'], [706, '818', '652', '779', '93', '681'],
                    [707, '306', '193', '998', '506', '734'], [709, '268', '641', '864', '355', '977'],
                    [710, '966', '286', '465', '474', '765'], [711, '954', '562', '945', '327', '517'],
                    [713, '88', '971', '593', '680', '237'], [714, '481', '951', '630', '469', '368'],
                    [715, '737', '826', '218', '540', '36'], [717, '721', '958', '388', '387', '418'],
                    [719, '733', '836', '540', '549', '179'], [721, '52', '311', '365', '239', '107'],
                    [723, '770', '367', '715', '136', '764'], [725, '871', '757', '152', '598', '324'],
                    [727, '711', '636', '88', '537', '118'], [728, '133', '478', '807', '162', '107'],
                    [729, '199', '585', '126', '880', '855'], [731, '213', '971', '292', '345', '482'],
                    [733, '721', '254', '564', '944', '998'], [735, '447', '198', '448', '55', '947'],
                    [737, '251', '875', '930', '181', '324'], [739, '903', '106', '389', '877', '584'],
                    [741, '778', '61', '398', '50', '671'], [742, '133', '603', '78', '242', '583'],
                    [743, '570', '630', '608', '591', '633'], [744, '918', '100', '130', '469', '410'],
                    [745, '763', '317', '842', '510', '131'], [746, '483', '668', '251', '80', '364'],
                    [747, '664', '34', '894', '2', '990'], [748, '551', '527', '624', '78', '169'],
                    [749, '846', '73', '737', '631', '691'], [750, '3', '91', '986', '201', '50'],
                    [751, '127', '52', '79', '272', '505'], [753, '622', '163', '18', '367', '18'],
                    [755, '716', '863', '401', '336', '339'], [757, '317', '702', '820', '738', '367'],
                    [759, '478', '500', '290', '133', '5'], [760, '881', '577', '558', '16', '246'],
                    [761, '378', '222', '265', '355', '588'], [763, '891', '54', '483', '62', '374'],
                    [765, '60', '944', '158', '255', '599'], [767, '671', '552', '994', '37', '231'],
                    [768, '209', '845', '384', '93', '755'], [769, '287', '314', '507', '382', '427'],
                    [771, '853', '682', '453', '852', '815'], [772, '388', '478', '850', '12', '678'],
                    [773, '748', '257', '450', '81', '683'], [775, '829', '651', '597', '706', '327'],
                    [776, '912', '338', '190', '484', '154'], [777, '242', '745', '979', '849', '760'],
                    [779, '545', '503', '885', '484', '304'], [781, '212', '73', '909', '882', '175'],
                    [783, '352', '147', '193', '979', '130'], [785, '340', '633', '14', '615', '863'],
                    [787, '588', '477', '700', '808', '551'], [789, '113', '948', '510', '511', '253'],
                    [790, '478', '765', '631', '892', '187'], [791, '213', '205', '592', '714', '834'],
                    [793, '919', '345', '12', '42', '477'], [794, '658', '773', '5', '196', '478'],
                    [795, '181', '822', '827', '723', '345'], [797, '998', '850', '216', '607', '914'],
                    [799, '583', '819', '530', '199', '637'], [800, '902', '460', '344', '683', '104'],
                    [801, '61', '844', '258', '920', '911'], [803, '2', '545', '103', '53', '441'],
                    [805, '299', '928', '429', '39', '16'], [807, '996', '580', '33', '773', '48'],
                    [808, '28', '129', '797', '626', '952'], [809, '271', '792', '949', '816', '272'],
                    [811, '440', '454', '182', '258', '362'], [813, '207', '181', '207', '118', '254'],
                    [815, '798', '776', '826', '999', '190'], [817, '922', '38', '66', '992', '458'],
                    [819, '747', '609', '813', '316', '633'], [821, '277', '549', '86', '416', '538'],
                    [823, '531', '222', '202', '399', '522'], [825, '528', '551', '272', '677', '949'],
                    [827, '712', '50', '449', '888', '381'], [829, '998', '786', '228', '303', '235'],
                    [831, '473', '649', '577', '2', '723'], [833, '581', '135', '266', '183', '108'],
                    [835, '105', '677', '82', '71', '254'], [836, '705', '374', '949', '116', '460'],
                    [837, '3', '260', '451', '905', '551'], [839, '600', '159', '488', '52', '309'],
                    [841, '322', '218', '417', '699', '740'], [843, '713', '918', '92', '206', '771'],
                    [845, '409', '119', '941', '18', '738'], [847, '378', '746', '4', '310', '898'],
                    [849, '68', '584', '571', '230', '494'], [850, '264', '469', '769', '753', '958'],
                    [851, '581', '659', '51', '620', '638'], [853, '222', '578', '923', '25', '198'],
                    [854, '13', '275', '556', '328', '275'], [855, '580', '730', '363', '883', '443'],
                    [856, '514', '301', '390', '52', '921'], [857, '655', '819', '653', '990', '715'],
                    [859, '481', '766', '391', '134', '945'], [861, '420', '99', '970', '341', '790'],
                    [863, '37', '249', '284', '377', '307'], [865, '684', '424', '798', '913', '268'],
                    [867, '362', '99', '957', '828', '41'], [868, '892', '465', '641', '948', '498'],
                    [869, '745', '231', '106', '574', '869'], [870, '155', '853', '709', '584', '566'],
                    [871, '432', '242', '792', '590', '551'], [873, '636', '267', '598', '981', '624'],
                    [874, '218', '228', '347', '678', '538'], [875, '137', '351', '738', '888', '576'],
                    [877, '377', '344', '490', '208', '629'], [879, '820', '775', '390', '584', '233'],
                    [881, '74', '952', '146', '221', '330'], [882, '662', '680', '525', '762', '977'],
                    [883, '687', '877', '762', '527', '777'], [884, '295', '722', '383', '600', '216'],
                    [885, '994', '94', '940', '861', '80'], [886, '637', '765', '523', '173', '554'],
                    [887, '596', '290', '490', '787', '557'], [888, '927', '293', '644', '54', '612'],
                    [889, '601', '285', '378', '839', '390'], [891, '957', '727', '721', '981', '902'],
                    [893, '543', '845', '732', '700', '454'], [895, '397', '313', '593', '866', '127'],
                    [897, '788', '421', '112', '514', '74'], [899, '942', '232', '644', '180', '935'],
                    [900, '305', '105', '172', '948', '873'], [901, '464', '887', '747', '667', '52'],
                    [902, '346', '371', '862', '930', '776'], [903, '227', '897', '656', '827', '435'],
                    [904, '141', '227', '576', '654', '549'], [905, '513', '548', '124', '374', '505'],
                    [907, '576', '777', '841', '479', '149'], [908, '18', '610', '446', '80', '697'],
                    [909, '516', '851', '873', '387', '516'], [910, '191', '543', '129', '504', '626'],
                    [911, '276', '809', '343', '131', '773'], [913, '137', '904', '912', '12', '424'],
                    [915, '655', '479', '512', '594', '243'], [916, '505', '207', '13', '856', '920'],
                    [917, '159', '175', '312', '156', '342'], [918, '222', '838', '812', '596', '260'],
                    [919, '294', '801', '13', '591', '613'], [920, '793', '651', '979', '717', '857'],
                    [921, '12', '442', '736', '941', '252'], [923, '499', '375', '129', '31', '857'],
                    [925, '382', '45', '659', '970', '395'], [927, '814', '831', '954', '362', '641'],
                    [929, '712', '809', '621', '361', '305'], [931, '894', '134', '242', '693', '510'],
                    [933, '650', '866', '945', '40', '866'], [935, '174', '82', '172', '902', '471'],
                    [937, '658', '100', '258', '123', '418'], [939, '469', '368', '17', '590', '365'],
                    [941, '928', '511', '339', '368', '364'], [942, '812', '839', '592', '297', '455'],
                    [943, '708', '211', '604', '829', '363'], [944, '627', '378', '467', '847', '746'],
                    [945, '348', '591', '401', '399', '5'], [947, '626', '25', '819', '877', '390'],
                    [949, '869', '888', '922', '23', '772'], [951, '186', '99', '479', '170', '421'],
                    [952, '259', '339', '750', '763', '660'], [953, '475', '878', '705', '691', '308'],
                    [955, '966', '310', '569', '276', '917'], [957, '377', '391', '936', '589', '135'],
                    [958, '329', '436', '171', '894', '173'], [959, '227', '280', '118', '962', '37'],
                    [960, '525', '366', '19', '279', '721'], [961, '939', '979', '406', '319', '198'],
                    [963, '92', '213', '590', '829', '418'], [965, '686', '34', '101', '520', '248'],
                    [966, '982', '524', '586', '723', '530'], [967, '388', '867', '607', '476', '910'],
                    [969, '971', '87', '4', '601', '399'], [970, '896', '793', '544', '698', '558'],
                    [971, '859', '776', '770', '12', '496'], [972, '404', '683', '636', '666', '139'],
                    [973, '537', '783', '51', '143', '588'], [975, '512', '315', '893', '560', '84'],
                    [976, '921', '993', '705', '440', '932'], [977, '392', '565', '159', '577', '118'],
                    [978, '131', '651', '475', '402', '877'], [979, '32', '204', '730', '67', '797'],
                    [980, '190', '377', '837', '892', '220'], [981, '919', '521', '322', '431', '344'],
                    [983, '908', '12', '258', '284', '404'], [984, '937', '733', '84', '525', '642'],
                    [985, '48', '32', '83', '391', '820'], [987, '388', '731', '907', '969', '675'],
                    [988, '449', '608', '22', '485', '427'], [989, '834', '522', '278', '403', '411'],
                    [991, '377', '133', '737', '527', '824'], [993, '820', '432', '316', '477', '757'],
                    [995, '113', '330', '192', '328', '434'], [997, '631', '380', '765', '982', '734'],
                    [998, '401', '326', '127', '152', '958'], [999, '188', '337', '47', '128', '178'],
                    [1000, '190', '501', '1', '744', '85'], [1001, '23', '961', '331', '442', '564'],
                    [1002, '789', '758', '129', '740', '506'], [1003, '917', '723', '66', '571', '892'],
                    [1004, '840', '2', '147', '998', '71'], [1005, '187', '259', '628', '529', '815'],
                    [1006, '520', '943', '970', '727', '578'], [1007, '417', '811', '798', '742', '346'],
                    [1008, '567', '344', '71', '766', '330'], [1009, '7', '393', '62', '312', '285'],
                    [1010, '648', '6', '409', '745', '294'], [1011, '580', '598', '117', '856', '83'],
                    [1012, '645', '503', '856', '164', '653'], [1013, '680', '924', '806', '374', '916'],
                    [1014, '12', '642', '102', '763', '137'], [1015, '352', '129', '343', '144', '64'],
                    [1016, '89', '797', '968', '597', '320'], [1017, '828', '599', '402', '224', '875'],
                    [1018, '437', '241', '476', '911', '912'], [1019, '392', '937', '591', '650', '488'],
                    [1020, '937', '480', '869', '315', '216'], [1021, '286', '401', '448', '856', '246'],
                    [1022, '924', '908', '10', '879', '180'], [1023, '654', '474', '537', '563', '488'],
                    [1024, '865', '335', '529', '320', '488'], [1025, '793', '938', '521', '945', '336'],
                    [1026, '992', '838', '803', '700', '199'], [1027, '551', '359', '883', '867', '507'],
                    [1028, '887', '254', '901', '104', '948'], [1029, '767', '890', '661', '972', '139'],
                    [1030, '474', '354', '183', '398', '643'], [1031, '703', '124', '759', '290', '528'],
                    [1032, '338', '360', '977', '599', '604'], [1033, '649', '653', '635', '98', '898'],
                    [1034, '29', '581', '889', '461', '116'], [1035, '321', '732', '705', '270', '524'],
                    [1036, '326', '928', '75', '78', '351'], [1037, '381', '726', '903', '821', '867'],
                    [1038, '597', '580', '798', '840', '416'], [1039, '315', '667', '455', '437', '455'],
                    [1040, '895', '84', '680', '66', '732'], [1041, '209', '436', '562', '94', '74'],
                    [1042, '990', '156', '173', '55', '273'], [1043, '138', '752', '915', '794', '285'],
                    [1044, '519', '193', '153', '791', '14'], [1045, '590', '985', '616', '147', '979'],
                    [1046, '182', '222', '379', '887', '843'], [1047, '339', '314', '303', '279', '689'],
                    [1048, '825', '101', '651', '670', '681'], [1049, '725', '619', '306', '132', '961'],
                    [1050, '176', '916', '316', '567', '352'], [1051, '442', '903', '893', '359', '94'],
                    [1052, '166', '246', '209', '42', '262'], [1053, '459', '752', '569', '745', '315'],
                    [1054, '564', '439', '890', '446', '982'], [1055, '870', '197', '819', '677', '886'],
                    [1056, '146', '198', '341', '285', '825'], [1057, '274', '473', '576', '9', '964'],
                    [1058, '711', '141', '639', '902', '652'], [1059, '766', '409', '484', '790', '511'],
                    [1060, '494', '349', '83', '334', '977'], [1061, '840', '539', '19', '938', '905'],
                    [1062, '902', '863', '45', '443', '265'], [1063, '583', '536', '353', '36', '983'],
                    [1064, '829', '34', '10', '405', '39'], [1065, '331', '39', '807', '369', '278'],
                    [1066, '292', '259', '179', '507', '857'], [1067, '75', '684', '974', '466', '947'],
                    [1068, '194', '543', '121', '255', '252'], [1069, '322', '9', '993', '316', '734'],
                    [1070, '579', '273', '577', '163', '361'], [1071, '700', '544', '748', '534', '54'],
                    [1072, '632', '498', '920', '151', '786'], [1073, '753', '372', '297', '556', '844'],
                    [1074, '310', '259', '188', '926', '632'], [1075, '419', '84', '756', '549', '542'],
                    [1076, '821', '753', '464', '215', '851'], [1077, '675', '863', '906', '397', '850'],
                    [1078, '933', '203', '231', '211', '967'], [1079, '195', '654', '117', '780', '508'],
                    [1080, '487', '883', '363', '503', '286'], [1081, '745', '967', '337', '358', '870'],
                    [1082, '686', '278', '748', '701', '637'], [1083, '52', '53', '634', '940', '693'],
                    [1084, '990', '939', '109', '782', '143'], [1085, '785', '529', '777', '501', '410'],
                    [1086, '985', '90', '923', '273', '281'], [1087, '154', '728', '787', '845', '940'],
                    [1088, '141', '223', '839', '440', '536'], [1089, '402', '968', '643', '6', '313'],
                    [1090, '256', '680', '670', '175', '806'], [1091, '646', '496', '696', '914', '135'],
                    [1092, '331', '227', '668', '178', '47'], [1093, '44', '51', '108', '369', '889'],
                    [1094, '157', '387', '297', '360', '342'], [1095, '541', '158', '751', '507', '610'],
                    [1096, '715', '788', '434', '738', '650'], [1097, '472', '705', '904', '600', '542'],
                    [1098, '216', '214', '826', '470', '985'], [1099, '198', '655', '99', '340', '167'],
                    [1100, '264', '64', '926', '131', '779'], [1101, '634', '106', '888', '113', '545'],
                    [1102, '549', '997', '891', '433', '701'], [1103, '377', '937', '190', '450', '888'],
                    [1104, '520', '841', '481', '695', '493'], [1105, '345', '227', '643', '397', '968'],
                    [1106, '402', '708', '951', '672', '429'], [1107, '636', '429', '721', '817', '163'],
                    [1108, '311', '622', '429', '244', '693'], [1109, '945', '214', '223', '879', '90'],
                    [1110, '688', '992', '968', '925', '710'], [1111, '470', '719', '837', '231', '116'],
                    [1112, '849', '855', '23', '940', '518'], [1113, '216', '430', '46', '701', '355'],
                    [1114, '51', '206', '916', '293', '465'], [1115, '952', '546', '971', '429', '310'],
                    [1116, '27', '802', '867', '793', '392'], [1117, '915', '327', '746', '551', '298'],
                    [1118, '847', '855', '407', '996', '550'], [1119, '761', '690', '15', '27', '362'],
                    [1120, '447', '766', '153', '288', '196'], [1121, '851', '594', '55', '165', '45'],
                    [1122, '108', '68', '333', '880', '537'], [1123, '217', '927', '696', '659', '756'],
                    [1124, '529', '709', '182', '63', '326'], [1125, '117', '549', '401', '759', '475'],
                    [1126, '959', '984', '976', '590', '817'], [1127, '131', '218', '690', '525', '787'],
                    [1128, '563', '623', '560', '645', '543'], [1129, '811', '855', '730', '111', '702'],
                    [1130, '363', '644', '40', '477', '9'], [1131, '719', '261', '503', '855', '880'],
                    [1132, '511', '891', '138', '445', '785'], [1133, '657', '465', '877', '916', '997'],
                    [1134, '406', '49', '188', '538', '400'], [1135, '428', '97', '576', '622', '323'],
                    [1136, '590', '449', '595', '163', '552'], [1137, '167', '633', '909', '316', '406'],
                    [1138, '950', '434', '80', '987', '848'], [1139, '484', '798', '653', '620', '745'],
                    [1140, '105', '551', '224', '478', '954'], [1141, '540', '434', '342', '494', '495'],
                    [1142, '526', '657', '277', '18', '868'], [1143, '879', '189', '172', '368', '758'],
                    [1144, '384', '279', '489', '854', '667'], [1145, '183', '516', '370', '551', '236'],
                    [1146, '266', '761', '211', '296', '114'], [1147, '461', '852', '594', '256', '222'],
                    [1148, '585', '68', '487', '793', '887'], [1149, '393', '764', '291', '702', '25'],
                    [1150, '800', '253', '407', '613', '652'], [1151, '120', '122', '431', '941', '387'],
                    [1152, '289', '465', '827', '775', '758'], [1153, '553', '870', '432', '448', '108'],
                    [1154, '788', '572', '572', '721', '76'], [1155, '780', '70', '503', '687', '968'],
                    [1156, '655', '242', '426', '327', '159'], [1157, '349', '450', '68', '575', '376'],
                    [1158, '973', '272', '250', '244', '849'], [1159, '488', '811', '373', '514', '957'],
                    [1160, '618', '956', '880', '499', '591'], [1161, '966', '887', '254', '175', '157'],
                    [1162, '538', '141', '306', '734', '54'], [1163, '500', '607', '448', '64', '829'],
                    [1164, '519', '286', '901', '482', '358'], [1165, '601', '97', '788', '491', '740'],
                    [1166, '439', '152', '716', '667', '834'], [1167, '996', '798', '399', '783', '501'],
                    [1168, '135', '777', '309', '941', '844'], [1169, '531', '794', '863', '106', '273'],
                    [1170, '5', '699', '934', '444', '621'], [1171, '642', '858', '978', '309', '459'],
                    [1172, '952', '714', '705', '684', '452'], [1173, '99', '984', '975', '929', '139'],
                    [1174, '253', '755', '612', '505', '584'], [1175, '415', '742', '157', '760', '965'],
                    [1176, '244', '440', '518', '193', '406'], [1177, '106', '591', '535', '544', '439'],
                    [1178, '492', '276', '263', '231', '664'], [1179, '821', '296', '866', '800', '692'],
                    [1180, '313', '126', '594', '219', '934'], [1181, '431', '121', '640', '598', '100'],
                    [1182, '365', '40', '880', '882', '422'], [1183, '907', '448', '197', '442', '641'],
                    [1184, '136', '19', '668', '775', '162'], [1185, '597', '652', '242', '624', '407'],
                    [1186, '854', '200', '605', '232', '361'], [1187, '832', '430', '233', '609', '279'],
                    [1188, '413', '260', '715', '108', '752'], [1189, '121', '372', '79', '766', '943'],
                    [1190, '794', '418', '72', '155', '814'], [1191, '375', '285', '72', '185', '393'],
                    [1192, '201', '879', '687', '906', '610'], [1193, '769', '489', '830', '454', '156'],
                    [1194, '566', '210', '54', '3', '473'], [1195, '344', '207', '229', '367', '540'],
                    [1196, '165', '136', '326', '351', '660'], [1197, '32', '832', '648', '426', '955'],
                    [1198, '460', '870', '814', '924', '980'], [1199, '250', '982', '465', '187', '459'],
                    [1200, '69', '11', '734', '867', '864'], [1201, '145', '326', '133', '95', '577'],
                    [1202, '823', '815', '465', '140', '136'], [1203, '411', '488', '323', '46', '786'],
                    [1204, '512', '319', '366', '962', '122'], [1205, '111', '634', '279', '10', '828'],
                    [1206, '672', '512', '555', '154', '251'], [1207, '118', '123', '612', '463', '574'],
                    [1208, '235', '904', '262', '171', '110'], [1209, '253', '9', '531', '155', '578'],
                    [1210, '412', '245', '683', '331', '387'], [1211, '151', '304', '155', '447', '823'],
                    [1212, '487', '815', '672', '676', '751'], [1213, '318', '567', '798', '597', '14'],
                    [1214, '50', '772', '812', '861', '667'], [1215, '150', '922', '155', '833', '51'],
                    [1216, '488', '401', '101', '135', '360'], [1217, '656', '117', '748', '412', '127'],
                    [1218, '829', '70', '695', '235', '522'], [1219, '792', '496', '205', '62', '700'],
                    [1220, '810', '470', '99', '744', '554'], [1221, '370', '872', '128', '224', '676'],
                    [1222, '468', '412', '183', '167', '836'], [1223, '120', '84', '588', '502', '857'],
                    [1224, '896', '569', '965', '505', '600'], [1225, '490', '424', '296', '310', '6'],
                    [1226, '619', '917', '373', '415', '749'], [1227, '777', '615', '473', '228', '43'],
                    [1228, '917', '516', '92', '390', '217'], [1229, '597', '154', '408', '507', '704'],
                    [1230, '23', '78', '600', '511', '762'], [1231, '304', '805', '469', '365', '132'],
                    [1232, '693', '571', '722', '626', '750'], [1233, '224', '51', '274', '773', '585'],
                    [1234, '933', '510', '459', '817', '111'], [1235, '212', '966', '494', '663', '27'],
                    [1236, '855', '712', '949', '589', '745'], [1237, '880', '469', '292', '828', '999'],
                    [1238, '352', '2', '82', '647', '351'], [1239, '395', '93', '203', '179', '150'],
                    [1240, '670', '494', '146', '732', '792'], [1241, '124', '669', '267', '924', '57'],
                    [1242, '187', '905', '250', '175', '644'], [1243, '687', '395', '795', '24', '504'],
                    [1244, '447', '451', '496', '577', '50'], [1245, '19', '615', '735', '42', '199'],
                    [1246, '460', '609', '166', '452', '143'], [1247, '304', '499', '905', '83', '541'],
                    [1248, '591', '488', '706', '86', '821'], [1249, '88', '530', '400', '477', '387']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table1, oldest.")
        expected = [['index', 'length', 'width', 'height', 'mass', 'temperature'],
                    [1, '892', '106', '254', '861', '648']]
        self.assertEqual(actual, expected)

        actual = db.query("show me, table1, latest.")
        expected = [['index', 'length', 'width', 'height', 'mass', 'temperature'],
                    [1249, '88', '530', '400', '477', '387']]
        self.assertEqual(actual, expected)

    # def test_nnc(self):
    #     plot = False
    #
    #     """
    #     (1) Day/Night image classification: Suppose brightness of an image is measured
    #     between 0 and 1, and we are provided labeled examples of the brightness levels of
    #     images that were taken during night and during day. Given a new image brightness level,
    #     predict whether the image was taken during night or day.
    #     """
    #     # 1a: test from specs
    #     data = [(0.18, "night"), (0.21, "night"), (0.29, "night"),
    #             (0.49, "night"), (0.51, "day"), (0.53, "day"),
    #             (0.97, "day"), (0.98, "day"), (0.99, "day")]
    #     nnc = NearestNeighborClassifier(resolution=1)
    #     nnc.fit(data)
    #
    #     test_images = [0.1, 0.2, 0.5, 0.8, 0.9]
    #     expected = ["night", "night", "day", None, "day"]
    #     actual = [nnc.predict(x=image, delta=0.1) for image in test_images]
    #     self.assertEqual(expected, actual)
    #
    #     # 1b: larger test
    #     random.seed(331)
    #     night_images = [(random.random() / 2, "night") for _ in range(50)]
    #     day_images = [(random.random() / 2 + 0.5, "day") for _ in range(50)]
    #     data = night_images + day_images
    #
    #     nnc = NearestNeighborClassifier(resolution=1)
    #     nnc.fit(data)
    #
    #     test_images = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]
    #     expected = ["night"] * 4 + ["day"] * 4
    #     actual = [nnc.predict(x=image, delta=0.1) for image in test_images]
    #     if plot:
    #         import numpy as np
    #         import matplotlib.pyplot as plt
    #         np.random.seed(331)
    #         x_night = np.array([x[0] for x in night_images])
    #         x_day = np.array([x[0] for x in day_images])
    #         x_test = np.array(test_images)
    #         plt.scatter(x=x_night, y=np.random.rand(
    #             len(x_night)), label="night")
    #         plt.scatter(x=x_day, y=np.random.rand(len(x_day)), label="day")
    #         plt.scatter(x=x_test, y=np.zeros(len(x_test)), c="k", label="test")
    #         plt.xlabel("Value")
    #         plt.yticks([], [])
    #         plt.legend()
    #         plt.show()
    #
    #     self.assertEqual(expected, actual)
    #
    #     """
    #     (2) Season Classification: Suppose temperature is measured between 0 and 1, and we are
    #     provided labeled examples of the season in which each temperature was recorded.
    #     Given a new temperature, predict the season we are experiencing.
    #     """
    #     random.seed(331)
    #     winter_temps = [(random.random() / 4, "winter") for _ in range(50)]
    #     spring_temps = [(random.random() / 4 + 0.25, "spring")
    #                     for _ in range(50)]
    #     summer_temps = [(random.random() / 4 + 0.75, "summer")
    #                     for _ in range(50)]
    #     fall_temps = [(random.random() / 4 + 0.5, "fall") for _ in range(50)]
    #     data = winter_temps + spring_temps + summer_temps + fall_temps
    #
    #     nnc = NearestNeighborClassifier(resolution=1)
    #     nnc.fit(data)
    #
    #     test_temps = [i / 20 for i in range(20)]
    #     expected = ["winter"] * 6 + ["spring"] * 5 + ["fall"] * 4 + ["summer"] * 5
    #     actual = [nnc.predict(x=temp, delta=0) for temp in test_temps]
    #     if plot:
    #         np.random.seed(331)
    #         x_winter, x_spring, x_summer, x_fall = \
    #             np.array([x[0] for x in winter_temps]), np.array([x[0] for x in spring_temps]), \
    #             np.array([x[0] for x in summer_temps]), np.array(
    #                 [x[0] for x in fall_temps])
    #         x_test = np.array(test_temps)
    #         plt.scatter(x=x_winter, y=np.random.rand(
    #             len(x_winter)), label="winter")
    #         plt.scatter(x=x_spring, y=np.random.rand(
    #             len(x_spring)), label="spring")
    #         plt.scatter(x=x_summer, y=np.random.rand(
    #             len(x_summer)), label="summer")
    #         plt.scatter(x=x_fall, y=np.random.rand(len(x_fall)), label="fall")
    #         plt.scatter(x=x_test, y=np.zeros(len(x_test)), c="k", label="test")
    #         plt.xlabel("Value")
    #         plt.yticks([], [])
    #         plt.legend()
    #         plt.show()
    #
    #     self.assertEqual(expected, actual)
    #
    #     """
    #     (3) Rainfall Classification: Suppose daily rainfall is measured between 0 and 1
    #     relative to some baseline, and we are provided labeled examples of whether each year
    #     experienced drought, normal, or flood conditions. Given a new rainfall measurement, predict
    #     whether this year will experience drought, normal, or flood conditions.
    #     """
    #     random.seed(331)
    #     drought_rains = [(random.random() / 2, "drought") for _ in range(1000)]
    #     normal_rains = [(random.random() / 5 + 0.4, "normal")
    #                     for _ in range(1000)]
    #     flood_rains = [(random.random() / 2 + 0.5, "flood")
    #                    for _ in range(1000)]
    #     data = drought_rains + normal_rains + flood_rains
    #     # equals = data == eval(open('data.txt').read())
    #
    #     nnc = NearestNeighborClassifier(resolution=2)
    #     nnc.fit(data)
    #
    #     test_rains = [i / 100 for i in range(100)]
    #     expected = ["drought"] * 40 + ["normal"] * 21 + ["flood"] * 39
    #     actual = [nnc.predict(x=rain, delta=0.01) for rain in test_rains]
    #     for rain, predict in zip(test_rains, actual):
    #         print(rain, predict)
    #     print(nnc.predict(x=0.62, delta=0.01))
    #     if plot:
    #         np.random.seed(331)
    #         x_drought, x_normal, x_flood = np.array([x[0] for x in drought_rains]), \
    #                                        np.array([x[0] for x in normal_rains]), np.array(
    #             [x[0] for x in flood_rains])
    #         x_test = np.array(test_rains)
    #         plt.scatter(x=x_normal, y=np.random.rand(
    #             len(x_normal)), label="normal")
    #         plt.scatter(x=x_drought, y=np.random.rand(
    #             len(x_drought)), label="drought")
    #         plt.scatter(x=x_flood, y=np.random.rand(
    #             len(x_flood)), label="flood")
    #         plt.scatter(x=x_test, y=np.zeros(len(x_test)), c="k", label="test")
    #         plt.xlabel("Value")
    #         plt.yticks([], [])
    #         plt.legend()
    #         plt.show()
    #
    #     self.assertEqual(expected, actual)
    #
    # def test_nnc_comprehensive(self):
    #
    #     plot = False
    #     """
    #     (4) Iris Species Classification: Given measurements of sepal length, sepal width,
    #     petal length and petal width, predict the species of iris flower.
    #     Data from the UCI ML repository via sklearn.datasets, with credit to R.A. Fisher.
    #     https://archive.ics.uci.edu/ml/datasets/iris
    #     """
    #     iris_labels = ['setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
    #                    'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
    #                    'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
    #                    'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
    #                    'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
    #                    'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'versicolor', 'versicolor', 'versicolor',
    #                    'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
    #                    'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
    #                    'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
    #                    'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
    #                    'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
    #                    'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
    #                    'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'virginica',
    #                    'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
    #                    'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
    #                    'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
    #                    'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
    #                    'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
    #                    'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
    #                    'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica']
    #     sepal_length = [0.2222, 0.1667, 0.1111, 0.0833, 0.1944, 0.3056, 0.0833, 0.1944, 0.0278, 0.1667, 0.3056, 0.1389,
    #                     0.1389, 0.0, 0.4167, 0.3889, 0.3056, 0.2222, 0.3889, 0.2222, 0.3056, 0.2222, 0.0833, 0.2222,
    #                     0.1389, 0.1944, 0.1944, 0.25, 0.25, 0.1111, 0.1389, 0.3056, 0.25, 0.3333, 0.1667, 0.1944,
    #                     0.3333, 0.1667, 0.0278, 0.2222, 0.1944, 0.0556, 0.0278, 0.1944, 0.2222, 0.1389, 0.2222, 0.0833,
    #                     0.2778, 0.1944, 0.75, 0.5833, 0.7222, 0.3333, 0.6111, 0.3889, 0.5556, 0.1667, 0.6389, 0.25,
    #                     0.1944, 0.4444, 0.4722, 0.5, 0.3611, 0.6667, 0.3611, 0.4167, 0.5278, 0.3611, 0.4444, 0.5,
    #                     0.5556, 0.5, 0.5833,
    #                     0.6389, 0.6944, 0.6667, 0.4722, 0.3889, 0.3333, 0.3333, 0.4167, 0.4722, 0.3056, 0.4722, 0.6667,
    #                     0.5556, 0.3611, 0.3333, 0.3333, 0.5, 0.4167, 0.1944, 0.3611, 0.3889, 0.3889, 0.5278, 0.2222,
    #                     0.3889, 0.5556, 0.4167, 0.7778, 0.5556, 0.6111, 0.9167, 0.1667, 0.8333, 0.6667, 0.8056, 0.6111,
    #                     0.5833, 0.6944, 0.3889, 0.4167, 0.5833, 0.6111, 0.9444, 0.9444, 0.4722, 0.7222, 0.3611, 0.9444,
    #                     0.5556, 0.6667, 0.8056, 0.5278, 0.5, 0.5833, 0.8056, 0.8611, 1.0, 0.5833, 0.5556, 0.5, 0.9444,
    #                     0.5556, 0.5833, 0.4722, 0.7222, 0.6667, 0.7222, 0.4167, 0.6944, 0.6667, 0.6667, 0.5556, 0.6111,
    #                     0.5278, 0.4444]
    #     sepal_width = [0.625, 0.4167, 0.5, 0.4583, 0.6667, 0.7917, 0.5833, 0.5833, 0.375, 0.4583, 0.7083, 0.5833,
    #                    0.4167, 0.4167, 0.8333, 1.0, 0.7917, 0.625, 0.75, 0.75, 0.5833, 0.7083, 0.6667, 0.5417, 0.5833,
    #                    0.4167, 0.5833, 0.625, 0.5833, 0.5, 0.4583, 0.5833, 0.875, 0.9167, 0.4583, 0.5, 0.625, 0.6667,
    #                    0.4167, 0.5833, 0.625, 0.125, 0.5, 0.625, 0.75, 0.4167, 0.75, 0.5, 0.7083, 0.5417, 0.5, 0.5,
    #                    0.4583, 0.125, 0.3333, 0.3333, 0.5417, 0.1667, 0.375, 0.2917, 0.0, 0.4167, 0.0833, 0.375, 0.375,
    #                    0.4583, 0.4167, 0.2917, 0.0833, 0.2083, 0.5, 0.3333, 0.2083, 0.3333, 0.375,
    #                    0.4167, 0.3333, 0.4167, 0.375, 0.25, 0.1667, 0.1667, 0.2917, 0.2917, 0.4167, 0.5833, 0.4583,
    #                    0.125, 0.4167, 0.2083, 0.25, 0.4167, 0.25, 0.125, 0.2917, 0.4167, 0.375, 0.375, 0.2083, 0.3333,
    #                    0.5417, 0.2917, 0.4167, 0.375, 0.4167, 0.4167, 0.2083, 0.375, 0.2083, 0.6667, 0.5, 0.2917,
    #                    0.4167, 0.2083, 0.3333, 0.5, 0.4167, 0.75, 0.25, 0.0833, 0.5, 0.3333, 0.3333, 0.2917, 0.5417,
    #                    0.5, 0.3333, 0.4167, 0.3333, 0.4167, 0.3333, 0.75, 0.3333, 0.3333, 0.25, 0.4167, 0.5833, 0.4583,
    #                    0.4167, 0.4583, 0.4583, 0.4583, 0.2917, 0.5, 0.5417, 0.4167, 0.2083, 0.4167, 0.5833, 0.4167]
    #     petal_length = [0.0678, 0.0678, 0.0508, 0.0847, 0.0678, 0.1186, 0.0678, 0.0847, 0.0678, 0.0847, 0.0847, 0.1017,
    #                     0.0678, 0.0169, 0.0339, 0.0847, 0.0508, 0.0678, 0.1186, 0.0847, 0.1186, 0.0847, 0.0, 0.1186,
    #                     0.1525, 0.1017, 0.1017, 0.0847, 0.0678, 0.1017, 0.1017, 0.0847, 0.0847, 0.0678, 0.0847, 0.0339,
    #                     0.0508, 0.0678, 0.0508, 0.0847, 0.0508, 0.0508, 0.0508, 0.1017, 0.1525, 0.0678, 0.1017, 0.0678,
    #                     0.0847, 0.0678, 0.6271, 0.5932, 0.661, 0.5085, 0.6102, 0.5932, 0.6271, 0.3898, 0.6102, 0.4915,
    #                     0.4237, 0.5424, 0.5085, 0.6271, 0.4407, 0.5763, 0.5932, 0.5254, 0.5932, 0.4915, 0.6441, 0.5085,
    #                     0.661, 0.6271,
    #                     0.5593, 0.5763, 0.6441, 0.678, 0.5932, 0.4237, 0.4746, 0.4576, 0.4915, 0.6949, 0.5932, 0.5932,
    #                     0.6271, 0.5763, 0.5254, 0.5085, 0.5763, 0.6102, 0.5085, 0.3898, 0.5424, 0.5424, 0.5424, 0.5593,
    #                     0.339, 0.5254, 0.8475, 0.6949, 0.8305, 0.7797, 0.8136, 0.9492, 0.5932, 0.8983, 0.8136, 0.8644,
    #                     0.6949, 0.7288, 0.7627, 0.678, 0.6949, 0.7288, 0.7627, 0.9661, 1.0, 0.678, 0.7966, 0.661,
    #                     0.9661, 0.661, 0.7966, 0.8475, 0.6441, 0.661, 0.7797, 0.8136, 0.8644, 0.9153, 0.7797, 0.6949,
    #                     0.7797, 0.8644, 0.7797, 0.7627, 0.6441, 0.7458, 0.7797, 0.6949, 0.6949, 0.8305, 0.7966, 0.7119,
    #                     0.678, 0.7119, 0.7458, 0.6949]
    #     petal_width = [0.0417, 0.0417, 0.0417, 0.0417, 0.0417, 0.125, 0.0833, 0.0417, 0.0417, 0.0, 0.0417, 0.0417, 0.0,
    #                    0.0, 0.0417, 0.125, 0.125, 0.0833, 0.0833, 0.0833, 0.0417, 0.125, 0.0417, 0.1667, 0.0417, 0.0417,
    #                    0.125, 0.0417, 0.0417, 0.0417, 0.0417, 0.125, 0.0, 0.0417, 0.0417, 0.0417, 0.0417, 0.0, 0.0417,
    #                    0.0417, 0.0833, 0.0833, 0.0417, 0.2083, 0.125, 0.0833, 0.0417, 0.0417, 0.0417, 0.0417, 0.5417,
    #                    0.5833, 0.5833, 0.5, 0.5833, 0.5, 0.625, 0.375, 0.5, 0.5417, 0.375, 0.5833, 0.375, 0.5417, 0.5,
    #                    0.5417, 0.5833, 0.375, 0.5833, 0.4167, 0.7083, 0.5, 0.5833, 0.4583,
    #                    0.5, 0.5417, 0.5417, 0.6667, 0.5833, 0.375, 0.4167, 0.375, 0.4583, 0.625, 0.5833, 0.625, 0.5833,
    #                    0.5, 0.5, 0.5, 0.4583, 0.5417, 0.4583, 0.375, 0.5, 0.4583, 0.5, 0.5, 0.4167, 0.5, 1.0, 0.75,
    #                    0.8333, 0.7083, 0.875, 0.8333, 0.6667, 0.7083, 0.7083, 1.0, 0.7917, 0.75, 0.8333, 0.7917, 0.9583,
    #                    0.9167, 0.7083, 0.875, 0.9167, 0.5833, 0.9167, 0.7917, 0.7917, 0.7083, 0.8333, 0.7083, 0.7083,
    #                    0.7083, 0.8333, 0.625, 0.75, 0.7917, 0.875, 0.5833, 0.5417, 0.9167, 0.9583, 0.7083, 0.7083,
    #                    0.8333, 0.9583, 0.9167, 0.75, 0.9167, 1.0, 0.9167, 0.75, 0.7917, 0.9167, 0.7083]
    #     test_points = [i / 10 for i in range(11)]
    #
    #     # exploratory visualization for the curious coder
    #     if plot:
    #         import numpy as np
    #         import matplotlib.pyplot as plt
    #         for name, feature in [("sepal length", sepal_length), ("sepal width", sepal_width),
    #                               ("petal length", petal_length), ("petal width", petal_width)]:
    #             np.random.seed(331)
    #             x = np.array(feature)
    #             x_setosa, x_versicolour, x_virginica = x[:50], x[50:100], x[100:]
    #             x_test = np.array(test_points)
    #             plt.scatter(x=x_setosa, y=np.random.rand(
    #                 len(x_setosa)), label="setosa")
    #             plt.scatter(x=x_versicolour, y=np.random.rand(
    #                 len(x_versicolour)), label="versicolour")
    #             plt.scatter(x=x_virginica, y=np.random.rand(
    #                 len(x_virginica)), label="virginica")
    #             plt.scatter(x=x_test, y=np.zeros(
    #                 len(x_test)), c="k", label="test")
    #             plt.title(name)
    #             plt.xlabel("Value")
    #             plt.yticks([], [])
    #             plt.legend()
    #             plt.show()
    #
    #     # 4a: sepal length
    #     data = zip(sepal_length, iris_labels)
    #     nnc = NearestNeighborClassifier(resolution=2)
    #     nnc.fit(data)
    #     expected = ['setosa', 'setosa', 'setosa', 'setosa', 'versicolor', 'versicolor',
    #                 'virginica', 'virginica', 'virginica', 'virginica', 'virginica']
    #     actual = [nnc.predict(x=x, delta=0.05) for x in test_points]
    #     self.assertEqual(expected, actual)
    #
    #     # 4b: sepal width
    #     data = zip(sepal_width, iris_labels)
    #     nnc = NearestNeighborClassifier(resolution=2)
    #     nnc.fit(data)
    #     expected = ['versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
    #                 'virginica', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa']
    #     actual = [nnc.predict(x=x, delta=0.05) for x in test_points]
    #     self.assertEqual(expected, actual)
    #
    #     # 4c: petal length
    #     data = zip(petal_length, iris_labels)
    #     nnc = NearestNeighborClassifier(resolution=2)
    #     nnc.fit(data)
    #     expected = ['setosa', 'setosa', 'setosa', 'versicolor', 'versicolor', 'versicolor',
    #                 'versicolor', 'virginica', 'virginica', 'virginica', 'virginica']
    #     actual = [nnc.predict(x=x, delta=0.05) for x in test_points]
    #     self.assertEqual(expected, actual)
    #
    #     # 4d: petal width
    #     data = zip(petal_width, iris_labels)
    #     nnc = NearestNeighborClassifier(resolution=2)
    #     nnc.fit(data)
    #     expected = ['setosa', 'setosa', 'setosa', None, 'versicolor', 'versicolor',
    #                 'versicolor', 'virginica', 'virginica', 'virginica', 'virginica']
    #     actual = [nnc.predict(x=x, delta=0.05) for x in test_points]
    #     self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
