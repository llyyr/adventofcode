fn main() {
    let mut inp = include_str!("./01.txt")
        .split("\n\n")
        .map(|i| {
            i.split("\n")
                .map(str::parse::<i32>)
                .filter_map(Result::ok)
                .sum::<i32>()
        })
        .collect::<Vec<i32>>();
    inp.sort();
    println!("Part 1: {}", inp.last().unwrap());
    println!("Part 2: {}", inp.iter().rev().take(3).sum::<i32>());
}
