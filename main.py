import math
import numpy as np
import matplotlib.pyplot as plt

'''
Não pude resolver o problema da forma proposta na aula.
Instalei o Kinovea mas as coordenadas resultantes são relativas e sempre começam em (0,0)
por isso não pude usar os caixotes para a calibragem entre as cameras

Optei por tentar outra solução a partir de um angulo arbitrário que assumi haver entre as câmeras
Comentei com # dos arquivos c1.txt e c2.txt para o script ignorar os momentos em que a bola não se movimentoa.

Outra dificuldade com o Kinovea foi não poder configurar o contorno da bola com a ferramenta de desenhar trajetória
então ficou torto :P
'''


def coord_from_line(line: str):
    return [float(x.replace(',', '.')) for x in line.split(' ')[1:-1]]


def get_coords_from_file(filename: str):
    coords = []

    with open(filename, 'r') as c1:
        lines = c1.readlines()

        for line in lines:
            if line[0] == '#':
                continue

            result = coord_from_line(line)

            if len(result) == 2:
                coords.append(result)

    return coords

def rotate(coords, ang):
    n_coords = []

    for c in coords:
        rotated = c[0] * math.cos(ang)
        n_coords.append([rotated, c[1]]) 

    return n_coords

def plot_3d(x, y, z):
    

    plt.close('all')
    # plt.grid(True)

    
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z, 'gray')

    plt.show()

if __name__ == '__main__':
    xy_cam1 = get_coords_from_file("c1.txt")
    xy_cam2 = get_coords_from_file("c2.txt")
    angulo = 0.2 # angulo arbitrário em radianos

    xy = np.array(xy_cam1)
    zy = np.array(rotate(xy_cam2, angulo))
    
    y_mean = []
    for i, v in enumerate(xy):
        y_mean.append((v[1] + zy[i][1])/2)

    x = xy[:, 0]
    z = zy[:, 0]
    y = np.array(y_mean)

    max_len = min(len(x), len(z), len(y))
    x = x[:max_len]
    y = y[:max_len]
    z = z[:max_len]

    plot_3d(x, y, z)

    
    