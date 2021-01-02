# # Swap function
def swapPositions(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list
test_list = [2, 3, 4, 5]
print(swapPositions(test_list, 0, 1))
#This should print [4,3,2,5]

# rawIndices = input(
        #     'Input the numbers of 2 items to switch separated with a comma') #user inputs "34,45"
        # print(rawIndices) #print: '34,45'
        # indices = rawIndices.split(",")#split on "," to return array: ['34','45']
        # print(indices) #array: int([34, 45])

