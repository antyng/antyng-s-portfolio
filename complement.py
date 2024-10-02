"""
File: complement.py
Name:Anting
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(s):
   if s=="":
       return "DNA strand is missing."
   else:
        dna = ""
        for i in range(len(s)):
            ch = s[i]
            if ch == "A":
                dna += "T"
            elif ch == "T":
                dna += "A"
            elif ch == "C":
                dna += "G"
            else:
                dna += "C"
        return dna



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
