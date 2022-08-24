# Marking Comments

## SQL

### 1.1.1 - single column

Amazing definition and nice generic example too with the inclusion of multiple single column indexes too!
5/5

### 1.1.2 - multi column

It's one that's been raised amongst the instructors and we're giving this for multiple single indexes and a duplicate of the composite. Great sources too.
5/5

### 1.1.3 - Composite

Good example but the definition is lacking a little and missing a bits about the potential downsides. Say I definite a composite with (col1, col2, col3) I can query col1 with the same benefit as col1 + col2 and col1 + col2 + col3 but a standalone query for col2 or col3 won't. Order matters.
4/5

### 1.1.4 - Clustered

Great definition and knowledge the MySQL automatically uses the PRIMARY KEY. Great example use case too.
5/5

### 1.2

Missing?
0/5

### 1.3

Missing?
0/5


## Python

### 3.1
Nicely done, nice simply solution and nicely debugged.
2/2

### 3.2
Again well debugged and explained with a nice simple solution proposed.
2/2

### 3.3
Great understanding of data types. My minor picky comments are this allows 
for any input to be used e.g. -2 boxes spits out -3 omelettes can be made,
how could you protect your code against this? And assumes you can make half
an omelette too which I'm not sure about, how could you write this to give 
full integer omelettes?
4/5

### 3.4.1
Smashed it, nice simple replace!
2/2

### 3.4.2
Nice reassignment.
2/2

### 3.4.3
This works but there's a much easier way! Try `my_str_2.startswith('A')`. I'll let
you off with the slight indentation issue around your if/else.
1/2

### 3.4.4
My favorite string method and nice variable assignment.
2/2

### 3.5.1
Nicely done. Equally as valid is [-4:] but I tend to work with positive
indexes where possible as lists can be appended to. Great work.
2/2

### 3.5.2
You wanted to slice up to the 'o' not just to obtain 'o' so you wanted 'Pyth'
as the output. This could be done with `wrd[:4]`.
0/2

### 3.5.3
Smashed it!
2/2

### 3.5.4
Functionally it works for this string but there's no step count in your code
and you've manually obtained the two indexes needed. I was after `wrd[1:-1:2]`.
0/2

### 3.6
Extremely close to nailing it. You've got the iteration and that the o's are 
progressively longer but range(100) goes from 0-99. You're on the verge too with
99 o's at the end but the first instance has zero because 0 * 'o' = ''.
4/5

### 3.7
Great explanation of the function and the return value. You understand the
fundamentals of functions which is great! The answer you provided is a clean
and simple fix to the problem too. Great job!
5/5

### 3.8
It works and displays the required outputs but the question asked for a 
function. Try taking what you have here and reducing the code duplication
with function(s). One function could ask for the name/price of the item and
the other function could total the cost. You have understood the fundamentals
but missed the main aspect of the question!
2/5
