# song = "You could never know what it's like \nYour blood like winter freezes just like ice \nAnd there's a cold lonely light that shines from you \nYou'll wind up like the wreck you hide behind that mask you use \nAnd did you think this fool could never win? \nWell look at me, I'm coming back again \nI got a taste of love in a simple way \nAnd if you need to know while I'm still standing, you just fade away \nDon't you know I'm still standing better than I ever did \nLooking like a true survivor, feeling like a little kid \nI'm still standing after all this time \nPicking up the pieces of my life without you on my mind \nI'm still standing (Yeah, yeah, yeah) \nI'm still standing (Yeah, yeah, yeah)"

with open ('song.txt', 'w+') as myfile:
    myfile.write(song)
    myfile.close()

myLine = []                       # The list where we will store results.
linenum = 0
substr = "still".lower()          # Substring to search for.
with open ('song.txt', 'rt') as myfile:
    for line in myfile:
        linenum += 1
        if line.lower().find(substr) != -1:    # if case-insensitive match,
            myLine.append("Line " + str(linenum) + ": " + line.rstrip('\n'))
for still in myLine:
    print(still)