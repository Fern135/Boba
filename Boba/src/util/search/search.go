package search

import "math"

// ==================== Linear Search ====================
func linearSearch(arr []int, target int) int {
	for i, val := range arr {
		if val == target {
			return i
		}
	}
	return -1
}

// ==================== Binary Search ====================
func binarySearch(arr []int, target int) int {
	low, high := 0, len(arr)-1

	for low <= high {
		mid := low + (high-low)/2

		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1
}

// ==================== Jump Search ====================
func jumpSearch(arr []int, target int) int {
	n := len(arr)
	step := int(math.Sqrt(float64(n)))
	prev := 0

	for arr[min(step, n)-1] < target {
		prev = step
		step += int(math.Sqrt(float64(n)))
		if prev >= n {
			return -1
		}
	}

	for arr[prev] < target {
		prev++
		if prev == min(step, n) {
			return -1
		}
	}

	if arr[prev] == target {
		return prev
	}

	return -1
}

// ==================== Interpolation Search ====================
func interpolationSearch(arr []int, target int) int {
	low, high := 0, len(arr)-1

	for low <= high && target >= arr[low] && target <= arr[high] {
		pos := low + ((target - arr[low]) * (high - low) / (arr[high] - arr[low]))

		if arr[pos] == target {
			return pos
		}

		if arr[pos] < target {
			low = pos + 1
		} else {
			high = pos - 1
		}
	}

	return -1
}

// ==================== Utility Functions ====================
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
