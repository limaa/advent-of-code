use regex::Regex;

const DO: &str = r"do\(\)";
const DONT: &str = r"don't\(\)";
const MUL: &str = r"mul\((\d{1,3}),(\d{1,3})\)";

fn solve_1(input: &str) -> u64 {
    let re = Regex::new(MUL).unwrap();
    re.captures_iter(input)
        .map(|caps| caps.extract())
        .map(|(_, [a, b])| a.parse::<u64>().unwrap() * b.parse::<u64>().unwrap())
        .sum()
}

fn solve_2(input: &str) -> u64 {
    let re = Regex::new(&format!("{DO}|{DONT}|{MUL}")).unwrap();
    let (_, acc) = re
        .captures_iter(input)
        .fold((true, 0), |(mul_enabled, acc), captures| {
            let instruction = &captures[0];
            match instruction {
                "do()" => (true, acc),
                "don't()" => (false, acc),
                _ => {
                    if mul_enabled {
                        let a = &captures[1].parse::<u64>().unwrap();
                        let b = &captures[2].parse::<u64>().unwrap();
                        (mul_enabled, acc + a * b)
                    } else {
                        (mul_enabled, acc)
                    }
                }
            }
        });
    acc
}

fn main() {
    let input = include_str!("../input.txt");
    println!("{}", solve_1(input));
    println!("{}", solve_2(input));
}

#[test]
fn test_input() {
    let input: &str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
    assert_eq!(solve_1(input), 161);

    let input: &str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";
    assert_eq!(solve_2(input), 48);

    assert_eq!(solve_1(include_str!("../input.txt")), 166630675);
    assert_eq!(solve_2(include_str!("../input.txt")), 93465710);
}
