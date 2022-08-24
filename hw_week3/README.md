# Task 1 (Conditional flow)

## Question 1

Great code with a great while and if/else loop to ensure the input is valid. The one minor thing is `ValueError` started with a lower case in your code so never got raised.

4/5

## Question 2

Nicely identified and fixed 3/4 errors, nicely done! The comparison with `my_money` and `boat_cost` should be greater than or equal to.

3/4

## Question 3

This is great!! I wouldn't say it's the most elegant but it's definitely well separated out and readable! You check your inputs and print out accordingly. Extremely nit picky but isn't 1800 in the 19th Century? The condition comparisons are what lets you down here, a century ended at 1950 and any year ending in 0 failed, they just needed a greater than or equal to.

7/10

# Task 2 (Lists and Dictionaries)

## Question 1

You've over complicated it. All you needed to do was change the index from 1 to 0 for the first element. You don't need the last item, only the first.

0/2

## Question 2

Nice code! Good bit of string formatting too! Try using `lower` to ensure the user input matches regardless of case, this works great for an input of `milk` but not `Milk` or `MILK`. Nice catch for an invalid key!

4/5

## Question 3

This is awesome! It would've been nice if you didn't fix the lottery numbers but that's very minor. You use some great functions here `sample` and `intersection` are great choices. Great string formatting and if loops. Great code.

10/10

# Task 3 (Read and Write files)

## Question 1

Great answer, the world is your oyster.
2/2

## Question 2

Nice easy fix, line 3 was everything you needed for the marks, you're example has a slight error.
2/2

## Question 3

1. Write the lyrics to a new file called song.txt
2. Check that a file has been created successfully.
3. Read lines from this file and print out ONLY those lines that have the word ‘still’ in them.

3.1 - Lyrics written to file - done - missing the actual lyrics but would potentially work if `song` is a string of all the lyrics
3.2 - Nice check and exception catching - missing - could do with a quick check between writing and reading the file to check the file was created (see os.path.isfile).
3.3 - 5 lines printed to terminal (I thought there'd be more ... weird!) - done

Good! Defining `song` would've helped but the code works. It's literally the file check that let you down a little, but's it's a tricky one (see code added).
7/10

# Task 4 (API)

## Question 1

You did all the hard work with the request and iterating through to obtain the parameters of interest. You didn't include code that prints to a file, I used the code in the PDF but it didn't work, even with a little tinkering with variable names. Only a couple of lines extracting the moves and print the name/moves to a file and you would've aced this!

6/10

## Question 2

Amazing again, simple questions but shows you understand all the aspects.

5/5
