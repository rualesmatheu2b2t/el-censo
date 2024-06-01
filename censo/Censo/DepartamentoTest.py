from Departamento import Departamento
from Municipio import Municipio
import pytest

@pytest.fixture
def setup_escenario1():
    departamento = Departamento("Changai")
    return departamento

@pytest.fixture
def setup_escenario2():
    departamento = Departamento("Changai")

    municipio1 = Municipio()
    municipio1.asignarNombre("Silver")
    municipio1.asignarPoblacion(150)
    municipio1.asignarTotalHombres(70)
    municipio1.asignarEdadPromedio(49)
    municipio1.asignarIngresoPromedio(500000)
    municipio1.asignarTemperaturaMedia(30)

    departamento.agregarMunicipio(municipio1)

    municipio2 = Municipio()
    municipio2.asignarNombre("Silver2")
    municipio2.asignarPoblacion(200)
    municipio2.asignarTotalHombres(190)
    municipio2.asignarEdadPromedio(13)
    municipio2.asignarIngresoPromedio(600000)
    municipio2.asignarTemperaturaMedia(22)

    departamento.agregarMunicipio(municipio2)

    return departamento

def test_inicializacion(setup_escenario1):
    departamento = setup_escenario1
    assert departamento.darNombre() == "Changai", "El nombre es incorrecto"
    assert departamento.darMunicipios() is not None, "Debe inicializar el ArrayList de municipios"
    assert departamento.darPoblacion() == 0, "La población debe ser 0"
    assert departamento.darTotalHombres() == 0, "El total de hombres debe ser 0"
    assert departamento.darTotalMujeres() == 0, "El total de mujeres debe ser 0"

def test_poblacion(setup_escenario2):
    departamento = setup_escenario2
    assert departamento.darPoblacion() == 350, "La población es incorrecta"

def test_total_hombres(setup_escenario2):
    departamento = setup_escenario2
    assert departamento.darTotalHombres() == 260, "El total de hombres es incorrecto"

def test_total_mujeres(setup_escenario2):
    departamento = setup_escenario2
    assert departamento.darTotalMujeres() == 90, "El total de mujeres es incorrecto"

def test_edad_promedio(setup_escenario2):
    departamento = setup_escenario2
    assert departamento.darEdadPromedio() == 31, "La edad promedio es incorrecta"

def test_ingreso_promedio(setup_escenario2):
    departamento = setup_escenario2
    assert departamento.darIngresoPromedio() == 550000, "El ingreso promedio es incorrecto"

def test_temperatura(setup_escenario2):
    departamento = setup_escenario2
    assert departamento.darTemperaturaMedia() == 26, "La temperatura media es incorrecta"
