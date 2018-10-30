"""
Given a tree representation of a html parsed output, wherein every block is a node in the tree, find if two html docs contain the same text.
```
struct Node {
       string value;
       bool isMetadata;
       vector<Node*> children;
};
```
For eg, consider the two documents
<html><head>sample</head><body>
Hello world

</body></html> will be represented as Node1: value sample, children: <body> isMetadata: true Node2: value: <body> children:
isMetadata: true Node3: value:

: children: Hello world isMetadata: true Node4: value Hello world isMetadata: false

and a second document

<html><body>Hello world</body></html>
and both documents are equivalent since they contain the same data.

Note: the case of both documents fitting in memory is trivial, since it is just walking this tree list, consolidating data and comparing. As a follow up, solve the case where the whole documents may not be able to fit in memory.
"
""