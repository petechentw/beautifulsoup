# Milestone-4


In this milestone, I create a __iter__ to make soup iterable. It returns all the nodes in tree with pre-order DFS contains all page elements include whitespace and comment.
``` yield ``` can remenber which node iterate at temperorily, and when the function call ``` generator()``` again it will start from the node. 
``` yield ``` make sure visit and return it at the same time without list.
```.descentdants``` is a streaming traversal function that built in bs4.


## test_M4.py

``` pytest ./bs4/tests/test_M4.py  ``` 

## Milestone4.py
``` python3 -m apps.m4.Milestone4 ./apps/m4/test.html ```

     