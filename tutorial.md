
# Motivation of using REQL

Suppose you want to do a linguistic analysis focused on Chile's relations with its neighboring countries. A possible starting point would be to analyze the Wikipedia page corresponding to the History of Chile. For example, below is the summary of the Wikipedia page from Chile (from English Wikipedia) provided in plain text format.

>Chile, officially the Republic of Chile, is a country in western South America. It is the southernmost country in the world and the closest to Antarctica, stretching along a narrow strip of land between the Andes Mountains and the Pacific Ocean. With an area of 756,102 square kilometers (291,933 sq mi) and a population of 17.5 million as of 2017, Chile shares borders with Peru to the north, Bolivia to the northeast, Argentina to the east, and the Drake Passage to the south. The country also controls several Pacific islands, including Juan Fernández, Isla Salas y Gómez, Desventuradas, and Easter Island, and claims about 1,250,000 square kilometers (480,000 sq mi) of Antarctica as the Chilean Antarctic Territory. The capital and largest city of Chile is Santiago, and the national language is Spanish.
>
>
>Spain conquered and colonized the region in the mid-16th century, replacing Inca rule, but failed to conquer the independent Mapuche people who inhabited what is now south-central Chile. Chile emerged as a relatively stable authoritarian republic in the 1830s after their 1818 declaration of independence from Spain. During the 19th century, Chile experienced significant economic and territorial growth, putting an end to Mapuche resistance in the 1880s and gaining its current northern territory in the War of the Pacific (1879–83) by defeating Peru and Bolivia. In the 20th century, up until the 1970s, Chile underwent a process of democratization and experienced rapid population growth and urbanization, while relying increasingly on exports from copper mining to support its economy. During the 1960s and 1970s, the country was marked by severe left-right political polarization and turmoil, which culminated in the 1973 Chilean coup d'état that overthrew Salvador Allende's democratically elected left-wing government. This was followed by a 16-year right-wing military dictatorship under Augusto Pinochet, which resulted in more than 3,000 deaths or disappearances. The regime ended in 1990, following a referendum in 1988, and was succeeded by a center-left coalition, which ruled until 2010.
>
>
>Chile has a high-income economy and is one of the most economically and socially stable nations in South America, leading Latin America in competitiveness, per capita income, globalization, peace, and economic freedom. Chile also performs well in the region in terms of sustainability of the state and democratic development, and boasts the second lowest homicide rate in the Americas, following only Canada. Chile is a founding member of the United Nations, the Community of Latin American and Caribbean States (CELAC), and the Pacific Alliance, and joined the OECD in 2010.

Suppose you want to extract all the sentences from this Wikipedia article that first mention Chile and then one of its neighboring countries (Argentina, Bolivia, or Peru). A sentence is understood as a string that does not have line breaks or periods. Doing this in Python without the help of a library can be a bit complicated. An attempt could be the following:

    count = 1
    for line in text.split('\n'):
        for sentence in line.split('.'):
            x = sentence.find("Chile ")
            if x != -1:
                for pais in ["Peru", "Argentina", "Bolivia"]:
                    y = sentence.find(pais, x)
                    if y != -1:
                        print("{}. {}".format(count, sentence))
                        count += 1
                        break

where, for each line of the document, the find method of a string in Python is used to search for the relevant words.

This task requires little effort. Now, imagine that as a data expert, you need to do this task multiple times a day, with different data sets (potentially with large volumes of data) and where the requirements for extraction are very different. While writing and testing this code may take you 5 minutes to 30 minutes on average, performing this task repeatedly may be an unnecessary cost to your job as a data expert. Finally, your Python program will likely be inefficient and may take several minutes to finish for large documents.

