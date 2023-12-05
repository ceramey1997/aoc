package Day11

import (
	"errors"
	"fmt"
	"math"
	"strconv"
	"strings"
)

type Operator string
const (
	MULTIPLY Operator = "*"
	DIVIDE Operator = "/"
	ADD Operator = "+"
	SUBTRACT Operator = "-"
)

type Operation struct {
	firstIsOld bool
	first int
	operator Operator
	secondIsOld bool
	second int
}

type Test struct {
	testInt int
	throwTrue int
	throwFalse int
}

type Monkey struct {
	id int
	items map[int]int
	operation Operation
	test Test
	inspectCount int
}


func CreateMonkey(lines [6]string) (Monkey, error) { // should be given a list of strings length 6
	id, idErr := parseId(lines[0])
	if (idErr != nil) {
		return Monkey{}, idErr
	}

	items, itemsErr := parseItems(lines[1])
	if (itemsErr != nil) {
		return Monkey{}, errors.New(fmt.Sprintf("Error parsing monkey %v during test with error: %s", id, itemsErr.Error()))
	}

	operation, opErr := parseOperation(lines[2])
	if (opErr != nil) {
		return Monkey{}, errors.New(fmt.Sprintf("Error parsing monkey %v during test with error: %s", id, opErr.Error()))
	}

	test, testErr := parseTest([3]string{lines[3], lines[4], lines[5]})
	if (testErr != nil) {
		return Monkey{}, errors.New(fmt.Sprintf("Error parsing monkey %v during test with error: %s", id, testErr.Error()))
	}
	return Monkey{ id: id, items: items, operation: operation, test: test }, nil
}

func parseId(line string) (int, error) {
	fubarId, err := strconv.Atoi(strings.ReplaceAll(strings.Split(line, " ")[1], ":", ""))
	if (err != nil) {
		return 0, errors.New(fmt.Sprintf("Error parsing Id, resulted in error: %s", err))
	}
	return fubarId, nil
}

func parseItems(line string) (map[int]int, error) {
	strItems := strings.Split(line, ": ")[1]
	splitItems := strings.Split(strItems, ",")
	items := make(map[int]int)
	for idx, i := range splitItems {
		i = strings.TrimSpace(i)
		fubar, err := strconv.Atoi(i)
		if (err != nil) {
			return map[int]int{}, nil
		}
		items[idx] = fubar
	}
	return items, nil
}

func parseOperation(line string) (Operation, error) {
	strWithoutWord := strings.ReplaceAll(strings.TrimSpace(line), "Operation: new = ", "")
	splitStr := strings.Split(strWithoutWord, " ")
	
	firstOld := false
	secondOld := false
	var firstInt int
	var secondInt int

	operator, errOperator := getOperator(splitStr[1])
	if (errOperator != nil) {
		return Operation{}, errOperator
	}

	first := splitStr[0]
	if (first == "old") {
		firstOld = true
		firstInt = 0
	} else {
		tmp, convErr := strconv.Atoi(first)
		if (convErr != nil) {
			return Operation{}, convErr
		}
		firstInt = tmp
	}

	second := strings.TrimSpace(splitStr[2])
	if (second == "old") {
		secondOld = true
		secondInt = 0
	} else {
		tmp, convErr := strconv.Atoi(second)
		if (convErr != nil) {
			return Operation{}, convErr
		}
		secondInt = tmp
	}

	return Operation{firstIsOld: firstOld, first: firstInt, operator: operator, secondIsOld: secondOld, second: secondInt}, nil
}

func getOperator(s string) (Operator, error) {
	switch s {
	case "+":
		return ADD, nil
	case "-":
		return SUBTRACT, nil
	case "*":
		return MULTIPLY, nil
	case "/":
		return DIVIDE, nil
	default:
		return ADD, errors.New(fmt.Sprintf("Error getting Operator from: %s", s))
	}
}

