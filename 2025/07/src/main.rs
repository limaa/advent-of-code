use std::collections::{HashMap, HashSet};

fn solve_1(input: &[u8]) -> usize {
    let lines: Vec<&[u8]> = input.split(|x| x == &b'\n').collect();

    let width = lines[0].len();
    let height = lines.len();

    let mut beams = HashSet::new();
    let mut split = 0;

    for x in 0..width {
        if lines[0][x] == b'S' {
            beams.insert(x);
        }
    }
    assert_eq!(beams.len(), 1);

    for y in 1..height {
        for x in 0..width {
            if lines[y][x] == b'^' && beams.contains(&x) {
                split += 1;
                beams.insert(x - 1);
                beams.remove(&x);
                beams.insert(x + 1);
            }
        }
    }
    split
}

fn solve_2(input: &[u8]) -> usize {
    let lines: Vec<&[u8]> = input.split(|x| x == &b'\n').collect();

    let width = lines[0].len();
    let height = lines.len();

    let mut beams = HashMap::new();

    for x in 0..width {
        if lines[0][x] == b'S' {
            beams.insert(x, 1);
        }
    }
    assert_eq!(beams.len(), 1);

    for y in 1..height {
        for x in 0..width {
            if lines[y][x] == b'^' && beams.contains_key(&x) {
                let timelines = beams.remove(&x).unwrap();
                *beams.entry(x - 1).or_default() += timelines;
                *beams.entry(x + 1).or_default() += timelines;
            }
        }
    }

    beams.drain().map(|(_, v)| v).sum()
}

fn main() {
    let input = include_bytes!("../input.txt");
    println!("{}", solve_1(input));
    println!("{}", solve_2(input));
}

#[test]
fn test_input() {
    let input: &[u8] = b".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............";

    assert_eq!(solve_1(input), 21);
    assert_eq!(solve_2(input), 40);

    assert_eq!(solve_1(include_bytes!("../input.txt")), 1539);
    assert_eq!(solve_2(include_bytes!("../input.txt")), 6479180385864);
}
