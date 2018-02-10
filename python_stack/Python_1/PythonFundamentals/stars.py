def draw_stars(num_list):
    for num in num_list:
        print("\033[1;31;40m *" * num)

draw_stars([4, 6, 1, 3, 5, 7, 25])