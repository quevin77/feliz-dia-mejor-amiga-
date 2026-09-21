import pygame
import random
import math

pygame.init()

# =====================================================
# CONFIGURACIÓN
# =====================================================

ANCHO = 1400
ALTO = 900

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🌻 Feliz Día Mejor Amiga 🌻")

reloj = pygame.time.Clock()

# =====================================================
# COLORES
# =====================================================

NEGRO = (2, 3, 18)
AZUL = (8, 10, 40)
MORADO = (25, 10, 55)

BLANCO = (255, 255, 255)

AMARILLO = (255, 190, 10)
AMARILLO_CLARO = (255, 225, 70)
AMARILLO_BRILLO = (255, 245, 150)

MARRON = (100, 50, 10)

VERDE = (35, 120, 45)
VERDE_CLARO = (60, 160, 65)

ROSADO = (220, 80, 130)
PAPEL = (170, 100, 70)

# =====================================================
# FUENTES
# =====================================================

fuente_titulo = pygame.font.SysFont(
    "segoe script",
    80,
    bold=True
)

fuente_amiga = pygame.font.SysFont(
    "segoe script",
    95,
    bold=True
)

fuente_mensaje = pygame.font.SysFont(
    "segoe script",
    34,
    bold=True
)

fuente_pequena = pygame.font.SysFont(
    "arial",
    22
)

# =====================================================
# ESTRELLAS
# =====================================================

estrellas = []

for i in range(220):

    x = random.randint(0, ANCHO)
    y = random.randint(0, ALTO)

    tamaño = random.randint(1, 3)

    brillo = random.randint(150, 255)

    estrellas.append([
        x,
        y,
        tamaño,
        brillo
    ])

# =====================================================
# PLANETAS
# =====================================================

planetas = [
    [120, 170, 55],
    [1260, 180, 38],
    [110, 760, 42],
    [1280, 720, 65]
]

# =====================================================
# FLORES
# =====================================================

flores = [

    {
        "x": 700,
        "y": 420,
        "tamaño": 48,
        "mensaje": "Gracias por estar siempre 💛"
    },

    {
        "x": 570,
        "y": 490,
        "tamaño": 43,
        "mensaje": "Eres una gran amiga ✨"
    },

    {
        "x": 830,
        "y": 490,
        "tamaño": 43,
        "mensaje": "Nunca cambies 🌻"
    },

    {
        "x": 625,
        "y": 375,
        "tamaño": 45,
        "mensaje": "Te deseo lo mejor 💫"
    },

    {
        "x": 775,
        "y": 375,
        "tamaño": 45,
        "mensaje": "Mi amiga, mi cómplice.💛"
    }
]

# =====================================================
# PARTÍCULAS
# =====================================================

particulas = []

# =====================================================
# FUNCIÓN: FONDO DE GALAXIA
# =====================================================

def dibujar_fondo():

    for y in range(ALTO):

        porcentaje = y / ALTO

        r = int(NEGRO[0] +
                (MORADO[0] - NEGRO[0]) * porcentaje)

        g = int(NEGRO[1] +
                (AZUL[1] - NEGRO[1]) * porcentaje)

        b = int(NEGRO[2] +
                (MORADO[2] - NEGRO[2]) * porcentaje)

        pygame.draw.line(
            pantalla,
            (r, g, b),
            (0, y),
            (ANCHO, y)
        )

    # Nebulosa suave

    nebulosa = pygame.Surface(
        (ANCHO, ALTO),
        pygame.SRCALPHA
    )

    pygame.draw.circle(
        nebulosa,
        (90, 30, 140, 25),
        (700, 450),
        350
    )

    pygame.draw.circle(
        nebulosa,
        (20, 80, 180, 20),
        (700, 450),
        250
    )

    pantalla.blit(
        nebulosa,
        (0, 0)
    )

# =====================================================
# FUNCIÓN: ESTRELLAS
# =====================================================

def dibujar_estrellas():

    for estrella in estrellas:

        x = estrella[0]
        y = estrella[1]
        tamaño = estrella[2]
        brillo = estrella[3]

        color = (
            brillo,
            brillo,
            brillo
        )

        pygame.draw.circle(
            pantalla,
            color,
            (x, y),
            tamaño
        )

        # Algunas estrellas tienen brillo

        if tamaño >= 3:

            pygame.draw.line(
                pantalla,
                color,
                (x - 7, y),
                (x + 7, y),
                1
            )

            pygame.draw.line(
                pantalla,
                color,
                (x, y - 7),
                (x, y + 7),
                1
            )

