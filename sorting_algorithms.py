#! /home/lukas/projects/python/sorting/bin/python3


class _SortingAlgorithm(object):
    def __init__(self, array: list):
        self._array = array

    def is_sorted(self) -> bool:
        for index, element in enumerate(self._array[:-1]):
            if element > self._array[index + 1]:
                return False
        return True
    
    def next(self):
        raise NotImplementedError(f"Sorting algorithm has not been implemented yet, {self.__class__} is not implemented")

    def sort(self):
        while not sort._is_sorted():
            sort.next()
        

class BubbleSort(_SortingAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self._value_index = 0
        self._loop_index = 1

    def next(self) -> None:
        if self.is_sorted():
            return

        if self._value_index >= len(self._array) - self._loop_index:
            self._value_index = 0
            self._loop_index += 1
        if self._array[self._value_index] > self._array[self._value_index + 1]:
            self._array[self._value_index], self._array[self._value_index + 1] = self._array[self._value_index + 1], self._array[self._value_index]
            
        self._value_index += 1

    @property
    def indicies(self):
        return {
            "value_index": self._value_index,
            "loop_index": self._loop_index
        }


class InsertionSort(_SortingAlgorithm):
    def __init__(self, array: list):
        super().__init__(array)
        self._value_index = 1
        self._comparison_index = 0
        self._search_place = False

    def next(self) -> None:
        if self.is_sorted():
            return

        if not self._search_place:
            if self._array[self._value_index] < self._array[self._value_index - 1]:
                self._search_place = True
                self._comparison_index = self._value_index - 1
            else:
                self._value_index += 1    
        else:
            if self._comparison_index <= 0 or (self._array[self._value_index] >= self._array[self._comparison_index]):
                self._array = self._array[:self._comparison_index + 1] + [self._array[self._value_index]] + self._array[self._comparison_index + 1: self._value_index] + self._array[self._value_index + 1:]
                self._search_place = False
            else:
                self._comparison_index -= 1
        
    @property
    def indicies(self):
        return {
            "value_index": self._value_index,
            "comparison_index": self._comparison_index
        }
    

class SelectionSort(_SortingAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self._sorting_index = 0
        self._smallest_index = 0
        self._comparison_index = 0
    
    @property
    def indicies(self):
        return {
            "sorting_index": self._sorting_index,
            "smallest_index": self._smallest_index,
            "comparison_index": self._comparison_index
        }

    def _reset_indicies(self):
        self._sorting_index += 1
        self._smallest_index = self._sorting_index
        self._comparison_index = self._sorting_index
        

    def next(self):
        if self.is_sorted():
            return
        
        if self._comparison_index < len(self._array):
            if self._array[self._smallest_index] > self._array[self._comparison_index]:
                self._smallest_index = self._comparison_index
            self._comparison_index += 1
        else:
            self._array = self._array[:self._sorting_index] + [self._array[self._smallest_index]] + self._array[self._sorting_index:self._smallest_index] + self._array[self._smallest_index + 1:]
            self._reset_indicies()


class QuickSort(_SortingAlgorithm):
    def __init__(self, array):
        super().__init__(array)











if __name__ == "__main__":
    
    def test_algorithm(algorithm):
        print(algorithm)
        sort = algorithm([1, 2, 3, 3, 2, 6, 5, 4])
        print(sort._array, sort.indicies)
        while not sort.is_sorted():
            sort.next()
            print(sort._array, sort.indicies)
        print()

    test_algorithm(BubbleSort)
    test_algorithm(InsertionSort)
    test_algorithm(SelectionSort)
    

