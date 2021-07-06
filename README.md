# madlibs

To test, open terminal, cd to a folder of your choice, and copy/paste the following....

cd madlibs  
git clone https://github.com/jakekirsch2/madlibs.git  
docker build -t madlibs .  
docker run -dp 5000:5000 madlibs-run  


To test navigate to docker cli and run pytest, then navigate to http://localhost:5000/madlib to see result
