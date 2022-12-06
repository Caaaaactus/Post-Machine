from POST_MACHINE_class import post_machine
def main():
    '''

    '''

    t_l = [0] * 32
    s = True
    w_h = 16

    c_l = [[1, '<', 2],
           [2, 'v', 3],
           [3, '?', [1, 4]],
           [4, 'stop', 4]]

    p_m = post_machine(s, w_h, t_l, c_l)
    p_m.post_machine_working()


if __name__ == "__main__":
    main()