class Solution:
  def mySqrt(self, x: int) -> int:'''i=0
      while i*i <= x:
          i+=1
      
      return (i-1)'''
      if x < 2:
          return x

      low, high = 0, x
      res = 0
      while low<=high:
          mid = low+((high-low)//2)
          if mid*mid > x:
              high = mid - 1
          elif mid*mid < x:
              low = mid + 1
              res = mid
          else:
              return mid
      
      return res
      '''
      Time: O(logn)
      Exp: binary search

      Space: O(1)
      Exp: only update low, high, mid, res
      '''
