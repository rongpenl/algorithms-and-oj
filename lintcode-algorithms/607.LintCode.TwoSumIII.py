class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.eleList = []

    def add(self, number):
        self.eleList.append(number)
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        temp = set()
        for ele in self.eleList:
            if value - ele in temp:
                return True
            else:
                temp.add(ele)
        return False
