class Departamento:
    def __init__(self, pNombre):
        self.nombre = pNombre
        self.municipios = []

    def agregarMunicipio(self, pMunicipio):
        self.municipios.append(pMunicipio)

    def darNombre(self):
        return self.nombre

    def darMunicipios(self):
        return self.municipios

    def darIngresoPromedio(self):
        totalMunicipios = len(self.municipios)
        suma = 0
        for municipio in self.municipios:
            suma += municipio.darIngresoPromedio()
        promedio = suma / totalMunicipios 
        return promedio

    def darPoblacion(self):
        total = 0
        for municipio in self.municipios:
            total += municipio.darPoblacion()
        return total

    def darTemperaturaMedia(self):
        totalMunicipios = len(self.municipios)
        suma = 0
        for municipio in self.municipios:
            suma += municipio.darTemperaturaMedia()
        promedio = suma / totalMunicipios
        return promedio

    def darTotalHombres(self):
        total = 0
        for municipio in self.municipios:
            total += municipio.darTotalHombres()
        return total

    def darTotalMujeres(self):
        total = 0
        for municipio in self.municipios:
            total += municipio.darTotalMujeres()
        return total

    def darEdadPromedio(self):
        totalMunicipios = len(self.municipios)
        suma = 0
        for municipio in self.municipios:
            suma += municipio.darEdadPromedio()
        promedio = suma / totalMunicipios
        return promedio