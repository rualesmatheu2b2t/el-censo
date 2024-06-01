class Municipio:
    def __init__(self):
        self.nombre = ""
        self.poblacion = 0
        self.totalHombres = 0
        self.edadPromedio = 0
        self.ingresoPromedio = 0
        self.temperaturaMedia = 0

    def darIngresoPromedio(self):
        return self.ingresoPromedio

    def asignarIngresoPromedio(self, pIngresoPromedio):
        self.ingresoPromedio = pIngresoPromedio

    def darNombre(self):
        return self.nombre

    def asignarNombre(self, pNombre):
        self.nombre = pNombre

    def darPoblacion(self):
        return self.poblacion

    def asignarPoblacion(self, pPoblacion):
        self.poblacion = pPoblacion

    def darTemperaturaMedia(self):
        return self.temperaturaMedia

    def asignarTemperaturaMedia(self, pTemperaturaMedia):
        self.temperaturaMedia = pTemperaturaMedia

    def darTotalHombres(self):
        return self.totalHombres

    def darTotalMujeres(self):
        totalMujeres = self.poblacion - self.totalHombres
        return totalMujeres

    def asignarTotalHombres(self, pTotalHombres):
        self.totalHombres = pTotalHombres

    def darEdadPromedio(self):
        return self.edadPromedio

    def asignarEdadPromedio(self, pEdadPromedio):
        self.edadPromedio = pEdadPromedio
