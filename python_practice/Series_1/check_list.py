def is_ord_sub (sl , bl) : #sl --> small list & bl --> big list
  for i in range(10) :
    if i not in sl and i in bl :
      bl.remove(i)
  s = str(sl)
  b = str(bl)
  s = s[1:len(s)-1]
  b = b[1:len(b)-1]
  if s in b :
    return True
  else :
    return False
#---------------------------------------------------------------
print(is_ord_sub([5, 3, 1], [4 , 5 , 3 , 1, 2, 3, 4, 5])) # True
print(is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1])) # True
print(is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5])) # False
print(is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3])) # True
