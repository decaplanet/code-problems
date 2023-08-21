const TEST_CASES: [(&[i32], i32, &[i32]); 11] = [
    (&[2, 1, 2, 2, 2, 3, 4, 2], 2, &[4, 1, 3, 2, 2, 2, 2, 2]),
    (&[], 3, &[]),
    (&[1, 2, 4, 5, 6], 3, &[1, 2, 4, 5, 6]),
    (&[3, 3, 3, 3, 3], 3, &[3, 3, 3, 3, 3]),
    (&[3, 1, 2, 4, 5], 3, &[5, 1, 2, 4, 3]),
    (&[1, 2, 4, 5, 3], 3, &[1, 2, 4, 5, 3]),
    (&[1, 2, 3, 4, 5], 3, &[1, 2, 5, 4, 3]),
    (&[2, 4, 2, 5, 6, 2, 2], 2, &[6, 4, 5, 2, 2, 2, 2]),
    (
        &[5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12],
        5,
        &[12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 6, 5, 5, 5, 5, 5, 5],
    ),
    (
        &[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5],
        5,
        &[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5],
    ),
    (
        &[5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12],
        5,
        &[12, 1, 2, 11, 10, 3, 4, 6, 7, 9, 8, 5, 5, 5, 5, 5, 5],
    ),
];

fn main() {
    for (array, to_move, answer) in TEST_CASES {
        let mut array = array.to_vec();
        let result = move_element_to_end(&mut array, to_move);
        assert_eq!(result, answer);
    }

    println!("Yay, your code passed all the test cases!");
}

fn move_element_to_end(array: &mut Vec<i32>, to_move: i32) -> &mut Vec<i32> {
    if array.is_empty() {
        return array;
    }

    let mut i = 0;
    let mut j = array.len() - 1;

    while i < j {
        while i < j && array[j] == to_move {
            j -= 1
        }

        if array[i] == to_move {
            let (element_i, element_j) = (array[i], array[j]);
            array[i] = element_j;
            array[j] = element_i;
        }

        i += 1
    }

    array
}
