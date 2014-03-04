# Python script: calculate volume of a unit cell from a CONTCAR file.
# Written by Johnny C.E.Kim @ MTG, Yonsei univ.
def CONTCAR_get_volume(/Users/suhyun/util_comp_sci/python_room/ce_ex/CONTCAR):
    CONTCAR = open(/Users/suhyun/util_comp_sci/python_room/ce_ex/CONTCAR , 'r').readlines()
    Magnitude = float(CONTCAR[1])
    ABC = get_number_from_line(CONTCAR[2])
    DEF = get_number_from_line(CONTCAR[3])
    GHI = get_number_from_line(CONTCAR[4])
    a = ABC[0]
    b = ABC[1]
    c = ABC[2]
    d = DEF[0]
    e = DEF[1]
    f = DEF[2]
    g = GHI[0]
    h = GHI[1]
    i = GHI[2]
    print (Magnitude**3)*(a*e*i+b*f*g+c*d*h-c*e*g-b*d*i-a*f*h)
    return (Magnitude**3)*(a*e*i+b*f*g+c*d*h-c*e*g-b*d*i-a*f*h)

print (Magnitude**3)*(a*e*i+b*f*g+c*d*h-c*e*g-b*d*i-a*f*h)
