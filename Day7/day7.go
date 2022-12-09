package Day7

import (
	"AdventOfCode/Utils"
	"sort"
	"strconv"
	"strings"
)

func Part1(filename string) int64 {
	lines := Utils.GetLines(filename, 7)
	var stack []int64
	var sum int64

	for  _, line := range lines {
		switch line[:4] {
		case "$ cd":
			if path := line[5:]; path != ".." {
				stack = append(stack, 0)
				continue
			}

			dirSize := stack[len(stack)-1]
			if dirSize <= 100000 {
				sum += dirSize
			}

			if stack = stack[:len(stack)-1]; len(stack) > 0 {
				stack[len(stack)-1] += dirSize
			}
		case "$ ls", "dir ":
		default:
			fs := strings.Fields(line)
			fileSize, _ := strconv.ParseInt(fs[0], 10, 64)
			stack[len(stack)-1] += fileSize
		}
	}
	return sum
}

func Part2(filename string) int {
	lines := Utils.GetLines(filename, 7)

	var stack, sizes []int
	popd := func() {
		dirSize := stack[len(stack)-1]
		sizes = append(sizes, dirSize)
		if stack = stack[:len(stack)-1]; len(stack) > 0 {
			stack[len(stack)-1] += dirSize
		}
	}

	for _, line := range lines {
		switch line[:4] {
		case "$ cd":
			if path := line[5:]; path != ".." {
				stack = append(stack, 0)
			} else {
				popd()
			}
		case "$ ls", "dir ":
		default:
			fs := strings.Fields(line)
			fileSize, _ := strconv.Atoi(fs[0])
			stack[len(stack)-1] += fileSize
		}
	}

	for len(stack) > 0 {
		popd()
	}

	sort.Ints(sizes)

	used := sizes[len(sizes)-1]
	free := 70000000 - used

	i := sort.Search(len(sizes), func(i int) bool {
		return free+sizes[i] >= 30000000
	})
	return sizes[i]
}