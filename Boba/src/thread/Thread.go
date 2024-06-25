package thread

import (
	"fmt"
	"sync"
	"time"
)

type Thread struct {
	wg sync.WaitGroup
}

func NewThread() *Thread {
	return &Thread{}
}

func (t *Thread) Run(f interface{}, args ...interface{}) {
	t.wg.Add(1)
	go func() {
		defer t.wg.Done()
		switch f := f.(type) {
		case func():
			f()
		case func(...interface{}):
			f(args...)
		default:
			fmt.Println("Unsupported function type")
		}
	}()
}

func (t *Thread) Wait() {
	t.wg.Wait()
}

func ExampleUsage() {
	defer fmt.Println("starting new thread like: t := NewThread()")
	t := NewThread()

	// Function with parameters
	defer fmt.Println("making a functnion called printNumbers")
	defer fmt.Println(" where it'll count from start to end parameter")
	printNumbers := func(start, end int) {
		for i := start; i <= end; i++ {
			fmt.Println(i)
			time.Sleep(500 * time.Millisecond)
		}
	}

	// Function without parameters
	defer fmt.Println("Making a function called printHello what prints out hello world")
	printHello := func() {
		fmt.Println("Hello, World!")
	}

	// Run function with parameters
	defer fmt.Println("Using the t.Run function to use printNumbers function with parameters ")
	defer fmt.Println("with start and end paremeter")
	defer fmt.Println("t.Run(printNumbers, 1, 5)")
	t.Run(printNumbers, 1, 5)

	// Run function without parameters
	defer fmt.Println("using t.Run function to run printHello function which prints out")
	defer fmt.Println("Hello world")
	defer fmt.Println("t.Run(printHello)")
	t.Run(printHello)

	defer fmt.Println("using t.Wait() to wait for the other 'Threads to finish'")
	fmt.Println("t.Wait()")
	t.Wait()
	fmt.Println("All goroutines finished.")
}
