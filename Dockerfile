# Imagen base
FROM python:3.14-slim

RUN addgroup --system appgroup && adduser --system --group appuser



# Establece el directorio de trabajo
WORKDIR /app

# Copia el script al contenedor
COPY app.py .


# Instala Flask
RUN pip install flask
RUN pip install requests

RUN chown -R appuser:appgroup /app

USER appuser
# Expone el puerto en el que corre la app
EXPOSE 3000

# Comando por defecto para ejecutar la app
CMD ["python", "app.py"]
