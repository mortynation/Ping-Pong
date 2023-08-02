#! /bin/bash -x

echo "Build host: $HOSTNAME"
echo "Build running on ${NODE_NAME}"
echo "$WORKSPACE"

CONTAINER_ID=$(docker ps --filter "name=pong_serv_cont" | awk '{print $1}' |grep -v CONTAINER)
echo $CONTAINER_ID
kill_container () {
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID
}

run_container () {
docker run -p 8090:80 -d --name pong_serv_cont pong_serv_image
}
docker build -f $WORKSPACE/Dockerfile -t pong_serv_image .
[ ! -z $CONTAINER_ID ] && kill_container
run_container
# Show running containers
docker ps
