fn solve_1(input: &str) -> u32 {
    let mut pos = 50;
    let mut zeros = 0;

    for line in input.lines() {
        let distance: u32 = line[1..].parse().unwrap();
        match line.as_bytes()[0] {
            b'L' => pos = (pos + (100 - distance % 100)) % 100,
            b'R' => pos = (pos + distance) % 100,
            _ => unreachable!(),
        }

        zeros += (pos == 0) as u32;
    }
    zeros
}

fn solve_2(input: &str) -> u32 {
    let mut pos = 50;
    let mut zeros = 0;

    for line in input.lines() {
        let distance: u32 = line[1..].parse().unwrap();
        match line.as_bytes()[0] {
            b'L' => {
                zeros += ((100 - pos) % 100 + distance) / 100;
                pos = (pos + (100 - distance % 100)) % 100;
            }
            b'R' => {
                zeros += (pos + distance) / 100;
                pos = (pos + distance) % 100;
            }
            _ => unreachable!(),
        }
    }
    zeros
}

fn main() {
    let input = include_str!("../input.txt");
    println!("{}", solve_1(input));
    println!("{}", solve_2(input));
}

#[test]
fn test_input() {
    let input: &str = "L68
L30
R48
L5
R60
L55
L1
L99
R14
L82";

    assert_eq!(solve_1(input), 3);
    assert_eq!(solve_2(input), 6);

    assert_eq!(solve_1(include_str!("../input.txt")), 980);
    assert_eq!(solve_2(include_str!("../input.txt")), 5961);
}
