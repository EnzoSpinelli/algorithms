# import heapq

# # Criando uma min-heap vazia
# heap = []

# # Inserir tempos
# heapq.heappush(heap, 5)
# heapq.heappush(heap, 4)
# heapq.heappush(heap, 3)

# # Sempre que chamo heappop, sai o menor:
# print(heapq.heappop(heap))  # -> 1
# print(heapq.heappop(heap))  # -> 3
# print(heapq.heappop(heap)) 

def quickselect(nums, k):
    if len(nums) <= 1:
        return nums[0]
    pivot = nums[len(nums)//2]
    left  = [x for x in nums if x < pivot]
    mid   = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))

# Exemplo: 3º menor em [7,2,1,6,8,5,3,4]
print(quickselect([7,2,1,6,8,5,2,3,4], ))  # -> 3