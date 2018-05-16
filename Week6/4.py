def overlap(list1, list2):
	"""
	Function which accepts two lists and finds the union of the elements in the list, where the
	union are all unique values.  

	:param list1: list of elements
	:param list1: list of elements

	:return: a list containing the union of the elements
	"""

	set1 = set(list1)
	set2 = set(list2)
	overlap_list = []

	for x in set1:
		if x in set2:
			overlap_list.append(x)

	return overlap_list