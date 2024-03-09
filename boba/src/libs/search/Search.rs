pub struct Search<T> {
    data: Vec<T>,
}

impl<T: PartialOrd> Search<T> {
    pub fn new(data: Vec<T>) -> Self {
        Search { data }
    }

    /// Linear search algorithm.
    /// Time complexity: O(n)
    pub fn linear_search(&self, target: &T) -> Option<usize> {
        for (index, item) in self.data.iter().enumerate() {
            if item == target {
                return Some(index);
            }
        }
        None
    }

    /// Binary search algorithm.
    /// Requires sorted data.
    /// Time complexity: O(log n)
    pub fn binary_search(&self, target: &T) -> Option<usize> {
        let mut low = 0;
        let mut high = self.data.len() - 1;

        while low <= high {
            let mid = (low + high) / 2;
            if &self.data[mid] == target {
                return Some(mid);
            } else if &self.data[mid] < target {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        None
    }

}

/*
fn main() {
    Create a vector of integers
    let data = vec![1, 3, 5, 7, 9, 11, 13, 15];

    Create a Search instance with the vector
    let search = Search::new(data);

    Perform linear search
    let target_linear = 7;
    match search.linear_search(&target_linear) {
        Some(index) => println!("Linear search: Target {} found at index {}", target_linear, index),
        None => println!("Linear search: Target {} not found", target_linear),
    }

    Perform binary search
    let target_binary = 11;
    match search.binary_search(&target_binary) {
        Some(index) => println!("Binary search: Target {} found at index {}", target_binary, index),
        None => println!("Binary search: Target {} not found", target_binary),
    }

    Perform interpolation search
    let target_interpolation = 15;
    match search.interpolation_search(&target_interpolation) {
        Some(index) => println!("Interpolation search: Target {} found at index {}", target_interpolation, index),
        None => println!("Interpolation search: Target {} not found", target_interpolation),
    }
}

*/