fn parse(input: &str) -> Vec<Vec<u32>> {
    input
        .lines()
        .map(|report| {
            report
                .split(' ')
                .map(|level| level.parse().unwrap())
                .collect()
        })
        .collect()
}

fn is_report_safe(report: &Vec<u32>) -> bool {
    let diff: Vec<i32> = report
        .windows(2)
        .map(|x| x[0] as i32 - x[1] as i32)
        .collect();

    let decreasing = diff.iter().all(|&x| x > 0);
    let increasing = diff.iter().all(|&x| x < 0);
    let between_1_and_3 = diff.iter().all(|&x| 1 <= x.abs() && x.abs() <= 3);
    (decreasing || increasing) && between_1_and_3
}

fn solve_1(input: &str) -> u32 {
    parse(input)
        .iter()
        .filter(|&report| is_report_safe(report))
        .count() as u32
}

fn solve_2(input: &str) -> u32 {
    parse(input)
        .iter()
        .filter(|&report| {
            if !is_report_safe(&report) {
                for i in 0..report.len() {
                    let mut possible_report = report.clone();
                    possible_report.remove(i);

                    if is_report_safe(&possible_report) {
                        return true;
                    }
                }
                return false;
            } else {
                return true;
            }
        })
        .count() as u32
}

fn main() {
    let input = include_str!("input.txt");
    println!("{}", solve_1(input));
    println!("{}", solve_2(input));
}

#[test]
fn test_input() {
    const INPUT: &str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";

    assert_eq!(solve_1(INPUT), 2);
    assert_eq!(solve_2(INPUT), 4);

    assert_eq!(solve_1(include_str!("input.txt")), 486);
    assert_eq!(solve_2(include_str!("input.txt")), 540);
}
