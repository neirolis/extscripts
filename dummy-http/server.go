package main

import (
	"log"

	"github.com/gofiber/fiber/v2"
)

func init() {

}

func main() {
	app := fiber.New()
	app.Post("/", handleFrames)

	if err := app.Listen(":8090"); err != nil {
		log.Fatal(err)
	}
}

type Frame struct {
	Status string
	Items  []map[string]interface{}
}

func handleFrames(c *fiber.Ctx) error {
	var f Frame
	if err := c.BodyParser(&f); err != nil {
		return err
	}

	f.Status = "Dummy http status"

	for _, item := range f.Items {
		item["state"] = "fail"
	}

	return c.JSON(f)
}
