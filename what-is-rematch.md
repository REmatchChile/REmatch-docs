# What is REmatch?

**REmatch** is a novel C++/Python library for extracting information from plain documents by using his query language **REQL** (for *Regular Expressions Query Language*). The syntax of REQL is almost identical to that of standard RegEx libraries (like POSIX or PCRE), except for the treatment of capture variables (refered as capture groups in RegEx). This stems from the design philosophy behind REmatch: It is a library made to extract data from text. This is somewhat complementary to the main focus of standard RegEx libraries, whose main objective is to search for a pattern inside of a document.

To make this explicit, in REQL every extraction group is named, and called a variable. For example, instead of writing `([a-z]+)` to extract a sequence of one or more lower case letters with RegEx, in REQL we write `!x{[a-z]+}` indicating that a match of the pattern `[a-z]+` is extracted into the variable x. This is particularly useful when multiple variables are used, and when wanting to do more complex operations with the obtained results. For instance, we might want to take a variable `x` storing the name of a person, and a variable `y`, storing their last name, and return them in the format `last name, first name`. As we will see later, having variable names makes this rather trivial.

It is important to note that the syntax of REQL query without capture groups is identical as it is in any other RegEx library you might have encountered before.

## Another library for RegEx?

No. REmatch is not just another RegEx library. Regarding evaluating simple RegEx patterns (without variables), REmatch has no differences and runs as fast as other libraries. However, suppose you want to extract information. In that case, REmatch is different: REmatch always looks for **ALL MATCHES** of your REQL query with the document. To illustrate why this might be useful, consider a use case from text analysis where we want to analyze the first paragraph of Tom Sawyer's book "Adventures of Huckleberry Finn" shown below.

> You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer but that ain't no matter. That book was made by Mr Mark Twain and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly or the widow, or maybe Mary. Aunt Polly-Tom's Aunt Polly, she is-and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.

One common task in analyzing a corpus of text is determining the context in which certain words appear. For instance, we might wish to extract each proper noun (for simplicity we will consider any uppercase letter a proper noun), together with the sentence in which it appears, in order to determine what is the most common way the noun is used.

If you are used to writing RegEx patterns, you would probably come up with something similar to the formula below:

    (^|\.)([^\.]*([A-Z][a-z]*)( [^\.]*)?\.)

