# DeepCNNClassifierProject

## workflow 

1. Update config.yaml
2. Update secrets.yaml 
3. Update params.yaml
4. Update the entity -> src/entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline
9. Run tox for testing package
10. Update the dvc.yaml -> same as main.py
11. run "dvc repro" for runnig all the stages in pipeline


MLFLOW_TRACKING_URI=https://dagshub.com/dibakar75/DeepCNNClassifierProject.mlflow \
MLFLOW_TRACKING_USERNAME=dibakar75 \
MLFLOW_TRACKING_PASSWORD=08c9c19bc9a213f095bcd2d4848e418544d69576 \
python script.py

## Sample data fro testing only
https://raw.githubusercontent.com/dibakar75/all_datasets/main/sample_data.zip