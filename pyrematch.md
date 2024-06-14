pyREmatch is the port of REmatch for Python. For installing the last release version from PyPI, run:

    pip install pyrematch

pyREmatch is designed to be compatible with a wide range of operating systems, including Windows, Mac OS, and most Linux distributions. If you encounter any issues with your specific operating system, please don't hesitate to contact us for support. 

The following explains how to use the pyRematch library in Python. We assume you already read REmatch's tutorial (in this wiki or at [https://rematch.cl/tutorial](https://rematch.cl/tutorial)) and are familiar with writing REQL queries. 

## Quick introduction

To quickly test pyREmatch, try the following code. 
```python
import pyrematch as REmatch

document = "cperez@gmail.com\npvergara@ing.uc.cl\njuansoto@uc.cl"
pattern = r"@!domain{(\w+\.)+\w+}(\n|$)"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(f'Match: "{match.group("domain")}"')
```
And you should get as output:
```
Match: "gmail.com"
Match: "ing.uc.cl"
Match: "uc.cl"
```
Let me briefly explain what this code does to get an idea. In the following sections, we explain all the methods and options of pyRematch in more detail. 

First, we take a string `document` as our input for REmatch, whose content is a simplified version of the running example used in REmatch's tutorial ([here](https://rematch.cl/tutorial)). The variable `document` has the following content:
```
cperez@gmail.com
pvergara@ing.uc.cl
juansoto@uc.cl
```
Then, we declare in `pattern` a REQL query `@!domain{(\w+\.)+\w+}(\n|$)`, also discussed during REmatch's tutorial. In a nutshell, these query looks for all email domains, saving the content after `@` in the variable `domain.` For compiling the query in `pattern` we call REmatch with line: 
```python
query = REmatch.reql(pattern)
```
Now, `query` is optimized and ready to evaluate for any string you want. For evaluating it over `document` we call:
```python
match_iterator = query.finditer(document)
```
that retrieves an iterator that allows you to loop over all matches and do what you want to fulfill your data-intensive task. In the code above, we print the string captured by each match. Simple as that!

## Finding matches

### The match object: group and span

As you may already know, **capture variables** are first citizens in REmatch for specifying in REQL what you want to extract when a query matches inside a document. When we run a REQL query over a document, REmatch returns all the query matches into the document. A **match** is a mapping of the variables to intervals of the document, namely, pairs `[i, j]` where `i` and `j` are the starting and ending positions of the substring captured by a variable. We usually call these intervals **spans** in REmatch. 

The object `match` in pyREmatch encodes a REmatch single output, storing one mapping from capture variables to spans. To see how the object `match` works, let's take the REQL query used in REmatch's tutorial for extracting the name and domain of each e-mail as follows:
```
(\n|^)!name{\w+}@!domain{(\w+\.)+\w+}(\n|$) 
```
Here, `name` and `domain` are variable names for capture variables that will store the name and domain of each e-mail, respectively. You can try this query with the following code to see how the match object works:
```python
import pyrematch as REmatch

document = "cperez@gmail.com\npvergara@ing.uc.cl\njuansoto@uc.cl"
pattern = r"(\n|^)!name{\w+}@!domain{(\w+\.)+\w+}(\n|$)"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(f'Match:')
    print(f'\tname -> "{match.group("name")}" at {match.span("name")}')
    print(f'\tdomain -> "{match.group("domain")}" at {match.span("domain")}')
```
The previous code iterates over all matches output by REmatch with the object `match` by performing a for-loop. For each `match`, we can retrieve the string and its span captured by variable `name`, and similarly for the variable `domain`. For printing the string, we use the method `group` and for printing the span, we use the method `span`. Both methods must receive the name of the variable. 

More specifically, the two methods of the object `match` that you need to know are `group` and `span`. 

- `match.group(variable-name)` retrieves the string captured by a variable. In the previous example, `match.group("name")` returns the string captured by variable `name` and `match.group("domain")` the string captured by variable `domain`.

- `match.span(variable-name)` allows access to the span \[i,j\], where the substring captured by the variable starts and ends. In the previous example, `match.span("name")` returns the span of variable `name` and `match.span("name")` the span of variable `domain`. 

