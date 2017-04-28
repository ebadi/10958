# 10958
[Crazy Sequential Representation](https://arxiv.org/abs/1302.1479)
This program tries to find valid crazy sequential representations of 10958.

One solution with using loose/weak concatenation function is presented here.
[Problem](https://www.youtube.com/watch?v=-ruC5A9EzzE)
[Solution](https://www.youtube.com/watch?v=pasyRUj7UwM)

The solution mentioned in the video assumes loose concatenation function.
Loose/weak concatenation function can concatenate two intermediate numeric results  `(1+2)|(3+4) =37`. This means that '|' has to explicitly defiend for represeting a number.

Strict concatenation function can only concatenate single digits that are not produced as an intermediate computation such as `(1|2|3) + (4|5) = 123 + 45`. No extra operations for represeting a number.
I used [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) to deal with placing parentheses. Since a calculation can easily grow large, I put few restrictions on the range of intermediate results instead of entirely ignoring exponentiation.

Parker number, `1*(2|3)*(((4*5*6)|7)+8)*9)`, can be represented as `123|*45*6*7|8+9*+`  in the RPN noation (found around 782740)
The program similarly tries to use the same loose/weak concatenation function. The user can later ignore representations that are not strict. It is easy to identify loose solutions as they have an operator (`+-/*^`) just before or with one element distance before "|". (eg `123+|` or `12+3` )
We found 239 expressions that all need loose concatenation function.

Complexity and number of cases that are need be checked: pow(NumberOfOperations,NumberOfDigits-1) * (numberOfInterleave ) =` 6^9 * 1430 = 10077696 * 1430 = 14411105280`


How to try the program:
```
python2.7 10958.py 4000000 10 | tee out4000000-x.txt
```
