from Municipio import Municipio
import pytest

@pytest.fixture
def setup_escenario1():
    municipio = Municipio()
    return municipio

def test_nombre(setup_escenario1):
    municipio = setup_escenario1
    municipio.asignarNombre("Furby")
    assert municipio.darNombre() == "Furby", "El nombre es incorrecto"

def test_poblacion(setup_escenario1):
    municipio = setup_escenario1
    municipio.asignarPoblacion(53)
    assert municipio.darPoblacion() == 53, "La población es incorrecta"

def test_total_hombres(setup_escenario1):
    municipio = setup_escenario1
    municipio.asignarTotalHombres(53)
    assert municipio.darTotalHombres() == 53, "El total de hombres es incorrecto"

def test_total_mujeres(setup_escenario1):
    municipio = setup_escenario1
    municipio.asignarPoblacion(100)
    municipio.asignarTotalHombres(53)
    assert municipio.darTotalMujeres() == 47, "El total de mujeres es incorrecto"

def test_edad_promedio(setup_escenario1):
    municipio = setup_escenario1
    municipio.asignarEdadPromedio(52)
    assert municipio.darEdadPromedio() == 52, "La edad promedio es incorrecta"

def test_ingreso_promedio(setup_escenario1):
    municipio = setup_escenario1
    municipio.asignarIngresoPromedio(100001)
    assert municipio.darIngresoPromedio() == 100001, "El ingreso promedio es incorrecto"

def test_temperatura(setup_escenario1):
    municipio = setup_escenario1
    municipio.asignarTemperaturaMedia(28)
    assert municipio.darTemperaturaMedia() == 28, "La temperatura media es incorrecta"
