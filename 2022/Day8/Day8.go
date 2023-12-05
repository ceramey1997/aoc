package Day8

import (
	"AdventOfCode/Utils"
)

func GetRowsAndColumns(fileName string) ([][]int, [][]int) {
	lines := Utils.GetLines(fileName, 8)
	rows := Utils.GetIntRows(lines)
	columns := Utils.GetColumns(fileName, 8)
	return rows, columns
}

func Parts(inputFile string) (int, int) {
	rows, columns := GetRowsAndColumns(inputFile)
	visable := 0
	mostVisable := 0
	for row:=0;row<len(rows); row++ {
		for column:=0;column<len(rows[row]); column++ {
			tree := CreateTree(CreateCoordinate(row, column), rows[row], columns[column])
			if (tree.visability.outerVisability == true) {
				visable++
			}
			if (tree.scenicScore > mostVisable) {
				mostVisable = tree.scenicScore
			}
		}
	}
	return visable, mostVisable
}