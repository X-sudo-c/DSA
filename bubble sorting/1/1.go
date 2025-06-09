package main

import ("fmt")



func main(){
	fmt.Println("Welcome to simple calculator\n")
	var choice string
	fmt.Printf("Do you want to add, substract, or divide: ")
	fmt.Scanln(&choice)

	if choice == "add"{

		fmt.Println("You chose add")

	}else if choice == "subtract"{

		fmt.Println("You chose subtract")

	}else if choice == "divide"{

		println("You chose divide")

	}else{
		fmt.Println("undefined option")
	}

}