# =====================================================
# FUNCIÓN: PLANETA
# =====================================================

def dibujar_planeta(x, y, tamaño):

    # Brillo exterior

    brillo = pygame.Surface(
        (tamaño * 3, tamaño * 3),
        pygame.SRCALPHA
    )

    pygame.draw.circle(
        brillo,
        (80, 120, 255, 30),
        (tamaño * 1.5, tamaño * 1.5),
        tamaño
    )

    pantalla.blit(
        brillo,
        (
            x - tamaño * 1.5,
            y - tamaño * 1.5
        )
    )

    # Planeta

    pygame.draw.circle(
        pantalla,
        (55, 85, 190),
        (x, y),
        tamaño
    )

    # Parte iluminada

    pygame.draw.circle(
        pantalla,
        (90, 125, 230),
        (
            x - tamaño // 3,
            y - tamaño // 3
        ),
        tamaño // 3
    )

# =====================================================
# FUNCIÓN: GLOW
# =====================================================

def dibujar_glow(x, y, tamaño):

    glow = pygame.Surface(
        (tamaño * 4, tamaño * 4),
        pygame.SRCALPHA
    )

    for radio in range(tamaño * 2, 5, -5):

        alpha = int(
            35 * (radio / (tamaño * 2))
        )

        pygame.draw.circle(
            glow,
            (255, 210, 40, alpha),
            (
                tamaño * 2,
                tamaño * 2
            ),
            radio
        )

    pantalla.blit(
        glow,
        (
            x - tamaño * 2,
            y - tamaño * 2
        )
    )

# =====================================================
# FUNCIÓN: GIRASOL
# =====================================================

def dibujar_girasol(x, y, tamaño, seleccionado):

    # Brillo cuando el mouse está encima

    if seleccionado:

        dibujar_glow(
            x,
            y,
            tamaño
        )

    # Pétalos

    for i in range(12):

        angulo = (
            i * math.pi * 2 / 12
        )

        distancia = tamaño * 0.72

        px = (
            x +
            math.cos(angulo) * distancia
        )

        py = (
            y +
            math.sin(angulo) * distancia
        )

        pygame.draw.ellipse(
            pantalla,
            AMARILLO_CLARO
            if seleccionado
            else AMARILLO,
            (
                int(px - tamaño * 0.48),
                int(py - tamaño * 0.30),
                int(tamaño * 0.96),
                int(tamaño * 0.60)
            )
        )

    # Segunda capa de pétalos

    for i in range(12):

        angulo = (
            i * math.pi * 2 / 12
            + math.pi / 12
        )

        distancia = tamaño * 0.55

        px = (
            x +
            math.cos(angulo) * distancia
        )

        py = (
            y +
            math.sin(angulo) * distancia
        )

        pygame.draw.circle(
            pantalla,
            AMARILLO,
            (
                int(px),
                int(py)
            ),
            int(tamaño * 0.30)
        )

    # Centro oscuro

    pygame.draw.circle(
        pantalla,
        MARRON,
        (x, y),
        int(tamaño * 0.43)
    )

    # Semillas

    for i in range(12):

        angulo = i * math.pi / 6

        distancia = tamaño * 0.25

        sx = (
            x +
            math.cos(angulo) * distancia
        )

        sy = (
            y +
            math.sin(angulo) * distancia
        )

        pygame.draw.circle(
            pantalla,
            (160, 90, 20),
            (
                int(sx),
                int(sy)
            ),
            3
        )

# =====================================================
# FUNCIÓN: TALLOS Y HOJAS
# =====================================================

def dibujar_tallos():

    for flor in flores:

        x = flor["x"]
        y = flor["y"]

        pygame.draw.line(
            pantalla,
            VERDE,
            (700, 700),
            (x, y + 30),
            8
        )

    # Hojas

    hojas = [

        (560, 590, 120, 45),
        (650, 620, 130, 45),
        (730, 600, 120, 45),
        (790, 650, 130, 45),
        (610, 670, 100, 40)
    ]

    for x, y, ancho, alto in hojas:

        pygame.draw.ellipse(
            pantalla,
            VERDE_CLARO,
            (
                x,
                y,
                ancho,
                alto
            )
        )

# =====================================================
# FUNCIÓN: RAMO
# =====================================================

