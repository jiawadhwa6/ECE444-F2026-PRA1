class utils:

    def reversed(self, number):
        if not isinstance(number, int):
            raise TypeError("number must be an integer")
        return int(str(number)[::-1])

    def formatter(self, number):
        if not isinstance(number, int):
            raise TypeError("number must be an integer")
        return bin(number), oct(number)

# print(utils().reversed(12345))
# print("------")
# print(utils().formatter(10))