func parseTest(lines [3]string) (Test, error) {
	strWithoutWord := strings.ReplaceAll(lines[0], "Test: divisible by ", "")
	num, err := strconv.Atoi(strings.TrimSpace(strWithoutWord))
	if (err != nil) {
		return Test{}, errors.New(fmt.Sprintf("Error parsing test number: %v.\n\twith error: %s", num, err.Error()))
	}
	trueId, errTrue := parseTestLogic(lines[1])
	if (errTrue != nil) {
		return Test{}, errors.New(fmt.Sprintf("Error parsing true condition: %s", errTrue.Error()))
	}
	falseId, errFalse := parseTestLogic(lines[2])
	if (errFalse != nil) {
		return Test{}, errors.New(fmt.Sprintf("Error parsing false condition: %s", errFalse.Error()))
	}
	return Test{testInt: num, throwTrue: trueId, throwFalse: falseId}, nil
}

func parseTestLogic(line string) (int, error) {
	strWithoutWord := strings.ReplaceAll(line, " throw to monkey ", "")
	strWithoutWord = strings.ReplaceAll(strWithoutWord, "If ", "")
	splits := strings.Split(strWithoutWord, ":")
	id, err := strconv.Atoi(strings.TrimSpace(splits[1]))
	if (err != nil) {
		return 0, errors.New(fmt.Sprintf("Error parsing condition %s, was given invalid: %s", strings.TrimSpace(splits[0]), splits[1]))
	}
	return id, nil
}


func InspectItem(this map[int]Monkey, monkeyIdx int, ItemIdx int, divisor int) {
	preformWorryOperation(this, monkeyIdx, ItemIdx)
	if (divisor != 0) {
		haveRelief(this, monkeyIdx, ItemIdx, divisor)
	} else {
		haveRelief(this, monkeyIdx, ItemIdx, 0)
	}
	
	incrementInspect(this, monkeyIdx)

}

func PreformTest(monkeys map[int]Monkey, monkeyId int, idxItem int) {
	var newMonkeyId int
	worryLevel := monkeys[monkeyId].items[idxItem]
	divisor := monkeys[monkeyId].test.testInt
	if (worryLevel % divisor == 0) {
		newMonkeyId = monkeys[monkeyId].test.throwTrue
	} else {
		newMonkeyId = monkeys[monkeyId].test.throwFalse
	}
	monkeys[newMonkeyId].items[len(monkeys[newMonkeyId].items)] = worryLevel
}

func preformWorryOperation(this map[int]Monkey, monkeyIdx int, itemIdx int){
	var firstVal int
	var secondVal int
	var tmp int

	if (this[monkeyIdx].operation.firstIsOld) {
		firstVal = this[monkeyIdx].items[itemIdx]
	} else {
		firstVal = this[monkeyIdx].operation.first
	}
	if (this[monkeyIdx].operation.secondIsOld) {
		secondVal = this[monkeyIdx].items[itemIdx]
	} else {
		secondVal = this[monkeyIdx].operation.second
	}
	switch this[monkeyIdx].operation.operator {
	case ADD:
		tmp = firstVal + secondVal
	case SUBTRACT:
		tmp = firstVal - secondVal
	case MULTIPLY:
		tmp = firstVal * secondVal
	case DIVIDE:
		tmp = firstVal / secondVal
	}
	this[monkeyIdx].items[itemIdx] = tmp
}

func haveRelief(this map[int]Monkey, monkeyIdx int, itemIdx int, divisor int) {
	var newVal int
	val := this[monkeyIdx].items[itemIdx]
	if (divisor == 0) {
		newVal = int(math.Floor(float64(val / 3)))
	} else {
		newVal = val % divisor
	}
	
	this[monkeyIdx].items[itemIdx] = newVal
}

func incrementInspect(this map[int]Monkey, monkeyIdx int) {
	newVal := this[monkeyIdx].inspectCount + 1
	monkeyCopy := this[monkeyIdx]
	monkeyCopy.inspectCount = newVal
	this[monkeyIdx] = monkeyCopy
}