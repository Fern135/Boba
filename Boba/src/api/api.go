package api

import (
	"boba/src/db"
	"boba/src/util"
	"fmt"
	"net/http"
)

/*
	api for handling the front end work.
*/

func setUp() {
	filePath := "./st.txt"
	data := []byte("Done")
	exists, err := util.Exists("./st.txt")

	if err != nil {
		fmt.Println(err)
	} else if !exists {
		fmt.Println("File does not exist, creating it now.")
		err = util.WriteToFile(filePath, data)
		if err != nil {
			fmt.Println("Error writing to file:", err)
		} else {
			fmt.Println("File created and data written successfully!")
		}
	} else {
		fmt.Println("File already exists, not writing data.")
	}
}

func SetUpApi() {
	db.InitDB()

	defer setUp()
}

func Start() {
	fmt.Println("Server starting at :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println(err)
	}
}
