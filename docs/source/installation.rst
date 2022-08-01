Installation
==============
Use the following commands to build the project::

    docker build -t kalmanfilterpython .
    docker run -d -it --user dev --name kalmanfilterpythondev --mount type=bind,source="$(pwd)",target=/home/dev/app kalmanfilterpython
    docker exec -it kalmanfilterpythondev /bin/bash
    cd home/app
    ./build-test.sh
