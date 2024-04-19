
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

This pattern describes the extraction task that REmatch should do. The language of this pattern is REQL, a RegEx-based query language for information extraction. RegEx (for Regular Expressions) is a language of characters and special operators that allow us to describe groups of sequences in strings, which one would like to identify, verify, and extract. These expressions will simplify the task of extracting information from documents, allowing us to define our task and letting a library like REmatch execute and optimize the task in the best possible way. 

Below, we will introduce REQL to verify simple RegEx patterns in strings and then use these patterns to extract information from documents with the REmatch library. We will start by introducing the most common RegEx operators and then show the main features of REQL for extracting information from documents. 

# Standard RegEx operators in REQL

## Simple patterns 

The simplest form of a RegEx is a word. A word like gmail defines the string 'gmail' and describes that only strings containing the word 'gmail' will satisfy the property. For a running example of this tutorial, consider the following document that includes a list of e-mails separated by commas.

>cperez@gmail.com, soto@uc.cl, sdelcampo@gmail.com, lpalacios@gmeil.com, rramirez@gmsil.com, pvergara@ing.uc.cl, ndelafuente@ing.puc.cl, tnovoa@mail.uc.cl, nnarea@myucmail.uc.cl, nomail@gmail.coom, juan.soto@uc.cl


The for finding the word 'gmail' in the previous document, we only need to write the following REQL query:

    !output{gmail}

Then if you run this query on REmatch over the e-mails document, you will find the three positions where the word 'gmail' appears. You can try the same query by modifying gmail with your favorite word to search and see the result. You can try this example [here](https://rematch.cl/?query=%21output%7Bgmail%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false).

**IMPORTANT**: For the rest of this section, forget about the clause **!output{...}** in the REQL examples. This operator is one of the main constructs of REQL for information extraction and we will cover it in full detail in a while. This construct says: "When you find the word 'Gmail,' capture it in the object 'output'." Indeed, if you write 'gmail' without the clause **!output{...}**, this is a valid REQL query, but REmatch will only tell you TRUE or FALSE, depending on whether the substring gmail appears or not in the document, but without retrieving the positions of that substrings. For the following examples, we will maintain this clause  **!output{...}** in the queries to cover it later in the tutorial (after you are a master of RegEx patterns in REQL). 

## Character operators

Many times we will know the pattern we want to define, but there are certain positions of the pattern that can be any character. For this, we will use the pattern '.' (a dot), which simply means we want to see one letter. For example, if we want to find the word 'gm?il' where the third letter can be any symbol, then we define that with the following REQL query:

    !output{gm.il}

where the dot represents any symbol. By running this query, we will have the same results as for the simple gmail pattern but with more results. Try it [here](https://rematch.cl/?query=%21output%7Bgm.il%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false).

In some cases, with the pattern we want to define that not just any symbol will go in that position, but rather a symbol of a special class. In our 'gm?il' example, we would like to say that the third symbol is a vowel. For this, we use the '[ ]' operator that allows us to specify character classes, where within the square parentheses we list all the symbols that can appear. For example, to define the vowel class, we use [aeiou], and to say that we want to find 'gm_il' where the symbol _ can be a vowel, we use the pattern (try it [here](https://rematch.cl/?query=%21output%7Bgm%5Baeiou%5Dil%7D&doc=cperez%40gmail.com%2C+soto%40uc.cl%2C+sdelcampo%40gmail.com%2C+lpalacios%40gmeil.com%2C+rramirez%40gmsil.com%2C+pvergara%40ing.uc.cl%2C+ndelafuente%40ing.puc.cl%2C+tnovoa%40mail.uc.cl%2C+nnarea%40myucmail.uc.cl%2C+nomail%40gmail.coom%2C+juan.soto%40uc.cl&isMultiRegex=false)):

    !output{gm[aeiou]il}

The previous mailing list has now been reduced because we only want the ones with a vowel in the third symbol. If we want to add more symbols, we can place as many as we want inside the '[ ]', such as all the lowercase letters of the alphabet (English):

    [abcdefghijklmnopqrstuvwxyz]

This doesn't look very elegant at first glance. RegEx and REQL allow you to define character ranges to simplify character classes. If we want to define all lowercase letters we can use [a-z], which means "a to z", or if we want all uppercase and lowercase letters, we can use [a-zA-Z], which is the same as [a-z] but adding the section of capital letters from A to Z. Finally, the character classes '[ ]' allow you to define a class of symbols that excludes all the symbols listed within the parentheses. For this, we use the '^' symbol at the beginning of the character class. Thus, if we want to say any symbol except vowels, we write [^abcde].
