# function to accept two strings, and determine if they are anagrams.
def find_anagrams(string1, string2):
	
	if(sorted(string1)== sorted(string2)):
		print("True")
	else:
		print("False")		
		
# driver code
string1 ="sword"
string2 ="words"
find_anagrams(string1, string2)
