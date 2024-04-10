# What is REmatch?

**REmatch** is a novel C++/Python library for extracting information from plain documents by using his query language **REQL** (for *Regular Expressions Query Language*). The syntax of **REQL** is almost identical to that of standard RegEx libraries (like POSIX or PCRE), except for the treatment of capture groups. This stems from the design philosophy behind **REmatch**: It is a library made to extract data from text. This is somewhat complementary to the main focus of standard RegEx libraries, whose main objective is to search for a pattern inside of a document.

To make this explicit, in **REQL** every extraction group is named, and called a variable. For example, instead of writing `([a-z]+)` to extract a sequence of one or more lower case letters, in **REQL** we write `!x{[a-z]+}` indicating that a match of the pattern `[a-z]+` is extracted into the variable x. This is particularly useful when multiple variables are used, and when wanting to do more complex operations with the obtained results. For instance, we might want to take a variable x storing the name of a person, and a variable y, storing their last name, and return them in the format `last name, first name`. As we will see later, having variable names makes this rather trivial.

It is important to note that the syntax of REQL query without capture groups is identical as it is in any other RegEx library you might have encountered before.

## Another library for RegEx?

No. **REmatch** is different from other RegEx libraries. Regarding evaluating simple regular expressions (without grouping), **REmatch** has no differences, and it runs as fast as other libraries. However, suppose you want to extract information. In that case, **REmatch** is different: **REmatch** looks for **ALL POSSIBLE** matches of your regular expression with the document. To illustrate why this might be useful, we provide several examples from text analysis. For this purpose, we will analyze the first paragraph of Tom Sawyer's book "Adventures of Huckleberry Finn" shown in the box below.

> You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer but that ain't no matter. That book was made by Mr Mark Twain and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly or the widow, or maybe Mary. Aunt Polly-Tom's Aunt Polly, she is-and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.

### Example 1

One common task in analyzing a corpus of text is determining the context in which certain words appear. For instance, we might wish to extract each proper noun (for simplicity we will consider any uppercase letter a proper noun), together with the sentence in which it appears, in order to determine what is the most common way the noun is used.

If you are used to writing regular expressions, you would probably come up with something similar to the formula below:

```
(^|\.)([^\.]*([A-Z][a-z]*)( [^\.]*)?\.)
```

