def lower_bound(arr, target):
  st, en=0, len(arr)
  while st < en:
    mid = (st + en)//2
    if arr[mid] < target:
     st = mid + 1
    else:
     en = mid
  return st

def suggestword (products, searchWord):
  products.sort()
  result = []
  prefix = ""

  for char in searchWord:
    prefix += char

    i = lower_bound(products, prefix)
    suggest = []

    for k in range (i, min(i + 3, len(products))):
      if products[k].startswith(prefix):
        suggest.append(products[k])
      else:
        break
    result.append(suggest)
  return result

products = ["alsdklaksd", "ksdlakds", 'kakasdk', "sldklds", "kaslasmz"]
searchWord = str(input("Search: "))
print(suggestword(products, searchWord))