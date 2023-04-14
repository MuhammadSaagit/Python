def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height-1:
            print('|' +'-' * (width-1) + '|')
        else:
            print('|' + ' ' * (width-1) + '|')

draw_rectangle(10,3)