import time
file = open("rand1000000.txt","r")
data2 = file.read().split(" ")

# Read in the input file and strip out any extra characters.
for index,element in enumerate(data2):
    data2[index] = element.strip()
data2 = [int(x) for x in data2 if x != '']

file.close()
counter = 0
def masterRec():
    # Create empty array of 10 elements.
    tenArr = data2[0:10]
    print(tenArr)

    
    def lcs(X, Y, m, n):
        global counter
        counter+=1

        # Base case: if the lengths of the input is 0, return 0
        if (m == 0 or n == 0):
            return 0
        # If the last characters of the input are the same, then recursively call lcs again and cut off the last characters of the input.
        if (X[m - 1] == Y[n - 1]):
            return 1 + lcs(X, Y, m - 1, n - 1)
        # Else, recursively call the function with the last two characters in the input string.
        else:
            return max(lcs(X, Y, m, n - 1),
                    lcs(X, Y, m - 1, n))
    
    

    # Driver program to test the above function
    for i in data2: #change to data
        global counter
        X = str(i)
        Y = "0123456789"
        print("Testing {} against {}".format(X,Y))
        print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)))
        print("Number of Recursive calls ",counter)
        counter = 0
# start = time.process_time() #starting time is set to start
# masterRec()
# print()
# end = time.process_time() #ending time is set to end
# execution_time = end - start
# print('Time Taken naive reccursion: ', execution_time, '\n')


def masterDP():
    maximum =1000
    tenArr = data2[0:10]
    print(tenArr)
    def lcs(X, Y, m, n, dp):
        
        # Base case: if the lengths of the input is 0, return 0
        if (m == 0 or n == 0):
            return 0
    
        # If the last characters of the input are the same, then recursively call lcs again and cut off the last characters of the input.
        if (dp[m - 1][n - 1] != -1):
            return dp[m - 1][n - 1]
    
        # If the last characters of the input are the same, then store the value of the function call and recursively call lcs again and cut off the last characters of the input.
        if (X[m - 1] == Y[n - 1]):
    
            # store it in arr to avoid further repetitive
            # work in future function calls
            dp[m - 1][n - 1] = 1 + lcs(X, Y, m - 1, n - 1, dp)
    
            return dp[m - 1][n - 1]
    
        else :
    
            # Else, store the function call and memoize it to reduce runtime.
            dp[m - 1][n - 1] = max(lcs(X, Y, m, n - 1, dp),
                                lcs(X, Y, m - 1, n, dp))
    
            return dp[m - 1][n - 1]
    
    # Driver Code
    for i in data2: #change to data
        X = str(i)
        Y = "0123456789"
        dp = [[-1 for i in range(maximum)] 
        for i in range(len(Y))]
        print("Testing {} against {}".format(X,Y))
        print ("Length of LCS is ", lcs(X , Y, len(X), len(Y),dp))
        

start = time.process_time() #starting time is set to start
masterDP()
print()
end = time.process_time() #ending time is set to end
execution_time = end - start
print('Time Taken for dyanmic approach: ', execution_time, '\n')

def masterBup():
    tenArr = data2[0:10]
    print(tenArr)
    def LCSLength(X, Y):
        
        m = len(X)
        n = len(Y)
    
        # Search through saved results of already solved problems in the table.
        T = [[0 for x in range(n + 1)] for y in range(m + 1)]
    
        # fCreate the look up table through a bottom up approach
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if the current character of X and Y matches
                if X[i - 1] == Y[j - 1]:
                    T[i][j] = T[i - 1][j - 1] + 1
                # otherwise, if the current character of X and Y don't match
                else:
                    T[i][j] = max(T[i - 1][j], T[i][j - 1])
    
        # LCS will be the last entry in the lookup table
        return T[m][n]
    for i in data2: #change to data
        X = str(i)
        Y = "0123456789"
        print("Testing {} against {}".format(X,Y))
        print ("Length of LCS is ", LCSLength(X , Y))
start = time.process_time() #starting time is set to start
masterBup()
print()
end = time.process_time() #ending time is set to end
execution_time = end - start
print('Time Taken for bottom up : ', execution_time, '\n')
