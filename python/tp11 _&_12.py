def test1(ma_liste):
    return 1 in ma_liste

def test2(ma_liste):
    for n in ma_liste:
        if n==1 :
            return True
    return False
    