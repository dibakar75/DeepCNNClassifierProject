import pytest
from deepClassifier.entity import PrepareBaseModelConfig
from deepClassifier.components import PrepareBaseModel
from pathlib import Path
import os

class Test_DataIngestion_download:
    data_ingestion_config = DataIngestionConfig(
        root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES)

    def test_download(self):
        data_ingestion = DataIngestion(config=self.data_ingestion_config)
        data_ingestion.download_file()
        assert os.path.exists(self.data_ingestion_config.local_data_file)


class Test_DataIngestion_unzip:
    data_ingestion_config = DataIngestionConfig(
        root_dir="tests/data/", 
        source_URL="", 
        local_data_file="tests/data/sample_data.zip", 
        unzip_dir="tests/data/")

    def test_unzip(self):
        data_ingestion = DataIngestion(config=self.data_ingestion_config)
        data_ingestion.unzip_and_clean()
        assert os.path.isdir(Path("tests/data/PetImages"))
        assert os.path.isdir(Path("tests/data/PetImages/Cat"))
        assert os.path.isdir(Path("tests/data/PetImages/Dog"))