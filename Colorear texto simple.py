import sys

def gradient_text(text, start_color, end_color, steps):
    def interpolate_color(start, end, t):
        return tuple(int(start[i] + (end[i] - start[i]) * t) for i in range(3))

    def format_rgb(rgb):
        return f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m'

    # Convert start and end colors from RGB tuples
    start_color = [int(c) for c in start_color]
    end_color = [int(c) for c in end_color]

    for i in range(steps):
        t = i / (steps - 1)  # Normalizar t entre 0 y 1
        color = interpolate_color(start_color, end_color, t)
        sys.stdout.write(format_rgb(color) + text[i % len(text)])
    print('\033[0m')  # Resetea el color a por defecto

# Preguntar al usuario por el texto a colorear
text = input("Introduce el texto que deseas colorear: ")

# Definir los colores de inicio y final (en RGB)
start_color = input("Introduce el primer color (en RGB, por ejemplo 255,0,0 para rojo): ").split(',')
end_color = input("Introduce el segundo color (en RGB, por ejemplo 0,255,0 para verde): ").split(',')
steps = len(text)

# Convertir a listas de enteros
start_color = [int(c.strip()) for c in start_color]
end_color = [int(c.strip()) for c in end_color]

gradient_text(text, start_color, end_color, steps)
