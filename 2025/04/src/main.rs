fn accessible_rolls(grid: &Vec<Vec<u8>>) -> Vec<(usize, usize)> {
    let width = grid[0].len();
    let height = grid.len();

    let mut rolls = Vec::new();

    for x in 0..width {
        for y in 0..height {
            if grid[y][x] != b'@' {
                continue;
            }

            const OFFSETS: [(isize, isize); 8] = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ];

            let adjacent_rolls = OFFSETS
                .into_iter()
                .map(|(offset_x, offset_y)| (x as isize + offset_x, y as isize + offset_y))
                .filter(|&(pos_x, pos_y)| {
                    0 <= pos_x && pos_x < width as isize && 0 <= pos_y && pos_y < height as isize
                })
                .filter(|&(pos_x, pos_y)| grid[pos_y as usize][pos_x as usize] == b'@')
                .count();

            if adjacent_rolls < 4 {
                rolls.push((x, y));
            }
        }
    }
    rolls
}

fn solve_1(input: &[u8]) -> usize {
    let grid: Vec<Vec<u8>> = input
        .split(|b| b == &b'\n')
        .map(|row| row.to_vec())
        .collect();
    accessible_rolls(&grid).len()
}

fn solve_2(input: &[u8]) -> usize {
    let mut grid: Vec<Vec<u8>> = input
        .split(|b| b == &b'\n')
        .map(|row| row.to_vec())
        .collect();

    let mut rolls_removed = 0;
    loop {
        let accessible = accessible_rolls(&grid);
        rolls_removed += accessible.len();
        accessible.iter().for_each(|&(x, y)| {
            grid[y][x] = b'.';
        });

        if accessible.len() <= 0 {
            break;
        }
    }
    rolls_removed
}

fn main() {
    let input = include_bytes!("../input.txt");
    println!("{}", solve_1(input));
    println!("{}", solve_2(input));
}

#[test]
fn test_input() {
    let input: &[u8] = b"..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.";

    assert_eq!(solve_1(input), 13);
    assert_eq!(solve_2(input), 43);

    assert_eq!(solve_1(include_bytes!("../input.txt")), 1389);
    assert_eq!(solve_2(include_bytes!("../input.txt")), 9000);
}
