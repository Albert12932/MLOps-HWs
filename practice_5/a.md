docker build -t iris-trainer .
mkdir models
docker run -v ${PWD}\models:/app/models iris-trainer
docker run -e N_ESTIMATORS=500 -e TEST_SIZE=0.2 -e RANDOM_STATE=123 -v ${PWD}\models:/app/models iris-trainer

