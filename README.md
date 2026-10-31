# Sistema de Gestión de Productos
Laboratorio de Aseguramiento de la Calidad del Software.

## Ejecutar
```bash
python main.py
```
## Pruebas
```bash
python -m pytest -v
```
Los productos se almacenan únicamente en memoria. No se requiere base de datos.

## SonarQube Cloud
Reemplazar `sonar.projectKey` y `sonar.organization` en `sonar-project.properties` y agregar el secreto `SONAR_TOKEN` en GitHub Actions. Crear ramas `produccion` y `desarrollo` y enviar un cambio a `desarrollo`.