Other methods from the `match` object that can be helpful are. 

- `match.start(variable-name)` outputs the starting position `i` of the span `[i,j]` captured by a variable. 

- `match.end(variable-name)` outputs the ending position `j` of the span `[i,j]` captured by a variable. 

You can also print the content of a match by calling the standard print function in Python:
```python
print(match)
``` 

### Iterating through all variables

Whenever you want to access the names of the variables in the `match` object, you can use the method `match.variables`. 

- `match.variables` outputs all the captured variables used by the `match` object. 

For example, instead of using the direct names of the variable from a query, you can iterate over them by using `match.variables`.

```python
import pyrematch as REmatch

document = "cperez@gmail.com\npvergara@ing.uc.cl\njuansoto@uc.cl"
pattern = r"(\n|^)!name{\w+}@!domain{(\w+\.)+\w+}(\n|$)"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(f'Match:')
    for variable in match.variables():
        print(f'\t{variable} -> "{match.group(variable)}" at {match.span(variable)}')
```
Note that the order how variables appears in `match.variables` is undefined, and you should not assume that they will appear in some specific order. 

### No variables: the empty match

What happens if a REQL query has no variables? This query is possible in REmatch! If you don't put any variable in the query and there is a match in the document, REmatch will output a single match, called the empty-match. As an example of a query without variables, you can run our example query as above but without variables.
```python
import pyrematch as REmatch

document = "cperez@gmail.com\npvergara@ing.uc.cl\njuansoto@uc.cl"
pattern = r"(\n|^)\w+@(\w+\.)+\w+(\n|$)"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(f'Match: {match}')
```
The previous code will print a single line `Match: Empty match`. Intuitively, a REQL query without variables works as a boolean query with TRUE or FALSE output. If the presence of the empty match means that the output is TRUE (that is, the query holds), and otherwise,  there is no match to iterate, and the output is FALSE.

### The object Query: finditer, findone, or check

We explain in the quick introduction that one must compile a REQL query string with `REmatch.reql(string-query)` to run it over a string. This method returns an object `Query` where the REQL was compiled, optimized, and ready to be used over a string or several. In particular, you don't need to compile the query again if you want to run it over another document. Just use the same object for efficiency. 

The object `Query` contains three methods for running over a document:

- `Query.finditer(string)` returns a `MatchIterator` object for iterating with a for-loop over all matches found over the string. 

- `Query.findone(string)` returns a single `match` object if it exists. 

- `Query.check(string)` returns TRUE if there exists a match of the query over the string and FALSE if there is none. 

It's worth noticing that you can always use the `finditer` method to find one match (like `findone`) or check if one match exists (like `check`). So, what is the advantage of using `findone` or `check` instead of `finditer`? The answer is efficiency. If you only want a single output or to check wheather there exists an output, pyREmatch provides the methods `findone` and `check` that are optimized for such tasks. In particular, they will run faster than using `finditer` for these simpler tasks.  

# PyREmatch multi match

## Quick example of multimatch

- Show a quick example showing multimatch.
- Explain the difference of Regex versus MultiRegex.

## MultiMatch Object

- Groups
- Spans 
- Span, group versus spans, groups

## Submatch and multiple variables

- Submatch feature

## Check and findone in multimatch

- Explain that check and findone has the same semantics but now with multimatch

# PyREmatch Exceptions

## Summary of exceptions

- AnchorInsideCaptureException
- ComplexQueryException
- EmptyWordCaptureException
- InvalidCharacterException
- InvalidEscapeException
- InvalidRangeException
- MemoryLimitExceededException
- RegexSyntaxException
- SameNestedVariableException
- UnhandledExpressionException
- VariableLimitExceededException
- VariableNotFoundException
- VariableNotFoundInCatalogException
- MultiSpannersNotAllowedException

## Explain each exception one by one

## How to use exceptions

# PyREmatch flags

## Introduction to flags

## Line-by-line

## Max mempool duplication

- Default: max_mempool_duplications=8

## Max deterministic states

- Default: max_deterministic_states=1000