Intuitively, the outer group searches for the sentence (starting with a capital letter and expanding until a dot, without seeing any dots in between) , and the inner group looks for the proper noun inside of this sentence. If you try to evaluate this expression in your favourite RegEx engine (try it [here](https://regex101.com/r/ni9ewu/1)), you will indeed obtain all sentences which have a proper noun inside them, and the noun itself. The problem is, that for each sentence with more than one proper noun inside, only one occurrence is returned. For example, the very first sentence of our text contains a series of proper nouns, but only the very last one (Sawyer) will be returned. You can play around with RegEx libraries and come up with a series of similar expressions, but due to the "greedy" semantics they deploy, none of them will actually allow you to specify the desired data with a single RegEx.

On the other hand, the **REQL** query below does the trick.

```
(^|\.)!sentence{[^\.]*!noun{[A-Z][a-z]*}( [^\.]*)?\.}
```

You can test this query directly in our REmatch console by clicking [here](https://rematch.cl/?query=%28%5E%7C%5C.%29%21sentence%7B%5B%5E.%5D*%21noun%7B%5BA-Z%5D%5Ba-z%5D*%7D%28+%5B%5E.%5D*%29%3F%5C.%7D&doc=You+don%27t+know+about+me+without+you+have+read+a+book+by+the+name+of+The+Adventures+of+Tom+Sawyer+but+that+ain%27t+no+matter.+That+book+was+made+by+Mr+Mark+Twain+and+he+told+the+truth%2C+mainly.+There+was+things+which+he+stretched%2C+but+mainly+he+told+the+truth.+That+is+nothing.+I+never+seen+anybody+but+lied+one+time+or+another%2C+without+it+was+Aunt+Polly+or+the+widow%2C+or+maybe+Mary.+Aunt+Polly-Tom%27s+Aunt+Polly%2C+she+is-and+Mary%2C+and+the+Widow+Douglas+is+all+told+about+in+that+book%2C+which+is+mostly+a+true+book%2C+with+some+stretchers%2C+as+I+said+before.&isMultiRegex=false).

### Example 2

Another typical task is to analyze when two terms are used together in the same context. For example, we might wonder when two characters are talked about in the same sentence in our text. For this, we might want to extract all pairs of proper nouns that appear within the same sentence.

With RegEx, we might do something similar to the example above, but now adding an additional capture group inside of the sentence. The result is something similar to:

```
(^|\.)([^\.]*([A-Z][a-z]*) [^\.]*([A-Z][a-z]*)( [^\.]*)?\.)
```

Indeed, this expression works very well when only two proper nouns are present inside of a sentence (try it [here](https://regex101.com/r/iSj0t4/1)). However, in the final sentence of our paragraph this will not work since multiple proper nouns are present. On the other hand, in **REmatch**, the following **REQL** query does the trick (again, you can test it [here](https://rematch.cl/?query=%28%5E%7C%5C.%29%21sentence%7B%5B%5E.%5D*%21noun1%7B%5BA-Z%5D%5Ba-z%5D*%7D+%5B%5E.%5D*%21noun2%7B%5BA-Z%5D%5Ba-z%5D*%7D%28+%5B%5E.%5D*%29%3F%5C.%7D&doc=You+don%27t+know+about+me+without+you+have+read+a+book+by+the+name+of+The+Adventures+of+Tom+Sawyer+but+that+ain%27t+no+matter.+That+book+was+made+by+Mr+Mark+Twain+and+he+told+the+truth%2C+mainly.+There+was+things+which+he+stretched%2C+but+mainly+he+told+the+truth.+That+is+nothing.+I+never+seen+anybody+but+lied+one+time+or+another%2C+without+it+was+Aunt+Polly+or+the+widow%2C+or+maybe+Mary.+Aunt+Polly-Tom%27s+Aunt+Polly%2C+she+is-and+Mary%2C+and+the+Widow+Douglas+is+all+told+about+in+that+book%2C+which+is+mostly+a+true+book%2C+with+some+stretchers%2C+as+I+said+before.&isMultiRegex=false)):

```
(^|\.)!sentence{[^\.]*!noun1{[A-Z][a-z]*} [^\.]*!noun2{[A-Z][a-z]*}( [^\.]*)?\.}
```

We note that the logic is equivalent in both extensions: we simply duplicate the pattern for the proper noun. Also note that the **REQL** query above is a bit more verbose principally due to having explicit variable names, given that the remainder of the expressions is identical.

### Example 3

As our final example we will assume that we want to extract all non empty substrings from our text. The REmatch expression for this is simply (test it [here](https://rematch.cl/?query=%21substring%7B.%2B%7D&doc=You+don%27t+know+about+me+without+you+have+read+a+book+by+the+name+of+The+Adventures+of+Tom+Sawyer+but+that+ain%27t+no+matter.+That+book+was+made+by+Mr+Mark+Twain+and+he+told+the+truth%2C+mainly.+There+was+things+which+he+stretched%2C+but+mainly+he+told+the+truth.+That+is+nothing.+I+never+seen+anybody+but+lied+one+time+or+another%2C+without+it+was+Aunt+Polly+or+the+widow%2C+or+maybe+Mary.+Aunt+Polly-Tom%27s+Aunt+Polly%2C+she+is-and+Mary%2C+and+the+Widow+Douglas+is+all+told+about+in+that+book%2C+which+is+mostly+a+true+book%2C+with+some+stretchers%2C+as+I+said+before.&isMultiRegex=false):

```
!substring{.+}
```

The expression works as intended: `.+` positions us anywhere inside the document, then a non empty string is extracted into the variable `substring`, and finally the expression matches the remainder of the document via the `.+` statement.

Strictly speaking, standard RegEx libraries can not express this query in a single expression. Indeed, due to their semantics, the synthetic equivalent of the expression above, that is, `(.+)`, will simply match the entire document, and something similar occurs with `.*(.+).*`. One can use RegEx libraries and force the expression to try and retrieve the match from every possible position by using so-called *lookaround* operators. This will still not do the trick, as the entire remainder of the string will be consumed.

## More outputs more time?

No. **REmatch** is based on the [framework of document spanners](https://dl.acm.org/doi/10.1145/2699442) and the theory of [constant-delay algorithms](https://dl.acm.org/doi/abs/10.1145/1276920.1276923) that have been developed in the last years. In a nutshell, the **REmatch** algorithm reads your document just once and takes a fixed amount of time (say `0.001ms`) to give you the next output. Of course, if the engine finds 1 million results, it will take you 1 second to get all of them, but no more than that. In fact, suppose the file has `1MB` of data, and we take 1ms to read the document. In that case, the algorithm will take `0.001ms` to give you the next result, regardless that it found ten or 10^10 outputs.

Given its design philosophy, **REmatch** also does not suffer from the [catastrophic backtracking](https://www.regular-expressions.info/catastrophic.html) issue many RegEx engines are susceptible to. In a nutshell, **REmatch** can run even faster than standard RegEx libraries and finds more outputs at the same time!

We invite you to explore the **REmatch** algorithm in our [academic paper](https://www.vldb.org/pvldb/vol16/p2792-vrgoc.pdf), by examining its source code on [GitHub](https://github.com/REmatchChile), or by experimenting with a version of **REmatch** in your favourite programming language. The current support includes C++ and Python.
