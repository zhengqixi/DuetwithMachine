# DuetwithMachine
Parser that turns text, tokenizes them into phonetics, and translates it into music. This project requires the use of JythonMusic, found here:
http://jythonmusic.org/

To use:
Execute musicalPoetry.exe, or recompile it using the given .cpp and .h files with a c++11 capable compiler. 
This program asks for a dictionary, and a input document which music is to be made from. The dictionary is taken from the CMU Pronouncing Dictionary, seen here:
http://www.speech.cs.cmu.edu/cgi-bin/cmudict
The dictionary provides the phonemes of 134000 words. The dictionary is loaded into a hashtable, which is then used to convert the words in the input document into phonemes.
Execute JEM.jar found in JythonMusic. Load finalproject.py. This maps each phonemes to musical elements, which is done randomly. The final output file will be a midi file titled "song".
The tokenized form of the original text document is in out.txt.

Special thanks to Richard Steinholz for playing a duet on stage with the produced music.