In fact, the same previous task can be done with the following REQL query using the REmatch library (try it [here](https://rematch.cl/?query=%28%5E%7C%5B%5Cn.%5D%29%21sentence%7B%5B%5E.%5Cn%5D*Chile%5B%5E.%5Cn%5D*%28Peru%7CArgentina%7CBolivia%29%5B%5E.%5Cn%5D*%5C.%7D&doc=Chile%2C+officially+the+Republic+of+Chile%2C+is+a+country+in+western+South+America.+It+is+the+southernmost+country+in+the+world+and+the+closest+to+Antarctica%2C+stretching+along+a+narrow+strip+of+land+between+the+Andes+Mountains+and+the+Pacific+Ocean.+With+an+area+of+756%2C102+square+kilometers+%28291%2C933+sq+mi%29+and+a+population+of+17.5+million+as+of+2017%2C+Chile+shares+borders+with+Peru+to+the+north%2C+Bolivia+to+the+northeast%2C+Argentina+to+the+east%2C+and+the+Drake+Passage+to+the+south.+The+country+also+controls+several+Pacific+islands%2C+including+Juan+Fern%C3%A1ndez%2C+Isla+Salas+y+G%C3%B3mez%2C+Desventuradas%2C+and+Easter+Island%2C+and+claims+about+1%2C250%2C000+square+kilometers+%28480%2C000+sq+mi%29+of+Antarctica+as+the+Chilean+Antarctic+Territory.+The+capital+and+largest+city+of+Chile+is+Santiago%2C+and+the+national+language+is+Spanish.%0ASpain+conquered+and+colonized+the+region+in+the+mid-16th+century%2C+replacing+Inca+rule%2C+but+failed+to+conquer+the+independent+Mapuche+people+who+inhabited+what+is+now+south-central+Chile.+Chile+emerged+as+a+relatively+stable+authoritarian+republic+in+the+1830s+after+their+1818+declaration+of+independence+from+Spain.+During+the+19th+century%2C+Chile+experienced+significant+economic+and+territorial+growth%2C+putting+an+end+to+Mapuche+resistance+in+the+1880s+and+gaining+its+current+northern+territory+in+the+War+of+the+Pacific+%281879%E2%80%9383%29+by+defeating+Peru+and+Bolivia.+In+the+20th+century%2C+up+until+the+1970s%2C+Chile+underwent+a+process+of+democratization+and+experienced+rapid+population+growth+and+urbanization%2C+while+relying+increasingly+on+exports+from+copper+mining+to+support+its+economy.+During+the+1960s+and+1970s%2C+the+country+was+marked+by+severe+left-right+political+polarization+and+turmoil%2C+which+culminated+in+the+1973+Chilean+coup+d%27%C3%A9tat+that+overthrew+Salvador+Allende%27s+democratically+elected+left-wing+government.+This+was+followed+by+a+16-year+right-wing+military+dictatorship+under+Augusto+Pinochet%2C+which+resulted+in+more+than+3%2C000+deaths+or+disappearances.+The+regime+ended+in+1990%2C+following+a+referendum+in+1988%2C+and+was+succeeded+by+a+center-left+coalition%2C+which+ruled+until+2010.%0AChile+has+a+high-income+economy+and+is+one+of+the+most+economically+and+socially+stable+nations+in+South+America%2C+leading+Latin+America+in+competitiveness%2C+per+capita+income%2C+globalization%2C+peace%2C+and+economic+freedom.+Chile+also+performs+well+in+the+region+in+terms+of+sustainability+of+the+state+and+democratic+development%2C+and+boasts+the+second+lowest+homicide+rate+in+the+Americas%2C+following+only+Canada.+Chile+is+a+founding+member+of+the+United+Nations%2C+the+Community+of+Latin+American+and+Caribbean+States+%28CELAC%29%2C+and+the+Pacific+Alliance%2C+and+joined+the+OECD+in+2010.&isMultiMatch=false)).

    (^|[\n.])!sentence{[^.\n]*Chile[^.\n]*(Peru|Argentina|Bolivia)[^.\n]*\.}

This pattern describes the extraction task that REmatch should do (we will come back to this pattern later). The language of this pattern is REQL, a RegEx-based query language for information extraction. RegEx (for Regular Expressions) is a standard language of characters and special operators that allow us to describe groups of sequences in strings, which one would like to identify, verify, and extract. These expressions will simplify the task of extracting information from documents, allowing us to define our task and letting a library like REmatch execute and optimize the task in the best possible way. 

Below, we will introduce REQL to verify simple RegEx patterns in strings and then use these patterns to extract information from documents with the REmatch library. We will start by introducing the most common RegEx operators and then show the main features of REQL for extracting information from documents. 

# Brief overview of REQL

As mentioned, REQL is a RegEx-based query language for extracting information from text. REQL includes the main operators used in the POSIX standard and Perl-compatible regular expressions (PCRE). REQL syntax includes any UTF-8 character, character sets including PCRE abbreviations (like \d for a digit), beginning and end of a document, disjunction `|`, and quantifiers like `?`, `*`, and `+`, among others. All these operators behave the same as in standard RegEx, and thus, REQL has backward compatibility for queries without capture variables. Then, a user can use REQL syntax as standard RegEx. 

To be more specific, all the operators of REQL are the following:

1. `a`: character (UTF-8)
2. `.`: any character
3. `\.`: escape character
4. `[S]`: character set
5. `[^S]`: negated set
6. `\w`: special character set 
7. `\n`: special symbols
8. `ee`: concatenation
9. `e|e`: disjunction (alternation)
10. `e?`: optional
11. `e*`: zero-or-more
12. `e+`: one-or-more
13. `e{n,m}`: at leat n and at most m
14. `(e)`: normal parentheses
15. `^`: beginning of document
16. `$`: end of document
17. `!var{e}`: capture variables

Operators 1. to 16. are standard RegEx operators, and in the absence of capture variables (operator 17.), they behave similarly to any standard RegEx library. The key difference in REQL is the inclusion of *capture variables*, which work similarly to RegEx's capture groups but with a novel semantics for finding all matches.  

This tutorial will cover all the operators displayed above through examples. We will start by covering the standard RegEx operators (1. to 14.) and then present capture variables. Note that we will explain the operators for the beginning and end of a document (operators 15. and 16.) later in the tutorial after we introduce capture variables.

If you're already familiar with RegEx operators 1. to 14., you might consider skipping ahead to the section on capture variables. However, we strongly recommend going through the entire tutorial. Even if you're an expert, this will give you a comprehensive understanding of how REQL and REmatch work, enhancing your overall learning experience. So, let's get started. 

# Standard RegEx operators in REQL

## Simple patterns 

- `a`: character (UTF-8)
- `ee`: concatenation

The simplest form of a RegEx is a word. A word like `gmail` defines the string 'gmail' and describes that only strings containing the word 'gmail' will satisfy the property. For a running example of this tutorial, consider the following document that includes a list of emails separated by new lines:

    cperez@gmail.com
    soto@uc.cl
    sdelcampo@gmail.com
    lpalacios@gmeil.com
    pvergara@ing.uc.cl
    ndelafuente@ing.puc.cl
    ldelgado@gmsil.com
    tnovoa@mail.uc.cl
    nnarea@myucmail.uc.cl
    rramirez@gmail.com
    juansoto@uc.cl

Then, for finding the word 'gmail' in the previous document, we only need to write the following REQL query:

    !output{gmail}

You can try this example [here](https://rematch.cl/?query=%21output%7Bgmail%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false). If you run this query on REmatch over the emails list, you will find the three positions where the word 'gmail' appears. You can try the same query by modifying gmail with your favorite word to search and see the result. 

**IMPORTANT**: For the rest of this section, forget about the clause `!output{...}` in the REQL examples. This operator is a capture variable, one of the main constructs of REQL for information extraction, and we will cover it in full detail in a while. This construct says: "When you find the word 'gmail,' capture it in the variable 'output'." Indeed, if you write 'gmail' without the clause `!output{...}`, this is a valid REQL query, but REmatch will only tell you `TRUE` or `FALSE`, depending on whether the substring gmail appears or not in the document, but without retrieving the positions of that substrings. For the following examples, we will maintain this clause  `!output{...}` in the queries to cover it later in the tutorial (after you are a master of RegEx operators in REQL). 

## Any character and escape characters

- `.`: any character
- `\.`: escape character

Many times we will know the pattern we want to define, but there are certain positions of the pattern that can be any character. For this, we will use the pattern `.` (a dot), which simply means we want to see one letter. For example, if we want to find the word 'gm_il' where the third letter can be any symbol, then we define that with the following REQL query (try it [here](https://rematch.cl/?query=%21output%7Bgm.il%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{gm.il}

where the dot represents any symbol. By running this query, we will have the same results as for the simple gmail pattern but with more results (two more, indeed). 

The above describes all the simple patterns to find a sequence of symbols within a string. But how can we define that we want to find a dot? Since the `.` is part of the REQL's syntax, we must use the escape symbol `\`. Thus, to find all emails of type 'gmail.com', we must write the pattern as `gmail\.com`. We must do the same to find symbols like `[`, `]`, or `^` that are part of the syntax of the REQL queries, like the symbols of other operators that we will see below.

## Character sets

- `[S]`: character set
- `[^S]`: negated set

In some cases, with the pattern we want to define that not just any symbol will go in that position, but rather a symbol of a special class. In our `gm.il` example, we would like to say that the third symbol is a vowel. For this, we use the `[ ]` operator that allows us to specify character classes, where within the square brackets we list all the symbols that can appear. For example, to define the vowel class, we use `[aeiou]`, and to say that we want to find 'gm_il' where the symbol _ can be a vowel, we use the pattern (try it [here](https://rematch.cl/?query=%21output%7Bgm%5Baeiou%5Dil%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{gm[aeiou]il}

The previous mailing list has now been reduced because we only want the ones with a vowel in the third symbol. If we want to add more symbols, we can place as many as we want inside the `[ ]`, such as all the lowercase letters of the alphabet (English): `[abcdefghijklmnopqrstuvwxyz]`. This doesn't look very elegant at first glance. RegEx and REQL allow you to define character ranges to simplify character classes. If we want to define all lowercase letters we can use `[a-z]`, which means "a to z", or if we want all uppercase and lowercase letters, we can use `[a-zA-Z]`, which is the same as `[a-z]` but adding the section of capital letters from A to Z. Finally, the character classes `[ ]` allow you to define a class of symbols that excludes all the symbols listed within the parentheses. For this, we use the `^` symbol at the beginning of the character class. Thus, if we want to say any symbol except vowels, we write `[^abcde]` (try it [here](https://rematch.cl/?query=%21output%7Bgm%5B%5Eaeiou%5Dil%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{gm[^aeiou]il}

## Disjunction and optional

- `e|e`: disjunction (alternation)
- `(e)`: normal parentheses
- `e?`: optional

Although simple patterns allow us to define a sequence of fixed length that we want to find in a string, they do not allow us to search for the appearance of two or more possibilities simultaneously. For example, we would like to check the occurrence of the word 'gmail' or the word 'uc' if either appears in the string. For this, we can use the disjunction operator `|` (also called *alternation* in RegEx), which allows us to say `gmail|uc` and reads like "we want to see the appearance of gmail or uc in the string". Namely, the following REQL query (try it [here](https://rematch.cl/?query=%21output%7Bgmail%7Cuc%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{gmail|uc}

We can combine disjunction with simple patterns or within simple patterns. For example, instead of using a character class to define a vowel, we can use disjunction and define the pattern `gm(a|e|i|o|u)il` where parentheses are part of regular expression syntax and allow to group disjunctions. In other words, the subexpression `(a|e|i|o|u)` is equivalent to `[aeiou]`, which defines the vowel class. In particular, we can use the operator `|` to list different possibilities in a pattern like `gmail|uc|puc`.

Another way to choose between alternatives in RegEx (and REQL) is to use the optional operator `?`. An example of the optional is when we use `ing\.(uc|puc)` to search for the word 'ing.uc' or 'ing.puc' in an email. Both words are very similar; the only difference is that `p` may or may not appear in the email. For this, we can use the optional operator `?` and write the REQL query (try it [here](https://rematch.cl/?query=%21output%7Bing%5C.p%3Fuc%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{ing\.p?uc}

where the `\.` is to declare a dot in the query (which must be escaped, as we explained before). Note that we can use the optional `?` over a simple pattern, or nest this operator on top of other operators. For example, if we also want the prefix 'ing.' may or may not appear, we can define this as `(ing\.)?p?uc` where the parentheses `( )` help us group the subpattern where the optional operator will be applied.

## Repetitions and quantifiers

- `e*`: zero-or-more
- `e+`: one-or-more
- `e{n,m}`: at leat n and at most m

One of the most important classes of operators in REQL is repetition. So far, REQL allows us to identify patterns within a string but with a bounded number of letters. For example, an expression like `gmail|p?uc` will enable us to identify the occurrence of 'gmail', 'puc' or 'uc' in the string, but this is a limited number of possibilities.

We use the `+` and `*` operators to define patterns with *one-or-more* or *zero-or-more* characters. For example, if we want to identify emails that contain the domains '@ing.uc.cl' or '@mail.uc.cl' where the subdomain that is between '@' and the next dot could be any string, then we use the REQL query (try it [here](https://rematch.cl/?query=%21output%7B%40%5Ba-zA-Z%5D%2B%5C.p%3Fuc%5C.cl%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{@[a-zA-Z]+\.p?uc\.cl} 

In this last query, the `[a-zA-Z]+` means that we want to see a letter (upper or lower case, that is, `[a-zA-Z]`) one-or-more times. On the other hand, if we want to allow emails like '@.uc.cl', then we can use the `*` operator and write the expression `@[a-zA-Z]*\.p?uc\.cl` where now the `[a-zA-Z]*` means that we want to see a letter zero-or-more times.

The RegEx subpattern `[a-zA-Z]+` allows us to find one-or-more letters in an email, but there is no limit to the length of the word. In fact, the pattern `@[a-zA-Z]+\.p?uc\.cl` will match the string '@a.uc.cl' or the string '@aaaaaaaaaaaaaaaaaaaaaaa.uc.cl' (20 letters or more) or with any length between @ and the first period. We often do not want an arbitrary number of repetitions of a pattern but rather a number of repetitions within a range. For this, one can use the repetition operator with range `{n,m}`, which means that the pattern will repeat n-to-m times where n and m are numbers. Going back to our example, if we want the subdomain to be between 2 to 5 characters, then we use (try it [here](https://rematch.cl/?query=%21output%7B%40%5Ba-zA-Z%5D%7B2%2C5%7D%5C.p%3Fuc%5C.cl%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{@[a-zA-Z]{2,5}\.p?uc\.cl} 

## Special character sets and special symbols

- `\w`: special character set 
- `\n`: special symbols

In RegEx, allowing some operators to refer to a class of special symbols is useful. For example, RegEx allows the use of `\w` to refer to the class of alphanumeric and underscore characters; namely, `\w` is equivalent to `[A-Za-z0-9_]`. For our running example, we can use `\w` to capture the right-hand side of emails as follows (try it [here](https://rematch.cl/?query=%21output%7B%40%5Cw%2B%5C.p%3Fuc%5C.cl%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{@\w+\.p?uc\.cl}

For backward compatibility, REQL allows the following special character sets: 

- `\d`: a digit; equivalent to `[0-9]`
- `\D`: not a digit; equivalent to `[^0-9]`
- `\s`: a whitespace type; equivalent to `[\t\n\r\f\v]`
- `\S`: not a whitespace type, equivalent to `[^\t\n\r\f\v]`
- `\w`: a word character, equivalent to `[A-Za-z0-9_]`
- `\W`: not a word character, equivalent to `[^A-Za-z0-9_]`

Finally, REQL includes common special symbols to refer to a newline or a tab, which are common in text processing (see how to use them below for capturing outputs). The special characters supported in REQL are the following:

- `\t`: a tab
- `\n`: a newline
- `\r`: a carriage return (return to the beginning of the current line without advancing downward)
- `\v`: a vertical whitespace
- `\f`: a form feed (advance downward to the next "page")

We end this review of the main RegEx operators in REQL. We are ready to move on to the main novel feature of REQL: capture variables. 

# Capturing variables

## Variables, matches, and spans

- `!var{e}`: capture variables

To understand how to use REQL to extract parts of our strings, let's look at an example. First, recall our running example where we want to extract data from a list of emails like the following:

    cperez@gmail.com
    soto@uc.cl
    sdelcampo@gmail.com
    lpalacios@gmeil.com
    pvergara@ing.uc.cl
    ndelafuente@ing.puc.cl
    ldelgado@gmsil.com
    tnovoa@mail.uc.cl
    nnarea@myucmail.uc.cl
    rramirez@gmail.com
    juansoto@uc.cl

Consider our last example for checking the right side of a mail, only now we'll add variables to specify the parts we want to extract (try it [here](https://rematch.cl/?query=%21output%7B%40%21x%7B%5Cw%2B%7D%5C.p%3Fuc%5C.cl%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !output{@!x{\w+}\.p?uc\.cl}

Our new query has two variables: `output` and `x`. The first variable `!output{...}` extracts the whole text that matches the pattern, as we did with the previous examples above. The second variable `!x{...}` extracts a subdomain of the email, namely, what is matched by the subpattern `\w+`. Indeed, the identifiers 'output' and 'x' are the names of the variables and will allow us to refer by a name to each capture. These names are arbitrary, and one could use more suggestive identifiers like below (try it [here](https://rematch.cl/?query=%21email%7B%40%21subdomain%7B%5Cw%2B%7D%5C.p%3Fuc%5C.cl%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)): 
 
    !email{@!subdomain{\w+}\.p?uc\.cl}

where `email` and `subdomain` are the new identifiers for `output` and `x`. Note that this marks the first big difference with standard RegEx. In RegEx, one uses a capturing group to extract a substring that is denoted by normal parentheses `(...)` or, also, `(?<name>...)` to assign a name to the capturing group. Since extracting information is the main goal of REmatch, in REQL we have to always assign a name to what is captured, and for that, we use the notation `!name{...}`. Moreover, this allows the free use of normal parenthesis `(...)` as a syntactical object to group operators.

When we run a REQL query over a document, REmatch returns all the **matches** of the query into the document. A match is an assignment of the variables to intervals of the document, also called **spans**. For instance, if we run the above query over our document in the REmatch web interface (try it [here](https://rematch.cl/?query=%21email%7B%40%21subdomain%7B%5Cw%2B%7D%5C.p%3Fuc%5C.cl%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)), we can see the four matches that REmatch retrieves on the right-hand side. Furthermore, each variable maps to a span in the document, namely, a pair of positions. For the first match (Match 0), we can see that `email` is mapped to the span (76-86) and `subdomain` to the span (77-80). Spans allow us to extract the document's content and also help us find the context where the information was found. 

## Use and restrictions of variables

In REQL, one can use up to 32 variables in a single pattern. For instance, if we also want to capture the other subdomains in the same pattern, we can use more variables to capture them (try it [here](https://rematch.cl/?query=%21email%7B%40%21subdomain%7B%5Cw%2B%7D%5C.%21subdomain2%7Bp%3Fuc%7D%5C.%21subdomain3%7Bcl%7D%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !email{@!subdomain{\w+}\.!subdomain2{p?uc}\.!subdomain3{cl}}

Although we have always placed a variable surrounding the whole pattern (like `!output{...}`), this is unnecessary if we don't want to capture the span where all the pattern holds. For instance, if we want only to capture the subdomain, and not the whole right-hand side of an e-mail, we can write the query (try it [here](https://rematch.cl/?query=%40%21subdomain%7B%5Cw%2B%7D%5C.p%3Fuc%5C.cl&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    @!subdomain{\w+}\.p?uc\.cl

This feature is helpful for information extraction since it allows one to check the existence of a pattern before (like `@`) or after (like `\.p?uc\.cl`) without capturing it. This feature is another big difference with standard RegEx, where the patterns before or after a capturing group can affect the extraction process without retrieving all the outputs. Indeed, for checking patterns before or after a capturing group without consuming, RegEx provides *lookaround* operators, which are not necessary for REQL. See more discussion about this feature in the next subsection. 

In general, one can put a variable in any place of the pattern for capturing a span. However, there are four restrictions for correctly interpreting the meaning of a variable in REQL. The restrictions are the following.

1. *One cannot concatenate two subqueries `e1` and `e2` (namely, `e1e2`) when`e1` and `e2` have some variable name in common.*
    - `!x{a}!y{b}`is allowed.
    - `!x{a}!x{b}` is **NOT allowed**. 

2. *One cannot use disjunction `e1|e2` when subqueries `e1` and `e2` have a different set of variable names.*
    - `!x{a}|!x{b}` is allowed. 
    - `!x{a}|!y{b}` is **NOT allowed**.

3. *One cannot use repetitions `*` (zero-or-more) or `+` (one-or-more), quantifiers `{n,m}`, or optionals `?` over a subquery `e` that contains variables.*
    - `!x{a+}`, `!x{a}b{2,3}`, or `!x{a}b?` is allowed.
    - `!x{a}+`, `!x{a}{2,3}b`, or `!x{a}?b` is **NOT allowed**.

4. *One cannot put a variable over a subquery `e` that can match with an 'empty string'.*
    - `!x{a+}` is allowed.
    - `!x{a*}` or `!x{a?}` is **NOT allowed**.

In other words, (1) says that one cannot repeat the same variable over a sequence, (2) that the inputs for a disjunction need the same variable names, (3) that one cannot capture inside a repetition, a quantifier, or an optional, and (4) that variables only capture non-empty strings. If you test the examples that are NOT allowed in the REmatch web interface, you will see that the interface throws an error. These are natural restrictions that do not impose further limitations on information extraction. In case you still feel that these rules restrict the extraction process, we will later present in this tutorial the novel feature *multimatch* of REmatch where restrictions (1), (2), and (3) are relaxed for capturing a list of spans (another feature that standard RegEx does not support).

## All matches and without duplicates

A distinguished feature you have probably observed is that when REmatch runs a REQL query, it returns **ALL MATCHES** of the query. To test this, one can try the following REQL query in the REmatch web interface over our example document (try it [here](https://rematch.cl/?query=%21twoletters%7B%5Cw%5Cw%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !twoletters{\w\w}

This pattern searches for all pairs of consecutive letters. You can see that REmatch retrieves all appearances of two alphanumeric letters in the document. Instead, if we run the analogous query by replacing variables with capture group in a RegEx engine, like:

    (\w\w)          (RegEx)

you can verify that not all spans are retrieved. This shortcoming of RegEx engines can be solved by using *lookaround* operators, specifically by using the following RegEx query:

    (?=(\w\w))      (RegEx)

which says "lookahead for the pattern (\w\w) without consuming the letters". The lookaround operators work for some cases, like the previous scenario, but cannot generally work. For instance, if we want to find *all alphanumeric substrings* in our document, we can write the following REQL query (try it [here](https://rematch.cl/?query=%21substring%7B%5Cw%2B%7D&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    !substring{\w+}

that searches for all appearances of one-or-more alphanumeric symbols. One can test this query in the REmatch web interface and see that it retrieves all substrings. Note that this query cannot be defined using standard RegEx, no matter the operators one uses. Indeed, one can go through the examples in REmatch ([here](https://rematch.cl/examples)) and check that there are several practical cases where **ALL MATCHES** is helpful for information extraction (like DNA, literature, etc), but one cannot perform the same task with RegEx. 

It is worth noticing that REmatch retrieves all matches and **WITHOUT DUPLICATES**, no matter how one writes the REQL query. For instance, one can use the following REQL query:

    !twoletters{\w\w}|!twoletters{\w\w}

where the same pattern is copied twice on the left- and right-hand side of a disjunction. A user can naively guess that each subpattern will provide a new result, and then REmatch will find each output twice. Fortunately, this is not the case for REmatch evaluation, and each output will be retrieved once, no matter how the query is written.

Retrieving **ALL MATCHES** and **WITHOUT DUPLICATES** poses no problem to REmatch regarding efficiency. Indeed, REmatch runs as fast as any standard RegEx engine and always looks for all matches. REmatch is based on the [framework of document spanners](https://dl.acm.org/doi/10.1145/2699442) and the theory of [constant-delay algorithms](https://dl.acm.org/doi/abs/10.1145/1276920.1276923) that have been developed in the last years. In a nutshell, the REmatch algorithm reads a document just once and takes a fixed amount of time (say `0.001ms`) to give you the next output. Of course, if the engine finds 1 million results, it will take you 1 second to get all of them, but no more than that. In fact, suppose the file has `1MB` of data, and we take 1ms to read the document. In that case, the algorithm will take `0.001ms` to give you the next result, regardless of whether it found ten or 10^10 outputs.
 

## Specification of REQL queries under all matches

As someone said: "With great power comes great responsibility". Now that REQL finds all matches, one has to be more careful when specifying some queries. For instance, if we want to capture all names of our email list (that is, the strings before the `@`), one is tempting to write:

    !name{\w+}@

However, this query captures all alphanumeric substrings of one-or-more characters ending with an `@`. It will then find all names and all their suffixes. 

So, how can we capture all names? Now that REmatch always finds all matches, we must be more specific about what we want and declare where the pattern must start and end. For example, for the previous query, we can do it as follows:

    \n!name{\w+}@

This pattern is the same as before, but now we specify that it must start after a new line `\n`. One can check [here](https://rematch.cl/?query=%5Cn%21name%7B%5Cw%2B%7D%40&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false) that this will give (almost) all names used in our list of emails. Although this requires a bit more work by being more specific, one usually gains clarity in the query on what is searching for extraction. 

## The beginning and end of a document

- `^`: beginning of document
- `$`: end of document

The user can notice that we almost get all the results in the last example because the first name of the first email is not part of the results. The reason is that the first result doesn't start with a new line since there is no character before it. To solve this issue, REQL includes the operators `^` and `$` for declaring the beginning and the end of the document, respectively. Then, to get all the names of our example, we need to write the following REQL query (try it [here](https://rematch.cl/?query=%28%5Cn%7C%5E%29%21name%7B%5Cw%2B%7D%40&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    (\n|^)!name{\w+}@

Note that the operators `^` and `$` are not characters since they refer to the beginning and the end of the document, respectively. For this reason, REQL does not allow the use of `^` or `$` inside a variable. You can try to use `^` and `$` inside a variable in the REmatch web interface, but you will get an error from the interface. 

Now that we have introduced all the REQL operators, we end by combining all that we learned and showing how to extract all pairs of name/domain from the emails with the following REQL query (try it [here](https://rematch.cl/?query=%28%5Cn%7C%5E%29%21name%7B%5Cw%2B%7D%40%21domain%7B%28%5Cw%2B%5C.%29%2B%5Cw%2B%7D%28%5Cn%7C%24%29&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=false)):

    (\n|^)!name{\w+}@!domain{(\w+\.)+\w+}(\n|$)

# Some practical REQL use cases

Now that we have introduced REQL, we present some real use cases where REmatch can make a difference. For more examples, see REmatch's example section [here](https://rematch.cl/examples). 

## DNA sequences  

Motif detection is a key task in DNA analysis. Motifs are represandented as a sequence pattern usually assumed to be related to biological functions. Indeed, RegEx has been extensively used to find motifs in DNA sequences, where the location of such matches is important to understand their impact on an organism. 

For this scenario, we show the advantage of using REmatch to find all motif matches. For instance, the following REQL query searches for the N-myristoylation site motif:

    !motif{G[^EDRKHPFYW].{2}[STAGCN][^P]}

We can evaluate this query with REmatch over the list of proteomes of the zebrafish organism [here](https://rematch.cl/?query=%21motif%7BG%5B%5EEDRKHPFYW%5D.%7B2%7D%5BSTAGCN%5D%5B%5EP%5D%7D&doc=%3EXP_017210497.1+glutamate+%5BNMDA%5D+receptor+subunit+epsilon-2+isoform+X1+%5BDanio+rerio%5D%0AMGVGLAMFKGLYLHSSAMLVSLHLSSSPFSDCRVLSFVSLVSSFKLPLYISLLLLSLFFFPTCESRRGGGIGTPTGGMNSQSIISPPHYPPPGVSPVGPPMSPKFAQGLSIAVILVGNSSEVSLSEGLEKEDFLHVPLPPKVELVTMNETDPKSIINRICALMSRNWLQGVVFGDDTDQEAIAQILDFISAQTHIPILGIRGGSSMIMAAKDDHSMFFQFGPSIEQQASVMLNIMEEYDWYIFSIVTTYYPGHQDFVNRIRSTVDNSFVGWELEEVLLLDMSVDDGDSKIQNQMKKLQSPVILLYCTKEEATTIFEVAHSVGLTGYGYTWIVPSLVAGDTDNVPNVFPTGLISVSYDEWDYGLEARVRDAVAIIAMATSTMMLDRGPHTLLKSGCHGAPDKKGSKSGNPNEVLRYLMNVTFEGRNLSFSEDGFQMHPKLVIILLNKERQYERVGKWENGSLAMKYHVWPRFELYSDAEEREDDHLSIVTLEEAPFVIVEDVDPLSGTCMRNTVPCRKQLKLQNLTGDSGIYIKRCCKGFCIDILKKIAKSVKFTYDLYLVTNGKHGKKINGTWNGMVGEVVLKNAHMAVGSLTINEERSEVIDFSVPFIETGISVMVSRSNGTVSPSAFLEPFSADVWVMMFVMLLIVSAVAVFVFEYFSPVGYNRCLADGREPGGPSFTIGKAIWLLWGLVFNNSVPVQNPKGTTSKIMVSVWAFFAVIFLASYTANLAAFMIQEEYVDQVTGLSDKKFQHPNDFSPPFRFGTVPNGSTERNIRNNYKEMHSYMTSFHQKNVNEALHSLKSGKLDAFIYDAAVLNYMAGRDEGCKLVTIGSGYIFATTGYGIAIQKDSGWKRAVDLAILQLFGDGEMEELEALWLTGICHNEKNEVMSSQLDVDNMAGVFYMLGAAMALSLITFIAEHLFYWQLRFCFMGVCSGKPGMTFSISRGIYSCIHGVQIEENKSALNSPSATMKMNMNNTHSNILRLLRTAKNMTSVPGVNGSPHSALDYSHRESAVYDISEHRRSLAGHSDCKPPPYLPEDNMFSDYVSEVERTFGNLHLKDSNLYQDHYLHHHGGSELALGMSGPLPNRPRSLGSASSLEGGYDCDSLGGGVAPIFTTQPRQSLTHRNREKFDLIAGHPTQSSFKSGLPDLYGKFSFKGGASSSGFIAGHDRYCGGGGVGSGGDDGNIRSDVSDISTHTVTYGNLEGHSKRRKQYRDSLKKRPASAKSRREQDEIELGFRRRPHHTIHHHHHHHPATQAHRSATPPVERKSQRGGNCTSYLFRDKENLRDFYVDQFRAKEGASPWDLDLSDAPGMGGGVGLGGGSCGGVVSSGGAGGACTSLVPMEDFLKGKSKKTECKGGMGGGSPGQQGHACWEKGIGGVGGLAGGDWECRSCHSGGVGSGGSKPVCMHGGGGAGGYPAAGGVGGSSGGSGQISSRPSSATCKRCDSCKKPGNLYDISEDNLLLDQIAGKHPLESGKGGGGTGAQTQVQRRKFGPGGKVLRRQHSYDTFVELQKEGAGRMGGFGGGGGASMLPPPRSVSLKDKDRYMEGASPYAQMFEQYAGGERETSYFGDRGKGGGSSFSLFRGGEGGLHRRSVGERDMRDRDRGMMGGGVGGTRGVGTYSLSKSLYPDKVNQNPFIPTFGDDQCLLHGAKSYYIKKQQAQPQQQQTPQQQQQQLLNNSRADFRGSMGVTSYLPASATSGVLSNVAPRFPKELCLGGPLGNHHGGGPSNNKLLSARDGLGMGQGQRPFNGSSNGHVYEKLSSIESDV&isMultiMatch=false).  It is interesting to verify that REmatch found overlapped matches, while other traditional RegEx engines or wrappers used for DNA analysis do not find these overlapped hits (without using lookaround).

## Linguistic analysis 

Corpus extraction and context analysis are relevant tasks for linguistic analysis, and together with computer science, they have reached big achievements in natural language processing. RegEx engines are a helpful tool for efficient information extraction, giving the possibility, for example, to obtain the context of certain words, morphemes, or any other linguistic object that one can define with regular expressions. 

In this context, suppose that a user wants to process English text into k-grams (k consecutive words in a text) that satisfy some particular pattern. Specifically, suppose this user wants to extract all 2-grams where each word begins with the letter `a`. The user also wants to extract the sentence where the match happens, which could be useful for understanding the context where these 2-grams are used. We can express this task by the following REQL query:

    (^|(\.))!sent{[^.]* !w1{[Aa]\w+} !w2{[Aa]\w+}( [^.]*)?\.}

where `w1` and `w2` variables store the positions of the first and second word, respectively, and `sent` stores the position of the sentence.
The evaluation of this query over a fragment of the book "What is a man?" by Mark Twain can be checked [here](https://rematch.cl/?query=%28%5E%7C%28%5C.%29%29%21sent%7B%5B%5E.%5D*+%21w1%7B%5BAa%5D%5Cw%2B%7D+%21w2%7B%5BAa%5D%5Cw%2B%7D%28+%5B%5E.%5D*%29%3F%5C.%7D&doc=I+know+them+well.+They+are+extremes%2C+abnormals%3B+their+temperaments+are+as+opposite+as+the+poles.+Their+life-histories+are+about+alike+but+look+at+the+results.&isMultiMatch=false). Notice that finding all matches of `w1` and `w2` plus the context where they occur (i.e., the sentence) cannot be performed by traditional RegEx engines (here, lookaround will not help).

# Multimatch capturing

## Motivation of using multimatch capturing

REQL and RegEx are helpful languages for extracting information from unstructured data, like text, but sometimes they are not powerful enough for some tasks. Indeed, several times after extracting data with REQL or RegEx, we need to postprocess the output to find the real information we need. For example, this happens when we need to extract several fields but do not know how many in advance. Unfortunately, REQL (and also RegEx) only provides a fixed number of variables per query, and then, knowing the number of fields in advance is necessary to have several variables for extracting each field. 

To be more concrete, let's come back to our running example with the list of emails:

    cperez@gmail.com
    soto@uc.cl
    sdelcampo@gmail.com
    lpalacios@gmeil.com
    pvergara@ing.uc.cl
    ndelafuente@ing.puc.cl
    ldelgado@gmsil.com
    tnovoa@mail.uc.cl
    nnarea@myucmail.uc.cl
    rramirez@gmail.com
    juansoto@uc.cl

Suppose we now want to extract all subdomains inside a domain for each email. For instance, from `cperez@gmail.com` we want to get `gmail` and `com`, and from `pvergara@ing.uc.cl` we want to get `ing`, `uc`, and `cl`. The problem is that we need to know how many subdomains each email has. One possibility could be to extract the whole domain with the following REQL query:

    @!domain{(\w+\.)+\w+}(\n|$)

and postprocess each output (for example, with Python), splitting the subdomains by using the dot. Until now, this was the only solution that RegEx users had, which involved a third-party language like Python to concrete the task. Fortunately, we introduced the idea of **multimatch** in REQL, which allows us to extract a list of spans in each variable and provide a solution to these and more sophisticated use cases that usually appear in practice. 

## Multimatch = list of spans

Roughly speaking, the idea of multimatch is that each variable stores a *list of spans*, instead of a single span (like it was traditionally in RegEx). For the subdomain use case above, a multimatch can have a variable `subdomains` that stores the list of spans for all the subdomains appearing in an e-mail, which could be two, three, or more. The list of spans is not bounded, and then, depending on the input, a user can capture more or fewer spans to iterate over them later. 

With multimatch, we liberate you from the restrictions 1. to 3. over variables, as explained in the section "*Use and restrictions of variables*". You can now freely repeat variables, opening up new possibilities in your programming. Thus, we now allow these queries for multimatch capturing:

- `!x{e}!x{e}`: repeat variables in sequences
- `!x{e}+`: use repetitions *one-or-more* over variables
- `!x{e}*`: use repetitions *zero-or-more* over variables 
- `!x{e}{n,m}`: use quantifiers over variables
- `!x{e}|!y{e}`: use different set of variables in a disjunction 
- `!x{e}?`: use optional over variables

Recall that we banned these queries for "singlematch" REQL, and now they are valid for multimatch. Intuitively, the query `!x{a}!x{b}` will have a multimatch output where variable `x` will contain two spans (one for the letter `a` and one for letter `b`), and `!x{a}+` the multimatch output where `x` will contain one-or-more spans (one for each letter `a` that appears in a sequence). 

To truly grasp the power of multimatch capturing, let's move into some examples. These will demonstrate the consequences of leveraging each restriction of singlematch REQL, showing you the potential of multimatch in your programming tasks. 

## Repeating variables in sequences

- `!x{e}!x{e}`: repeat variables in sequences

We start with the most direct way of capturing multimatches by repeating the same variable in a query. To see the power of this feature, consider that you want to extract the subdomains of emails with only three subdomains, like `@ing.puc.cl`, but you want to use a single variable. With multimatch capturing, we can do it as follows (try it [here](https://rematch.cl/?query=%40%21subdomains%7B%5Cw%2B%7D%5C.%21subdomains%7B%5Cw%2B%7D%5C.%21subdomains%7B%5Cw%2B%7D%28%5Cn%7C%24%29&doc=cperez%40gmail.com%0Asoto%40uc.cl%0Asdelcampo%40gmail.com%0Alpalacios%40gmeil.com%0Apvergara%40ing.uc.cl%0Andelafuente%40ing.puc.cl%0Aldelgado%40gmsil.com%0Atnovoa%40mail.uc.cl%0Annarea%40myucmail.uc.cl%0Arramirez%40gmail.com%0Ajuansoto%40uc.cl&isMultiMatch=true)):

    @!subdomains{\w+}\.!subdomains{\w+}\.!subdomains{\w+}(\n|$)

In this query, you'll notice that the variable `subdomains` is repeated three times, once for each substring in an email domain. When executed in REmatch's web interface, you'll see one output for each email with three subdomains, and the variable `subdomains` will contain a list of three spans, just as you'd expect. 

It's important to remember that this functionality is not available in singlematch REQL or any standard RegEx library. Note that to allow multimatch capturing in REmatch, one must press the **Multi** button at the right of the query box. Although multimatch is more powerful than singlematch capturing, this new power for information extraction is non-standard (no library implements multimatches), and users could feel confused in a first approach (think that already "capturing all matches" with REQL can be confusing). For this reason, users must explicitly say if they want to use multimatch capturing in REmatch's web interface and also in REmatch's libraries.

## Using repetitions or quantifiers over variables

- `!x{e}+`: use repetitions *one-or-more* over variables
- `!x{e}*`: use repetitions *zero-or-more* over variables 
- `!x{e}{n,m}`: use quantifiers over variables

Repeating a variable in a sequence shows the use of multimatch capturing, but we still need to solve our original problem of several subdomains. Indeed, we are still force to capture a bounded number of spans for each multimatch. We can use repetitions and quantifiers over variables to go beyond a fixed number of spans. Let's return to our motivating examples of subdomains to exemplify this feature. With the following query, we can extract all subdomains for each email in the list (try it [here]):

    @(!subdomains{\w+}\.)+!subdomains{\w+}(\n|$)

Note that in this query, we not only use the repetition of the variable `subdomains` but also apply the repetition one-or-more over the first appearance of `subdomains`. This approach allows us to capture a list of one or more spans with the first 'subdomains ', and the last `subdomains` will capture the last span (after the last dot). When we run this query over the emails list, we observe that there is one output for each email where the variable contains the corresponding list of subdomains. This means that regardless of the number of subdomains an email has, the `subdomains` variable will capture all of them, effectively addressing our initial motivation for multimatch capturing. 

As you can expect, users can also use repetition zero-or-more or quantifiers for multmatch capturing. Similar than the example above, these operators increase the power of multimatch capturing for finding an unbounded number of spans. We invite the reader to try these operators by modifying the previous example and see their output. 

## Using disjunctions or optionals over variables

- `!x{e}|!y{e}`: use different set of variables in disjunctions 
- `!x{e}?`: use optional over variables

We end by explaining how to use disjunction or optional for multimatch capturing. These two operators help capture empty lists of spans when we have optional data that is not present. Of course, the best operator for illustrating this feature is optional `?`. Recall that our emails in the list may have two or three subdomains. Then a user may want to extract the last two subdomains in the variable `subdomains`, which always appear, and the first subdomain in a fresh variable called `extrasubdomain.` Note that this third subdomain may or may not exist, and the optional `?` is useful for this task. Let's see this with the following query (try it [here]):

    @(!extrasubdomain{\w+}\.)?!subdomains{\w+}\.!subdomains{\w+}(\n|$)

If we run this query over the data, we can check that when an email has two subdomains, the variable `extrasubdomain` is empty; that is, it has an empty list of spans. Instead, it has a span when the email has three subdomains. This case is an example of optional information that we can capture with a multimatch when it exists. One can think of several use cases where optional data appears, and then variables plus `?` help to extract this data when it is available. 

Finally, disjunction provides a more general form of adding alternatives for multimatch capturing. Similar to RegEx, disjunction `|` allows for choosing between several alternatives, and then one can select which variables save the spans. To illustrate this, suppose now that the user wants to extract the subdomains, but in case an email has three subdomains, then the user wants to store the first and second subdomain in special variables, as follows (try it [here]):
    
    @(!subdomain1{\w+}\.!subdomain2{\w+}|!subdomain{\w+})\.!subdomain{\w+}(\n|$)

One can see that the subquery `(!subdomain1{\w+}\.!subdomain2{\w+}|!subdomain{\w+})` does not respect the restrictions from singlematch REQL: the left-hand side of `|` uses variables `subdomain1` and `subdomain2`, and the right-hand side use just variable `subdomain`. The advantage here is that if the email has three subdomains, it will use the left-hand side, and if it has two, it will use the right-hand side. Note that variables will capture different spans depending on the number of subdomains. 

## More examples for multimatch capturing

To see other uses of multimatch capturing, we refer to our section of examples [here](https://rematch.cl/examples), where one can find practical use cases of multimatch capturing marked with the tag `MultiMatch`.
