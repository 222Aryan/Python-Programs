def encode(in1):
    l=len(in1)
    p=l//3

    if l%3==1:
        f = in1[:p]
        m = in1[p:2*p+1]
        l = in1[2*p+1:]
    elif l%3==2:
        f=[:p+2]
        m=[p+2:p+3]

encode("john")
