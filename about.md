# About

## Regular Expressions in REmatch

The syntax of regular expressions in **REmatch** is almost identical to that of standard libraries, except for the treatment of capture groups. This stems from the design philosophy behind **REmatch**: It is a library made to extract data from text. This is somewhat complementary to the main focus of standard regex libraries, whose main objective is to search for a pattern inside of a document.

To make this explicit, every extraction group is named, and called a variable. For example, instead of writing `([a-z]*)` to extract a sequence of lower case letters, in **REmatch** we write `!x{[a-z]*}` indicating that this information is extracted into the variable x. This is particularly useful when multiple variables are used, and when wanting to do more complex operations with the obtained results. For instance, we might want to take a variable x storing the name of a person, and a variable y, storing their last name, and return them in the format `last name, first name`. Having variable names makes this rather trivial.

It is important to note that the syntax of regular expressions without capture groups is identical in **REmatch** as it is in any other regex library you might have encountered before.

## Another library for regular expressions?

No. **REmatch** is different from other regex libraries. Regarding evaluating simple regular expressions (without grouping), **REmatch** has no differences, and it runs as fast as other libraries. However, suppose you want to extract information. In that case, **REmatch** is different: **REmatch** looks for **ALL POSSIBLE** matches of your regular expression with the document. To illustrate why this might be useful, we provide several examples from text analysis. For this purpose, we will analyze the first paragraph of Tom Sawyer's book "Adventures of Huckleberry Finn" shown in the box below.

You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer but that ain't no matter. That book was made by Mr Mark Twain and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly or the widow, or maybe Mary. Aunt Polly-Tom's Aunt Polly, she is-and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.

> You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer but that ain't no matter. That book was made by Mr Mark Twain and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly or the widow, or maybe Mary. Aunt Polly-Tom's Aunt Polly, she is-and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.

### Example 1

One common task in analyzing a corpus of text is determining the context in which certain words appear. For instance, we might wish to extract each proper noun (for simplicity we will consider any uppercase letter a proper noun), together with the sentence in which it appears, in order to determine what is the most common way the noun is used.

If you are used to writing regular expressions, you would probably come up with something similar to the formula below:

```
(^|\.)([^\.]*([A-Z][a-z]*)( [^\.]*)?\.)
```

Intuitively, the outer group searches for the sentence (starting with a capital letter and expanding until a dot, without seeing any dots in between) , and the inner group looks for the proper noun inside of this sentence. If you try to evaluate this expression in your favourite regex engine (that, surprisingly, differs from **REmatch**), you will indeed obtain all sentences which have a proper noun inside them, and the noun itself. The problem is, that for each sentence with more than one proper noun inside, only one occurrence is returned. For example, the very first sentence of our text contains a series of proper nouns, but only the very last one (Sawyer) will be returned. You can play around with regex libraries and come up with a series of similar expressions, but due to the "greedy" semantics they deploy, none of them will actually allow you to specify the desired data with a single regex.

On the other hand, the **REmatch** expression below does the trick.

```
(^|\.)!sentence{[^\.]*!noun{[A-Z][a-z]*}( [^\.]*)?\.}
```

### Example 2

Another typical task is to analyze when two terms are used together in the same context. For example, we might wonder when two characters are talked about in the same sentence in our text. For this, we might want to extract all pairs of proper nouns that appear within the same sentence.

With regex, we might do something similar to the example above, but now adding an additional capture group inside of the sentence. The result is something similar to:

```
(^|\.)([^\.]*([A-Z][a-z]*) [^\.]*([A-Z][a-z]*)( [^\.]*)?\.)
```

Indeed, this expression works very well when only two proper nouns are present inside of a sentence. However, in the final sentence of our paragraph this will not work since multiple proper nouns are present. On the other hand, in **REmatch**, the following expression does the trick:

```
(^|\.)!sen{[^\.]*!n1{[A-Z][a-z]*} [^\.]*!n2{[A-Z][a-z]*}( [^\.]*)?\.}
```

We note that the logic is equivalent in both extensions: we simply duplicate the pattern for the proper noun. Also note that **REmatch** expression is more verbose principally due to having explicit variable names, given that the remainder of the expressions is identical.

### Example 3

As our final example we will assume that we want to extract all non empty substrings from our text. The REmatch expression for this is simply:

```
!x{.+}
```

The expression works as intended: `.*` positions us anywhere inside the document, then a non empty string is extracted into the variable `x`, and finally the expression matches the remainder of the document via the `.*` statement.

Strictly speaking, standard regex libraries can not express this query in a single expression. Indeed, due to their semantics, the synthetic equivalent of the expression above, that is, `(.+)`, will simply match the entire document, and something similar occurs with `.*(.+).*` One can use regex libraries and force the expression to try and retrieve the match from every possible position, this will still not do the trick, as the entire remainder of the string will be consumed.

While this example might seem very academic, and one might argue that something like overlapping matches might not be very useful (e.g. in a sequence `abcde` having both the substrings `bc` and `cde` might seem and overkill). We however argue that there are many use cases when precisely this type of behaviour is sought after.

The classical example here is DNA sequencing, where the DNA strand is represented as a string, and one would like to analyze different proteins involved in defining this DNA strand. The thing here is that proteins can be joined at certain points, meaning that if our strand has the letter sequence `abcabbcdefbb`, both `abcabb` (substring from positions 0 to 5), and `abbcdefbb` (positions 3 to 11) might be two proteins participating in this DNA strand (for simplicity we assume `ab` to be the start trigger, and `bb` the end trigger, the situation in real world is much more involved).

## More outputs more time?

No. **REmatch** is based on the [framework of document spanners](https://dl.acm.org/doi/10.1145/2699442) and the theory of ["constant-delay" algorithms](https://dl.acm.org/doi/abs/10.1145/1276920.1276923) that have been developed in the last years. In a nutshell, the **REmatch** algorithm reads your document just once and takes a fixed amount of time (say `0.001ms`) to give you the next output. Of course, if the engine finds 1 million results, it will take you 1 second to get all of them, but no more than that. In fact, suppose the file has `1MB` of data, and we take 1ms to read the document. In that case, the algorithm will take `0.001ms` to give you the next result, regardless that it found ten or 10^10 outputs.

Given its design philosophy, **REmatch** also does not suffer from the [catastrophic backtracking](https://www.regular-expressions.info/catastrophic.html) issue many regex engines are susceptible to. In a nutshell, **REmatch** can run even faster than standard regex libraries and finds more outputs at the same time!

We invite you to explore the **REmatch** algorithm in our [academic paper](https://dl.acm.org/doi/10.1145/3351451), by examining its source code on [GitHub](https://github.com/REmatchChile), or by experimenting with a version of **REmatch** in your favourite programming language. The current support includes `C++`, `Python` and `JavaScript`.

## About us

**REmatch** is currently being developed by **Nicolás Van Sint Jan**, **Vicente Calisto**, **Oscar Cárcamo**, **Kyle Bossonney** and professors [**Cristian Riveros**](https://criveros.sitios.ing.uc.cl/) and [**Domagoj Vrgoč**](https://dvrgoc.ing.puc.cl/), of the [Millenium Institute Foundational Research on Data](https://imfd.cl/en/) and the [School of Engineering of the Pontificia Universidad Católica de Chile](https://www.ing.uc.cl/en/). We thank **Martín de la Fuente**, **Javier Montoya** and **Marjorie Bascuñán**, for collaborating on earlier versions of this project.
