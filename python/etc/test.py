class Solution:
    def reverseWords(self, s: str) -> str:
        print("good")

if __name__ == '__main__' :
    tstr = "  good  is  bad  "
    tstr_test = tstr.strip().split(' ')
    tstr_test.reverse()
    tstr_test = filter(lambda x : x != ' ', tstr_test)
    tstr_test = " ".join(tstr_test)
    print(tstr_test)