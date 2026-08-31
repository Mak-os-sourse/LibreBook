FROM node:alpine AS Frontend
WORKDIR /app
COPY . .

RUN npm i --omit=dev
RUN npm run build

FROM ghcr.io/astral-sh/uv:alpine AS Backend
WORKDIR /app
COPY . .
COPY --from=Frontend /app/dist /app/dist
RUN apk update && apk add libmagic file-dev tzdata
RUN uv sync --no-dev

CMD ["uv", "run", "backend/manage.py", "runserver", "0.0.0.0:8000"]

FROM nginx:alpine AS Nginx
COPY --from=Frontend /app/dist /dist
COPY /nginx/default.conf /etc/nginx/conf.d/default.conf