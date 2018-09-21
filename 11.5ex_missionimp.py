"""MissionImp"""
def main():
    """main func"""
    num_a, num_b, num_c = int(input()), int(input()), int(input())
    num_e, num_f, num_g = int(input()), int(input()), int(input())
    num_i, num_j, num_k = int(input()), int(input()), int(input())

    det_a = num_a*num_f*num_k
    det_a += num_b*num_g*num_i
    det_a += num_c*num_e*num_j
    det_a -= num_i*num_f*num_c
    det_a -= num_j*num_g*num_a
    det_a -= num_k*num_e*num_b

    #find X






main()
