def isAinsideB(A, B):
    x, y, w, h = A
    xb, yb, wb, hb = B
    if ((y + h >= yb and x + w > xb and x < xb + wb)
    and (x + w >= xb and y + h > yb and y < yb + hb)):
        return True
    return False