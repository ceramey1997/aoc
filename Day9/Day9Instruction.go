package Day9

import (
	"errors"
	"math"
	"strconv"
)

const (
	RIGHT Direction9  = "R"
	LEFT Direction9 = "L"
	UP Direction9 = "U"
	DOWN Direction9 = "D"
)

type Coordinate struct {
	X int
	Y int
}

type Direction9 string

type Day9Instruction struct {
	direction Direction9
	moveUnits int
}


func CreateDay9Instruction(dir string, units string) (Day9Instruction, error) {
	d, err := getDirection9FromString(dir)
	if (err != nil) {
		return Day9Instruction{}, err
	}
	u, err2 := strconv.Atoi(units)
	if (err != nil) {
		return Day9Instruction{}, err2
	}
	return Day9Instruction{ direction: d, moveUnits: u}, nil
}

func getDirection9FromString(dir string) (Direction9, error) {
	switch dir {
	case "R":
		return RIGHT, nil
	case "L":
		return LEFT, nil
	case "U":
		return UP, nil
	case "D":
		return DOWN, nil
	default:
		return UP, errors.New("error, direction not in expected range")
	}
}

func (direction Day9Instruction) Execute(startCoordHead Coordinate, startCoordTail Coordinate) ([]Coordinate, []Coordinate) {
	currentCordHead := startCoordHead
	currentCordTail := startCoordTail
	var visitedHead []Coordinate 
	var visitedTail []Coordinate
	for i:=0; i<direction.moveUnits; i++ {
		headCord := direction.executeSingleMove(currentCordHead)
		visitedHead = append(visitedHead, headCord)
		currentCordHead = headCord

		tailCord := direction.follow(currentCordHead, currentCordTail)
		visitedTail = append(visitedTail, tailCord)
		currentCordTail = tailCord
	}
	return visitedHead, visitedTail
}

func (dir Day9Instruction) follow(headCurrentCord Coordinate, tailCurrentCord Coordinate) Coordinate {
	dX := headCurrentCord.X - tailCurrentCord.X
	dY := headCurrentCord.Y - tailCurrentCord.Y
	hypot := math.Sqrt(
		(float64(dX) * float64(dX)) +
		(float64(dY) * float64(dY)))
	if (hypot > 2) {
		tailCurrentCord.X += sign(dX)
		tailCurrentCord.Y += sign(dY)
	} else if (math.Abs(float64(dX)) == 2) {
		tailCurrentCord.X += sign(dX)
	} else if (math.Abs(float64(dY)) == 2) {
		tailCurrentCord.Y += sign(dY)
	}
	return tailCurrentCord
}

func sign(x int) int {
	if (x > 0) {
		return 1
	}
	return -1
}

func (dir Day9Instruction) executeSingleMove(startCordHead Coordinate) Coordinate {
	switch dir.direction {
	case RIGHT:
		startCordHead.X++
	case LEFT:
		startCordHead.X--
	case UP:
		startCordHead.Y++
	case DOWN:
		startCordHead.Y--
	}
	return startCordHead
}