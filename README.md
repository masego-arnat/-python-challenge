# python-challenge  
the client and the API have their own separate docker files 


to have both containers on the same network and not necessarily the same container run the following commands:

docker network create example  <br />
docker run -d --net example --name container1 <image>  <br />
docker run -d --net example --name container2 <image> <br />
 <br />
 to access the API from the client you call an endpoint similar to this:  <br />
 <container-name>.example:<port>

 
