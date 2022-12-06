package Day5

type Crate struct {
	char string
	position int
}

func NewCrate(char string, position int) Crate {
	c := Crate { char, position }
	return c
}