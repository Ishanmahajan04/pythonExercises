import time, os
from string import punctuation

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
	 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',
	 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar',
	 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
	 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
	 'z':'zulu'}

def icao(txt, icao_pause=1, word_pause=3):
	words = txt.split()
	for word in words:
		for char in word:
			if char not in punctuation:
				os.system('say ' + d[char.lower()])
				time.sleep(icao_pause)
		time.sleep(word_pause)
#test
icao("Hello world, hi, I'm Nick!", 0.10, 1)
icao("The quick brown Fox jumps over the laZy Dog!")