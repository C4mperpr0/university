package stack

type stack struct {
	arr []int
	pointer int
}

func (s *Stack) Push(e int) {
	s.arr(s.pointer) = e
	s.pointer++
}

func (s *Stack) Pop() {
	r int = arr[-1]
	arr.Pop(-1)
	pointer--
	return r
}

func (s *Stack) Top() {
	return arr[-1]
}

func (s *Stack) IsEmpty() {
	return s.arr.Length == 0
}


