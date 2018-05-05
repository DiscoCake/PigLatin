vowel_pyg = 'yay'
cons_pyg = 'ay'

original = raw_input('Enter a sentence:')
words = original.split()
for word in words:
	word = word.lower()
	first = word[0]
	if len(word) > 0 and word.isalpha():
    		if first == "a" or "e" or "i" or "o" or "u": #vowel
        		new_word = word + vowel_pyg
			print(new_word),
    		else: #consonant
       			new_word = word[1:] + word[0] + cons_pyg
       			print(new_word),
