from music import *
import random

key = 8
finalScore = Score("Musical Poetry", 80) 
instrument = PIANO
drum = MRC
how_often = 5

phon = ["AA", "AE", "AH", "AO", "AW", "AY", "B", "CH", "D", "DH",
   "EH", "ER", "EY", "F", "G", "HH", "IH", "pIY", "JH", "K", "L", "M",
   "N", "NG", "OW", "OY", "P", "R", "S", "SH", "T", "TH", "UH", "UW",
   "V", "W", "Y", "Z", "ZH", "SIL"]

#key change function
def setKey(note, key):
   if key == 2:
      return note+2
   elif key == 3:
        return note+4
   elif key == 4:
        return note+5
   elif key == 5:
        return note+7
   elif key == 6:
        return note-3
   elif key == 7:
        return note-1
   elif key == 8:
        if (note ==64)|(note==69)|(note==71):
            note = note-1
        else:
            note = note
   elif key == 9:
        if (note ==64)|(note==69)|(note==71):
            note = note+1
        else:
            note = note+2
   elif key == 10:
        if (note ==64)|(note==69)|(note==71):
            note = note+3
        else:
            note = note+4
   elif key == 11:
        if (note ==64)|(note==69)|(note==71):
            note = note+4
        else:
            note = note+5
   elif key == 12:
        if (note ==64)|(note==69)|(note==71):
            note = note+6
        else:
            note = note+7
   elif key == 13:
        if (note ==64)|(note==69)|(note==71):
            note = note-4
        else:
            note = note-3
   elif key == 14:
        if (note ==64)|(note==69)|(note==71):
            note = note-2
        else:
            note = note-1
   return note

#correspond each sound to a note length
def rhy(p, phon):
   R = [.5, .5, .75, .5, .75, .75, .25, .25, .25, .5, 
   .5, 1, 1, .25, .25, .125, .5, .5, .25, .25, .5, .5,
   .25, .5, .25, .25, .125, .125, .25, .125, .25, .5, .5,
   .25, .25, .25, .25, .5, .5, 1] 
   i = phon.index(p)
   return R[i]

#correspond each sound to a note
single = [72, 71, 69, 67, 65, 64, 62, 60, 59, 57, 55, 53, 52, 50, 48]
for i in range(len(single)):
   single[i] = setKey(single[i], key)
chords = [[C3, E3, G3], [C4, E4, G4], [F3, A3, C3], [G4, B4, D4], [F5, F5, C5], [G3, B3, D3]]
for i in range(len(chords)):
   for j in range(3):
      chords[i][j]= setKey(chords[i][j], key) 
possibilities = [REST]
for i in single:
   possibilities.append(i)
for i in chords:
   possibilities.append(i)
   

notes = []
for i in range(len(phon)):
   notes.append(random.choice(possibilities))
def pitch(p, notes, phon):
   i = phon.index(p)
   return notes[i]

#drums
bang=[]
bang.append(drum)
for i in range(how_often):
   bang.append(REST)

melodyPart = Part(instrument, 1)
melodyPhrase = Phrase()
drumPart = Part("Drums", 0, 9)
drumPhrase = Phrase()

my_file = open('out.txt','r')
for line in my_file:
   line = line.rstrip()
   phonetics = line.split()
   rhythm1 = []
   pitches1 = []
   drumDurations = []
   drumPitches = []
   counter = 0
   for p in phonetics:
      if p in phon:
         pitches1.append(pitch(p, notes, phon))
         beat = rhy(p, phon)
         rhythm1.append(beat)
         drumDurations.append(beat)
         drumPitches.append(bang[counter])
         counter = counter+1
         if counter > len(bang) - 1:
            counter = 0
   melodyPhrase.addNoteList(pitches1, rhythm1)
   drumPhrase.addNoteList(drumPitches, drumDurations)

#combining the piece
drumPart.addPhrase(drumPhrase) # add phrases to parts
melodyPart.addPhrase(melodyPhrase)
 
finalScore.addPart(melodyPart) # add parts to score
finalScore.addPart(drumPart)


Write.midi(finalScore, "song.mid")