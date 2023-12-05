package Day7

import (
	"errors"
	"strconv"
	"strings"
)

type File struct {
	name string
	size int
}

func CreateFile(line string) (File, error) {
	trimmedLine := strings.TrimSpace(line)
	ll := strings.Split(trimmedLine, " ")
	size, err := strconv.Atoi(ll[0])
	if (err != nil) {
		return File{}, errors.New("file size is not an int")
	}
	name := ll[1]
	return File { name, size }, nil
}