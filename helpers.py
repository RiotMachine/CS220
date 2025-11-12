def getInt(queryString):
    while True:
        value = input(queryString)
        try:
            return int(value)
        except:
            print(f"You must input an integer.")

def getIndex(length):
    while length > 0:
        value = getInt("Choose the desired index: ")
        if -length <= value < length:
            return value
        else:
            print("That is not a valid index.")
    else:
        raise ValueError