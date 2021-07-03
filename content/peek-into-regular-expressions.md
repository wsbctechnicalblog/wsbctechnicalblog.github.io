Title: Quick peek into regular expressions
Date: 2021-04-13 13:13
Category: Posts
Tags: code, posters
Slug: peek-into-regular-expressions
Author: Willy-Peter Schaub
Summary: Regular expressions are fundamental to programming

When I reviewed a pull request with a few commits focused on regular expression code changes, I decided to re-create a quick reference cheat sheet. Regular expression (regex), a variant of conventional set theory, has a few oddities with infrequent use. Hopefully this cheat sheet will turn regular expressions into a less daunting ally in your world programming and configuration.

> Regular Expressions
>
>  ![Regular Expressions](/images/peek-into-regular-expressions-1.png)

---

# Common Expressions

| Category | Expression | Description | 
|-------------|----------------|----------------|
| Special Characters | .<br/>\\.<br/>\\n<br/>\\f<br/>\\t<br/>\\xhhhh | any character<br/>dot<br/>newline character<br/>form feed character<br/>tab character<br/>Unicode character as hexadecimal number, i.e. \xFFFF | 
| Quantifiers | +<br/>?<br/>\*<br/>{x,y} | 1 or more<br/>0 or one<br/>0 or more<br/>at least ‘x’ but no more that ‘y’ occurrences | 
| Character Sets | \\s<br/>\\S<br/>\\d<br/>\\D<br/>\\w<br/>\\W<br/> [a-x] <br/>[^a-x] | whitespace character<br/>non-whitespace character<br/>digit character (0-9) <br/>non-digit character<br/>any letter (a-zA-Z) or digit (0-9) or underscore (_) character <br/>non-word character<br/>characters in the range of a to x, excluding yz<br/>characters except in the range of a to x, i.e. y and z | 
| Anchoring | ^<br/>$<br/>\\b<br/>\\B | if first char, indicates that match starts at start of  string<br/>match must continue to end of string<br/>word boundary<br/>non-word boundary |

---

# Example

> Regular Expression Example
>
>  ![Regular Expression Example](/images/peek-into-regular-expressions-2.png)

| #   | EXPRESSION  | DESCRIPTION |
|:---:|:-----------:|-------------|
| 1   | ^           | The first character ^ indicates that the next match (19\|20) starts at beginning of string. |
| 2   | (19\|20)    | We either need a 19 or a 20 at the beginning of the string. |
| 3   | \\d\\d        | Next we have two digit character (0-9). |
| 4   | [- /.]      | Next we have a range of valid characters, in this case minus, slash, space and dot. 
| 5.1 | (0[1-9]     | Either we have a 0, followed by a digit in the range of 1-9, i.e. 01 to 09.
| 5.2 | \|1[012])   | **OR** we have a 1, followed by a zero, one or two, i.e. 10, 11 or 12. | 
| 6.1 | (0[1-9]     | Either we have a 0, followed by a digit in the range of 1-9, i.e. 01 to 09. |
| 6.2 | \|[12][0-9) | **OR** we have a 1 or a 2, followed by a digit in the range of 0-9, i.e. 10 to 29. |
| 6.3 | \|3[01])    | **OR**** we have a three, followed by a zero or a one, i.e. 30 - 31. |
| 7   | $           | The last character $ indicates that the next match must continue to end of string. | 

If you need more examples, go to [regularexpressions.info](http://www.regular-expressions.info/).

