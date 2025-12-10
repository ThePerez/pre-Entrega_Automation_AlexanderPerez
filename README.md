# 🚀 QA Automation Framework | Hybrid (UI + API)

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-Framework-brightgreen.svg)
![Selenium](https://img.shields.io/badge/Selenium-UI%20Automation-yellow.svg)
![Requests](https://img.shields.io/badge/Requests-API%20Testing-orange.svg)

Este repositorio contiene un framework de automatización de pruebas robusto y escalable, diseñado para validar tanto el Frontend (UI) como el Backend (API) de aplicaciones modernas. 

El proyecto implementa las mejores prácticas de la industria, incluyendo el patrón **Page Object Model (POM)**, inyección de dependencias con **Fixtures**, generación de reportes detallados con evidencia visual (**Screenshots automáticos**) y **Logging** centralizado.

---

## 🎯 Alcance del Proyecto

### 🖥️ UI Automation (Frontend)
Pruebas E2E sobre **SauceDemo (Swag Labs)** enfocadas en flujos críticos de negocio:
- **Autenticación:** Validación de usuarios estándar, bloqueados y credenciales inválidas (Parametrización).
- **Catálogo de Productos:** Verificación de inventario, precios e integridad de datos.
- **Carrito de Compras:** Flujo de agregar/remover ítems.
- **Checkout E2E:** Ciclo completo de compra (Datos de envío -> Resumen -> Finalización) con validaciones de éxito.

### 🔌 API Automation (Backend)
Pruebas de integración sobre **JSONPlaceholder** y **Restful-Booker**:
- **CRUD Completo:** Create, Read, Update (PATCH), Delete.
- **Ciclo de Vida del Dato:** Tests encadenados (E2E) donde se crea un recurso, se modifica y se elimina validando la persistencia.
- **Autenticación API:** Obtención y validación de Tokens de seguridad.
- **Validación de Esquemas:** Verificación de códigos de estado (200, 201, 204), headers y tiempos de respuesta (< 3s).

---

## 🛠️ Stack Tecnológico

| Herramienta | Uso Principal |
|-------------|---------------|
| **Python 3.x** | Lenguaje base del framework. |
| **Pytest** | Runner de pruebas, gestión de fixtures y aserciones. |
| **Selenium WebDriver** | Automatización de interacciones con el navegador. |
| **Requests** | Cliente HTTP para pruebas de API REST. |
| **WebDriver Manager** | Gestión automática de binarios (ChromeDriver). |
| **Pytest-HTML** | Generación de reportes visuales autocontenidos. |
| **Logging** | Registro detallado de la ejecución para depuración. |

---

## 📂 Arquitectura del Proyecto

La estructura sigue un diseño modular para facilitar el mantenimiento y la escalabilidad:

```text
proyecto/
├── logs/                   # Historial de ejecuciones (suite.log)
├── pages/                  # Page Objects (POM) - Abstracción de UI
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_information_page.py
│   └── checkout_overview_page.py
├── reports/                # Reportes HTML generados
│   └── screens/            # Capturas de pantalla de respaldo
├── tests/                  # Tests de UI (Frontend)
│   ├── conftest.py         # Configuración y Hooks de UI (Screenshots)
│   └── test_sauceDemo.py
├── tests_api/              # Tests de API (Backend)
│   ├── conftest.py         # Fixtures y Hooks de API
│   ├── test_login_api.py
│   ├── test_users_api.py
│   ├── test_create_user_api.py
│   └── test_post_lifecycle.py
├── utils/                  # Utilidades transversales
│   ├── api_utils.py
│   └── logger.py           # Configuración de Logging
├── pytest.ini              # Configuración global de Pytest
└── requirements.txt        # Dependencias del proyecto
