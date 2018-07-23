import pandas as pd

"""
Requirements:
Tested in python3.6
Input File containing First Name, Last Name, Email
"""

def verifyNameInEmail(sheet, columns):

    firstName = columns[0]
    lastName = columns[1]
    emailAddress = columns[2]

    for index, row in sheet.iterrows():
        first = row[firstName]
        last = row[lastName]
        email = row[emailAddress]

        conditions = [
            pd.isnull(first) == False,
            pd.isnull(last) == False,
            pd.isnull(email) == False
        ]

        if(all(conditions)):
            namePart, provider = email.split('@')
            verify = verifyEmail(first.lower(), last.lower(), namePart.lower())
            sheet["EmailVerification"][index] = verify

    print(sheet)


def verifyEmail(first, last, namePart):
    """
    Set of rules for verifying name in email.
    first = first name
    last = last name
    namePart -> part in email before '@' 
    """

    conditions = [
        first in namePart,
        last in namePart,
        (first[0] + "." + last) in namePart,
        (first + "." + last[0]) in namePart,
        (last[0] + "." + first) in namePart,
        (last + "." + first[0]) in namePart,
        (first + "." + last) in namePart,
        (last + "." + first) in namePart,
        (first + last) in namePart,
        (last + first) in namePart,
        (first + "_" + last) in namePart,
        (last + "_" + first) in namePart,
        (first[0] + last) in namePart,
        (first + last[0]) in namePart,
        (last + first[0]) in namePart,
        (last[0] + first) in namePart,
        (first + "-" + last) in namePart,
        (last + "-" + first) in namePart,
        (first[0] + last[0]) in namePart,
        (last[0] + first[0]) in namePart,
        (first[0] + "." + last[0]) in namePart,
        (last[0] + "." + first[0]) in namePart,
        namePart in first,
        namePart in last
    ]

    # if any of the conditions are satisfied then email verified to True.
    if any(conditions):
        return "True"
    else:
        return "False"


def writeIntoFile(sheet, fileName):
    
    if('.csv' in fileName):
        fileName = fileName.replace('.csv', '')

    outputFileName = fileName + '-result.csv'
    sheet.to_csv(outputFileName, sep='\t')


def openFile(fileName):

    sheet = pd.read_csv(fileName, sep='\t|,')
    sheet["EmailVerification"] = "None"
    return(sheet)


def Main():
    """
    Working:
    ->1. Read Input File
    ->2. Get Column names
    ->3. verify name in the email using the set of rules
    ->4. Write the columns in main file + the verification result into new file
    """
    fileName = input("Name of File...")

    if('.csv' not in fileName):
        fileName = fileName + '.csv'

    sheet = openFile(fileName)

    print("Columns in {} = {}".format(fileName, list(sheet.head(0))))

    columnFirstName = input("Enter the name of column with first name...")
    columnLastName = input("Enter the name of column with last name...")
    columnEmail = input("Enter the name of column with email...")

    columns = [columnFirstName, columnLastName, columnEmail]
    
    verifyNameInEmail(sheet, columns)

    writeIntoFile(sheet, fileName)


if __name__ == '__main__':
    Main()