### 1. Python theory questions (20)

1.1 - 2/2 - instructions in a programming language. Nailed it.
1.2 - 2/2
1.3 - 2/2
1.4 - 2/2
1.5 - 0/2 - GIL is a Global Interpreter Lock used to ensure only one thread is running in the interpreter. Python utilises it.
1.6 - 2/2
1.7 - 2/2
1.8 - 2/2
1.9 - 1/2 - Livelock is a situation where a request for an exclusive lock is denied repeatedly, the processes keep on changing their status, which further prevents them from completing the task.
1.10 - 2/2

### 2. Python 2 and Python 3 (8)

The number and examples of the differences more than meets the criteria. You mentioned python 3 is the latest and python 2 is in legacy mode which is required for the top marks, great answer! Minor and doesn't impact the marks but python 2 has already been discontinued.

8/8

### 3. Palindrome (8)

Nice! Awesome checks to ensure it's doing what you expect too! I'm not convinced the range if loop is the best approach, it took me a little while to figure out what i ends up being. You could reverse the string using slicing or if you really wanted the for loop use it to check each character and fail early, otherwise there's no benefit. It works though, just a little odd. Also a string like `Hannah` fails because `.lower()` should be used.

6/8

### 4. Palindrome Tests (8)

As is your tests don't work because `palindrome.py` must've been renamed to `number3anspalindrome.py`. Minor but just be careful. It's also not advised to use `*` imports.

Nice tests for pass and failure cases! Nicely done. Unfortunately `testUppercase` fails because you don't change case in you palindrome (even though your comments say otherwise) which is unfortunate!

6/8

### 5. Agile (8)

Great understanding of different agile meetings. Nicely done!

8/8

### 6. Exception Handling (8)

Great definitions and understanding of the try/except block keywords.

8/8

### 7. Python and Databases (8)

Great knowledge of the MySQL connector and how to implement it. For full marks the concept of using an "engine" to connect to a database was needed (generalising the connection).

7/8

### 8. SQL practical question (10)

Smashed it. Absolute textbook answer.

10/10

### 9. Two Number Sum (22)

This is a great bit of code, annoyingly there's 3 minor issues otherwise it would've been top marks. You needed to return an array of pairs that make the sum, although yours clearly works you've not returned anything. Having the `arr_size` argument is redundant as this could be worked out in function. A very minor point is avoid using numbers as dictionary keys, python will hash them and they work in mysterious ways! This is so close to being a perfect answer though, just a few tweaks needed.

18/22

### Overall

88/100
