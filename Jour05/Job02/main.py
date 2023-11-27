def draw_rectangle(width, height):
    top_bottom = '|' + '-' * (width - 2) + '|'
    print(top_bottom)
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    print(top_bottom)

# Appel de la fonction 
draw_rectangle(10, 3)
