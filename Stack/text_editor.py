class Stack:
    def __init__(self):
        self.items = []  # Initialize empty list for stack

    def push(self, value):
        self.items.append(value)  # Add item to end (top of stack), O(1)

    def peek(self):
        if self.is_empty():
            return None  # Return None for empty stack
        return self.items[-1]  # Return top element without removing

    def pop(self):
        if self.is_empty():
            return None  # Return None for empty stack
        return self.items.pop()  # Remove and return top element, O(1)

    def is_empty(self) -> bool:
        return len(self.items) == 0  # True if stack is empty

    def print_stack(self) -> None:
        # Print stack with top element first to reflect LIFO
        if self.is_empty():
            print("[]")
        else:
            print("[", end="")
            print(", ".join(str(item) for item in self.items), end="")
            print("]")


class Command:
    def __init__(self, editor: "TextEditor"):
        self.editor = editor

    def execute(self):
        """Perform the action"""
        pass

    def undo(self):
        """Reverse the action"""
        pass


class InsertCommand(Command):
    def __init__(self, editor: "TextEditor", text: str, position: int):
        super().__init__(editor)
        self.text_to_insert = text
        self.position = position
        self.previous_text = editor.text  # Store state before execution

    def execute(self):
        # Insert text at position
        self.editor.text = (
            self.editor.text[: self.position]
            + self.text_to_insert
            + self.editor.text[self.position :]
        )

    def undo(self):
        # Revert to previous text
        self.editor.text = self.previous_text


class DeleteCommand(Command):
    def __init__(self, editor: "TextEditor", start: int, length: int):
        super().__init__(editor)
        self.start = start
        self.length = length
        self.deleted_text = ""
        self.previous_text = editor.text

    def execute(self):
        # Delete text from start to start+length
        if self.start < len(self.editor.text):
            self.deleted_text = self.editor.text[self.start : self.start + self.length]
            self.editor.text = (
                self.editor.text[: self.start]
                + self.editor.text[self.start + self.length :]
            )

    def undo(self):
        # Restore deleted text
        self.editor.text = (
            self.editor.text[: self.start]
            + self.deleted_text
            + self.editor.text[self.start :]
        )


class TextEditor:
    def __init__(self):
        self.text = ""  # Current text
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def insert(self, text: str, position: int = None):
        """Insert text at position (default: end of text)"""
        if position is None:
            position = len(self.text)

        # Create and execute command
        command = InsertCommand(self, text, position)
        command.execute()

        # Push to undo stack and clear redo stack
        self.undo_stack.push(command)
        self.redo_stack = Stack()  # Clear redo on new action

        return True

    def delete(self, start: int, length: int = 1):
        """Delete text starting at position"""
        if start >= len(self.text) or length <= 0:
            return False

        # Create and execute command
        command = DeleteCommand(self, start, length)
        command.execute()

        # Push to undo stack and clear redo stack
        self.undo_stack.push(command)
        self.redo_stack = Stack()

        return True

    def undo(self):
        """Undo last operation"""
        if self.undo_stack.is_empty():
            return False

        # Get last command and undo it
        command = self.undo_stack.pop()
        command.undo()

        # Push to redo stack
        self.redo_stack.push(command)

        return True

    def redo(self):
        """Redo last undone operation"""
        if self.redo_stack.is_empty():
            return False

        # Get last undone command and re-execute it
        command = self.redo_stack.pop()
        command.execute()

        # Push back to undo stack
        self.undo_stack.push(command)

        return True

    def get_text(self):
        return self.text

    def print_state(self):
        """Helper to see current state"""
        print(f"Text: '{self.text}'")
        print(f"Undo stack size: {len(self.undo_stack.items)}")
        print(f"Redo stack size: {len(self.redo_stack.items)}")
        print("-" * 30)


def main():
    editor = TextEditor()

    print("=== Text Editor Demo ===\n")

    # Test 1: Basic insert
    print("1. Insert 'hello'")
    editor.insert("hello")
    editor.print_state()

    # Test 2: Insert at position
    print("2. Insert ' world' at end")
    editor.insert(" world", 5)
    editor.print_state()

    # Test 3: Insert in middle
    print("3. Insert ' beautiful' at position 5")
    editor.insert(" beautiful", 5)
    editor.print_state()

    # Test 4: Delete
    print("4. Delete ' beautiful'")
    editor.delete(5, 11)  # Delete 11 chars starting at position 5
    editor.print_state()

    # Test 5: Undo
    print("5. Undo (bring back ' beautiful')")
    editor.undo()
    editor.print_state()

    # Test 6: Redo
    print("6. Redo (remove ' beautiful' again)")
    editor.redo()
    editor.print_state()

    # Test 7: Multiple undos/redos
    print("7. Multiple operations:")
    editor.undo()  # Undo the delete
    editor.undo()  # Undo the middle insert
    editor.undo()  # Undo the append
    editor.undo()  # Undo the first insert
    editor.print_state()

    print("8. Redo everything:")
    editor.redo()  # Redo first insert
    editor.redo()  # Redo append
    editor.redo()  # Redo middle insert
    editor.redo()  # Redo delete
    editor.print_state()


if __name__ == "__main__":
    main()
