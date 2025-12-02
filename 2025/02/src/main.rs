// Using modulo trick from:
//  <https://github.com/MizardX/AdventOfCode_2025/blob/main/src/day_02.rs>
//  <https://github.com/timvisee/advent-of-code-2025/blob/master/day02a/src/main.rs>

fn parse(input: &[u8]) -> impl Iterator<Item = usize> {
    input
        .split(|x| x == &b',')
        .map(|x| {
            let mut iter = x
                .splitn(2, |x| x == &b'-')
                .map(|x| atoi::atoi::<usize>(x).unwrap());
            (iter.next().unwrap(), iter.next().unwrap())
        })
        .flat_map(|(a, b)| a..=b)
}

fn solve_1(input: &[u8]) -> usize {
    parse(input)
        .filter(|x| match x {
            10..=99 => x % 11 == 0,
            1_000..=9_999 => x % 101 == 0,
            100_000..=999_999 => x % 1_001 == 0,
            10_000_000..=99_999_999 => x % 10_001 == 0,
            1_000_000_000..=9_999_999_999 => x % 100_001 == 0,
            _ => false,
        })
        .sum()
}

fn solve_2(input: &[u8]) -> usize {
    parse(input)
        .filter(|x| match x {
            10..=99 => x % 11 == 0,
            100..=999 => x % 111 == 0,
            1_000..=9_999 => x % 101 == 0 || x % 1_111 == 0,
            10_000..=99_999 => x % 11_111 == 0,
            100_000..=999_999 => x % 1_001 == 0 || x % 10_101 == 0 || x % 111_111 == 0,
            1_000_000..=9_999_999 => x % 1_111_111 == 0,
            10_000_000..=99_999_999 => x % 10_001 == 0 || x % 1_010_101 == 0 || x % 11_111_111 == 0,
            100_000_000..=999_999_999 => x % 1_001_001 == 0 || x % 111_111_111 == 0,
            1_000_000_000..=9_999_999_999 => {
                x % 100_001 == 0 || x % 101_010_101 == 0 || x % 1_111_111_111 == 0
            }
            _ => false,
        })
        .sum()
}

fn main() {
    let input = include_bytes!("../input.txt");
    println!("{}", solve_1(input));
    println!("{}", solve_2(input));
}

#[test]
fn test_input() {
    let input: &[u8] = b"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";

    assert_eq!(solve_1(input), 1227775554);
    assert_eq!(solve_2(input), 4174379265);

    assert_eq!(solve_1(include_bytes!("../input.txt")), 30608905813);
    assert_eq!(solve_2(include_bytes!("../input.txt")), 31898925685);
}
