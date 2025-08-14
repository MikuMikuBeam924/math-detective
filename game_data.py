EXERCISES = [
    # Álgebra
    {'id': 1, 'topic': 'Álgebra', 'question': 'Si 3x - 7 = 2, ¿cuál es el valor de x?', 'answer': 3, 'safe': 1},
    {'id': 2, 'topic': 'Álgebra', 'question': 'Si x/2 + 4 = 6, ¿x?', 'answer': 4, 'safe': 1},
    {'id': 3, 'topic': 'Álgebra', 'question': 'Si 2(x+1)=10, ¿x?', 'answer': 4, 'safe': 1},

    # Aritmética
    {'id': 4, 'topic': 'Aritmética', 'question': 'El banco mide 120 m de largo y su ancho es 30 m menor. Calcula la diagonal. ¿Cuál es la segunda cifra del resultado?', 'answer': 5, 'safe': 2},
    {'id': 5, 'topic': 'Aritmética', 'question': '¿Cuál es el último dígito de 7^3 (7 elevado a la 3)?', 'answer': 3, 'safe': 2},
    {'id': 6, 'topic': 'Aritmética', 'question': 'Suma: 28 + 16. ¿Cuál es el último dígito del resultado?', 'answer': 4, 'safe': 2},
    {'id': 7, 'topic': 'Aritmética', 'question': 'Si divides 45 entre 9, ¿cuál es el cociente?', 'answer': 5, 'safe': 3},

    # Geometría
    {'id': 8, 'topic': 'Geometría', 'question': 'La suma de los ángulos interiores de la caja fuerte es 360°. ¿Cuál es la primera cifra del resultado?', 'answer': 3, 'safe': 3},
    {'id': 9, 'topic': 'Geometría', 'question': 'Un cuadrado tiene lado 3 m. ¿Cuál es su perímetro? (último dígito)', 'answer': 2, 'safe': 3},
    {'id': 10, 'topic': 'Geometría', 'question': 'Triángulo con base 4 y altura 3, área = (base*altura)/2. ¿Cuál es el resultado?', 'answer': 6, 'safe': 4},
    {'id': 11, 'topic': 'Geometría', 'question': 'Si el radio es 7, el diámetro es ?. (último dígito)', 'answer': 4, 'safe': 4},

    # Estadística
    {'id': 12, 'topic': 'Estadística', 'question': 'Promedio 36.6, mediana 36.7, moda 37.2. Si sumas los tres obtienes 110.5. ¿Cuál es la primera cifra del resultado?', 'answer': 1, 'safe': 4},
    {'id': 13, 'topic': 'Estadística', 'question': 'Conjunto: [2,4,6,8]. ¿Cuál es la media aritmética? (último dígito)', 'answer': 5, 'safe': 5},
    {'id': 14, 'topic': 'Estadística', 'question': 'Moda del conjunto [1,2,2,3] es ?', 'answer': 2, 'safe': 5},
    {'id': 15, 'topic': 'Estadística', 'question': 'Mediana de [1,3,5] es ?', 'answer': 3, 'safe': 5},
]

SUSPECTS = [
    {'id': 'A', 'name': 'Alejandro Cruz', 'image': '/static/img/suspect1.jpg', 'description': 'Curador del museo'},
    {'id': 'B', 'name': 'Isabella Chen', 'image': '/static/img/suspect2.jpg', 'description': 'Visitante frecuente'},
    {'id': 'C', 'name': 'María López', 'image': '/static/img/suspect3.jpg', 'description': 'Guardia de seguridad'},
    {'id': 'D', 'name': 'Carlos Ruiz', 'image': '/static/img/suspect4.jpg', 'description': 'Restaurador de arte'},
]

SAFE_CLUES = {
    1: ['A_note'],
    2: ['B_note'],
    3: ['C_fiber'],
    4: ['D_ticket'],
    5: ['final_note']
}

CULPRIT = 'B'
