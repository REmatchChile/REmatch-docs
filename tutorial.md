
# Motivation of using REmatch

Suppose you want to do a linguistic analysis focused on Chile's relations with its neighboring countries. A possible starting point would be to analyze the Wikipedia page corresponding to the History of Chile. For example, below is the summary of the Wikipedia page from Chile (from English Wikipedia) provided in plain text format.

>Chile, officially the Republic of Chile, is a country in western South America. It is the southernmost country in the world and the closest to Antarctica, stretching along a narrow strip of land between the Andes Mountains and the Pacific Ocean. With an area of 756,102 square kilometers (291,933 sq mi) and a population of 17.5 million as of 2017, Chile shares borders with Peru to the north, Bolivia to the northeast, Argentina to the east, and the Drake Passage to the south. The country also controls several Pacific islands, including Juan Fernández, Isla Salas y Gómez, Desventuradas, and Easter Island, and claims about 1,250,000 square kilometers (480,000 sq mi) of Antarctica as the Chilean Antarctic Territory. The capital and largest city of Chile is Santiago, and the national language is Spanish.
>
>Spain conquered and colonized the region in the mid-16th century, replacing Inca rule, but failed to conquer the independent Mapuche people who inhabited what is now south-central Chile. Chile emerged as a relatively stable authoritarian republic in the 1830s after their 1818 declaration of independence from Spain. During the 19th century, Chile experienced significant economic and territorial growth, putting an end to Mapuche resistance in the 1880s and gaining its current northern territory in the War of the Pacific (1879–83) by defeating Peru and Bolivia. In the 20th century, up until the 1970s, Chile underwent a process of democratization and experienced rapid population growth and urbanization, while relying increasingly on exports from copper mining to support its economy. During the 1960s and 1970s, the country was marked by severe left-right political polarization and turmoil, which culminated in the 1973 Chilean coup d'état that overthrew Salvador Allende's democratically elected left-wing government. This was followed by a 16-year right-wing military dictatorship under Augusto Pinochet, which resulted in more than 3,000 deaths or disappearances. The regime ended in 1990, following a referendum in 1988, and was succeeded by a center-left coalition, which ruled until 2010.
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

