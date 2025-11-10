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
        ## using Zlatko's suggestion
        ## https://stackoverflow.com/questions/29715501/how-can-i-check-if-a-list-index-exists#29715530
        if value in range(-length, length):
            return value
        else:
            print("That is not a valid index.")
    else:
        raise ValueError