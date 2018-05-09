"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-").
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
"""
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # defining variables.
        list_transformation = []
        english_dict = dict()
        morse_alphabet = [".-","-...","-.-.","-..",".","..-.","--.",
                          "....","..",".---","-.-",".-..","--","-.",
                          "---",".--.","--.-",".-.","...","-","..-",
                          "...-",".--","-..-","-.--","--.."]

        # creating a dictionary from the morse alphabet
        for i in range(len(morse_alphabet)):
            english_dict[chr(ord('a') + i)] = morse_alphabet[i]

        # forming a list containing all the passed words as morse.
        for i in range(len(words)):
            string = ""
            for j in range(len(words[i])):
                string += english_dict[words[i][j]]
            list_transformation.append(string)

        # removing duplicates from our morse list to reveal the number of different transformations.
        final_list = []
        for item in list_transformation:
            if item not in final_list:
                final_list.append(item)

        # returning the number of different transformations.
        return len(final_list)
