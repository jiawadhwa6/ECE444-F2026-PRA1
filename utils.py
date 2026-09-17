class utils:

    def reversed(self, number):
        return int(str(number)[::-1])

    def formatter(self, number):
        number = int(number)
        return bin(number), oct(number)

# print(utils().reversed(12345))
# print("------")
# print(utils().formatter(10))