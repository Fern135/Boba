package enc

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"errors"
	"io"
	"log"
	"os"
)

func getKey() []byte {
	// var env = util.GetEnv("../../../.env")
	// var key = []byte(env["secret_key"])
	// var key = []byte(secretKeyStr)
	envDir := "../../../.env"
	secretKeyStr, found := os.LookupEnv(envDir)
	if !found {
		log.Fatal("secret_key environment variable not set")
	}

	return []byte(secretKeyStr)
}

func Encrypt(data []byte) ([]byte, error) {
	if len(data) <= 1 {
		log.Fatal("SECRET_KEY environment variable not set")
	}
	key := getKey()
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	ciphertext := make([]byte, aes.BlockSize+len(data))
	iv := ciphertext[:aes.BlockSize]
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		return nil, err
	}
	cfb := cipher.NewCFBEncrypter(block, iv)
	cfb.XORKeyStream(ciphertext[aes.BlockSize:], data)
	return ciphertext, nil
}

func Decrypt(ciphertext []byte) (string, error) {
	key := getKey()
	block, err := aes.NewCipher(key)
	if err != nil {
		return "", err
	}
	if len(ciphertext) < aes.BlockSize {
		return "", errors.New("ciphertext too short")
	}
	iv := ciphertext[:aes.BlockSize]
	ciphertext = ciphertext[aes.BlockSize:]
	cfb := cipher.NewCFBDecrypter(block, iv)
	cfb.XORKeyStream(ciphertext, ciphertext)

	return string(ciphertext), nil
}

// plaintext := []byte("Hello, world!")

// ciphertext, err := Encrypt(plaintext)
// if err != nil {
// 	log.Fatal(err)
// }

// decryptedText, err := decrypt(ciphertext)
// if err != nil {
// 	log.Fatal(err)
// }

// log.Println("Decrypted:", string(decryptedText))
