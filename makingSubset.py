# O(n^2) 用遞迴方式Divide and conquer

def find_subsets(so_far, rest, count=0):
    if not rest:
        print(so_far)
        return count + 1  # 子集總數
    else:
        # 包含第一個
        count = find_subsets(so_far + [rest[0]], rest[1:], count)
        # 撇除第一個
        count = find_subsets(so_far, rest[1:], count)
        return count

def main():
    original_list = ["a","b","c","d","e","f"]  # 題目
    total_subsets = find_subsets([], original_list)
    print(f"Total subsets: {total_subsets}")

main()


