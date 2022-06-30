from src.client import Calculator


if __name__ == '__main__':
    c = Calculator(verbose=True)
    c.create_user_interface()

    c.add_btn.click(10)
    c.add_shortcut.key_press(10)
    c.multiply_btn.click(3)
    c.undo_shortcut.key_press()
    c.add_shortcut.key_press(3)
    c.subtract_shortcut.key_press(11)
    c.undo_shortcut.key_press()
    c.divide_shortcut.key_press(3)

    c.undo_shortcut.key_press()
    c.undo_shortcut.key_press()
    c.undo_shortcut.key_press()
    c.undo_shortcut.key_press()
    c.undo_shortcut.key_press()
    c.undo_shortcut.key_press()
    c.undo_shortcut.key_press()
    c.undo_shortcut.key_press()
