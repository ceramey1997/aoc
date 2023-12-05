package Utils

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)


func CreateScanner(fileName string, day int) *bufio.Scanner {
	filePath := GetFullPath(fileName, day)
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Print(err)
	}
	return bufio.NewScanner(file)
}

func GetFullPath(fileName string, day int) string {
	path, err := filepath.Abs(".")
	if (err != nil) {
		fmt.Println(err)
	}
	return fmt.Sprintf("%s\\Day%s\\%s", path,strconv.Itoa(day), fileName)
}

func GetLines(fileName string, day int) []string {
	var lines []string
	scanner := CreateScanner(fileName, day)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func GetStringRows(lines []string) [][]string {

	var rows [][]string
	for _, line := range lines {
		rows = append(rows, strings.Split(line, ""))
	}
	return rows
}

func GetIntRows(lines []string) [][]int {
	var rows [][]string
	for _, line := range lines {
		rows = append(rows, strings.Split(line, ""))
	}
	var intRows [][]int
	var iRow []int
	for _, l := range lines {
		sRow := strings.Split(l, "")
		for _, item := range sRow {
			i, _ := strconv.Atoi(item)
			iRow = append(iRow, i)
			
		}
		intRows = append(intRows, iRow)
		iRow = []int{}
	}
	return intRows
}

func GetColumns(fileName string, day int) [][]int {
	lines := GetLines(fileName, day)
	rows := GetIntRows(lines)
	var columns [][]int
	var column []int
	for i:=0; i<len(rows); i++ {
		for j:=0; j<len(rows); j++ {
			column = append(column, rows[j][i])
		}
		columns = append(columns, column)
		column = []int{}
	}
	return columns
}

func Contains[T string | int](slice []T, searchElement T) bool {
	for _, ele := range slice {
		if (ele == searchElement) {
			return true
		}
	}
	return false
}