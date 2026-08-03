## Configuración del proyecto

Este proyecto utiliza variables de entorno para gestionar datos sensibles (como `SECRET_KEY` y credenciales de base de datos), evitando exponerlos en el control de versiones.

### Requisitos previos

- Python 3.x
- pip

### Instalación

1. Cloná el repositorio:
```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
```

2. Creá y activá un entorno virtual:
```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalá las dependencias:
```bash
   pip install -r requirements.txt
```

4. Creá un archivo `.env` en la raíz del proyecto, usando `.env.example` como referencia, y completá tus propios valores:

5. Ejecutá el servidor de desarrollo:
```bash
   python manage.py runserver
```

### Seguridad

Las credenciales y claves sensibles se gestionan mediante `python-decouple` y un archivo `.env` (excluido del repositorio vía `.gitignore`), siguiendo buenas prácticas de seguridad en proyectos Django.