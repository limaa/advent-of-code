fn parse(input: &[u8]) -> impl Iterator<Item = usize> {
    input
        .split(|x| x == &b',')
        .map(|x| {
            let mut iter = x
                .splitn(2, |x| x == &b'-')
                .map(|x| str::from_utf8(x).unwrap().parse().unwrap());
            (iter.next().unwrap(), iter.next().unwrap())
        })
        .flat_map(|(a, b)| a..=b)
}

fn solve_1(input: &[u8]) -> usize {
    parse(input)
        .filter(|x| {
            let x = format!("{x}");
            if x.len() % 2 != 0 {
                return false;
            }

            let (a, b) = x.split_at(x.len() / 2);
            a == b
        })
        .sum()
}

fn solve_2(input: &[u8]) -> usize {
    parse(input)
        .filter(|x| {
            let x = format!("{x}");
            (1..=x.len() / 2)
                .map(|idx| {
                    if x.len() % idx != 0 {
                        return false;
                    }

                    x == x[0..idx].repeat(x.len() / idx)
                })
                .any(|x| x)
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
