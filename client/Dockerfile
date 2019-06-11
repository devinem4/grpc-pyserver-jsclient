FROM grpcmatt/common

COPY . .

RUN protoc -I=. echo.proto \
--js_out=import_style=commonjs:. \
--grpc-web_out=import_style=commonjs,mode=grpcwebtext:.

RUN npm install && \
  npx webpack && \
  cp echotest.html /var/www/html && \
  cp dist/main.js /var/www/html/dist

EXPOSE 8081
WORKDIR /var/www/html
CMD ["python", "-m", "SimpleHTTPServer", "8081"]
