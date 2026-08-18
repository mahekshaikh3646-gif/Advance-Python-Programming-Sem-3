#Experiment No. 5

#Title: Longest Common Subsequence using Dynamic Programming

#Function to find the Longest Common Subsequence

def find_lcs(X, Y):

    #Find the length of the first string
    m = len(X)

    #Find the length of the second string
    n = len(Y)

    #Create a table with (m+1) rows and (n+1) columns

    #Initially, all values are 0
    dp=[[0 for j in range(n+1)] for i in range(m + 1)]

    #Fill the DP table row by row
    for i in range(1, m+1):

        #Check every character of the second string
        for j in range(1, n + 1):

            #If characters are same, add 1 to diagonal value
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            #If characters are different, take the maximum value

            #from the top or left cell
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    #The last cell contains the length of the LCS
    lcs_length = dp[m][n]

    #Create an empty string to store the LCS
    lcs = ""

    #Start from the bottom-right corner of the table
    i = m
    j = n

    #Move backwards through the table
    while i > 0 and j > 0:

        #If the characters are same, add the character to LCS
        if X[i - 1] == Y[j-1]:

            lcs = X[i-1] + lcs

            #Move diagonally up-left
            i = i-1
            j = j-1

        #If the value above is greater, move up
        elif dp[i-1][j] > dp[i][j-1]:
            i = i-1

        #Otherwise, move left
        else:
            j = j-1

    #Return the LCS and its length
    return lcs, lcs_length


#Take the first string as input from the user
X = input("Enter first sequence: ")

#Take the second string as input from the user
Y = input("Enter second sequence: ")

#Call the function to find the LCS
lcs, length = find_lcs(X, Y)

#Display the Longest Common Subsequence
print("Longest Common Subsequence:", lcs)

#Display the length of the LCS
print("Length of LCS:", length)


#Simple Working.......

#For AGGTAB and GXTXAYB:
#Create a DP table to store LCS lengths.
#Compare characters of both sequences.
#If characters are same, add 1 to the diagonal value.
#If characters are different, take the maximum of the top and left values.
#The last cell gives the length of LCS.
#Trace the table backwards to find the actual LCS.
#The final answer is GTAB, with length 4.
#Time Complexity: O(mxn)
#Space Complexity: O(mxn)
