from Departamento import Departamento

class Censo:
    TOTAL_DEPARTAMENTOS = 32
    
    def __init__(self):
        self.departamentos = [0] * self.TOTAL_DEPARTAMENTOS
        self.DEPTO()

    def DEPTO(self):
        nombresDepartamentos = ["Amazonas", "Antioquia", "Arauca", "Atlántico", "Bolivar", "Boyacá", "Caldas",
                                 "Caquetá", "Casanare", "Cauca", "Cesar", "Chocó", "Córdoba", "Cundinamarca",
                                 "Guainía", "Guajira", "Guaviare", "Huila", "Magdalena", "Meta", "Nariño",
                                 "Norte de Santander", "Putumayo", "Quindío", "Risaralda", "San Andrés y Providencia",
                                 "Santander", "Sucre", "Tolima", "Valle Del Cauca", "Vaupés", "Vichada"]
        for i, nombre in enumerate(nombresDepartamentos):
            self.departamentos[i] = Departamento(nombre)

    def darDepartamento(self, pPosicion):
        return self.departamentos[pPosicion]

    def darIngresoPromedio(self):
        suma = 0
        totalDepartamentos = 0
        for dpto in self.departamentos:
            if dpto.darPoblacion() > 0:
                suma += dpto.darIngresoPromedio()
                totalDepartamentos += 1
        promedio = suma / totalDepartamentos
        return promedio

    def darPoblacion(self):
        total = 0
        for dpto in self.departamentos:
            total += dpto.darPoblacion()
        return total

    def darTemperaturaMedia(self):
        suma = 0
        totalDepartamentos = 0
        for dpto in self.departamentos:
            if dpto.darPoblacion() > 0:
                suma += dpto.darTemperaturaMedia()
                totalDepartamentos += 1
        promedio = suma / totalDepartamentos
        return promedio

    def darTotalHombres(self):
        total = 0
        for dpto in self.departamentos:
            total += dpto.darTotalHombres()
        return total

    def darTotalMujeres(self):
        total = 0
        for dpto in self.departamentos:
            total += dpto.darTotalMujeres()
        return total

    def darEdadPromedio(self):
        suma = 0
        totalDepartamentos = 0
        for dpto in self.departamentos:
            if dpto.darPoblacion() > 0:
                suma += dpto.darEdadPromedio()
                totalDepartamentos += 1
        promedio = suma / totalDepartamentos
        return promedio

    def existeDptoIngresoSuperior(self, pValor):
        existe = False
        for dpto in self.departamentos:
            if dpto.darPoblacion() > 0 and dpto.darIngresoPromedio() > pValor:
                existe = True
        return existe

    def existenDosDptosIgualPoblacion(self):
        existe = False
        for i in range(len(self.departamentos)):
            dpto1 = self.departamentos[i]
            for i2 in range(i + 1, len(self.departamentos)):
                dpto2 = self.departamentos[i2]
                if dpto1.darPoblacion() == dpto2.darPoblacion() and dpto1.darPoblacion() != 0:
                    existe = True
        return existe