FROM grpcmatt/common

COPY . ./server/node

RUN cd ./server/node && \
  npm install

EXPOSE 9090
CMD ["node", "./server/node/server.js"]