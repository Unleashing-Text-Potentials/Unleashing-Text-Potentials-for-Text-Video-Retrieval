from config.base_config import Config
from datasets.model_transforms import init_transform_dict
from datasets.msrvtt_dataset import MSRVTTDataset
from datasets.lsmdc_dataset import LSMDCDataset
from datasets.didemo_dataset import DiDeMoDataset
from datasets.dataloader_activitynet_retrieval import ActivityNet_DataLoader
from torch.utils.data import DataLoader

class DataFactory:

    @staticmethod
    def get_data_loader(config: Config, split_type='train'):
        img_transforms = init_transform_dict(config.input_res)
        train_img_tfms = img_transforms['clip_train']
        test_img_tfms = img_transforms['clip_test']

        if config.dataset_name == "MSRVTT":
            if split_type == 'train':
                dataset = MSRVTTDataset(config, split_type, train_img_tfms)
                return DataLoader(dataset, batch_size=config.batch_size,
                           shuffle=True, num_workers=config.num_workers)
            else:
                dataset = MSRVTTDataset(config, split_type, test_img_tfms)
                return DataLoader(dataset, batch_size=config.batch_size,
                           shuffle=False, num_workers=config.num_workers)
        elif config.dataset_name == "ActivityNet":
            if split_type == 'train':
                dataset = ActivityNet_DataLoader(config, split_type, train_img_tfms)
                return DataLoader(dataset, batch_size=config.batch_size,
                        shuffle=True, num_workers=config.num_workers)
            else:
                dataset = ActivityNet_DataLoader(config, split_type, test_img_tfms)
                return DataLoader(dataset, batch_size=config.batch_size,
                        shuffle=False, num_workers=config.num_workers)    
          
        elif config.dataset_name == 'LSMDC':
            if split_type == 'train':
                dataset = LSMDCDataset(config, split_type, train_img_tfms)
                return DataLoader(dataset, batch_size=config.batch_size,
                            shuffle=True, num_workers=config.num_workers)
            else:
                dataset = LSMDCDataset(config, split_type, test_img_tfms)
                return DataLoader(dataset, batch_size=config.batch_size,
                            shuffle=False, num_workers=config.num_workers)

        elif config.dataset_name == "DiDeMo":
            if split_type == 'train':
                dataset = DiDeMoDataset(config, split_type, train_img_tfms)
                shuffle = True
                return DataLoader(dataset, batch_size=config.batch_size, shuffle=shuffle, num_workers=config.num_workers)
            else:
                dataset = DiDeMoDataset(config, split_type, test_img_tfms)
                shuffle = False
                return DataLoader(dataset, batch_size=config.batch_size, shuffle=shuffle, num_workers=config.num_workers)


        else:
            raise NotImplementedError
