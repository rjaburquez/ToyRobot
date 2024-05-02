class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.table_size = 5

    def place(self, x, y, direction):
        if self.is_valid_position(x, y):
            self.x = x
            self.y = y
            self.direction = direction

    def move(self):
        if self.direction == "NORTH" and self.y < self.table_size - 1:
            self.y += 1
        elif self.direction == "EAST" and self.x < self.table_size - 1:
            self.x += 1
        elif self.direction == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.direction == "WEST" and self.x > 0:
            self.x -= 1

    def left(self):
        if self.direction == "NORTH":
            self.direction = "WEST"
        elif self.direction == "EAST":
            self.direction = "NORTH"
        elif self.direction == "SOUTH":
            self.direction = "EAST"
        elif self.direction == "WEST":
            self.direction = "SOUTH"

    def right(self):
        if self.direction == "NORTH":
            self.direction = "EAST"
        elif self.direction == "EAST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "WEST"
        elif self.direction == "WEST":
            self.direction = "NORTH"

    def is_valid_position(self, x, y):
        return 0 <= x < self.table_size and 0 <= y < self.table_size

    def report(self):
        if self.x is not None and self.y is not None and self.direction is not None:
            print(f"Output: {self.x}, {self.y}, {self.direction}")
        else:
            print("Output: Toy Robot is not placed on the table yet.")


def main():
    robot = ToyRobot()
    placed = False

    while True:
        command = input("Enter command: ").strip().upper()

        if not placed and not command.startswith("PLACE"):
            print("Please place the toy robot first.")
            continue

        if command.startswith("PLACE"):
            args = command.split()
            if len(args) == 4:
                _, x, y, direction = args
                x = int(x)
                y = int(y)
                robot.place(x, y, direction)
                placed = True
            else:
                print("Invalid PLACE command format. Should be: PLACE X Y DIRECTION")
            continue

        if command == "MOVE":
            robot.move()
        elif command == "LEFT":
            robot.left()
        elif command == "RIGHT":
            robot.right()
        elif command == "REPORT":
            robot.report()
        elif command == "EXIT":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
