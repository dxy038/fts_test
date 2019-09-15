from newutils import *

randomandfile=open("randomWordsAND.txt", "w")
randomorfile=open("randomWordsOR.txt", "w")
randompfile=open("randomPhrase.txt", "w")
for i in range(0,500):
    stri = "%s %s %s" % (randomword(4,9), randomword(4,9), randomword(4,9))
    print(stri, file=randomandfile)
    stri = "%s %s %s" % (randomword(9,15), randomword(9,15), randomword(9,15))
    print(stri, file=randomorfile)
    stri = "%s" % randomphrase(4,9)
    print(stri, file=randompfile)
    print("\r%d rows inserted in three files . . ." % (i+1), end="")