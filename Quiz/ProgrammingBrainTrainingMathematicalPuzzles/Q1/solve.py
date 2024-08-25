# Q01 10進数で回文 
# 逆から数字を読んでも同じ数になる数のことを「回文数」と呼びます。例えば、「123454321」のような数のことです。


# 10進数、2進数、8進数のいずれで表現しても回文数となる数のうち、10進数の10以上で最小の値を求めてください。
def is_palindrome(s):
    return s == s[::-1]

target = 10

while True:
    str_target = str(target)
    bin_target = bin(target)[2:]  # 2進数に変換してプレフィックス "0b" を除く
    oct_target = oct(target)[2:]  # 8進数に変換してプレフィックス "0o" を除く

    if is_palindrome(str_target) and is_palindrome(bin_target) and is_palindrome(oct_target):
        print(target)
        break
    
    target += 1


