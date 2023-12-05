/*
A for Rock             X for Rock
B for Paper            Y for Paper
C for Scissors         Z for Scissors
score:

  - 1 for rock
  - 2 for paper
  - 3 for scissors
  - 0 for loss
  - 3 for draw
  - 6 for win
*/
package Day2

import (
	"AdventOfCode/Utils"
	"bufio"
	"fmt"
	"strings"
)

 func Part1() int {
	reader := Utils.CreateScanner("input.txt", 2)
	reader.Split(bufio.ScanLines)
	totalScore := 0
	for reader.Scan() {
		text := reader.Text()
		plays := strings.Split(text, " ")
		opponentPlay, errOpp := getPlayFromChar(plays[0])
		yourPlay, errYou := getPlayFromChar(plays[1])
		if (errOpp != nil) {
			fmt.Println(errOpp)
		}
		if (errYou != nil) {
			fmt.Println(errYou)
		}
		totalScore += roundScore(opponentPlay, yourPlay)
	}
	return totalScore
}