from django.apps import AppConfig


class HelloConfig(AppConfig):
    name = 'hello'

def add(a,b):
    return a+b

def sortf(point):
    avgx=np.mean(point[0,:])
    avgy=np.mean(point[:,1])
    angle=[]
    n=[]
    for i in range(len(point)):
        p= math.degrees(math.atan((point[i,1] - avgy)/(point[i,0] - avgx)))
        angle.append(p)
    sangle = np.sort(angle)
    for i, a in enumerate(angle):
        if sangle[i] in angle:
            n.append(angle.index(sangle[i]))
    abc=[]
    for i in n:
        abc.append(point[i,:])
  
    return abc
