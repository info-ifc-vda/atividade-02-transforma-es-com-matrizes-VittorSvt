import glfw
from OpenGL.GL import *
import numpy as np
import math

# Vértices do triângulo
vertices = [
    [ -0.2, -0.2, 1],
    [  0.2, -0.2, 1],
    [  0.0,  0.2, 1]
]

def init():
    glClearColor(0, 0, 0, 1)

def aplicar_transformacao(v, matriz):
    novo = []
    for ponto in v:
        # Multiplicação da Matriz pelo ponto (vetor coluna)
        resultado = np.dot(matriz, ponto)
        novo.append(resultado)
    return novo

# --- Funções de Matriz ---

def matriz_translacao(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def matriz_escala(sx, sy):
    return np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1]
    ])

def matriz_rotacao(angulo_graus):
    rad = math.radians(angulo_graus)
    return np.array([
        [math.cos(rad), -math.sin(rad), 0],
        [math.sin(rad),  math.cos(rad), 0],
        [0,             0,              1]
    ])

def render(v, cor=(1, 1, 1)):
    glColor3f(*cor) # Define a cor do triângulo
    glBegin(GL_TRIANGLES)
    for ponto in v:
        glVertex2f(ponto[0], ponto[1])
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Matrizes de Transformação", None, None)
    glfw.make_context_current(window)
    init()

    # Criando as transformações
    T = matriz_translacao(-0.5, 0.5)
    S = matriz_escala(1.5, 1.5)
    R = matriz_rotacao(45)

    # Aplicando nos vértices
    v_transladado = aplicar_transformacao(vertices, T)
    v_escalado    = aplicar_transformacao(vertices, S)
    v_rotacionado = aplicar_transformacao(vertices, R)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        render(vertices, (1, 0, 0))      # Original em Vermelho
        render(v_transladado, (0, 1, 0)) # Transladado em Verde
        render(v_escalado, (0, 0, 1))    # Escalonado em Azul
        render(v_rotacionado, (1, 1, 0)) # Rotacionado em Amarelo

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
