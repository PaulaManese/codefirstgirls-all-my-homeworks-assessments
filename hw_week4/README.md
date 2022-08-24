## Task 1 (Git and Github)

### 1.1
Good answers, you've shown you understand the flow and how git works. The definition for the remote repository has been mixed up with the master definition (probably due to it being in brackets for some reason). I was simply looking for a hosted version of the repository e.g. Github or a private server.

3/4

### 1.2
Again, you've shown you understand the flow and how git works, nice work!

3/3

### 1.3
Great stuff, just missing a definition for `git merge`. Also be careful about copy/paste answers. You're expected to write your own answers to show you understand it.

5/6

## Task 2 (Exception Handling)

Awesome code!! It's amazing!! I've been through and tried to break it, here's what I found:
- The pin functionality works great! Accepts any input without raising errors but only lets me in with a correct pin.
- It does accept a non-numeric and errors if you put in a string. You int the input straight away which falls over.
- It does allow negative numbers, so if I take out -30 my balance goes up. I would LOVE that.
- Changing pin also fails but this is additional functionality (I'm not going to mark you down on this! That'd be mean)

The two things stipulated in the mark scheme are 2 exceptions caught in try/except (you don't have any unfortunately) and raising an exception (again, none here), it's a real shame both these are missing.

I just want to give you a few pointers. I wouldn't use `quit()` in production code, it's similar to `exit()` and should really be used in the interpreter, I much prefer `sys.exit()`, it's a much safer and stable way of doing the same thing. Plus you can pass sys.exit a message/value which can be surfaced by catching `SystemExit` (like all the bogus error codes you get when some software breaks).

Also make sure you break your code down into functions to remove repetitive code blocks. There's a lot here that could be reduced down.

10/15

## Task 3 (Testing)

Unit testing is difficult and I know you were under time constraints. Check out the `main.py` and `test_main.py` examples I added. I took a little code snippet and turned it into a function, there's a bunch of different test types I've got in those 2 little tests but hopefully that helps.

0/15
