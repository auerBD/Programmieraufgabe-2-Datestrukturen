import numpy as np
import sys
import time

sys.setrecursionlimit(500000)

def insertion_sort(arr: np.ndarray) -> np.ndarray:
	# outer loop: starts at index 1, since a single element is always sorted
	for i in range(1, len(arr)):
		key = arr[i]  # pick up the current element to be inserted at the right position
		j = i - 1     # j points to the last element of the already sorted portion
 
		# inner loop: as long as there are larger elements to the left,
		# shift them one position to the right to make room
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]  # shift element one position to the right
			j -= 1               # move one step further to the left
 
		# gap found: insert key at the correct position
		arr[j + 1] = key
 
	return arr


def selection_sort(arr: np.ndarray) -> np.ndarray:
	n = len(arr)
	for i in range(n):
		# search for the index of the minimum in the unsorted part of the array
		min_idx = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
 
		# switch minimum with the first unsorted element
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
 
	return arr
 
 
def _merge_sort_helper(arr: np.ndarray) -> np.ndarray:
	# your implementation goes here
	# you may want to look up the operator // as in 
	# mid = len(arr) // 2

	result = np.empty(len(arr), dtype=arr.dtype)
	# ...
	return result


def merge_sort(arr: np.ndarray) -> np.ndarray:
	arr[:] = _merge_sort_helper(arr)
	return arr


def quick_sort(arr: np.ndarray) -> np.ndarray:
	def _quick_sort_helper(arr, low, high):
		if low < high:
			pivot_idx = partition(arr, low, high)
			_quick_sort_helper(arr, low, pivot_idx - 1)
			_quick_sort_helper(arr, pivot_idx + 1, high)

	def partition(arr, low, high):
		pivot = arr[high]
		i = low - 1
		for j in range(low, high):
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i + 1], arr[high] = arr[high], arr[i + 1]
		return i + 1

	if len(arr) > 1:
		_quick_sort_helper(arr, 0, len(arr) - 1)
	return arr


def _is_non_decreasing(arr: np.ndarray) -> bool:
	if len(arr) < 2:
		return True
	return bool(np.all(arr[:-1] <= arr[1:]))


def run_basic_verification_tests() -> None:
	tests = [
		[5, 2, 4, 6, 1, 3],
		[1, 2, 3],
		[3, 2, 1],
		[2, 2, 1, 1],
		[],
		[7],
	]

	sort_fns = [insertion_sort, selection_sort, merge_sort, quick_sort]
	for sort_fn in sort_fns:
		for test in tests:
			arr = np.array(test)
			out = sort_fn(arr)
			if out is not arr:
				raise AssertionError(f"{sort_fn.__name__} should return the same array object")
			if not _is_non_decreasing(arr):
				raise AssertionError(f"{sort_fn.__name__}: array is not sorted: {arr}")

	print("basic verification tests: PASSED")


if __name__ == "__main__":
	# turn on basic verification tests once you expect them to pass 
	#run_basic_verification_tests() # <---- uncomment this to start the tests

	rng = np.random.default_rng(42)
	lengths = [10, 100, 1000, 10000, 50000, 200000]
	quadratic_max_length = 10000
	sort_fns = [insertion_sort, selection_sort, merge_sort, quick_sort]

	for length in lengths:
		increasing = np.arange(length)
		decreasing = np.arange(length, 0, -1)
		random = np.arange(length)
		rng.shuffle(random)

		print(f"length={length}")
		for sort_fn in sort_fns:
			if sort_fn in (insertion_sort, selection_sort) and length >= quadratic_max_length:
				continue
			for name, base_arr in [("increasing", increasing), ("decreasing", decreasing), ("random", random)]:
				arr = base_arr.copy()
				start = time.perf_counter()
				sort_fn(arr)
				elapsed = time.perf_counter() - start
				is_sorted = _is_non_decreasing(arr)

				print(
					f"sort={sort_fn.__name__} | name={name} | runtime={elapsed:.8f} s | sorted={is_sorted}"
				)
