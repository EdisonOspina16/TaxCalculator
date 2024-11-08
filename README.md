# Tax Calculator
El proyecto "Calculadora de Impuestos" tiene como objetivo desarrollar una aplicación para calcular la declaración del Impuesto sobre la Renta de un empleado. La solicitud tendrá en cuenta diversos insumos, como ingresos del trabajo, otros ingresos, retenciones, pagos de seguridad social, aportes a pensiones, préstamos hipotecarios, donaciones y gastos de educación del año. Con esta información calcularás los ingresos gravados y no gravados, los costos deducibles y finalmente determinarás el monto a pagar por concepto de impuesto a la renta. Esta herramienta facilitará a los empleados el cálculo y la presentación de su declaración anual del impuesto sobre la renta.

## Datos necesarios para la ejecucion
- Total de ingresos laborales en el año: Representa la suma acumulada de los salarios percibidos a lo largo de todo el año.

- Valor otros ingresos gravables: Comprende aquellos ingresos que, de acuerdo con la legislación colombiana, están sujetos a un porcentaje de impuestos. Esto incluye fuentes como loterías, negocios, inversiones, alquileres, entre otros.

- Valor otros ingresos no gravables: Son aquellos que no están sujetos a un porcentaje de impuesto según la legislación. Ejemplos de estos ingresos incluyen subsidios, indemnizaciones, herencias, donaciones, entre otros.

- Valor retencion en la fuente al año: Representa la cantidad total retenida en concepto de impuestos a lo largo del año.

- Pago créditos hipoteca en el año: Es un deducible que abarca todos los gastos relacionados con la vivienda, incluyendo seguros y préstamos hipotecarios.

- Valor donaciones en el año: Es una deducción que se refiere a las contribuciones que has realizado a lo largo del año en forma de donaciones.

- Gastos en educación en el año: Representan una deducción relacionada con los costos asociados a la educación durante el período anual.

## Datos resultantes de la ejecucion
- Total de ingresos gravados: (Ingresos laborales + otros ingresos gravados + otros ingresos no gravables) – otros ingresos gravables.
- Total ingresos no gravables: Todos los ingresos no gravables del año.
- Total costos deducibles: pago seguridad social + aportes pensión en el año + pago créditos hipotecarios en el año + valor donaciones en al año + gastos educación en el año.
- Valor a pagar por impuesto de renta: Se refiere a la cantidad total que debe abonarse como impuesto de renta.
- Este monto está determinado por porcentajes variables que se definen en función de la cantidad total de ingresos gravables percibidos.

## Como funciona 

### Modificación de parámetros
En la opción de modificar parámetros, puedes ajustar los valores que se utilizan en los cálculos de la calculadora de impuestos. Por ejemplo, puedes cambiar el porcentaje de impuestos sobre la renta, deducciones permitidas, créditos fiscales, entre otros. Para hacer esto, simplemente selecciona la opción de modificar parámetros en el menú, luego ingresa el nuevo valor para el parámetro que deseas cambiar.

### Manejo de porcentajes
En la calculadora, los porcentajes se manejan como valores decimales. Por ejemplo, un 30% se representa como 0.30. Esto se debe a que en matemáticas, un porcentaje es una forma de representar una fracción con denominador 100. Entonces, 30% es lo mismo que 30/100, lo que equivale a 0.30.

Ejemplo de uso de la calculadora con un salario
Supongamos que estás calculando los impuestos sobre un ingreso anual de $60,000,000 COP.

Ingresar el ingreso bruto: Primero, debes ingresar el ingreso bruto anual, en este caso $60,000,000 COP.

**Aplicar deducciones**: Supongamos que tienes deducciones permitidas por $10,000,000 COP. Estas deducciones se restarán del ingreso bruto, dejando un ingreso imponible de $50,000,000 COP.

**Calcular el impuesto sobre la renta**: Usando la calculadora, se aplicará el porcentaje correspondiente al ingreso imponible. Supongamos que la tasa de impuesto sobre la renta es del 20%. El impuesto calculado sería $10,000,000 COP.

**Aplicar créditos fiscales**: Si tienes créditos fiscales por $2,000,000 COP, estos se restarán del impuesto sobre la renta calculado, resultando en un impuesto neto de $8,000,000 COP.

**Resultado final**: El monto final de impuestos a pagar sería de $8,000,000 COP.

Este proceso simplificado te permite calcular rápidamente el monto de impuestos que necesitas pagar con base en tus ingresos, deducciones y créditos fiscales.


# ¿Como lo hago funcionar-ejecutar?

## Configurar el secret configt
Primero debes de crear un servidor en la web de la base de datos de su preferencia, nosotros te recomendamos neon.tech,
luego de crear la base de datos debes de obtener la coneccion a esta y debes de pegarlo en el SecretConfig-sample.py.
Con esto ya listo puedes tener tu base de datos y ejecutar correctamente la app con la base de datos.

## Dependencias
- ` pip install psycopg2`
- `pip install flask`

### Pruebas unitarias
- `python testMVC\TaxCalculator_test.py`

### Correr la app
- `python app.py`


## ¿Quien hizo esto?
- Edison Ospina Arroyave.
- Juan Diego Usuga
