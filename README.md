# python-challenge  
the client and the API have their own separate docker files 

navigate to the client folder and run this command: <br />

*docker build -t client .*
 <br />
then  navigate to the api folder and run this command: <br />
*docker build -t api .*

 <br />
to have both containers on the same network and not necessarily the same container run the following commands:

docker network create example  <br />
docker run -d --net example --name container1 < image>  <br />
docker run -d --net example --name container2 < image> <br />
 <br />
 to access the API from the client you call an endpoint similar to this:  <br />
 < container-name>.example:< port>
 <br />
  <br />
  When testing the API please let me know so I whitelist the IP address 

  if you
 
