# Abstracta Automation Web

Este repositorio contiene un proyecto de automatización de pruebas web utilizando **Selenium** con **Python** y **Behave**, junto con **Allure Reports** como gestor de reportes.

## Requisitos previos

Antes de clonar este repositorio, asegúrate de cumplir con los siguientes requisitos:

- **Python 3.8 o superior**
- **Pip** para la gestión de paquetes de Python
- **Google Chrome** y el correspondiente driver de Chrome (Chromedriver)
- **Git** para clonar el repositorio
- **Allure** instalado para generar reportes

## Instalación

Sigue estos pasos para clonar y configurar el proyecto:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/RulosHD/Abstracta_Automation_Web.git
   ```

2. **Accede al directorio del proyecto:**

   ```bash
   cd Abstracta_Automation_Web
   ```

3. **Crea un entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate # En Windows usa: venv\Scripts\activate
   ```

4. **Instala las dependencias:**

   Ejecuta el siguiente comando para instalar las dependencias definidas en `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. **Verifica la instalación de Allure:**

   Asegúrate de que Allure está instalado y configurado correctamente. Puedes verificarlo con:

   ```bash
   allure --version
   ```

## Uso

### Ejecución de pruebas

1. Ejecuta las pruebas con el siguiente comando:

   ```bash
   behave
   ```

### Generación de reportes

1. Después de ejecutar las pruebas, los resultados estarán disponibles en el directorio `reports`.
2. Para generar y visualizar los reportes de Allure:

   ```bash
   allure serve reports
   ```

## Estructura del Proyecto

- **features:** Contiene los archivos `.feature` con los escenarios de prueba.
- **steps:** Implementación de los pasos definidos en los escenarios.
- **config:** Archivos de configuración del proyecto.
- **reports:** Carpeta donde se generan los resultados y reportes de las pruebas.
- **drivers:** Contiene el driver de Chrome necesario para Selenium.

## Contribuciones

Si deseas contribuir a este proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección de errores:

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. Realiza tus cambios y haz un commit:

   ```bash
   git commit -m "Descripción de los cambios realizados"
   ```

4. Haz push a tu rama:

   ```bash
   git push origin feature/nueva-funcionalidad
   ```

5. Crea un Pull Request detallando los cambios realizados.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

## Contacto

Si tienes dudas o problemas con el proyecto, no dudes en abrir un **issue** o contactar al administrador del repositorio.
