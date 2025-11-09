def getInt(queryString):
    while True:
        value = input(queryString)
        try:
            return int(value)
        except:
            print(f"You must input an integer.")

def getIndex(length):
    while True:
        value = getInt("Choose the desired index: ")
        if abs(value) < length:
            return value
        else:
            print("That is not a valid index.")