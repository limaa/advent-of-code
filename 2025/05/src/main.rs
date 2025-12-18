fn solve_1(input: &[u8]) -> usize {
    let mut lines = input.split(|b| b == &b'\n');

    let fresh: Vec<_> = lines
        .by_ref()
        .take_while(|b| !b.is_empty())
        .map(|range| range.split_at(range.iter().position(|b| b == &b'-').unwrap()))
        .map(|(a, b)| {
            (
                atoi::atoi::<usize>(a).unwrap(),
                atoi::atoi::<usize>(&b[1..]).unwrap(),
            )
        })
        .map(|(a, b)| a..=b)
        .collect();

    lines
        .map(|l| atoi::atoi::<usize>(l).unwrap())
        .filter(|n| fresh.iter().any(|r| r.contains(n)))
        .count()
}

fn solve_2(input: &[u8]) -> usize {
    let mut ranges: Vec<_> = input
        .split(|b| b == &b'\n')
        .take_while(|b| !b.is_empty())
        .map(|range| range.split_at(range.iter().position(|b| b == &b'-').unwrap()))
        .map(|(a, b)| {
            (
                atoi::atoi::<usize>(a).unwrap(),
                atoi::atoi::<usize>(&b[1..]).unwrap(),
            )
        })
        .collect();

    ranges.sort_by_key(|&(a, _)| a);

    let (ingredients, (a, b)) =
        ranges
            .iter()
            .fold((0, (0, 0)), |(ingredients, (prev_a, prev_b)), &(a, b)| {
                if prev_a <= a && a <= prev_b {
                    return (ingredients, (prev_a, b.max(prev_b)));
                } else {
                    return (ingredients + (prev_b - prev_a + 1), (a, b));
                }
            });

    return ingredients + (b - a);
}

fn main() {
    let input = include_bytes!("../input.txt");
    println!("{}", solve_1(input));
    println!("{}", solve_2(input));
}

#[test]
fn test_input() {
    let input: &[u8] = b"3-5
10-14
16-20
12-18

1
5
8
11
17
32";

    assert_eq!(solve_1(input), 3);
    assert_eq!(solve_2(input), 14);

    assert_eq!(solve_1(include_bytes!("../input.txt")), 567);
    assert_eq!(solve_2(include_bytes!("../input.txt")), 354149806372909);
}
