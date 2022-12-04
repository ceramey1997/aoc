package Utils

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
)

func CreateScanner(fileName string, day int) *bufio.Scanner {
	filePath := getFullPath(fileName, day)
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Print(err)
	}
	return bufio.NewScanner(file)
}

func getFullPath(fileName string, day int) string {
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

func Contains[T string | int](slice []T, searchElement T) bool {
	for _, ele := range slice {
		if (ele == searchElement) {
			return true
		}
	}
	return false
}