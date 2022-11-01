class Solution:
    def sortSentence(self, s: str) -> str:

        w = s.split(" ")  # splitting based on space
        dic = {}  # Creating a dictionary
        for i in w:
            dic[i[-1]] = i[:-1]  # Defining the last letter(digit)
        return " ".join([dic[j] for j in sorted(dic)])
        #Sorting based on the last digit in the words
