
> **🎯 Propósito:** Este documento define la estructura completa del repositorio, patrones de desarrollo, y arquitectura de sistemas para el proyecto de salvamento de vidas más avanzado de Europa.

---

## 📁 **ESTRUCTURA COMPLETA DEL REPOSITORIO**

```
AlertaCadiz-SalvemosVidas/
│
├── 📂 .github/                           # GitHub Actions y Templates
│   ├── workflows/
│   │   ├── ci-cd-pipeline.yml           # Pipeline CI/CD completo
│   │   ├── security-scan.yml            # Escaneo de vulnerabilidades
│   │   ├── performance-tests.yml        # Tests de rendimiento
│   │   ├── deploy-production.yml        # Despliegue automático
│   │   └── backup-database.yml          # Backup automático diario
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md               # Template reporte de bugs
│   │   ├── feature_request.md          # Template nueva funcionalidad
│   │   └── emergency_alert.md          # Template alerta crítica
│   └── PULL_REQUEST_TEMPLATE.md        # Template para PRs
│
├── 📂 docs/                             # Documentación Completa
│   ├── 📂 architecture/                # Arquitectura del Sistema
│   │   ├── system-overview.md          # Visión general
│   │   ├── microservices-design.md     # Diseño de microservicios
│   │   ├── database-schema.md          # Esquema de BD
│   │   ├── api-specification.md        # Especificación APIs
│   │   └── security-architecture.md    # Arquitectura de seguridad
│   ├── 📂 deployment/                  # Guías de Despliegue
│   │   ├── docker-setup.md            # Configuración Docker
│   │   ├── kubernetes-config.md       # Configuración K8s
│   │   ├── cloud-deployment.md        # Despliegue en cloud
│   │   └── monitoring-setup.md        # Configuración monitoreo
│   ├── 📂 user-guides/                # Guías de Usuario
│   │   ├── citizen-app-guide.md       # Guía app ciudadana
│   │   ├── authority-dashboard.md     # Panel autoridades
│   │   └── volunteer-handbook.md      # Manual voluntarios
│   └── 📂 scientific/                 # Documentación Científica
│       ├── seismic-algorithms.md      # Algoritmos sísmicos
│       ├── astronomical-correlations.md # Correlaciones astronómicas
│       └── tsunami-prediction-models.md # Modelos de predicción
│
├── 📂 src/                             # Código Fuente Principal
│   ├── 📂 backend/                     # Backend Services
│   │   ├── 📂 seismic-monitor/         # Servicio Monitoreo Sísmico
│   │   │   ├── app.py                 # Aplicación principal
│   │   │   ├── models/
│   │   │   │   ├── earthquake.py      # Modelo terremoto
│   │   │   │   ├── sensor.py          # Modelo sensor
│   │   │   │   └── alert.py           # Modelo alerta
│   │   │   ├── services/
│   │   │   │   ├── data_ingestion.py  # Ingesta de datos
│   │   │   │   ├── analysis_engine.py # Motor de análisis
│   │   │   │   └── prediction_ml.py   # ML para predicciones
│   │   │   ├── api/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py          # Rutas API
│   │   │   │   └── validators.py      # Validadores
│   │   │   ├── utils/
│   │   │   │   ├── logger.py          # Sistema de logs
│   │   │   │   ├── config.py          # Configuración
│   │   │   │   └── helpers.py         # Funciones auxiliares
│   │   │   ├── tests/
│   │   │   │   ├── test_models.py
│   │   │   │   ├── test_services.py
│   │   │   │   └── test_api.py
│   │   │   ├── requirements.txt       # Dependencias Python
│   │   │   └── Dockerfile            # Container seismic-monitor
│   │   │
│   │   ├── 📂 astronomical-analyzer/   # Servicio Análisis Astronómico
│   │   │   ├── app.py
│   │   │   ├── models/
│   │   │   │   ├── celestial_body.py  # Cuerpos celestes
│   │   │   │   ├── gravitational_force.py # Fuerzas gravitacionales
│   │   │   │   └── tidal_influence.py # Influencias mareales
│   │   │   ├── services/
│   │   │   │   ├── ephemeris_calculator.py # Cálculo efemérides
│   │   │   │   ├── gravitational_analyzer.py # Análisis gravitacional
│   │   │   │   └── correlation_engine.py # Motor correlaciones
│   │   │   ├── external_apis/
│   │   │   │   ├── nasa_horizons.py   # API NASA Horizons
│   │   │   │   ├── jpl_ephemeris.py   # API JPL
│   │   │   │   └── iers_service.py    # Servicio IERS
│   │   │   ├── algorithms/
│   │   │   │   ├── lunar_cycles.py    # Ciclos lunares
│   │   │   │   ├── planetary_alignment.py # Alineaciones planetarias
│   │   │   │   └── tidal_forces.py    # Fuerzas mareales
│   │   │   ├── tests/
│   │   │   ├── requirements.txt
│   │   │   └── Dockerfile
│   │   │
│   │   ├── 📂 alert-dispatcher/        # Servicio Dispatch de Alertas
│   │   │   ├── app.py
│   │   │   ├── models/
│   │   │   │   ├── alert_level.py     # Niveles de alerta
│   │   │   │   ├── communication_channel.py # Canales comunicación
│   │   │   │   └── target_audience.py # Audiencia objetivo
│   │   │   ├── services/
│   │   │   │   ├── alert_generator.py # Generador alertas
│   │   │   │   ├── message_composer.py # Compositor mensajes
│   │   │   │   └── dispatch_manager.py # Gestor de envíos
│   │   │   ├── channels/
│   │   │   │   ├── whatsapp_sender.py # Envío WhatsApp
│   │   │   │   ├── telegram_sender.py # Envío Telegram
│   │   │   │   ├── sms_sender.py      # Envío SMS
│   │   │   │   ├── social_media.py    # Redes sociales
│   │   │   │   ├── email_sender.py    # Envío email
│   │   │   │   └── push_notifications.py # Notificaciones push
│   │   │   ├── templates/
│   │   │   │   ├── emergency_messages/ # Mensajes emergencia
│   │   │   │   ├── alert_templates/   # Templates alertas
│   │   │   │   └── social_media_posts/ # Posts redes sociales
│   │   │   ├── tests/
│   │   │   ├── requirements.txt
│   │   │   └── Dockerfile
│   │   │
│   │   ├── 📂 user-management/         # Servicio Gestión de Usuarios
│   │   │   ├── app.py
│   │   │   ├── models/
│   │   │   │   ├── user.py            # Usuario
│   │   │   │   ├── subscription.py    # Suscripciones
│   │   │   │   ├── location.py        # Ubicaciones
│   │   │   │   └── preferences.py     # Preferencias
│   │   │   ├── services/
│   │   │   │   ├── authentication.py  # Autenticación
│   │   │   │   ├── authorization.py   # Autorización
│   │   │   │   ├── profile_manager.py # Gestor perfiles
│   │   │   │   └── geolocation.py     # Geolocalización
│   │   │   ├── api/
│   │   │   ├── tests/
│   │   │   ├── requirements.txt
│   │   │   └── Dockerfile
│   │   │
│   │   ├── 📂 data-analytics/          # Servicio Análisis de Datos
│   │   │   ├── app.py
│   │   │   ├── models/
│   │   │   │   ├── analytics_event.py # Eventos analytics
│   │   │   │   ├── metric.py          # Métricas
│   │   │   │   └── report.py          # Reportes
│   │   │   ├── services/
│   │   │   │   ├── data_collector.py  # Recolector datos
│   │   │   │   ├── metrics_calculator.py # Calculador métricas
│   │   │   │   ├── report_generator.py # Generador reportes
│   │   │   │   └── ml_predictor.py    # Predictor ML
│   │   │   ├── ml_models/
│   │   │   │   ├── tsunami_predictor.py # Predictor tsunami
│   │   │   │   ├── user_behavior.py   # Comportamiento usuario
│   │   │   │   └── alert_effectiveness.py # Efectividad alertas
│   │   │   ├── tests/
│   │   │   ├── requirements.txt
│   │   │   └── Dockerfile
│   │   │
│   │   └── 📂 api-gateway/             # Gateway API Principal
│   │       ├── app.py
│   │       ├── middleware/
│   │       │   ├── authentication.py  # Middleware auth
│   │       │   ├── rate_limiting.py   # Rate limiting
│   │       │   ├── logging.py         # Logging
│   │       │   └── cors.py            # CORS
│   │       ├── routes/
│   │       │   ├── public_api.py      # API pública
│   │       │   ├── admin_api.py       # API admin
│   │       │   └── internal_api.py    # API interna
│   │       ├── services/
│   │       │   ├── service_discovery.py # Descubrimiento servicios
│   │       │   ├── load_balancer.py   # Balanceador carga
│   │       │   └── health_checker.py  # Checker salud
│   │       ├── tests/
│   │       ├── requirements.txt
│   │       └── Dockerfile
│   │
│   ├── 📂 frontend/                    # Frontend Applications
│   │   ├── 📂 citizen-app/             # App Ciudadana (React Native)
│   │   │   ├── package.json
│   │   │   ├── App.js                 # Componente principal
│   │   │   ├── src/
│   │   │   │   ├── components/        # Componentes React Native
│   │   │   │   │   ├── AlertCard.js   # Tarjeta de alerta
│   │   │   │   │   ├── MapView.js     # Vista de mapa
│   │   │   │   │   ├── ProfileForm.js # Formulario perfil
│   │   │   │   │   └── EmergencyButton.js # Botón emergencia
│   │   │   │   ├── screens/           # Pantallas
│   │   │   │   │   ├── HomeScreen.js  # Pantalla principal
│   │   │   │   │   ├── AlertsScreen.js # Pantalla alertas
│   │   │   │   │   ├── MapScreen.js   # Pantalla mapa
│   │   │   │   │   ├── ProfileScreen.js # Pantalla perfil
│   │   │   │   │   └── SettingsScreen.js # Configuración
│   │   │   │   ├── services/          # Servicios
│   │   │   │   │   ├── ApiService.js  # Servicio API
│   │   │   │   │   ├── NotificationService.js # Notificaciones
│   │   │   │   │   ├── LocationService.js # Geolocalización
│   │   │   │   │   └── StorageService.js # Almacenamiento local
│   │   │   │   ├── utils/             # Utilidades
│   │   │   │   │   ├── constants.js   # Constantes
│   │   │   │   │   ├── helpers.js     # Funciones auxiliares
│   │   │   │   │   └── validators.js  # Validadores
│   │   │   │   ├── styles/            # Estilos
│   │   │   │   │   ├── colors.js      # Colores
│   │   │   │   │   ├── typography.js  # Tipografía
│   │   │   │   │   └── layout.js      # Layout
│   │   │   │   └── navigation/        # Navegación
│   │   │   │       ├── AppNavigator.js # Navegador principal
│   │   │   │       └── TabNavigator.js # Navegador tabs
│   │   │   ├── __tests__/             # Tests
│   │   │   ├── android/               # Configuración Android
│   │   │   ├── ios/                   # Configuración iOS
│   │   │   └── Dockerfile
│   │   │
│   │   ├── 📂 admin-dashboard/         # Dashboard Administrador (React)
│   │   │   ├── package.json
│   │   │   ├── public/
│   │   │   │   ├── index.html
│   │   │   │   └── manifest.json
│   │   │   ├── src/
│   │   │   │   ├── components/        # Componentes React
│   │   │   │   │   ├── Dashboard/     # Componentes dashboard
│   │   │   │   │   │   ├── MetricsCard.js # Tarjeta métricas
│   │   │   │   │   │   ├── AlertsTable.js # Tabla alertas
│   │   │   │   │   │   ├── SensorMap.js # Mapa sensores
│   │   │   │   │   │   └── UserActivity.js # Actividad usuarios
│   │   │   │   │   ├── Charts/        # Gráficos
│   │   │   │   │   │   ├── SeismicChart.js # Gráfico sísmico
│   │   │   │   │   │   ├── AstronomicalChart.js # Gráfico astronómico
│   │   │   │   │   │   └── UsageChart.js # Gráfico uso
│   │   │   │   │   ├── Forms/         # Formularios
│   │   │   │   │   │   ├── AlertForm.js # Formulario alerta
│   │   │   │   │   │   ├── UserForm.js # Formulario usuario
│   │   │   │   │   │   └── SensorForm.js # Formulario sensor
│   │   │   │   │   └── Common/        # Componentes comunes
│   │   │   │   │       ├── Header.js  # Cabecera
│   │   │   │   │       ├── Sidebar.js # Barra lateral
│   │   │   │   │       ├── Footer.js  # Pie
│   │   │   │   │       └── LoadingSpinner.js # Spinner carga
│   │   │   │   ├── pages/             # Páginas
│   │   │   │   │   ├── DashboardPage.js # Dashboard principal
│   │   │   │   │   ├── AlertsPage.js  # Página alertas
│   │   │   │   │   ├── UsersPage.js   # Página usuarios
│   │   │   │   │   ├── SensorsPage.js # Página sensores
│   │   │   │   │   ├── ReportsPage.js # Página reportes
│   │   │   │   │   └── SettingsPage.js # Configuración
│   │   │   │   ├── services/          # Servicios
│   │   │   │   ├── utils/             # Utilidades
│   │   │   │   ├── styles/            # Estilos CSS/SCSS
│   │   │   │   └── hooks/             # Custom Hooks
│   │   │   ├── __tests__/
│   │   │   └── Dockerfile
│   │   │
│   │   └── 📂 public-website/          # Sitio Web Público (Next.js)
│   │       ├── package.json
│   │       ├── next.config.js
│   │       ├── pages/
│   │       │   ├── index.js           # Página principal
│   │       │   ├── about.js           # Acerca de
│   │       │   ├── alerts.js          # Alertas públicas
│   │       │   ├── education.js       # Educación
│   │       │   ├── contact.js         # Contacto
│   │       │   └── api/               # API Routes
│   │       │       ├── alerts.js      # API alertas
│   │       │       └── status.js      # API estado
│   │       ├── components/
│   │       ├── styles/
│   │       ├── public/
│   │       ├── utils/
│   │       └── Dockerfile
│   │
│   ├── 📂 mobile/                      # Aplicaciones Móviles Nativas
│   │   ├── 📂 android/                 # App Android (Kotlin/Java)
│   │   │   ├── app/
│   │   │   │   ├── src/
│   │   │   │   │   ├── main/
│   │   │   │   │   │   ├── java/com/alertacadiz/
│   │   │   │   │   │   │   ├── MainActivity.kt
│   │   │   │   │   │   │   ├── services/
│   │   │   │   │   │   │   │   ├── NotificationService.kt
│   │   │   │   │   │   │   │   ├── LocationService.kt
│   │   │   │   │   │   │   │   └── ApiService.kt
│   │   │   │   │   │   │   ├── adapters/
│   │   │   │   │   │   │   ├── fragments/
│   │   │   │   │   │   │   ├── models/
│   │   │   │   │   │   │   └── utils/
│   │   │   │   │   │   ├── res/
│   │   │   │   │   │   │   ├── layout/
│   │   │   │   │   │   │   ├── values/
│   │   │   │   │   │   │   ├── drawable/
│   │   │   │   │   │   │   └── mipmap/
│   │   │   │   │   │   └── AndroidManifest.xml
│   │   │   │   │   └── test/
│   │   │   │   ├── build.gradle
│   │   │   │   └── proguard-rules.pro
│   │   │   ├── gradle/
│   │   │   ├── build.gradle
│   │   │   └── settings.gradle
│   │   │
│   │   └── 📂 ios/                     # App iOS (Swift)
│   │       ├── AlertaCadiz.xcodeproj/
│   │       ├── AlertaCadiz/
│   │       │   ├── AppDelegate.swift
│   │       │   ├── SceneDelegate.swift
│   │       │   ├── ViewControllers/
│   │       │   │   ├── MainViewController.swift
│   │       │   │   ├── AlertsViewController.swift
│   │       │   │   ├── MapViewController.swift
│   │       │   │   └── ProfileViewController.swift
│   │       │   ├── Services/
│   │       │   │   ├── NotificationService.swift
│   │       │   │   ├── LocationService.swift
│   │       │   │   └── ApiService.swift
│   │       │   ├── Models/
│   │       │   ├── Views/
│   │       │   ├── Utils/
│   │       │   └── Resources/
│   │       │       ├── Assets.xcassets/
│   │       │       └── Info.plist
│   │       └── AlertaCadizTests/
│   │
│   ├── 📂 iot-sensors/                 # Código para Sensores IoT
│   │   ├── 📂 seismic-sensor/          # Sensor Sísmico
│   │   │   ├── firmware/
│   │   │   │   ├── main.cpp           # Código principal Arduino/ESP32
│   │   │   │   ├── sensor_reader.cpp  # Lector de sensor
│   │   │   │   ├── data_transmitter.cpp # Transmisor datos
│   │   │   │   └── config.h           # Configuración
│   │   │   ├── libraries/             # Librerías específicas
│   │   │   ├── schematics/            # Esquemas electrónicos
│   │   │   └── 3d-models/             # Modelos 3D para impresión
│   │   │
│   │   ├── 📂 tidal-sensor/            # Sensor de Mareas
│   │   │   ├── firmware/
│   │   │   ├── calibration/
│   │   │   └── documentation/
│   │   │
│   │   └── 📂 communication-hub/       # Hub de Comunicaciones
│   │       ├── firmware/
│   │       ├── protocols/
│   │       └── testing/
│   │
│   ├── 📂 ml-models/                   # Modelos de Machine Learning
│   │   ├── 📂 tsunami-predictor/       # Predictor de Tsunamis
│   │   │   ├── data/
│   │   │   │   ├── raw/               # Datos en bruto
│   │   │   │   ├── processed/         # Datos procesados
│   │   │   │   └── external/          # Datos externos
│   │   │   ├── notebooks/             # Jupyter Notebooks
│   │   │   │   ├── exploratory_analysis.ipynb
│   │   │   │   ├── feature_engineering.ipynb
│   │   │   │   ├── model_training.ipynb
│   │   │   │   └── model_evaluation.ipynb
│   │   │   ├── src/
│   │   │   │   ├── data/
│   │   │   │   │   ├── make_dataset.py
│   │   │   │   │   └── preprocess.py
│   │   │   │   ├── features/
│   │   │   │   │   ├── build_features.py
│   │   │   │   │   └── feature_selection.py
│   │   │   │   ├── models/
│   │   │   │   │   ├── train_model.py
│   │   │   │   │   ├── predict_model.py
│   │   │   │   │   └── evaluate_model.py
│   │   │   │   └── visualization/
│   │   │   │       ├── visualize.py
│   │   │   │       └── plots.py
│   │   │   ├── models/                # Modelos entrenados
│   │   │   ├── reports/               # Reportes y métricas
│   │   │   └── requirements.txt
│   │   │
│   │   ├── 📂 astronomical-correlator/ # Correlador Astronómico
│   │   │   ├── data/
│   │   │   ├── notebooks/
│   │   │   ├── src/
│   │   │   ├── models/
│   │   │   └── requirements.txt
│   │   │
│   │   └── 📂 user-behavior/           # Análisis Comportamiento Usuario
│   │       ├── data/
│   │       ├── notebooks/
│   │       ├── src/
│   │       ├── models/
│   │       └── requirements.txt
│   │
│   └── 📂 shared/                      # Código Compartido
│       ├── 📂 utils/                   # Utilidades Comunes
│       │   ├── logger.py              # Sistema de logging
│       │   ├── config_manager.py      # Gestor configuración
│       │   ├── database_connector.py  # Conector BD
│       │   ├── cache_manager.py       # Gestor caché
│       │   ├── email_sender.py        # Envío emails
│       │   └── crypto_utils.py        # Utilidades criptográficas
│       ├── 📂 models/                  # Modelos de Datos Compartidos
│       │   ├── base_model.py          # Modelo base
│       │   ├── user_model.py          # Modelo usuario
│       │   ├── alert_model.py         # Modelo alerta
│       │   └── sensor_model.py        # Modelo sensor
│       ├── 📂 constants/               # Constantes del Sistema
│       │   ├── alert_levels.py        # Niveles de alerta
│       │   ├── sensor_types.py        # Tipos de sensores
│       │   ├── communication_channels.py # Canales comunicación
│       │   └── geographic_zones.py    # Zonas geográficas
│       └── 📂 validators/              # Validadores Comunes
│           ├── data_validators.py     # Validadores de datos
│           ├── input_sanitizers.py    # Sanitizadores entrada
│           └── format_checkers.py     # Checkers formato
│
├── 📂 infrastructure/                  # Infraestructura como Código
│   ├── 📂 docker/                     # Configuración Docker
│   │   ├── docker-compose.yml         # Compose desarrollo
│   │   ├── docker-compose.prod.yml    # Compose producción
│   │   ├── docker-compose.test.yml    # Compose testing
│   │   └── 📂 dockerfiles/            # Dockerfiles específicos
│   │       ├── Dockerfile.api-gateway
│   │       ├── Dockerfile.seismic-monitor
│   │       ├── Dockerfile.alert-dispatcher
│   │       └── Dockerfile.frontend
│   │
│   ├── 📂 kubernetes/                 # Configuración Kubernetes
│   │   ├── 📂 base/                   # Configuración base
│   │   │   ├── namespace.yaml
│   │   │   ├── configmap.yaml
│   │   │   ├── secrets.yaml
│   │   │   └── rbac.yaml
│   │   ├── 📂 services/               # Servicios K8s
│   │   │   ├── api-gateway.yaml
│   │   │   ├── seismic-monitor.yaml
│   │   │   ├── alert-dispatcher.yaml
│   │   │   └── databases.yaml
│   │   ├── 📂 ingress/                # Configuración Ingress
│   │   │   ├── api-ingress.yaml
│   │   │   └── web-ingress.yaml
│   │   └── 📂 monitoring/             # Monitoreo K8s
│   │       ├── prometheus.yaml
│   │       ├── grafana.yaml
│   │       └── alertmanager.yaml