Intuitively, the outer group searches for the sentence (starting with a capital letter and expanding until a dot, without seeing any dots in between), and the inner group looks for the proper noun inside of this sentence. If you try to evaluate this pattern in your favorite RegEx engine (try it [here](https://regex101.com/r/ni9ewu/1)), you will indeed obtain all sentences that have a proper noun inside them and the noun itself. The problem is that only one occurrence is returned for each sentence with more than one proper noun inside. For example, the very first sentence of our text contains a series of proper nouns, but only the very last one (Sawyer) will be returned. You can play around with RegEx libraries and come up with a series of similar patterns, but due to the "greedy" semantics they deploy, none of them will allow you to specify the desired data with a single RegEx.

On the other hand, the REQL query below does the trick.

    (^|\.)!sentence{[^.]*!noun{[A-Z][a-z]*}( [^.]*)?\.}

You can test this query directly in our REmatch console by clicking [here](https://rematch.cl/?query=%28%5E%7C%5C.%29%21sentence%7B%5B%5E.%5D*%21noun%7B%5BA-Z%5D%5Ba-z%5D*%7D%28+%5B%5E.%5D*%29%3F%5C.%7D&doc=You+don%27t+know+about+me+without+you+have+read+a+book+by+the+name+of+The+Adventures+of+Tom+Sawyer+but+that+ain%27t+no+matter.+That+book+was+made+by+Mr+Mark+Twain+and+he+told+the+truth%2C+mainly.+There+was+things+which+he+stretched%2C+but+mainly+he+told+the+truth.+That+is+nothing.+I+never+seen+anybody+but+lied+one+time+or+another%2C+without+it+was+Aunt+Polly+or+the+widow%2C+or+maybe+Mary.+Aunt+Polly-Tom%27s+Aunt+Polly%2C+she+is-and+Mary%2C+and+the+Widow+Douglas+is+all+told+about+in+that+book%2C+which+is+mostly+a+true+book%2C+with+some+stretchers%2C+as+I+said+before.&isMultiRegex=false). As you can see, REmatch is different from any standard RegEx library. The crucial distinction between REmatch and your favorite RegEx library is that REmatch always returns all matches, giving more power to extract relevant information from documents and more flexibility for your programming tasks. You can try more examples and see this difference in other scenarios [here](https://rematch.cl/examples).

## More outputs more time?

No. REmatch is based on the [framework of document spanners](https://dl.acm.org/doi/10.1145/2699442) and the theory of [constant-delay algorithms](https://dl.acm.org/doi/abs/10.1145/1276920.1276923) that have been developed in the last decade. In a nutshell, the REmatch algorithm reads your document just once and takes a fixed amount of time (say `0.001ms`) to give you the next output. Of course, if the engine finds 1 million results, it will take you 1 second to get all of them, but no more than that. In fact, suppose the file has `1MB` of data, and we take 1ms to read the document. In that case, the algorithm will take `0.001ms` to give you the next result, regardless of whether it found ten or 10^10 outputs.

To give a feeling of REmatch's algorithmic approach, we can write a query with REQL that extracts all substrings from our text. The REQL query for this is simply (test it [here](https://rematch.cl/?query=%21substring%7B.%2B%7D&doc=You+don%27t+know+about+me+without+you+have+read+a+book+by+the+name+of+The+Adventures+of+Tom+Sawyer+but+that+ain%27t+no+matter.+That+book+was+made+by+Mr+Mark+Twain+and+he+told+the+truth%2C+mainly.+There+was+things+which+he+stretched%2C+but+mainly+he+told+the+truth.+That+is+nothing.+I+never+seen+anybody+but+lied+one+time+or+another%2C+without+it+was+Aunt+Polly+or+the+widow%2C+or+maybe+Mary.+Aunt+Polly-Tom%27s+Aunt+Polly%2C+she+is-and+Mary%2C+and+the+Widow+Douglas+is+all+told+about+in+that+book%2C+which+is+mostly+a+true+book%2C+with+some+stretchers%2C+as+I+said+before.&isMultiRegex=false)):

    !substring{.+}

The query works as intended: the `.+` matches any substring in the document, and REmatch stores it into the variable `substring`. Again, standard RegEx libraries cannot express this query in a single pattern. Indeed, due to their semantics, the synthetic equivalent of the query above (for example, `(.+)`) will simply match the entire document, and something similar occurs with any other RegEx pattern you can write. 

What is more important is that with this query, REmatch outputs a huge number of outputs without degrading his performance. Indeed, you can increase the document size, and REmatch provides you with all the outputs quickly (you can play with this by increasing the document size yourself). As you can see, no matter how big the document is, REmatch will give you the first output once it is read, enumerating all the results and taking a fixed amount of time between two consecutive outputs.

Given its design philosophy, REmatch also does not suffer from the [catastrophic backtracking](https://www.regular-expressions.info/catastrophic.html) issue many RegEx engines are susceptible to. In a nutshell, REmatch can run even faster than standard RegEx libraries and finds more outputs at the same time!

## Beyond RegEx with multimatch capturing

REmatch goes even beyond the capabilities of any RegEx library by introducing the novel idea of **MultiMatch**. In a nutshell, multimatch capturing allows you to extract lists of spans in variables, and then, with one match, one can capture an unbounded number of spans! This unique feature is helpful when extracting an unbounded number of fields or optional fields from data, which one cannot do with normal matches. 

To briefly exemplify the power of multimatch, suppose that we want to extract all sentences from our document and all its words for each sentence. We can do this task by using REQL and multimatch as follows:

    (^|\. )!sentence{(!words{[A-Za-z']+}[^A-Za-z'.]+)*!words{[A-Za-z']+}\.}

In this query, we allow using variables inside repetitions `+`, which intuitively means that we want to capture one or more words in the variable `words`. By running this query in REmatch's web interface (try it [here](https://rematch.cl/?query=%28%5E%7C%5C.+%29%21sentence%7B%28%21words%7B%5BA-Za-z%27%5D%2B%7D%5B%5EA-Za-z%27.%5D%2B%29*%21words%7B%5BA-Za-z%27%5D%2B%7D%5C.%7D&doc=You+don%27t+know+about+me+without+you+have+read+a+book+by+the+name+of+The+Adventures+of+Tom+Sawyer+but+that+ain%27t+no+matter.+That+book+was+made+by+Mr+Mark+Twain+and+he+told+the+truth%2C+mainly.+There+was+things+which+he+stretched%2C+but+mainly+he+told+the+truth.+That+is+nothing.+I+never+seen+anybody+but+lied+one+time+or+another%2C+without+it+was+Aunt+Polly+or+the+widow%2C+or+maybe+Mary.+Aunt+Polly-Tom%27s+Aunt+Polly%2C+she+is-and+Mary%2C+and+the+Widow+Douglas+is+all+told+about+in+that+book%2C+which+is+mostly+a+true+book%2C+with+some+stretchers%2C+as+I+said+before.&isMultiMatch=true)), you can see that now each output contains a sentence, and the variable word contains all its words. 

REmatch's multimatch feature significantly enhances the capabilities of information extraction, surpassing any RegEx library. Its practicality in handling unbounded fields or optional fields in data makes it a valuable tool for developers and data scientists.

## Try REmatch!

We invite you to explore REmatch and learn to use REQL from this website. The section [examples](https://rematch.cl/examples) contains more REQL queries and use cases. Further, the [REQL tutorial](https://rematch.cl/tutorial) will help you to learn how to extract information with REQL features like capturing variables, its all-match semantics, and multimatch capturing. 

You can also take a look at the insides of REmatch's engine by reading our [academic paper](https://www.vldb.org/pvldb/vol16/p2792-vrgoc.pdf), examining its source code on [GitHub](https://github.com/REmatchChile), or by experimenting with a version of REmatch in your favorite programming language like C++ or Python.
