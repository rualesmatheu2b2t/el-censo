from Censo import Censo
from Municipio import Municipio
import pytest

@pytest.fixture
def setup_escenario1():
    censo = Censo()
    return censo

@pytest.fixture
def setup_escenario2():
    censo = Censo()

    municipio = Municipio()
    municipio.asignarNombre("Silver")
    municipio.asignarPoblacion(150)
    municipio.asignarTotalHombres(70)
    municipio.asignarEdadPromedio(49)
    municipio.asignarIngresoPromedio(500000)
    municipio.asignarTemperaturaMedia(30)
    censo.darDepartamento(5).agregarMunicipio(municipio)

    municipio2 = Municipio()
    municipio2.asignarNombre("Silver2")
    municipio2.asignarPoblacion(200)
    municipio2.asignarTotalHombres(190)
    municipio2.asignarEdadPromedio(13)
    municipio2.asignarIngresoPromedio(600000)
    municipio2.asignarTemperaturaMedia(22)
    censo.darDepartamento(25).agregarMunicipio(municipio2)

    return censo

def test_inicializacion(setup_escenario1):
    censo = setup_escenario1
    for i in range(Censo.TOTAL_DEPARTAMENTOS):
        assert censo.darDepartamento(i) is not None, f"El departamento {i} debe estar inicializado"
    assert censo.darPoblacion() == 0, "La población debe ser 0"
    assert censo.darTotalHombres() == 0, "El total de hombres debe ser 0"
    assert censo.darTotalMujeres() == 0, "El total de mujeres debe ser 0"

def test_poblacion(setup_escenario2):
    censo = setup_escenario2
    assert censo.darPoblacion() == 350, "La población es incorrecta"

def test_total_hombres(setup_escenario2):
    censo = setup_escenario2
    assert censo.darTotalHombres() == 260, "El total de hombres es incorrecto"

def test_total_mujeres(setup_escenario2):
    censo = setup_escenario2
    assert censo.darTotalMujeres() == 90, "El total de mujeres es incorrecto"

def test_edad_promedio(setup_escenario2):
    censo = setup_escenario2
    assert censo.darEdadPromedio() == 31, "La edad promedio es incorrecta"

def test_ingreso_promedio(setup_escenario2):
    censo = setup_escenario2
    assert censo.darIngresoPromedio() == 550000, "El ingreso promedio es incorrecto"

def test_temperatura(setup_escenario2):
    censo = setup_escenario2
    assert censo.darTemperaturaMedia() == 26, "La temperatura media es incorrecta"

def test_existe_dpto_ingreso_inferior(setup_escenario2):
    censo = setup_escenario2
    assert not censo.existeDptoIngresoSuperior(600000), "No debe haber departamentos con ingreso superior a 600000"
    assert censo.existeDptoIngresoSuperior(500000), "Debe haber departamentos con ingreso superior a 500000"
    assert censo.existeDptoIngresoSuperior(0), "Debe haber departamentos con ingreso superior a 0"

def test_dos_dptos_igual_poblacion(setup_escenario1):
    censo = setup_escenario1
    assert not censo.existenDosDptosIgualPoblacion(), "No debe haber departamentos con igual población inicialmente"

    municipio = Municipio()
    municipio.asignarNombre("Municipio")
    municipio.asignarPoblacion(100000)
    censo.darDepartamento(5).agregarMunicipio(municipio)
    assert not censo.existenDosDptosIgualPoblacion(), "No debe haber departamentos con igual población"

   
