from string import ascii_lowercase

frankenstein = open('./books/frankenstein.txt','r').read()
longString = "After you've completed this step, I recommend peeking at the solution and comparing your code to ours. Remember, there are many ways to solve a problem in programming! Just because your code is different doesn't mean it's wrong."

# words = longString.lower()

words = frankenstein.lower()
alphabetArray = list(ascii_lowercase)
for x in alphabetArray:
	print("The '",x,"' character was found", ": " , words.count(x), " times")


# words = longString.split(" ")
# print(len(words))