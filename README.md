# python-challenge  
the client and the API have their own separate docker files 


to have both containers on the same network and not necessarily the same container run the following commands:

docker network create example  <br />
docker run -d --net example --name container1 <image>
docker run -d --net example --name container2 <image>
