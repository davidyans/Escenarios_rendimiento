class Cronograma:
    def __init__(self, nombre_materia, grupo):
        self.nombre_materia = nombre_materia
        self.grupo = grupo
        self.tiempo_en_semanas = []
        self.temas = []
        self.completados = []
        self.tema_i = 0

    def agregar_tema(self, temas):
        self.temas = temas
        self.llenar_arreglo_completados()

    def agregar_semanas(self, tiempo_en_semanas):
        self.tiempo_en_semanas = tiempo_en_semanas

    def llenar_arreglo_completados(self):
        self.completados = [False] * len(self.temas)  # Inicializa la lista con False

    def chequear_tema(self):
        self.completados[self.tema_i] = True
        self.tema_i += 1


class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cronogramas = []
        self.estado = ""

    def registrar_cronograma(self, cronograma: Cronograma):
        self.cronogramas.append(cronograma)

    def proyeccion_ideal_definida(self):
        # Lógica para verificar si la proyección ideal está definida
        return True

    def marcar_tema_visto(self, nombre_materia, grupo):
        for cronograma in self.cronogramas:
            if cronograma.nombre_materia == nombre_materia and cronograma.grupo == grupo:
                cronograma.chequear_tema()
                #print(cronograma.completados)
                return cronograma.tema_i - 1  # para devolver el id del tema que se marco recien

    def progreso_semanal_registrado(self, id_tema, nombre_materia, grupo):
        for cronograma in self.cronogramas:
            if cronograma.nombre_materia == nombre_materia and cronograma.grupo == grupo:
                return cronograma.completados[id_tema]

        return False

    def visualizar_progreso(self, semana_actual, nombre_materia, grupo):
        cronograma_materia = []

        for cronograma in self.cronogramas:
            if cronograma.nombre_materia == nombre_materia and cronograma.grupo == grupo:
                cronograma_materia = cronograma

        index_tema = -1
        for i in range(semana_actual):
            index_tema += 1
            semana_actual = semana_actual - cronograma_materia.tiempo_en_semanas[i]

            if semana_actual <= 0: break

        if index_tema == len(cronograma_materia.completados):
            if cronograma_materia.completados[index_tema]:
                self.estado = "normal"
                return "Todos los temas hasta la semana actual están marcados"
            else:
                self.estado = "atrasado"
                return "Faltan temas por marcar en la semana actual"
        else:
            if (cronograma_materia.completados[index_tema]
                    and cronograma_materia.completados[index_tema + 1]):
                self.estado = "adelantado"
                return "Temas de semanas futuras están marcados"
            elif (cronograma_materia.completados[index_tema]
                  and not cronograma_materia.completados[index_tema + 1]):
                self.estado = "normal"
                return "Todos los temas hasta la semana actual están marcados"
            else:
                self.estado = "atrasado"
                return "Faltan temas por marcar en la semana actual"
