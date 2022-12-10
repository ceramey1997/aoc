package Day9

import (
	"errors"
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
		headCord, tailCord := executeSingleMove(currentCordHead, currentCordTail, direction)
		visitedHead = append(visitedHead, headCord)
		currentCordHead = headCord
		currentCordTail = tailCord
		visitedTail = append(visitedTail, tailCord)
	}
	return visitedHead, visitedTail
}

func executeSingleMove(startCordHead Coordinate, startCordTail Coordinate,  dir Day9Instruction) (Coordinate, Coordinate) {
	switch dir.direction {
	case RIGHT:
		startCordHead.X++
		if (startCordTail.X == startCordHead.X - 2) {
			if (startCordTail.Y != startCordHead.Y) {
				startCordTail.Y = startCordHead.Y
			}
			startCordTail.X++
		}
	case LEFT:
		startCordHead.X--
		if (startCordTail.X == startCordHead.X + 2) {
			if (startCordTail.Y != startCordHead.Y) {
				startCordTail.Y = startCordHead.Y
			}
			startCordTail.X--
		}
	case UP:
		startCordHead.Y++
		if (startCordTail.Y == startCordHead.Y - 2) {
			if (startCordTail.X != startCordHead.X) {
				startCordTail.X = startCordHead.X
			}
			startCordTail.Y++
		}
	case DOWN:
		startCordHead.Y--
		if (startCordTail.Y == startCordHead.Y + 2) {
			if (startCordTail.X != startCordHead.X) {
				startCordTail.X = startCordHead.X
			}
			startCordHead.Y--
		}
	}
	return startCordHead, startCordTail
}



func (direction Day9Instruction) Execute2(startCoordHead Coordinate, startCoordTail Coordinate) ([]Coordinate, []Coordinate) {
	currentCordHead := startCoordHead
	currentCordTail := startCoordTail
	var visitedHead []Coordinate 
	var visitedTail []Coordinate
	for i:=0; i<direction.moveUnits; i++ {
		headCord, tailCord := executeSingleMove(currentCordHead, currentCordTail, direction)
		visitedHead = append(visitedHead, headCord)
		currentCordHead = headCord
		currentCordTail = tailCord
		visitedTail = append(visitedTail, tailCord)
	}
	return visitedHead, visitedTail
}