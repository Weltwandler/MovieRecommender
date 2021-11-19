# Note: This implementation of the classic heapsort algorithm is specifically designed for elements that are all objects of the Movie class.
# It will compare the rating of each element instead of the element itself, and would create errors if it were used with other kinds of elements.

class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0
    
    # Helper methods
    def parent_idx(self, idx):
        return idx // 2
    
    def left_child_idx(self, idx):
        return idx * 2
    
    def right_child_idx(self, idx):
        return idx * 2 + 1
    
    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count
    
    # Method for adding a new element to the heap
    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()
    
    # Method to re-sort the heap from the end (once a new element has been added)
    def heapify_up(self):
        idx = self.count
        # Go through the list until there is no more parent element
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            # If the rating of the parent-movie is higher than that of the child-movie, swap places
            if parent.rating > child.rating:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            # Move on to the parent of the current element
            idx = self.parent_idx(idx)
    
    # Method to retrieve the highest-rated element
    def retrieve_max(self):
        if self.count == 0:
            return None
        # Store the current highest-rated movie in a separate variable
        max_value = self.heap_list[1]
        # Replace the top of the list with the last entry on the list, then shorten the list and re-sort
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return max_value

    # Method to re-sort the list from the start (after the highest-rated movie has been removed)
    def heapify_down(self):
        idx = 1
        # Keep going through the list until there are no more child elements
        while self.child_present(idx):
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
            # If the rating of the parent element is smaller than that of the child element, swp them
            if parent.rating < child.rating:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            # Move on to the largest child element
            idx = larger_child_idx
    
    # Method to get the largest child of an element at a given index
    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            # This case means there is no right child - return the left child index
            return self.left_child_idx(idx)
        else:
            # If there are two child elements, check which is larger and return that index
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child.rating > right_child.rating:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