def dibujar_ramo():

    # Tallos

    dibujar_tallos()

    # Papel

    puntos = [

        (555, 720),
        (845, 720),
        (785, 870),
        (615, 870)
    ]

    pygame.draw.polygon(
        pantalla,
        PAPEL,
        puntos
    )

    # Línea decorativa

    pygame.draw.line(
        pantalla,
        (210, 140, 100),
        (580, 735),
        (820, 735),
        5
    )

    # Cinta

    pygame.draw.rect(
        pantalla,
        ROSADO,
        (660, 735, 80, 25),
        border_radius=8
    )

    # Lazo

    pygame.draw.ellipse(
        pantalla,
        ROSADO,
        (620, 720, 70, 45)
    )

    pygame.draw.ellipse(
        pantalla,
        ROSADO,
        (710, 720, 70, 45)
    )

# =====================================================
# FUNCIÓN: PARTÍCULAS
# =====================================================

def crear_particulas(x, y):

    for i in range(25):

        particulas.append({

            "x": x,
            "y": y,

            "dx": random.uniform(-3, 3),

            "dy": random.uniform(-4, -1),

            "vida": 60

        })

def actualizar_particulas():

    for p in particulas[:]:

        p["x"] += p["dx"]

        p["y"] += p["dy"]

        p["vida"] -= 1

        if p["vida"] <= 0:

            particulas.remove(p)

        else:

            pygame.draw.circle(

                pantalla,

                AMARILLO_BRILLO,

                (
                    int(p["x"]),
                    int(p["y"])
                ),

                4
            )

# =====================================================
# MENSAJE
# =====================================================

mensaje = ""

# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

ejecutando = True

while ejecutando:

    # ================================================
    # EVENTOS
    # ================================================

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            ejecutando = False

        # Clic

        if evento.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = evento.pos

            for flor in flores:

                x = flor["x"]

                y = flor["y"]

                tamaño = flor["tamaño"]

                distancia = math.sqrt(

                    (mouse_x - x) ** 2
                    +
                    (mouse_y - y) ** 2

                )

                if distancia < tamaño + 20:

                    mensaje = flor["mensaje"]

                    crear_particulas(
                        x,
                        y
                    )

    # ================================================
    # FONDO
    # ================================================

    dibujar_fondo()

    # ================================================
    # ESTRELLAS
    # ================================================

    dibujar_estrellas()

    # ================================================
    # PLANETAS
    # ================================================

    for planeta in planetas:

        dibujar_planeta(
            planeta[0],
            planeta[1],
            planeta[2]
        )

    # ================================================
    # TÍTULO
    # ================================================

    texto1 = fuente_titulo.render(
        "Feliz Día",
        True,
        BLANCO
    )

    texto2 = fuente_amiga.render(
        "Mejor Amiga",
        True,
        AMARILLO_CLARO
    )

    # Brillo del título

    sombra = fuente_titulo.render(
        "Feliz Día",
        True,
        (100, 70, 20)
    )

    pantalla.blit(
        sombra,
        sombra.get_rect(
            center=(704, 72)
        )
    )

    pantalla.blit(
        texto1,
        texto1.get_rect(
            center=(700, 65)
        )
    )

    pantalla.blit(
        texto2,
        texto2.get_rect(
            center=(700, 160)
        )
    )

    # ================================================
    # RAMO
    # ================================================

    dibujar_ramo()

    # ================================================
    # FLORES
    # ================================================

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for flor in flores:

        x = flor["x"]

        y = flor["y"]

        tamaño = flor["tamaño"]

        distancia = math.sqrt(

            (mouse_x - x) ** 2
            +
            (mouse_y - y) ** 2

        )

        seleccionado = (
            distancia < tamaño + 20
        )

        dibujar_girasol(
            x,
            y,
            tamaño,
            seleccionado
        )

    # ================================================
    # MENSAJE
    # ================================================

    if mensaje != "":

        caja = pygame.Rect(
            280,
            245,
            840,
            70
        )

        pygame.draw.rect(
            pantalla,
            (8, 8, 35),
            caja,
            border_radius=25
        )

        pygame.draw.rect(
            pantalla,
            AMARILLO,
            caja,
            3,
            border_radius=25
        )

        texto = fuente_mensaje.render(
            mensaje,
            True,
            AMARILLO_BRILLO
        )

        pantalla.blit(
            texto,
            texto.get_rect(
                center=caja.center
            )
        )

    else:

        texto = fuente_pequena.render(
            "Haz clic en una flor 🌻",
            True,
            (190, 190, 220)
        )

        pantalla.blit(
            texto,
            texto.get_rect(
                center=(700, 850)
            )
        )

    # ================================================
    # PARTÍCULAS
    # ================================================

    actualizar_particulas()

    # ================================================
    # ACTUALIZAR
    # ================================================

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()