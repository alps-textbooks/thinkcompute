# About This Book

![2Sigma School](2sigma-school-logo.svg)

**Think and Compute: a Primer for Digital Humanists** · *Computational thinking and Python programming for the humanities*

**2Sigma School** · Alps edition · Updated November 2026

Think and Compute introduces computational thinking and Python programming to students in the humanities, from algorithms and data structures to recursion, graphs, and working with relational and graph data. This Alps edition keeps the authors' words and runs the book's code in the page, with nothing to install.

| At a glance | |
|---|---|
| **9 parts** | Basics of Computation; Basics of Programming; A Python Laboratory; Additional Algorithmic Techniques and Data Structures; Laboratory on Divide-and-Conquer and File Handling; Managing Data in Python; A Laboratory on Managing Data; Databases; Laboratory on Databases |
| **299 code cells** | Python that runs in the browser, in the chapters and the laboratories |

## How to Use It

Read each chapter in order and run its code as you go. Laboratories and data chapters are notebooks: run a cell on its own, or choose **Run All** in the toolbar to run the page from the top.

> **Found a problem?** Teachers: choose Report Bug in the left menu, then select the bug icon on the item, or highlight the text. Students: tell your teacher. You can also email [support@alps.2sigma.us](mailto:support@alps.2sigma.us) with the book, chapter and page name.

## Credits

*Think and Compute: a Primer for Digital Humanists* is by Silvio Peroni, Ivan Heibi and Arcangelo Massari.

Source: [https://github.com/thinkcompute/thinkcompute.github.io](https://github.com/thinkcompute/thinkcompute.github.io)

License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This edition is shared under the same license.

This edition has been adapted for Alps. As with every book on Alps, its preparation draws on Alps's content-enhancement capabilities, which include the use of language models.

The authors of the original book are not affiliated with, and do not endorse, this edition.

## Alps Compatibility Changes

The book's text is otherwise as its authors wrote it. These are the only changes, and each one is there so the page imports or runs in Alps. The numbering of the book's chapters is not affected: this page closes the Preface.

| Page | Change |
|---|---|
| Configuring and populating a graph database | The cell that uploads triples to a Blazegraph server is shown for reference and does not run, because no server can run in a browser tab. A screenshot's file name is corrected so the picture loads. |
| Interacting with databases using Pandas | An explanation and a code cell are added. The cell loads the triples built in the previous chapter from `notebook/graph.ttl`, a file added to this edition, into an in-memory graph, and defines a `get` function that does what the one in `sparql_dataframe` does. The book's SPARQL queries then run unchanged. The query cells no longer import `sparql_dataframe`. |
| Organising information: unordered structures | In `python/set_instructions.py`, the source of this page's runnable code, `my_first_set.set("Silvio")` becomes `my_first_set.add("Silvio")`, as the chapter's own text has it, so the cell runs. |
| Greedy algorithms; Part 4: Exercises | A code fence is corrected, and in the exercises the accents around a cross-reference become backticks, so each page renders as written. |
| Lists, loops, conditionals, and functions; Working with files | The fences around admonition boxes are lengthened, so the code examples inside them stay inside the box. |
| Getting started with Python | A note is added at the top. It says that the lab's code cells run in the page, that its installation steps are for working on your own computer, and that its rocket icon and **Live Code** steps are for the book's own website. |
