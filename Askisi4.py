ari=(int(raw_input("Dwse mou enan arithmo(mexri to 1000000): ")))
pin=""
while ari!=0:
    if ari>=1000000:
        ar=ari//1000000
        div=1000000
        for i in range(0,ar):
            pin+= u"M\u0305"
    elif ari>=900000:
        ar=ari//900000
        div=900000
        for i in range(0,ar):
            pin+= u"C\u0305M\u0305"
    elif ari>=500000:
        ar=ari//500000
        div=500000
        for i in range(0,ar):
            pin+= u"D\u0305"
    elif ari>=400000:
        ar=ari//400000
        div=400000
        for i in range(0,ar):
            pin+= u"C\u0305D\u0305"
    elif ari>=100000:
        ar=ari//100000
        div=100000
        for i in range(0,ar):
            pin+= u"C\u0305"
    elif ari>=90000:
        ar=ari//90000
        div=90000
        for i in range(0,ar):
            pin+= u"C\u0305L\u0305"
    elif ari>=50000:
        ar=ari//50000
        div=50000
        for i in range(0,ar):
            pin+= u"L\u0305"
    elif ari>=40000:
        ar=ari//40000
        div=40000
        for i in range(0,ar):
             pin+= u"X\u0305L\u0305"
    elif ari>=10000:
        ar=ari//10000
        div=10000
        for i in range(0,ar):
            pin+= u"X\u0305"
    elif ari>=9000:
        ar=ari//9000
        div=9000
        for i in range(0,ar):
            pin+= u"V\u0305M\u0305"
    elif ari>=5000:
        ar=ari//5000
        div=5000
        for i in range(0,ar):
            pin+= u"V\u0305"
    elif ari>=4000:
        ar=ari//4000
        div=4000
        for i in range(0,ar):
            pin+= u"M\u0305V\u0305"
    elif ari>=1000:
        ar=ari//1000
        div=1000
        for i in range(0,ar):
            pin+= "M"
    elif ari>=900:
        ar=ari//900
        div=900
        for i in range(0,ar):
            pin+= "CM"
    elif ari>=500:
        ar=ari//500
        div=500
        for i in range(0,ar):
            pin+= "D"
    elif ari>=400:
        ar=ari//400
        div=400
        for i in range(0,ar):
            pin+= "CD"
    elif ari>=100:
        ar=ari//100
        div=100
        for i in range(0,ar):
            pin+= "C"
    elif ari>=90:
        ar=ari//90
        div=90
        for i in range(0,ar):
            pin+= "CL"
    elif ari>=50:
        ar=ari//50
        div=50
        for i in range(0,ar):
            pin+= "L"
    elif ari>=40:
        ar=ari//40
        div=40
        for i in range(0,ar):
             pin+= "XL"
    elif ari>=10:
        ar=ari//10
        div=10
        for i in range(0,ar):
            pin+= "X"
    elif ari>=9:
        ar=ari//9
        div=9
        for i in range(0,ar):
            pin+= "VI"
    elif ari>=5:
        ar=ari//5
        div=5
        for i in range(0,ar):
            pin+= "V"
    elif ari>=4:
        ar=ari//4
        div=4
        for i in range(0,ar):
            pin+= "IV"
    else:
        ar=ari
        div=1
        for i in range(0,ar):
            pin+= "I"
    ari=ari%div
    
print pin
