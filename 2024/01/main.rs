fn parse(input: &str) -> (Vec<u32>, Vec<u32>) {
    let mut first_list: Vec<u32> = vec![];
    let mut second_list: Vec<u32> = vec![];

    for l in input.lines() {
        let (a, b) = l.split_once(' ').expect("whitespace");

        first_list.push(a.parse().expect("parse 'first'"));
        second_list.push(b.trim().parse().expect("parse 'second'"));
    }

    (first_list, second_list)
}

fn solve_1(input: &str) -> u32 {
    let (mut first_list, mut second_list) = parse(input);

    first_list.sort();
    second_list.sort();

    std::iter::zip(first_list, second_list)
        .map(|(a, b)| a.abs_diff(b))
        .sum()
}

fn solve_2(input: &str) -> u32 {
    let (first_list, second_list) = parse(input);
    first_list
        .iter()
        .map(|&a| a * second_list.iter().filter(|&x| *x == a).count() as u32)
        .sum()
}

fn main() {
    let input = include_str!("input.txt");
    println!("{}", solve_1(input));
    println!("{}", solve_2(input));
}

#[test]
fn test_input() {
    const INPUT: &str = "3   4
4   3
2   5
1   3
3   9
3   3";

    assert_eq!(solve_1(INPUT), 11);
    assert_eq!(solve_2(INPUT), 31);

    assert_eq!(solve_1(include_str!("input.txt")), 2904518);
    assert_eq!(solve_2(include_str!("input.txt")), 18650129);
}
