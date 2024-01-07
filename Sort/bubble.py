# bubbleソートとは隣接する要素同士を比較して順序が逆であれば交換を行い、リスト全体を一巡することを繰り返すことで、要素が正しい順序になるまで繰り返します。

# [2,1,5,7,8,3]をbubbleソートを使ってソートしなさい
class Bubble:
  def sort(self, nums: list[int]) -> list[int]:
    for i in range(len(nums)):
      for j in range(len(nums) -i -1):
        if nums[j] > nums[j+1]:
          nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
  
if __name__ == '__main__':
  import random
  nums = [2,5,1,8,7,1]
  bubble = Bubble()
  print(bubble.sort([random.randint(50, 100) for i in range(10)]))
