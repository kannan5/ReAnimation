

class Solution:
    def find_alphabets(self, str_data):
        abc = dict()
        for x in str_data:
            if x in abc:
                abc[x] = abc[x] + 1
            else:
                abc[x] = 1
        return list(abc.values())



if __name__ == "__main__":
    a = Solution()
    print(a.find_alphabets("aaaabbbsscccc"))