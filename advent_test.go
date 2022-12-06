package main

import (
	"AdventOfCode/Day5"
	"testing"
)

func setupTestCase(t *testing.T) func(t *testing.T){
	t.Log("setup test case")
	return func(t *testing.T) {
		t.Log("teardown test case")
	}
}

func TestDay5Part1(t *testing.T) {
	got := Day5.Part1("testinput.txt")
	expected := "CMZ"
		if (got != expected) {
			t.Errorf("got wrong answer: %s", got)
		}	
}