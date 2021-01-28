class Solution:
    def nearestPalindromic(self, n: str) -> str:
        n_int = int(n)
        if n_int < 10:
            return str(abs(n_int - 1))
        if n_int <= 11:
            return str(9)

        lengn = len(n)
        sub_num = (lengn + 1)//2
        inverse_num = lengn // 2
        sub_str = n[0:sub_num]

        sub_num = int(sub_str)
        sub_num1 = sub_num + 1
        sub_num2 = sub_num - 1

        num_str = str(sub_num)+str(sub_num)[0:inverse_num][::-1]
        num_str1 = str(sub_num1)+str(sub_num1)[0:inverse_num][::-1]
        if len(str(sub_num2)) < inverse_num:
            num_str2 = str(sub_num2) + '9' + str(sub_num2)[0:inverse_num-1][::-1]
        else:
            num_str2 = str(sub_num2) + str(sub_num2)[0:inverse_num][::-1]

        num = int(num_str)
        num1 = int(num_str1)
        num2 = int(num_str2)

        if num == n_int:
            num = n_int * 1000
        d_ls = abs(num2 - n_int), abs(num - n_int), abs(num1 - n_int)
        i = d_ls.index(min(d_ls))
        if i == 0:
            return num_str2
        elif i == 1:
            return num_str
        else:
            return num_str1


if __name__=="__main__":
    solution = Solution()
    solution.nearestPalindromic(str(1000))
    print([solution.nearestPalindromic(str(i)) for i in range(1000)])