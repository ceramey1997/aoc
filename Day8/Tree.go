package Day8

type ITree interface {
	IsVisableUp() bool
	IsVisableDown() bool
	IsVisableLeft() bool
	IsVisableRight() bool
}

type Tree struct {
	height int
	visability Visability
	scenicScore int
}

type Visability struct {
	left Direction
	right Direction
	up Direction
	down Direction
	outerVisability bool
}

type Direction struct {
	outerVisable bool
	numberOut int
}

type Coordinate struct {
	rowNumber int
	idxInRow int
	idxInCol int
}

func CreateDirection(outerVisable bool, numOut int) Direction {
	return Direction{ outerVisable: outerVisable, numberOut: numOut }
}

func CreateCoordinate(r int, c int) Coordinate{
	return Coordinate{ rowNumber: r, idxInRow: c, idxInCol: r }
}

func createVisability(up Direction, down Direction, left Direction, right Direction, outerVisability bool) Visability {
	return Visability{left, right, up, down, outerVisability}
}

func CreateTree(cords Coordinate, row []int, column []int) Tree {
	var height int
	height = row[cords.idxInRow]
	vis := GetVisability(height, cords, row, column)
	scenicScore := vis.GetScenicScore()
	return Tree{ height: height, visability: vis, scenicScore: scenicScore}
}

func GetVisability(height int, cords Coordinate, row []int, column []int) Visability {
	up := VisableUp(height, cords, column)
	down := VisableDown(height, cords, column, row)
	left := VisableLeft(height, cords, row)
	right := VisableRight(height,cords, row)
	outerVisability := false
	if (up.outerVisable || down.outerVisable || left.outerVisable || right.outerVisable) {
		outerVisability = true
	}
	return createVisability(up, down, left, right, outerVisability)
}

func VisableUp(height int, cord Coordinate, column []int) Direction {
	var n int = 0
	if (cord.rowNumber == 0) {
		return CreateDirection(true, n)
	}
	
	for i:=cord.idxInCol-1;i>=0;i-- {
		if (column[i] >= height) {
			n++
			return CreateDirection(false, n)
		}
		n++
	}
	return CreateDirection(true, n)
}

func VisableDown(height int, cord Coordinate, column []int, row []int) Direction {
	n := 0
	if (cord.rowNumber == len(row)-1) {
		return CreateDirection(true, n)
	}
	for i:=cord.idxInCol+1;i<len(column);i++ {
		if (column[i] >= height) {
			n++
			return CreateDirection(false, n)
		}
		n++
	}
	return CreateDirection(true, n)
}

func VisableLeft(height int, cord Coordinate, row []int) Direction {
	n := 0
	if (cord.idxInRow == 0) {
		return CreateDirection(true, n)
	}
	for i:=cord.idxInRow-1;i>=0;i-- {
		if (row[i] >= height) {
			n++
			return CreateDirection(false, n)
		}
		n++
	}
	return CreateDirection(true, n)
}

func VisableRight(height int, cord Coordinate, row []int) Direction {
	n := 0
	if (cord.idxInRow == len(row) - 1) {
		return CreateDirection(true, n)
	}
	for i:=cord.idxInRow+1;i<len(row);i++ {
		if (row[i] >= height) {
			n++
			return CreateDirection(false, n)
		}
		n++
	}
	return CreateDirection(true, n)
}

func (v Visability) GetScenicScore() int {
	return v.up.numberOut *
		   v.left.numberOut *
		   v.down.numberOut *
		   v.right.numberOut
}