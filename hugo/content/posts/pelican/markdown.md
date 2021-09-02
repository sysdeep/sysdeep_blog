---
Title: Markdown syntax for Pelican Quick Reference
Date: 2014-06-20T15:28:00+03:00
Category: Development
Tags: [development, markdown]
---

This post is a simple markdown syntax reference for Pelican(the static blog generator that builds this blog), especially coupled with some features from Python-Markdown.

Basic Syntax
============


Headings
--------

Setext style:

	This is an H1
	=============

	This is an H2
	-------------

Atx style:

	# This is H1 (#)optional
	# This is H2 (#)
	###### This is H6 (######)

Blockquote
----------
	> This is the first level of quoting.
	>
	> > This is nested blockquote.
	>
	> Back to the first level.

will output:

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.


List
----

Unordered list:

	* Red
	+ Green
	- Blue

* Red
+ Green
- Blue


Ordered list:

	1. Thor
	2. Ironman
	3. Hulk
1. Thor
2. Ironman
3. Hulk


Code block
----------
    Some text.

    code goes here.



Horizontal rules
----------------

	*** or --- or ___

*** 





Image
-----

Inline style:

	![Alt text](/path/to/img.jpg "Optional title")

Reference style:

	![Alt text][id]
	[id]: url/to/image  "Optional title attribute"


Link
----

	* This is an [Google](http://google.com/ "Googlelink") inline link.

	* This is an [Google][id] reference-style link.
	[id]: http://google.com/  "Optional Title Here"

	* See my [About](/about/) page for details.

	* An implict [Google][] link.
	[Google]: http://google.com/

	* An autolink <http://google.com/>

	* Email link <address@gmail.com>

* This is an [Google](http://google.com/ "Googlelink") inline link.

* This is an [Google][id] reference-style link.
[id]: http://google.com/  "Optional Title Here"

* See my [About](/about/) page for details.

* An implict [Google][] link.
[Google]: http://google.com/

* An autolink <http://google.com/>

* Email link <address@gmail.com>

Phrase Emphasis
---------------

	*stupid* or _stupid_ will output stupid.

	**stupid** or __stupid__ will output stupid.

Manual Line Breaks
------------------

Blackslash Escape
-----------------
	\ can escape following symbols: \`*_{}[]()#+-.!







Extra Features From Python-Markdown
===================================

Default features supported by Python-Markdown, i.e. extra and codehilite extension function. Consult here for more details. If you want to add more features, you should change the setting MD_EXTENSIONS (['codehilite','extra']).

Abbreviations
-------------

Attribute Lists
---------------

Definition Lists
----------------

	Apple
	:   Pomaceous fruit of plants of the genus Malus in 
	    the family Rosaceae.

	Orange
	:   The fruit of an evergreen tree of the genus Citrus.

Apple
:   Pomaceous fruit of plants of the genus Malus in 
    the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.



Fenced Code Blocks
------------------
	~~~~.python
	def factorial(n):
	if n == 0:
	    return 1
	else:
	    return n * factorial(n - 1)
	~~~~
will output:

~~~~.python
def factorial(n):
if n == 0:
    return 1
else:
    return n * factorial(n - 1)
~~~~


--- 

	~~~~{.python}
	def factorial(n):
	if n == 0:
	    return 1
	else:
	    return n * factorial(n - 1)
	~~~~
will output:

~~~~{.python}
def factorial(n):
if n == 0:
    return 1
else:
    return n * factorial(n - 1)
~~~~

---


	~~~~.html
	<p style="color: red">HTML Document</p>
	~~~~
will output:

~~~~.html
<p style="color: red">HTML Document</p>
~~~~




Github's tilde syntax:


	```python
	def factorial(n):
	if n == 0:
	    return 1
	else:
	    return n * factorial(n - 1)
	```
will output:

```python
def factorial(n):
if n == 0:
    return 1
else:
    return n * factorial(n - 1)
```


Footnotes
---------

	Footnotes[^1] have a label[^label] and a definition[^!DEF].

	[^1]: This is a footnote.
	    Paragraph two of the definition.

	    > A blockquote with
	    > multiple lines.

	        a code block

	    A final paragraph.

	[^label]: A footnote on "label"
	[^!DEF]: The definition of a footnote.

Footnotes[^1] have a label[^label] and a definition[^!DEF].

[^1]: This is a footnote.
    Paragraph two of the definition.

    > A blockquote with
    > multiple lines.

        a code block

    A final paragraph.

[^label]: A footnote on "label"
[^!DEF]: The definition of a footnote.






Tables
------

	First Header  | Second Header
	------------- | -------------
	Content Cell  | Content Cell
	Content Cell  | Content Cell

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell


CodeHilite
----------


Metadata for post
-----------------

	Title: Blog Title
	Date: 2010-12-03 10:20
	Tags: thats, awesome
	Category: yeah
	Slug: my-super-post
	Author: authorname
	Summary: Short version for index and feeds
	Status: draft

	This is the content of my super blog post.


	