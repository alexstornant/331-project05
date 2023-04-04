# Project 7: AVL Trees

**Due: Thursday, March 31st @ 10:00pm ET**

_This is not a team project. Do not copy someone else’s work._

## Assignment Overview

[AVL trees](https://en.wikipedia.org/wiki/AVL_tree) are a self-balancing [binary search tree (BST)](https://en.wikipedia.org/wiki/Binary_search_tree) optimized to maintain logarithmic-time operations regardless of the order in which data is inserted and deleted. First introduced by Soviet computer scientists Georgy Adelson-Velsky and Evgenii Landis in their 1962 paper "[An algorithm for the organization of information](https://zhjwpku.com/assets/pdf/AED2-10-avl-paper.pdf)," AVL trees have stood the test of time and remain a popular choice when a space-efficient data structure supporting fast insertion/search/deletion is necessary.

![](img/avl.gif)

To motivate AVL trees, it is worth considering a common problem that arises in traditional BSTs. BSTs are designed to perform logarithmic-time insertion/search/deletion, but may operate at linear-time if data is inserted or deleted according to certain patterns which cause the BST to become _unbalanced_. For example, when data is inserted into a traditional BST in sorted (or reverse-sorted) order, the BST will grow leaves in a single direction and effectively turn into a linked list.

![](img/balance.png)

If our dataset is small, this may not be a problem—but when we're working with thousands or millions of records in a database, the difference between logarithmic and linear is astounding!

![](img/bigogrowth.png)

AVL trees improve upon traditional BSTs by _self-balancing_ in order to guarantee logarithmic-time operations. In this project, you will be implementing a traditional BST, then an AVL tree from scratch in Python, using the latter to solve a machine learning-inspired application problem. For more information on BSTs and AVL Trees, check out [Week 7-8 Content on D2L](https://d2l.msu.edu/d2l/le/content/1676253/Home).

## Assignment Notes

1. In this project, you'll be using Python `Generator` objects to traverse a tree in a space-efficient manner. Unlike a traversal returned in the form `List[Node]` using _O(n)_ space, a traversal returning a generator will use _O(1)_ space by _yielding_ each `Node` in a sequential, on-demand manner. See [this link](https://realpython.com/introduction-to-python-generators/) for a nice introduction to `Generator`s in Python! 
You can also look back at the [March 1st Live Class Activity and Week 7-8 Yield](https://d2l.msu.edu/d2l/le/content/1676253/Home) materials in D2L.

2. One of the most common errors in this project is forgetting or incorrectly updating the height and rebalancing within functions that change the tree structure (insert and remove). Read the notes we put under the function description in the specs carefully and think about how you can use recursion/call stack to help you rebalance the tree. What is the call stack's relationship to the node which you removed/inserted?

3. AVL Trees are more complicated structures than what you have worked with before but if you boil each function down to the different cases within them, then it begins to look a lot simpler. Try to decompose each function into what checks/cases you need to look for before an operation. Checks like is the node I'm removing/inserting the origin? Is there a right node before I make a call on node.right? Am I updating the correct pointers?

4. The debugger is your friend! Do not be scared to use it, it is worth the extra time to learn its functionality if you haven't yet. Use it to determine if what you think your code is doing, is actually what it's doing! It's the most helpful tool when trying to figure out why your more complex functions aren't working.

5. We have provided visualization and printing functions for when you just want to get a birds eye view of your tree and don't want to have to click through several levels of objects in the debugger. Using the visualization functions is as simple as calling `tree.visualize()` on an object of type AVLTree. We are, of course, human, and cannot guarantee these visualizations are 100% bug free; if you encounter issues, let us know.

6. Using global variables (with the nonlocal keyword) will result in a 20 point flat-rate deduction.

7. Changing function signatures will result in a 2 point deduction for each violation, up to a maximum of 20 points.

8. If you run the solution.py file after implementing all AVLTree functions, you will be greeted by a performance comparison between the two trees!


 
## Assignment Specifications

#### class Node:

Implements a tree node used in the AVLTree classes.

_DO NOT MODIFY the following attributes/functions_

- **Attributes**
  - **value: T:** Value held by the `Node`. Note that this may be any type, such as a `str`, `int`, `float`, `dict`, or a more complex object.
  - **parent: Node:** Reference to this `Node`'s parent `Node` (may be `None`).
  - **left: Node:** Reference to this `Node`'s left child `Node` (may be `None`).
  - **right: Node:** Reference to this `Node`'s right child `Node` (may be `None`).
  - **height: int:** Number of levels of `Node`s below (the height of a leaf `Node` is 0).
  - **data: T:** Additional data for use in application problem
- **\_\_init\_\_(self, value: T, parent: Node = None, left: Node = None, right: Node = None) -> None**
  - Constructs an AVL Tree node.
  - **value: T:** Value held by the `Node`.
  - **parent: Node:** Reference to this `Node`'s parent `Node` (may be `None`).
  - **left: Node:** Reference to this `Node`'s left child `Node` (may be `None`).
  - **right: Node:** Reference to this `Node`'s right child `Node` (may be `None`).
  - **Returns:** `None`.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Represents the `Node` as a string in the form `<value_held_by_node>`. Thus, `<7>` indicates a `Node` object holding an `int` value of 7, whereas `<None>` indicates a `Node` object holding a value of `None`.
  - Note that Python will automatically invoke this function when using printing a `Node` to the console, and PyCharm will automatically invoke this function when displaying a `Node` in the debugger.
  - Call this with `str(node)` (rather than `node.__str__()`).
  - **Returns:** `str`.  
  
#### class AVLTree:

Implements a self-balancing BSTree for faster operation.

_DO NOT MODIFY the following attributes/functions_

- **Attributes**
  - **origin: Node:** Root node of the entire `AVLTree` (may be `None`). This naming convention helps us disambiguate between when we are referring to the root of the entire `AVLTree` and the root of a subtree within the `AVLTree`. In fact, any given `Node` object within an `AVLTree` can be thought of as being the root of the subtree of all `Node`s below—and `origin` is the uppermost such root in our tree.
  - **size: int:** Number of nodes in the `AVLTree`.
- **\_\_init\_\_(self) -> None**
  - Construct an empty `AVLTree`. Initialize the `origin` to `None` and set the size to zero.
  - **Returns:** `None`.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Returns a pretty printed string representation of the binary tree. Each node will be of the form `{value},h={height},⬆{parent.value}`
  - Note that Python will automatically invoke this function when printing a `Node` to the console, and PyCharm will automatically invoke this function when displaying a `Node` in the debugger.
  - Call this with `str(node)` (rather than `node.__str__()`).
  - **Returns:** `str`.

- **visualize(self, filename="avl_tree_visualization.svg") -> str**
  - Generates an svg image file of the binary tree.
  - filename: str: The filename for the generated svg file. Should end with .svg. Defaults to avl_tree_visualization.svg
  - **Returns:** The svg string.

- **height(self, root: Node) -> int**
  - Return height of a subtree in the AVL tree, properly handling the case of `root = None`. Recall that the height of an empty subtree is -1.
  - _Time / Space: O(1) / O(1)_.
  - **root: Node:** The root `Node` of the subtree being measured.
  - **Returns:** Height of the subtree at `root`, i.e., the number of levels of `Node`s below this `Node`. The height of a leaf `Node` is 0, and the height of a `None`-type is -1.

- **left_rotate(self, root: Node) -> Node**
  - Perform a left rotation on the subtree rooted at `root`. Return root of new subtree after rotation.
  - This method is already implemented for you.
  - _Time / Space: O(1) / O(1)_.
  - **root: Node:** The root `Node` of the subtree being rotated.
  - **Returns:** Root of new subtree after rotation.
 
- **remove(self, root: Node, val: T) -> Node**
  - This method is already implemented for you.
  - Removes the node with value `val` from the subtree rooted at `root`, and returns the root of the balanced subtree following removal.
  - If `val` does not exist in the AVL tree, do nothing.
  - Updates `size` and `origin` attributes of `AVLTree` and correctly update parent/child pointers of `Node` objects as necessary.
  - Updates the `height` attribute and call `rebalance` on all `Node` objects affected by the removal (ancestor nodes directly above on path to origin).
  - Note that that there are [three distinct cases of BST removal to consider](https://en.wikipedia.org/wiki/Binary_search_tree#Deletion).
  - Implemented recursively.
  - If the node being removed has two children, swaps the value of this node with its **predecessor** and recursively removes this predecessor node (which contains the value to be removed after swapping and is guaranteed to be a leaf).
    - Although one technically _could_ swap values with the successor node in a two-child removal, we choose to swap with the predecessor.
  - _Time / Space: O(log n) / O(1)_.
  - **root: Node:** The root `Node` of the subtree from which to delete `val`.
  - **val: T:** The value to be deleted from the subtree rooted at `root`.
  - **Returns:** Root of new subtree after removal and rebalancing (could be the original root).

_IMPLEMENT the following functions_
- **right_rotate(self, root: Node) -> Node**
  - Perform a right rotation on the subtree rooted at `root`. Return root of new subtree after rotation.
  - This should be nearly identical to `left_rotate`, with only a few lines differing. Team 331 agreed that giving one rotation helps ease the burden of this project on the heels of Exam 2—but writing the other rotation will be a good learning experience!
  - _Time / Space: O(1) / O(1)_.
  - **root: Node:** The root `Node` of the subtree being rotated.
  - **Returns:** Root of new subtree after rotation.
- **balance_factor(self, root: Node) -> int**
  - Compute the balance factor of the subtree rooted at `root`.
  - Recall that the balance factor is defined to be `h_L - h_R` where `h_L` is the height of the left subtree beneath this `Node` and `h_R` is the height of the right subtree beneath this `Node`.
  - Note that in a properly-balanced AVL tree, the balance factor of all nodes in the tree will be in the set {-1, 0, +1}, as rebalancing will be triggered when a node's balance factor becomes -2 or +2.
  - The balance factor of an empty subtree (`None`-type `root`) is 0.
  - To stay within time complexity, keep the `height` attribute of each `Node` object updated on all insertions/deletions/rebalances, then use `h_L = left.height` and `h_R = right.height`.
  - _Time / Space: O(1) / O(1)_.
  - **root: Node:** The root `Node` of the subtree on which to compute the balance factor.
  - **Returns:** `int` representing the balance factor of `root`.
- **rebalance(self, root: Node) -> Node**
  - Rebalance the subtree rooted at `root` (if necessary) and return the new root of the resulting subtree.
  - Recall that rebalancing is only necessary at this `root` if the balance factor `b` of this `root` satisfies `b >= 2 or b <= -2`.
  - Recall that there are [four types of imbalances possible in an AVL tree](https://en.wikipedia.org/wiki/AVL_tree#Rebalancing), and that each requires a different sequence of rotation(s) to be called.
  - _Time / Space: O(1) / O(1)_.
  - **root: Node:** The root `Node` of the subtree to be rebalanced.
  - **Returns:** Root of new subtree after rebalancing (could be the original root).
- **insert(self, root: Node, val: T, data: List[str]) -> Node**
  - Insert a node with `val` into the subtree rooted at `root`, returning the root node of the balanced subtree after insertion.
  - If `val` already exists in the AVL tree, do nothing.
  - Should update `size` and `origin` attributes of `AVLTree` if necessary and correctly set parent/child pointers when inserting a new `Node`
  - Should update the `height` attribute and call `rebalance` on all `Node` objects affected by the insertion (ancestor nodes directly above on path to origin).
  - Easiest to implement recursively.
  - If you want to pass the application problem don't forget to ensure that the _data_ attribute isn't lost or set to None when performing recursion!!
  - _Time / Space: O(log n) / O(1)_.
  - **root: Node:** The root `Node` of the subtree in which to insert `val`.
  - **val: T:** The value to be inserted in the subtree rooted at `root`.
  - **Returns:** Root of new subtree after insertion and rebalancing (could be the original root).
- **min(self, root: Node) -> Node**
  - Find and return the `Node` with the smallest value in the subtree rooted at `root`.
  - Easiest to implement recursively.
  - _Time / Space: O(log n) / O(1)_.
  - **root: Node:** The root `Node` of the subtree in which to search for a minimum.
  - **Returns:** `Node` object containing the smallest value in the subtree rooted at `root`.
- **max(self, root: Node) -> Node**
  - Find and return the `Node` with the largest value in the subtree rooted at `root`.
  - Easiest to implement recursively.
  - _Time / Space: O(log n) / O(1)_.
  - **root: Node:** The root `Node` of the subtree in which to search for a maximum.
  - **Returns:** `Node` object containing the largest value in the subtree rooted at `root`.
- **search(self, root: Node, val: T) -> Node**
  - Find and return the `Node` with the value `val` in the subtree rooted at `root`.
  - If `val` does not exist in the subtree rooted at `root`, return the `Node` below which `val` would be inserted as a child. For example, on a balanced 1-2-3 tree (with 2 on top and 1, 3 as children), `search(node_2, 0)` would return `node_1` since the value of 0 would be inserted as a left child of `node_1`.
  - Easiest to implement recursively.
  - _Time / Space: O(log n) / O(1)_.
  - **root: Node:** The root `Node` of the subtree in which to search for `val`.
  - **val: T:** The value being searched in the subtree rooted at `root`.
  - **Returns:** `Node` object containing `val` if it exists, else the `Node` object below which `val` would be inserted as a child.
  
- **inorder(self, root: Node) -> Generator[Node, None, None]**
  - Perform an inorder (left, current, right) traversal of the subtree rooted at `root` using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use `yield` to immediately generate an element in your function, and `yield from` to generate an element from a recursive function call.
  - Do not yield (generate) `None`-types.
  - **To pass the test case for this function, you must also make the AVLTree class iterable such that doing `for node in avltree` iterates over the inorder traversal of the tree**
  - _Time / Space: O(n) / O(1)_.
    - Although we will traverse the entire tree and hence incur O(n) time, our use of a generator will keep us at constant space complexity since elements are yielded one at a time! This is a key advantage of returning a generator instead of a list.
  - **root: Node:** The root `Node` of the subtree currently being traversed.
  - **Returns:** `Generator` object which yields `Node` objects only (no `None`-type yields). Once all nodes of the tree have been yielded, a `StopIteration` exception is raised.
  
- **\_\_iter\_\_(self) -> Generator[Node, None, None]**
  - Implementing this "dunder" method allows you to use an AVL tree class object anywhere you can use an iterable, e.g., inside of a `for node in tree` expression. We want the iteration to use the inorder traversal of the tree so this should be implemented such that it returns the inorder traversal. 
  - **This function should only be one line, calling another function you have implemented.**
  - **Returns:** A generator that iterates over the inorder traversal of the tree
  
- **preorder(self, root: Node) -> Generator[Node, None, None]**
  - Perform a preorder (current, left, right) traversal of the subtree rooted at `root` using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use `yield` to immediately generate an element in your function, and `yield from` to generate an element from a recursive function call.
  - Do not yield (generate) `None`-types.
  - _Time / Space: O(n) / O(1)_.
    - Although we will traverse the entire tree and hence incur O(n) time, our use of a generator will keep us at constant space complexity since elements are yielded one at a time! This is a key advantage of returning a generator instead of a list.
  - **root: Node:** The root `Node` of the subtree currently being traversed.
  - **Returns:** `Generator` object which yields `Node` objects only (no `None`-type yields). Once all nodes of the tree have been yielded, a `StopIteration` exception is raised.
  
- **postorder(self, root: Node) -> Generator[Node, None, None]**
  - Perform a postorder (left, right, current) traversal of the subtree rooted at `root` using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use `yield` to immediately generate an element in your function, and `yield from` to generate an element from a recursive function call.
  - Do not yield (generate) `None`-types.
  - _Time / Space: O(n) / O(1)_.
    - Although we will traverse the entire tree and hence incur O(n) time, our use of a generator will keep us at constant space complexity since elements are yielded one at a time! This is a key advantage of returning a generator instead of a list.
  - **root: Node:** The root `Node` of the subtree currently being traversed.
  - **Returns:** `Generator` object which yields `Node` objects only (no `None`-type yields). Once all nodes of the tree have been yielded, a `StopIteration` exception is raised.
- **levelorder(self, root: Node) -> Generator[Node, None, None]**
  - Perform a level-order (breadth-first) traversal of the subtree rooted at `root` using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use the builtin `queue.SimpleQueue` class to maintain your queue of children throughout the course of the traversal—[see the official documentation here.](https://docs.python.org/3/library/queue.html#queue.SimpleQueue)
  - Use `yield` to immediately generate an element in your function, and `yield from` to generate an element from a recursive function call.
  - Do not yield (generate) `None`-types.
  - _Time / Space: O(n) / O(n)_.
    - We will traverse the entire tree and incur O(n) time. In addition, the queue we must use for an inorder traversal will grow to size n/2 = O(n) just before beginning the final level of leaf nodes in the case of a [perfect binary tree.](https://www.programiz.com/dsa/perfect-binary-tree)
  - **root: Node:** The root `Node` of the subtree currently being traversed.
  - **Returns:** `Generator` object which yields `Node` objects only (no `None`-type yields). Once all nodes of the tree have been yielded, a `StopIteration` exception is raised.

## Application: Simple Query Language ##
Some of the earliest programming languages like COBOL (Common Business Orientated Language)
and [SQL](https://en.wikipedia.org/wiki/SQL_syntax) (Structured Query Language) were designed to be used by nonprogrammers. As such, their
syntax is relatively close to English, moreso than many modern programming languages! However, many SQL users
still struggle to write queries. That's where Simple Query Language comes in! It's like SQL, but with much more lenient and English-like syntax. For the application problem, you will complete a simple Database Table class for a Database class that accepts queries in Simple Query Language. The
database will require fast insertions, deletions, and lookups, but it also needs to be indexed and memory-efficient. As 
a CSE 331 student, you know that balanced binary trees, particularly AVL trees, are perfect for this task.
#### class AVLDatabase:

Database class containing table name to Table object dictionary that also handles queries.

_DO NOT MODIFY THIS CLASS_

- **Attributes**
  - **names_to_tables: Dict[str, Table]:** Dictionary containing string table name keys and Table object values.
- **\_\_init\_\_(self) -> None**
  - Construct an empty `AVLDatabase`. Initializes `names_to_tables` to an empty dictionary.
  - **Returns:** `None`.
- **query(self, query: str) -> List[List[int or str]] or None:**
  - Performs queries on the database by parsing query strings and calling the appropriate Table's methods.
  - **query: str:** Near-English database query string
  - **Returns:** Table represented as list of lists for "show me" queries, None otherwise.

#### class Table:

Class representing a Table within an AVLDatabase.

_DO NOT MODIFY THESE_

- **Attributes**
  - **names_to_indices: Dict[str, int]:** Dictionary mapping attribute names to indices for use in insertion, since attributes and corresponding values can be provided in any order.
  - **header_row: List[str]:** Header row containing the attributes in the correct order defined at creation, along with the index attribute prepended to all tables.
  This is used when displaying data, similar to SQL, where the first row shows the attribute names.
  - **data_tree: AVLTree:** Inner AVL tree used for storing data.
  - **insertion_index: int:** In SQL it is common to put auto incrementing IDs or indices as an attribute in tables for use in joining tables and differentiating otherwise identical rows.
  This will start at zero and increase every time an insert occurs. It will never decrease, not even for removals.
- **\_\_init\_\_(self, attribute_names: List[str]) -> None**
  - Constructs an empty `Table` with correct initial attribute values.
  - **attribute_names: List[str]:** Names of attributes to act as column titles within our table in order.
  - **Returns:** `None`.

_COMPLETE THESE FUNCTIONS_
- **insert_rows(self, values: List[List[str]], attributes: List[str]) -> None:**
  - Goes through the lists in values and inserts their data one by one into the Table by inserting into **data_tree**.
  - You should insert the current **insertion_index** value as the AVL tree Node _value_ so it can be used for ordering. It should start at zero so increment it _after_ you insert.
  - The AVL tree Node _data_ should be a 1D list of values that correspond to the attributes in the correct order (the order at creation). Reorder the values as necessary (hint: use one of the **attributes** of this class as well as the attributes list from this function).
  - Do NOT create a Node object in this function! Use AVLTree's insert function to do it for you!
  - _Time / Space: O(r\*logn) / O(1)_, where _r_ is the number of rows to insert (number of lists in **values**), and _n_ is the total number of rows in the table. Do not make the space complexity _O(r)_! We assume the number of attributes is constant, so having inner loops that run len(attributes) many times or additional data of size len(attributes) is probably fine. The size of the AVL tree is not included in the space complexity.
  - **values: List[List[str]]:** List of lists of values where the 0th index in each list corresponds
  to the attribute at the 0th index in the attributes list and so on and so forth for the remaining indices. Each list within the list will become a row in the table. Lists should be inserted in order.
  - **attributes: List[str]:** List of attributes to which the values correspond. Note that the order here may differ from the order at creation, the latter of which is required for displaying the data in "show me" queries.
  - **Returns:** `None`.

- **remove_rows(self, indices: List[str]) -> None:**
  - Removes all specified indices from the table.
  - AVLTree's remove function uses the Node's _value_, so be sure to use **insertion_index** for it in **insert_rows**.
  - Should not throw an exception if the index is not present in the table.
  - Don't forget to cast the indices to integers so they match the type of **insertion_index**.
  - This function should be ~2 lines.
  - _Time / Space: O(r*logn) / O(1)_, where r is the number of indices to remove, and n is the total number of rows in the table. Do not make the space complexity O(r)!
  - **indices: List[str]:** List of indices to remove from the table.
  - **Returns:** `None`.
- **show_latest(self) -> List[List[str]]:**
  - Displays the header row and latest (highest index--what function gives you the Node with the highest _value_?) row in a list of lists (see examples).
  - Note that the index will be an integer type while the other data will be strings.
  - If the **data_tree** is empty, just display the **header row** inside a list so the result is still a list of lists.
  - You will need to combine the index (from _value_) with the data (from _data_). extend() is useful for this.
  - _Time / Space: O(logn) / O(1)_, where n is the total number of rows in the table. Remember the number of attributes is considered constant.
  - **Returns:** List of lists where the first list is the header row and the second list is the values of the most recently inserted row corresponding to the attributes at the same indices within the header row.
- **show_oldest(self) -> List[List[str]]:**
  - Displays the header row and oldest (lowest index--what function gives you the Node with the lowest _value_?) row in a list of lists (see examples).
  - Note that the index will be an integer type while the other data will be strings.
  - If the **data_tree** is empty, just display the **header row** inside a list so the result is still a list of lists.
  - You will need to combine the index (from _value_) with the data (from _data_). extend() is useful for this.
  - Should be very similar to show_latest().
  - _Time / Space: O(logn) / O(1)_, where n is the total number of rows in the table. Remember the number of attributes is considered constant.
  - **Returns:** List of lists where the first list is the header row and the second list is the values of the oldest inserted row corresponding to the attributes at the same indices within the header row.
- **show_everything(self) -> List[List[str]]:**
  - Displays the header row and all data rows with their indices **in ascending index order**.
  - The use of sorting for achieving ascending index order will result in a 0 for all points of this function.
  - Should be similar to the previous two functions in terms of constructing the resulting list of lists, possibly using extend().
  - Hint: You can iterate over an AVLTree generator object with a for loop thanks to the __iter__ method. What AVLTree function returns a generator and is the best choice for this function?
  - _Time / Space: O(n) / O(n)_, where n is the total number of rows in the table. Remember, the number of attributes is considered constant.
  - **Returns:** List of lists where the first list is the header row and the subsequent lists are the rows in the table in ascending index order whose values correspond via matching indices to the header row's attribute names.

### Examples:  
Example 1.  
```angular2html
db.query("Create for me an awesome table thingy or whatever, table1, "
         "and give it the attributes length, width, height, mass, temperature. Make it snappy!")

actual = db.query("Show me from the table, table1, like, everything.")
expected = [['index', 'length', 'width', 'height', 'mass', 'temperature']]
self.assertEqual(actual, expected)

actual = db.query("Show me from the table, table1, the latest row, okay?")
self.assertEqual(actual, expected)

actual = db.query("Show me the oldest row from the table, table1, got it?")
self.assertEqual(actual, expected)
```
An empty table should just return the header_row **in a list of lists**!

Example 2.  
```
db.query("create, table2, attributes annual revenue, annual expenses, account type.")
db.query("insert into, TABLE2, values: 100306, 64023, savings "
         "with attributes annual revenue, annual expenses, account type.")
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
```
Note that when table2 was created, the attribute order was annual revenue, annual expenses, account type.
However, when the second insert query happened the attribute order was account type, annual revenue, annual expenses, a completely different permutation!
The "show me everything" query shows the header row with the creation attribute order and as you can see the row from the second insert query (index 1)
had its values reordered to match the attribute order at creation.
Notice that the "show me latest" query includes the header row and only the row with the highest index, and similarly for the "show me oldest" query with the lowest index row.

Example 3.  
```angular2html
db.query("Create for me an awesome table thingy or whatever, table1, "
         "and give it the attributes length, width, height, mass, temperature. Make it snappy!")
db.query("Remove from the table, table1, like, the indices 5, 3, 2, 6, 1.")  # should not throw an error

db.query("create, table2, attributes annual revenue, annual expenses, account type.")
db.query("insert into, TABLE2, values: 100306, 64023, savings "
         "with attributes annual revenue, annual expenses, account type.")
db.query("insert into, table2, values: checking, 57821, 130012 "
         "with attributes account type, annual revenue, annual expenses.")

db.query("Remove from the table that I call, table2, those dang indices 1.")
actual = db.query("show me, table2, everything.")
expected = [['index', 'annual revenue', 'annual expenses', 'account type'],
            [0, '100306', '64023', 'savings']]
self.assertEqual(actual, expected)

actual = db.query("show me, table2, latest.")
self.assertEqual(actual, expected)

actual = db.query("show me, table2, oldest.")
self.assertEqual(actual, expected)
```
Removals should not throw exceptions if they target nonexistent indices. Removing an index should
drop it from the table so that it no longer shows up on a "show me" query. Note that with only one row, the oldest and latest rows are equivalent.

## Submission

#### Deliverables

Be sure to upload the following deliverables in a .zip folder to Mimir by 10:00p ET on Thursday, March 31st.

    Project07.zip
        |— Project07/
            |— feedback.xml     (for project feedback)
            |— __init__.py      (for proper Mimir testcase loading)
            |— solution.py      (contains your solution source code)

#### Grading

- Tests (75)
  - Coding Standard: \_\_/3
  - feedback.xml Validity Check: \_\_/3
  - `AVLTree`: \_\_/
    - `right_rotate`: \_\_/1
    - `balance_factor`: \_\_/1
    - `rebalance`: \_\_/8
    - `insert`: \_\_/8
    - `min`: \_\_/2
    - `max`: \_\_/2
    - `search`: \_\_/8
    - `inorder`/`__iter__`: \_\_/1
    - `preorder`: \_\_/1
    - `postorder`: \_\_/1
    - `levelorder`: \_\_/1
  - `Application Problem`: \_\_/
    - `basic`: \_\_/1
    - `large`: \_\_/1
- Manual (25)
  - Time and space complexity points are **all-or-nothing** for each function. If you fail to meet time **or** space complexity in a given function, you do not receive manual points for that function. 
  - Loss of 1 point per missing docstring (max 3 point loss)
  - Loss of 2 points per changed function signature (max 20 point loss)
  - Loss of 20 points (flat-rate) for use of global variables (with the nonlocal keyword)
    - `AVLTree` time & space: \_\_/15
      - `right_rotate`: \_\_/1
      - `balance_factor`: \_\_/2
      - `rebalance`: \_\_/2
      - `insert`: \_\_/2
      - `min`: \_\_/1
      - `max`: \_\_/1
      - `search`: \_\_/2
      - `inorder`/`__iter__`: \_\_/1
      - `preorder`: \_\_/1
      - `postorder`: \_\_/1
      - `levelorder`: \_\_/1
    - `Application Problem` time & space: \_\_/5
## Appendix

#### Authors

Project authored by Bank Premsri. Adapted from work by Andrew McDonald, Jacob Caurdy, Lukas Richters, and Joseph Pallipadan.

#### Memes

![](img/tree.jpg)

![](img/thanos.jpg)

![](img/bestworst.png)

![](img/img.png)