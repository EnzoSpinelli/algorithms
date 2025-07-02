def mmsm (points, k):
  points.sort(key=lambda p: p[0]**2 + p[1]**2)
  return points[:k]

k=5
points=[[1,1], [6,2], [3,7], [4,8], [9,2]]
print(mmsm(points, k))