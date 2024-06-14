import pyrematch as REmatch

print("********************")
print("** MATCH FEATURES **")
print("********************")

print("\nEXAMPLE 1: One output")

document = "abba"
pattern = r"!x{bb}"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(f'Match.span:      {match.span("x")}')
    print(f'Match.start,end: {match.start("x"), match.end("x")}')
    print(f'Match.group:     {match.group("x")}')


print("\nEXAMPLE 2: More outputs and reuse of query")

document = "abba"
pattern = r"!x{.}"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(f'Match.span:      {match.span("x")}')
    print(f'Match.start,end: {match.start("x"), match.end("x")}')
    print(f'Match.group:     {match.group("x")}')

print("New document now")
document = "doc"
match_iterator = query.finditer(document)

for match in match_iterator:
    print(f'Match.span:      {match.span("x")}')
    print(f'Match.start,end: {match.start("x"), match.end("x")}')
    print(f'Match.group:     {match.group("x")}')


print("\nEXAMPLE 3: More variables")

document = "12 345 678"
pattern = r"(^| )!x{[^ ]*!y{\d{2,}}[^ ]*}($| )"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    for variable in match_iterator.variables():
        print(variable, match.span(variable), match.group(variable))
    print()


print("\nEXAMPLE 4: Print empty match")

document = "document"
pattern = r"^.+$"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(match)


print("\nEXAMPLE 5: Print match - several variables")

document = "document"
pattern = r"^!x{.!y{.+}.}$"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(match)


print("\nEXAMPLE 6: Check output")

pattern = r"!x{a}"
document = "aa"

query = REmatch.reql(pattern)
print(query.check(document))

print("\nEXAMPLE 6.1: Findone")

pattern = r"!x{a}"
document = "aa"

query = REmatch.reql(pattern)
print(query.findone(document))



print("\n*************************")
print("** MULTIMATCH FEATURES **")
print("*************************")

print("\nEXAMPLE 7: Multimatch spans")

pattern = r"!x{a}+"
document = "aa"

query = REmatch.reql(pattern, flags=REmatch.Flags.MULTI_MATCH)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(match.spans("x"))


print("\nEXAMPLE 8: Multimatch groups")

pattern = r"(^|(\. ))!x{!y{\w+}([^\w.]+!y{\w+})*}\."
document = "Keep calm. Use Multiquery."

query = REmatch.reql(pattern, flags=REmatch.Flags.MULTI_MATCH)
match_iterator = query.finditer(document)

for i, match in enumerate(match_iterator):
    print("match", i)
    print("x ->", match.groups("x"))
    print("y ->", match.groups("y"))


print("\nEXAMPLE 9: Submatch")

pattern = r"(^|(\. ))!x{!y{\w+}([^\w.]+!y{\w+})*}\."
document = "Keep calm. Use Multiquery."

query = REmatch.reql(pattern, flags=REmatch.Flags.MULTI_MATCH)
match = query.findone(document)

print("groups:")
print("x ->", match.groups("x"))
print("y ->", match.groups("y"))
print("spans:")
print("x ->", match.spans("x"))
print("y ->", match.spans("y"))

submatch = match.submatch([3, 10])
print("\nSubmatch:", (3, 10))

print("groups:")
print("x ->", submatch.groups("x"))
print("y ->", submatch.groups("y"))
print("spans:")
print("x ->", submatch.spans("x"))
print("y ->", submatch.spans("y"))




print("\n****************")
print("** EXCEPTIONS **")
print("****************")

#

# esta celda falla por nested variables
#REmatch.reql(r"!x{a!x{b}}")

print("\nEXAMPLE 10: querySyntaxException")

try:
    REmatch.reql(r"!x{}")
except REmatch.QuerySyntaxException as e:
    print(e)


print("\nEXAMPLE 11: AnchorInsideCaptureException")

try:
    REmatch.reql(r"!x{$abc^}")
except REmatch.AnchorInsideCaptureException as e:
    print(e)


print("\nEXAMPLE 12: querySyntaxException 2")

try:
    REmatch.reql(r"!x{a{}")
except REmatch.QuerySyntaxException as e:
    print(e)


print("\nEXAMPLE 13: WrongVariableException")

document = "abba"
pattern = r"!x{.}"

query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

try:
    match = next(match_iterator)
    match.span("y")
except Exception as e:
    print(e)


print("\nEXAMPLE 14: Use multimatch exception")

pattern = "!x{a}+"

try:
    query = REmatch.reql(pattern)
except Exception as e:
    print(e)


print("\n***********")
print("** FLAGS **")
print("***********")

print("\nEXAMPLE 15: Max deterministic states")

pattern = "!x{" + "a" * 100 + "}"
document = "a" * 20000
query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

try:
    for match in match_iterator:
        pass
    print("Evaluated successfully")
except Exception as e:
    print(e)


query = REmatch.reql(pattern, max_deterministic_states=200)
match_iterator = query.finditer(document)

try:
    for match in match_iterator:
        pass
    print("Evaluated successfully")
except Exception as e:
    print(e)


print("\nEXAMPLE 16: Max mempool duplication")

pattern = "!x{.+}"
document = "a" * 200
query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

try:
    for match in match_iterator:
        pass
    print("Evaluated successfully")
except Exception as e:
    print(e)


query = REmatch.reql(pattern, max_mempool_duplications=0)
match_iterator = query.finditer(document)

try:
    for match in match_iterator:
        pass
    print("Evaluated successfully")
except Exception as e:
    print(e)


print("\nEXAMPLE 17: Line-by-line")

pattern = r"!name{([A-Z]\w+,\n)+}"
document = """
Name,
John,
Alice,
Bob,
Emma,
"""

print("With LINE_BY_LINE")
query = REmatch.reql(pattern, REmatch.Flags.LINE_BY_LINE)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(match.span(0))

print("Without LINE_BY_LINE")
query = REmatch.reql(pattern)
match_iterator = query.finditer(document)

for match in match_iterator:
    print(match.span(0))



