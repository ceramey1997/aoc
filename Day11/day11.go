package Day11

import (
	"AdventOfCode/Utils"
	"fmt"
)

func Part1(inputfile string) int {
	lines := Utils.GetLines(inputfile, 11)
	monkeys := make(map[int]Monkey)
	for i:=0; i<len(lines);i+=7 {
		var tmp [6]string
		copy(tmp[:], lines[i:i+6])
		monkey, err := CreateMonkey(tmp)
		if (err != nil) {
			fmt.Println(err)
		}
		monkeys[monkey.id] = monkey
	}
	for rnd:=1;rnd<=20;rnd++ {
		for m:=0;m<len(monkeys);m++ {

			for i:=0;i<len(monkeys[m].items);i++ {
				InspectItem(monkeys, m, i, 0)
				PreformTest(monkeys, monkeys[m].id, i)
			}
			// delete all old items from newMonkeys from struct (monkeyId is new monkey's)
			for k := range monkeys[m].items {
				delete(monkeys[m].items, k)
			}
		}
	}
	for _, monkey := range monkeys {
		fmt.Println(monkey.id, ": ", monkey.inspectCount)
	}
	fmt.Println("Finished Part 1")
	return 0
}

func Part2(inputfile string) int {
	lines := Utils.GetLines(inputfile, 11)
	monkeys := make(map[int]Monkey)
	for i:=0; i<len(lines);i+=7 {
		var tmp [6]string
		copy(tmp[:], lines[i:i+6])
		monkey, err := CreateMonkey(tmp)
		if (err != nil) {
			fmt.Println(err)
		}
		monkeys[monkey.id] = monkey
	}
	var divisor int
	var divisors []int
	for _, monkey := range monkeys {
		divisors = append(divisors, monkey.test.testInt)
	}
	divisor = leastCommonMultiple(divisors[0], divisors[1], divisors...)
	for rnd:=1;rnd<=10000;rnd++ {
		for m:=0;m<len(monkeys);m++ {

			for i:=0;i<len(monkeys[m].items);i++ {
				InspectItem(monkeys, m, i, divisor)
				PreformTest(monkeys, monkeys[m].id, i)
			}
			// delete all old items from newMonkeys from struct (monkeyId is new monkey's)
			for k := range monkeys[m].items {
				delete(monkeys[m].items, k)
			}
		}
	}
	for _, monkey := range monkeys {
		fmt.Println(monkey.id, ": ", monkey.inspectCount)
	}
	return 0
}

func greatesCommonDivisor(a, b int) int {
	for b != 0 {
			t := b
			b = a % b
			a = t
	}
	return a
}

func leastCommonMultiple(a, b int, integers ...int) int {
	result := a * b / greatesCommonDivisor(a, b)

	for i := 0; i < len(integers); i++ {
			result = leastCommonMultiple(result, integers[i])
	}

	return result
}