In fact, the same previous task can be done with the following REQL query using the REmatch library (try it [here](https://rematch.cl/?query=%28%5E%7C%5B%5Cn.%5D%29%21sentence%7B%5B%5E.%5Cn%5D*Chile%5B%5E.%5Cn%5D*%28Peru%7CArgentina%7CBolivia%29%5B%5E.%5Cn%5D*%5C.%7D&doc=Chile%2C+officially+the+Republic+of+Chile%2C+is+a+country+in+western+South+America.+It+is+the+southernmost+country+in+the+world+and+the+closest+to+Antarctica%2C+stretching+along+a+narrow+strip+of+land+between+the+Andes+Mountains+and+the+Pacific+Ocean.+With+an+area+of+756%2C102+square+kilometers+%28291%2C933+sq+mi%29+and+a+population+of+17.5+million+as+of+2017%2C+Chile+shares+borders+with+Peru+to+the+north%2C+Bolivia+to+the+northeast%2C+Argentina+to+the+east%2C+and+the+Drake+Passage+to+the+south.+The+country+also+controls+several+Pacific+islands%2C+including+Juan+Fern%C3%A1ndez%2C+Isla+Salas+y+G%C3%B3mez%2C+Desventuradas%2C+and+Easter+Island%2C+and+claims+about+1%2C250%2C000+square+kilometers+%28480%2C000+sq+mi%29+of+Antarctica+as+the+Chilean+Antarctic+Territory.+The+capital+and+largest+city+of+Chile+is+Santiago%2C+and+the+national+language+is+Spanish.%0ASpain+conquered+and+colonized+the+region+in+the+mid-16th+century%2C+replacing+Inca+rule%2C+but+failed+to+conquer+the+independent+Mapuche+people+who+inhabited+what+is+now+south-central+Chile.+Chile+emerged+as+a+relatively+stable+authoritarian+republic+in+the+1830s+after+their+1818+declaration+of+independence+from+Spain.+During+the+19th+century%2C+Chile+experienced+significant+economic+and+territorial+growth%2C+putting+an+end+to+Mapuche+resistance+in+the+1880s+and+gaining+its+current+northern+territory+in+the+War+of+the+Pacific+%281879%E2%80%9383%29+by+defeating+Peru+and+Bolivia.+In+the+20th+century%2C+up+until+the+1970s%2C+Chile+underwent+a+process+of+democratization+and+experienced+rapid+population+growth+and+urbanization%2C+while+relying+increasingly+on+exports+from+copper+mining+to+support+its+economy.+During+the+1960s+and+1970s%2C+the+country+was+marked+by+severe+left-right+political+polarization+and+turmoil%2C+which+culminated+in+the+1973+Chilean+coup+d%27%C3%A9tat+that+overthrew+Salvador+Allende%27s+democratically+elected+left-wing+government.+This+was+followed+by+a+16-year+right-wing+military+dictatorship+under+Augusto+Pinochet%2C+which+resulted+in+more+than+3%2C000+deaths+or+disappearances.+The+regime+ended+in+1990%2C+following+a+referendum+in+1988%2C+and+was+succeeded+by+a+center-left+coalition%2C+which+ruled+until+2010.%0AChile+has+a+high-income+economy+and+is+one+of+the+most+economically+and+socially+stable+nations+in+South+America%2C+leading+Latin+America+in+competitiveness%2C+per+capita+income%2C+globalization%2C+peace%2C+and+economic+freedom.+Chile+also+performs+well+in+the+region+in+terms+of+sustainability+of+the+state+and+democratic+development%2C+and+boasts+the+second+lowest+homicide+rate+in+the+Americas%2C+following+only+Canada.+Chile+is+a+founding+member+of+the+United+Nations%2C+the+Community+of+Latin+American+and+Caribbean+States+%28CELAC%29%2C+and+the+Pacific+Alliance%2C+and+joined+the+OECD+in+2010.&isMultiRegex=false)).

    (^|[\n.])!sentence{[^.\n]*Chile[^.\n]*(Peru|Argentina|Bolivia)[^.\n]*\.}

This pattern describes the extraction task that REmatch should do (we will come back to this pattern later). The language of this pattern is REQL, a RegEx-based query language for information extraction. RegEx (for Regular Expressions) is a standard language of characters and special operators that allow us to describe groups of sequences in strings, which one would like to identify, verify, and extract. These expressions will simplify the task of extracting information from documents, allowing us to define our task and letting a library like REmatch execute and optimize the task in the best possible way. 

Below, we will introduce REQL to verify simple RegEx patterns in strings and then use these patterns to extract information from documents with the REmatch library. We will start by introducing the most common RegEx operators and then show the main features of REQL for extracting information from documents. 

# Brief overview of REQL

- `a`: character (UTF-8)
- `.`: any character
- `\.`: escape character
- `[S]`: character set
- `[^S]`: negated set
- `\w`: special character set 
- `\n`: special symbols
- `ee`: concatenation
- `e|e`: disjunction (alternation)
- `e?`: optional
- `e*`: zero or more
- `e+`: one or more
- `e{n,m}`: at leat n and at most m
- `(e)`: normal parentheses
- `^`: beginning of document
- `$`: end of document
- `!var{e}`: capture variables

# Standard RegEx operators in REQL

## Simple patterns 

- `a`: character (UTF-8)
- `ee`: concatenation

The simplest form of a RegEx is a word. A word like `gmail` defines the string 'gmail' and describes that only strings containing the word 'gmail' will satisfy the property. For a running example of this tutorial, consider the following document that includes a list of emails separated by commas.

    cperez@gmail.com
    soto@uc.cl
    sdelcampo@gmail.com
    lpalacios@gmeil.com
    rramirez@gmsil.com
    pvergara@ing.uc.cl
    ndelafuente@ing.puc.cl
    tnovoa@mail.uc.cl
    nnarea@myucmail.uc.cl
    nomail@gmail.coom
    juan.soto@uc.cl

Then, for finding the word 'gmail' in the previous document, we only need to write the following REQL query:

    !output{gmail}

Then if you run this query on REmatch over the emails document, you will find the three positions where the word 'gmail' appears. You can try the same query by modifying gmail with your favorite word to search and see the result. You can try this example [here](https://rematch.cl/?query=%21output%7Bgmail%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false).

**IMPORTANT**: For the rest of this section, forget about the clause `!output{...}` in the REQL examples. This operator is one of the main constructs of REQL for information extraction and we will cover it in full detail in a while. This construct says: "When you find the word 'gmail,' capture it in the object 'output'." Indeed, if you write 'gmail' without the clause `!output{...}`, this is a valid REQL query, but REmatch will only tell you `TRUE` or `FALSE`, depending on whether the substring gmail appears or not in the document, but without retrieving the positions of that substrings. For the following examples, we will maintain this clause  `!output{...}` in the queries to cover it later in the tutorial (after you are a master of RegEx patterns in REQL). 

## Any character and escape characters

- `.`: any character
- `\.`: escape character

Many times we will know the pattern we want to define, but there are certain positions of the pattern that can be any character. For this, we will use the pattern `.` (a dot), which simply means we want to see one letter. For example, if we want to find the word 'gm_il' where the third letter can be any symbol, then we define that with the following REQL query (try it [here](https://rematch.cl/?query=%21output%7Bgm.il%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false)):

    !output{gm.il}

where the dot represents any symbol. By running this query, we will have the same results as for the simple gmail pattern but with more results. 

The above describes all the simple patterns to find a sequence of symbols within a string. But how can we define that we want to find a dot? Since the `.` is part of the REQL's syntax, we must use the escape symbol `\`. Thus, to find all emails of type 'gmail.com', we must write the pattern as `gmail\.com`. We must do the same to find symbols like `[` and `]` that are part of the syntax of the REQL queries, like the symbols of other operators that we will see below.

## Character sets

- `[S]`: character set
- `[^S]`: negated set

In some cases, with the pattern we want to define that not just any symbol will go in that position, but rather a symbol of a special class. In our `gm.il` example, we would like to say that the third symbol is a vowel. For this, we use the `[ ]` operator that allows us to specify character classes, where within the square parentheses we list all the symbols that can appear. For example, to define the vowel class, we use `[aeiou]`, and to say that we want to find 'gm_il' where the symbol _ can be a vowel, we use the pattern (try it [here](https://rematch.cl/?query=%21output%7Bgm%5Baeiou%5Dil%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false)):

    !output{gm[aeiou]il}

The previous mailing list has now been reduced because we only want the ones with a vowel in the third symbol. If we want to add more symbols, we can place as many as we want inside the `[ ]`, such as all the lowercase letters of the alphabet (English): `[abcdefghijklmnopqrstuvwxyz]`. This doesn't look very elegant at first glance. RegEx and REQL allow you to define character ranges to simplify character classes. If we want to define all lowercase letters we can use `[a-z]`, which means "a to z", or if we want all uppercase and lowercase letters, we can use `[a-zA-Z]`, which is the same as `[a-z]` but adding the section of capital letters from A to Z. Finally, the character classes `[ ]` allow you to define a class of symbols that excludes all the symbols listed within the parentheses. For this, we use the `^` symbol at the beginning of the character class. Thus, if we want to say any symbol except vowels, we write `[^abcde]` (try it [here](https://rematch.cl/?query=%21output%7Bgm%5B%5Eaeiou%5Dil%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false)):

    !output{gm[^aeiou]il}

## Disjunction and optional

- `e|e`: disjunction (alternation)
- `(e)`: normal parentheses
- `e?`: optional

Although simple patterns allow us to define a sequence of fixed length that we want to find in a string, they do not allow us to search for the appearance of two or more possibilities simultaneously. For example, we would like to check the occurrence of the word 'gmail' or the word 'uc' if either appears in the string. For this, we can use the disjunction operator `|` (also called *alternation* in RegEx), which allows us to say `gmail|uc` and reads like "we want to see the appearance of gmail or uc in the string". Namely, the following REQL query (try it [here](https://rematch.cl/?query=%21output%7Bgmail%7Cuc%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false)):

    !output{gmail|uc}

We can combine disjunction with simple patterns or within simple patterns. For example, instead of using a character class to define a vowel, we can use disjunction and define the pattern `gm(a|e|i|o|u)il` where parentheses are part of regular expression syntax and allow to group disjunctions. In other words, the subexpression `(a|e|i|o|u)` is equivalent to `[aeiou]`, which defines the vowel class. In particular, we can use the operator `|` to list different possibilities in a pattern like `gmail|uc|puc`.

Another way to choose between alternatives in RegEx (and REQL) is to use the optional operator `?`, another alternative to disjunction. An example of the optional is when we use `ing\.(uc|puc)` to search for the word 'ing.uc' or 'ing.puc' in an email. Both words are very similar; the only difference is that the 'p' may or may not appear in the email. For this, we can use the optional operator `?` and write the REQL query (try it [here](https://rematch.cl/?query=%21output%7Bing%5C.p%3Fuc%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false)):

    !output{ing\.p?uc}

where the `\.` is to declare a dot in the query (which must be escaped, as we explained before). Note that we can use the optional `?` over a simple pattern, or nest this operator on top of other operators. For example, if we also want the prefix 'ing.' may or may not appear, we can define this as `(ing\.)?p?uc` where the parentheses `( )` help us group the subpattern where the optional operator will be applied.

## Repetitions and quantifiers

- `e*`: zero or more
- `e+`: one or more
- `e{n,m}`: at leat n and at most m

One of the most important classes of operators in REQL is repetition. So far, REQL allows us to identify patterns within a string but with a bounded number of letters. For example, an expression like `gmail|p?uc` will enable us to identify the occurrence of 'gmail', 'puc' or 'uc' in the string, but this is a limited number of possibilities.

We use the `+` and `*` operators to define patterns with one-or-more or zero-or-more characters. For example, if we want to identify emails that contain '@ing.uc.cl' or '@mail.uc.cl' where what is between '@' and the next dot is of no interest to us, then we use the REQL query (try it [here](https://rematch.cl/?query=%21output%7B%40%5Ba-zA-Z%5D%2B%5C.uc%5C.cl%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false)):

    !output{@[a-zA-Z]+\.p?uc\.cl} 

In this last query, the `[a-zA-Z]+` means that we want to see a letter (upper or lower case, that is, `[a-zA-Z]`) one or more times. On the other hand, if we want to allow emails like '@.uc.cl', then we can use the `*` operator and write the expression `@[a-zA-Z]*\.uc\.cl` where now the `[a-zA-Z]*` means that we want to see a letter zero or more times.

The RegEx subpattern `[a-zA-Z]+` allows us to find one or more letters in an email, but there is no limit to the length of the word. In fact, the pattern `@[a-zA-Z]+\.uc\.cl` will match the string '@a.uc.cl' or the string '@aaaaaaaaaaaaaaaaaaaaaaa.uc.cl' (20 letters or more) or with any length between @ and the first period. We often do not want an arbitrary number of repetitions of a pattern but rather a number of repetitions within a range. For this, one can use the repetition operator with range `{n,m}`, which means that the pattern will repeat n-to-m times where n and m are numbers. Going back to our example, if we want the domain word to be between 2 to 5 characters, then we use (try it [here](https://rematch.cl/?query=%21output%7B%40%5Ba-zA-Z%5D%7B2%2C5%7D%5C.uc%5C.cl%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false)):

    !output{@[a-zA-Z]{2,5}\.p?uc\.cl} 

## Special character sets and special symbols

- `\w`: special character set 
- `\n`: special symbols

In RegEx, allowing some operators to refer to a class of special symbols is useful. For example, RegEx allows the use of `\w` to refer to the class of alphanumeric and underscore characters; namely, `\w` is equivalent to `[A-Za-z0-9_]`. For our running example, we can use `\w` to capture the right-hand side of emails as follows (try it [here]):

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

# Capturing variables

## Variables, matches, and spans

To understand how to use REQL to extract parts of our strings, let's look at an example. First, recall our running example where we want to extract data from a list of emails like the following:

    cperez@gmail.com
    soto@uc.cl
    sdelcampo@gmail.com
    lpalacios@gmeil.com
    rramirez@gmsil.com
    pvergara@ing.uc.cl
    ndelafuente@ing.puc.cl
    tnovoa@mail.uc.cl
    nnarea@myucmail.uc.cl
    nomail@gmail.coom
    juan.soto@uc.cl

Consider our last example for checking the right side of a mail, only now we'll add variables to specify the parts we want to extract (try it [here]):

 !output{@!x{\w+}\.p?uc\.cl}

Our new query has two variables: `output` and `x`. The first variable `!output{...}` extracts the whole text that matches the pattern, as we did with the previous example above. The second variable `!x{...}` extracts the internal domain of the email, namely, what is matched by the subpattern `\w+`. Indeed, the identifiers 'output' and 'x' are the names of the variables and will allow us to refer by a name to each capture. These names are arbitrary, and one could use more suggestive identifiers like below (try it [here]): 
 
 !email{@!domain{\w+}\.p?uc\.cl}

where 'email' and 'domain' are the new identifiers for 'output' and 'x'. Note that this marks the first big difference with standard RegEx. In RegEx, one uses a capturing group to extract a substring that is denoted by normal parentheses `(...)` or, also, `(?<name>...)` to assign a name to the capturing group. Since extracting information is the main goal of REmatch, in REQL we have to always assign a name to what is captured, and for that, we use the notation `!name{...}`. Moreover, this allows the free use of normal parenthesis `(...)` as a syntactical object to group operators.

When we run a REQL query over a document, REmatch returns all the **matches** of the query into the document. A match is an assignment of the variables to intervals of the document, also called **spans**. For instance, if we run the above query over our document in the REmatch web interface (try it [here]), we can see the four matches that REmatch retrieves on the right-hand side. Furthermore, each variable maps to a span in the document, namely, a pair of positions. For the first match (Match 0), we can see that 'email' is mapped to the span (95-105) and 'domain' to the span (96-99). Note that the spans allow us to extract the document's content and also help us find the context where the information was found. 


## Restrictions over variables

In REQL, one can use up to 32 different variables in a single pattern. For instance, if we also want to capture the other domains in the same pattern, we can use more variables to capture them (try it [here]):

    !email{@!domain{\w+}\.!domain2{p?uc}\.\domain3{cl}}



to capture text one has to use normal parenthesis, which refer 

Nuestra nueva expresion regular cuenta con dos variables. La primera variable, escrita como !x{...} nos permitirá obtener el identificador del correo, mientras que la segunda variable, escrita como !y{...} nos permitirá obtener el dominio del correo. De hecho, el identificador x e y son los nombres de estas variables, y nos permitirá referirnos por un nombre a cada captura. Estos nombres son arbitrarios, y podríamos haber ocupado identificadores más sugerentes como a continuación:

^!id{(\w+\.)?\w+}@!domain{(\w+\.)?\w+\.\w{2,3}}$

donde id y domain son los nuevos identificadores para x e y, respectivamente.

Ahora que tenemos nuestras variables para capturar contenido, necesitaremos ver como utilizar la librería REmatch para extraer el contenido. Para esto, veamos un ejemplo en ejecución.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "^!id{(\w+\.)?\w+}@!domain{(\w+\.)?\w+\.\w{2,3}}$"
regex = re.compile(pattern)

for s in seq:
    match = regex.find(s)
    if match:
        print("El correo " + s + 
              " tiene id " + match.group('id') + 
              " y dominio " + match.group('domain'))
Como se puede observar de este ejemplo, la función find del objeto regex nos devuelve un objeto match cuando obtiene un resultado. Este objeto match tiene la captura con el contenido de id y de domain. Para acceder el string capturado por estas variables, usamos la función group con el nombre de la variable.

** TODO: EXPLAIN RESTRICTTIONS ON THE USE OF VARIABLES **

# All possible matches

**EXPLAIN HERE ALL POSSIBLE MATCHES SEMANTICS**

** GIVE EXAMPLES WHERE THIS SEMANTICS IS NEEDED **
** USE THE JUSFITICATION IN THE DEMO PAPER TO EXPLAIN THIS **

# Separators and many matches

Suponga ahora que en vez de un solo string, usted cuenta con un documento que es una lista de string separados por comas, donde algunos de estos strings pueden ser correos y otros no. Por ejemplo, un posible documento con estas caracteristicas sería el siguiente:

Carlos Perez,cperez@gmail.com,Juan Soto,soto@uc.cl,Sebastian del Campo,sdelcampo@gmail.com

Usted desea extraer los strings que son correos, junto con su identificador y dominio. Si extendemos ligeramente nuestra expresión regular podremos identificar si un campo en los datos (esto es, un string separado por comas) es un correo y, utilizando las variables, podremos obtener el identificador el dominio. En otras palabras, considere la siguiente expresión regular:

(^|,)!id{(\w+\.)?\w+}@!domain{(\w+\.)?\w+\.\w{2,3}}($|,)

Lo que hicimos fue modificar el comienzo con (^|,) que nos permite partir desde el comienzo del string o desde una coma, y también modificar el fin con ($|,) que nos permite terminar desde el fin del string o desde una coma. Esta expresión regular busca un correo en el documento y, de encontrarlo, obtiene el identificador y dominio del correo.

** NO NEED OF BOUNDARIES OR LOOKAHEAD **

## Anchors and special symbols

- `^`: beginning of document
- `$`: end of document


So far, we have used our examples to ask for the occurrence of each pattern to be anywhere in the string. While this happens in most cases, other times we would like to refer to the beginning or end of the document, also known as anchors. For this, we will use the `^` operator to refer to the beginning and `$` to refer to the end of the document. To exemplify the use of both operators, we can define a pattern that allows us to verify that the entire string is an email using the following expression:

** PREVIOUS VERSION

^[a-zA-Z.]+@[a-zA-Z.]+\.[a-zA-Z]{2,3}$

Aquí el ^ al comienzo de la expresión nos dice que la aparición del patrón tiene que ser desde el comienzo del string y, en cambio, el $ al final nos dice que el patrón debe terminar justo al final del string.

[ ]
seq = ["cperez@gmail.com", "soto@uc.cl", "sdelcampo@gmail.com", 
       "lpalacios@gmeil.com", "rramirez@gmsil.com", "pvergara@ing.uc.cl", 
       "ndelafuente@ing.puc.cl", "tnovoa@mail.uc.cl", "nnarea@myucmail.uc.cl", 
       "nomail@gmail.coom", "juan.soto@uc.cl"]
pattern = "^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]{2,3}$"
regex = re.compile(pattern)

for s in seq:
    if regex.find(s):
        print(f"{s} cumple con el patrón")

** EXPLAIN HERE THE ESCAPE CHARACTERS THAT ARE ALLOWED LIKE \n **

## FULL EXAMPLE (sentences and content)


# Multispan capturing

** TODO: CAMBIAR PAGINA A QUE DIGA MULTI-SPAN Y NO MULTI-REGEX **



