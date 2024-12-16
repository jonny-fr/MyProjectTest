def draw_christmas_tree(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)


    trunk_width = height // 3 if height > 5 else 1
    trunk_height = 2
    trunk_spaces = ' ' * (height - trunk_width // 2 - 1)

    for _ in range(trunk_height):
        print(trunk_spaces + '|' * trunk_width)

draw_christmas_tree(10)