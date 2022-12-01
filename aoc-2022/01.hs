import Data.List (sort)
import Data.List.Split (splitOn)

solution n = sum . take n . reverse . sort . map (sum . map read) . splitOn [""] . lines

main = do
  contents <- readFile "01.txt"
  print $ map ($ contents) [solution 1, solution 3]
