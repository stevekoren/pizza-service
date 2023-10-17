FROM python:3.11.4-slim-buster  as final

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
LABEL name="pizza-service" \
      vendor="hiredscore" \
      version="0.1" \
      release="0.1" \
      summary="pizza service" \
      description="sample pizza service"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_NAME pizza_service
ENV WORKDIR /app

WORKDIR ${WORKDIR}
COPY . ${WORKDIR}

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

RUN groupadd -g 1001 appuser && useradd -r -u 1001 -g appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
