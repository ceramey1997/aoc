package Day5

import "fmt"

type Stack struct {
	crates []Crate
	column int
}

func NewStack(mp map[int]string, column int) Stack{
	var crates []Crate
	startingPosition := len(mp)
	for i:=0; i<len(mp); i++{
		if (mp[i] != " ") {
			c := NewCrate(mp[i], startingPosition)
			crates = append(crates, c)
		}
		startingPosition--
	}
	// fmt.Println("***** Creating stack********")
	// fmt.Println(crates)
	// fmt.Println(column)
	// fmt.Println("***** Creating stack********")
	return Stack { crates, column }
}

func PrettyPrint(stacks []Stack) {
	// for _, stack := range stacks {
	// 	for _, crate := range stack.crates {
	// 		fmt.Print(crate.char)
	// 	}
	// 	fmt.Println("")
	// }
	for stackNum:=0; stackNum<len(stacks); stackNum++ {
		for i:=len(stacks[stackNum].crates)-1; i>=0; i-- {
			fmt.Print(stacks[stackNum].crates[i].char)
		}
		fmt.Println("")
	}
}

func TopCrates(stacks []Stack) string{
	topCrates := ""
	for _, stack := range stacks {
		topCrates += stack.crates[0].char
	}
	return topCrates
}