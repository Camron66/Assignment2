import socket, sys

# Camron Cisneros - 6187231 - Basic Python Programming

class Assignment2:

    ## Task 1 Constructor
    def __init__(self, y):
        self.year = y

    #Task 2 Calculating Age
    def tellAge(self,currentYear):
        age = int(currentYear) - int(self.year)
        print("Your age is " + str(age))

    #Task 3 List Anniversaries
    def listAnniversaries(self):
        anniversary = int((2023 - int(self.year)) / 10)
        list = []
        for i in range(anniversary):
            i+=1
            list.append(i*10)
        return list

    #Task 4 String Manipulation
    def modifyYear(self,n):
        num = self.year
        string = ""
        arr = str(num)
        first2 = int(self.year / 100)
        for i in range(n):
            string += arr[:2]
        num = num*n
        first = str(num)
        arr2 = first[::2]
        string += arr2
        return string

    # Task 5 Loop + Conditional Statements
    def checkGoodString(staticmethod, string):
        if (len(string) < 9 or string[0].islower == False):
            return False
        count = 0
        for i in string:
            if i.isdigit():
                count += 1
            if count > 1:
                return False
        return True

    #Task 6 Socket
    def connectTcp(staticmethod, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = (host,int(port))
        print ("Connecting to " + str(host) + " on port " + str(port))
        try:
            hostIP = socket.gethostbyname(host)
        except socket.gaierror:
            return False
        try:
            sock.connect(serverAddress)
            return True
        except socket.error:
            return False




