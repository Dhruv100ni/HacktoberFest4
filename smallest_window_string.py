# Function to check if the substring contains all
# characters of the pattern


def containsAllCharacters(substr, pattern):
	count = [0] * 256

	# Count the frequency of each character in the pattern
	for ch in pattern:
		count[ord(ch)] += 1

	# For each character in the substring, decrement its count
	for ch in substr:
		if count[ord(ch)] > 0:
			count[ord(ch)] -= 1

	# If all counts in the count array are zero, the
	# substring contains all characters of the pattern
	for i in range(256):
		if count[i] > 0:
			return False

	return True

# Function to find the smallest substring containing all
# characters of the pattern


def findSmallestSubstring(s, pattern):
	len_str = len(s)
	len_pattern = len(pattern)
	smallestSubstring = ""

	minLength = float('inf')

	# Generate all substrings of the given string
	for i in range(len_str):
		for j in range(i, len_str):
			substr = s[i:j+1]

			# Check if the substring contains all
			# characters of the pattern
			if containsAllCharacters(substr, pattern):
				currentLength = len(substr)

				# Update the smallestSubstring if the
				# current substring is smaller
				if currentLength < minLength:
					minLength = currentLength
					smallestSubstring = substr

	return smallestSubstring


if __name__ == "__main__":
	str1 = "this is a test string"
	pattern1 = "tist"
	print("Input: string = \"" + str1 + "\", pattern = \"" + pattern1 + "\"")
	print("Output: \"" + findSmallestSubstring(str1, pattern1) + "\"")

	str2 = "geeksforgeeks"
	pattern2 = "ork"
	print("Input: string = \"" + str2 + "\", pattern = \"" + pattern2 + "\"")
	print("Output: \"" + findSmallestSubstring(str2, pattern2) + "\"")
