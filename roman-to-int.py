class Solution(object):
    def romanToInt(s):
        romanValues = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000}

        # For saving if there is an instance where substraction is used
        isSubstraction = False

        # Variable that will save the result
        res = 0

        # Calculate result
        for i, letter in enumerate(s):
            # Save the next letter and last letter.
            # This is for testing whether there is a substraction or not
            lastLetter = s[i-1]
            nextLetter = s[i+1] if i < len(s) - 1 else 'I'

            # If the roman numeral is not playing a potential subtraction
            if (romanValues[letter] >= romanValues[nextLetter]):
                if (not isSubstraction):
                    res += romanValues[letter]
                else:
                    res += romanValues[letter] - romanValues[lastLetter]
                    isSubstraction = False

            # The roman numeral is playing a potential substraction and is taken in account
            # For the next roman numeral
            else:
                isSubstraction = True

        # Return the result
        return res

    s = 'IV'
    answer = romanToInt(s)
    print(answer)