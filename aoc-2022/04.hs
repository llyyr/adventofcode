import Data.List
import Data.List.Split (splitOn)

parse :: String -> [[[Int]]]
parse = map (map pair . splitOn ",") . lines
    where
        interval [a, b] = [read a .. read b]
        pair = interval . splitOn "-"

subset :: [[Int]] -> Bool
subset l = foldl1 intersect l `elem` l

overlap :: [[Int]] -> Bool
overlap = not . null . foldl1 intersect

main = do
    inp <- parse <$> readFile "04.txt"
    print $ length . filter (== True) $ map subset inp
    print $ length . filter (== True) $ map overlap inp
