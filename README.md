Pre-Entrega: Automatización de UI con Pytest y Selenium.

Este proyecto documenta la implementación de una suite de pruebas de automatización de interfaz de usuario para Sauce Demo, utilizando el patrón Page Object Model (POM).

🎯 Objetivo del Proyecto
El proyecto verifica la funcionalidad crítica de la aplicación, asegurando:

Login Exitoso: Validación de credenciales de usuario estándar.

Carga del Catálogo: Verificación de títulos, existencia de productos y formato de precios.

Flujo del Carrito: Capacidad para agregar un producto y navegar correctamente a la página del carrito.

🛠️ Stack Tecnológico

Python 3.x	
Pytest	
Selenium WebDriver	
WebDriver Manager	
pytest-html	Reporting	

📂 Estructura del Proyecto (POM)
El proyecto separa la lógica de prueba (en tests/) de la representación de la UI (en utils/).

.
├── tests/
│   └── test_sauceDemo.py      # Casos de prueba (login, catálogo, carrito).
└── utils/
    ├── login_page.py          # Page Object para el login.
    ├── catalog_page.py        # Page Object para el inventario.
    └── cart_page.py           # Page Object para el carrito.

🚀 Instalación y Ejecución

1. Configuración del Entorno
Se debe activar el entorno virtual y asegurar que las dependencias estén instaladas:

# Activar el entorno virtual (PowerShell)
.\venv\Scripts\Activate

# Instalar dependencias
pip install pytest selenium webdriver-manager pytest-html

2. Comando para Ejecutar las Pruebas

Ejecuta la suite de pruebas completa desde la raíz del proyecto para generar el reporte de resultados:

pytest -v --html=reporte.html tests/