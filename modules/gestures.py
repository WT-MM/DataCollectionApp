
def getRelPositions(landmarks):
    dists = []
    dists.append(calcDist(1,0, landmarks))
    dists.append(calcDist(2,1, landmarks))
    dists.append(calcDist(3,2, landmarks))
    dists.append(calcDist(4,3, landmarks))
    dists.append(calcDist(5,0, landmarks))
    dists.append(calcDist(6,5, landmarks))
    dists.append(calcDist(7,6, landmarks))
    dists.append(calcDist(8,7, landmarks))
    dists.append(calcDist(9,5, landmarks))
    dists.append(calcDist(10,9, landmarks))
    dists.append(calcDist(11,10, landmarks))
    dists.append(calcDist(12,11, landmarks))
    dists.append(calcDist(13,9, landmarks))
    dists.append(calcDist(14,13, landmarks))
    dists.append(calcDist(15,14, landmarks))
    dists.append(calcDist(16,15, landmarks))
    dists.append(calcDist(17,13, landmarks))
    dists.append(calcDist(18,17, landmarks))
    dists.append(calcDist(19,18, landmarks))
    dists.append(calcDist(20,19, landmarks))
    dists.append(calcDist(17,0, landmarks))
    return [item for sublist in dists for item in sublist]

def calcDist(first, second, landmarks):
    flip = True
    calculated = (landmarks[first].get('x')-landmarks[second].get('x'), landmarks[first].get('y')-landmarks[second].get('y'), landmarks[first].get('z')-landmarks[second].get('z'))
    if flip:
        calculated = [-1 * m for m in calculated]
    return calculated