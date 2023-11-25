from typing import TYPE_CHECKING

from deep_utils.dummy_objects.dummy_framework import LazyModule, is_groundingdino_available
from .utils.lib_utils.integeration_utils import import_lazy_module

# Deep Utils version number
__version__ = "1.3.0"

from .utils.constants import DUMMY_PATH, Backends

# no third-party python libraries are required for the following classes
_import_structure = {
    "utils.box_utils.boxes": ["Box", "Point"],
    "utils.box_utils.box_dataclasses": ["BoxDataClass", "PointDataClass"],
    "utils.os_utils.os_path": ["validate_file_extension", "is_img", "split_extension", "split_all", "get_file_name"],
    "utils.dir_utils.dir_utils": ["transfer_directory_items",
                                  "dir_train_test_split",
                                  "split_dir_of_dir",
                                  "split_xy_dir",
                                  "crawl_directory_dataset",
                                  "remove_create",
                                  "mkdir_incremental",
                                  "file_incremental",
                                  "cp_mv_all",
                                  "split_segmentation_dirs",
                                  "find_file",
                                  "combine_directory_of_directories",
                                  "DirUtils"],
    "utils.logging_utils.logging_utils": ["get_logger"],
    "utils.lr_scheduler_utils.warmup": ["cosine_reduce", "warmup_cosine"],
    "utils.py_utils.py_utils": ["PyUtils"],
    "utils.json_utils.json_utils": ["JsonUtils"],
    "utils.pickle_utils.pickle_utils": ["PickleUtils"],
    DUMMY_PATH: [],
}

import_lazy_module("SITKUtils", "medical/sitk_utils/sitk_utils")
import_lazy_module("TFUtils", "utils.tf_utils.main")
import_lazy_module('QdrantUtils', 'utils.qdrant_utils.qdrant_utils')
import_lazy_module('DownloadUtils', 'utils.download_utils.download_utils')
import_lazy_module('Text2BoxVisualGroundingDino', 'vision.text2box_visual_grounding.dino.visual_grounding_dino_torch')
import_lazy_module('ImageEditingGLIDE', 'vision.image_editing.glide.glide_image_editing')
import_lazy_module('ImageEditingGLIDETypes', 'vision.image_editing.glide.glide_image_editing')
import_lazy_module('BlipTorchImageCaption', 'vision.image_caption.blip.torch.blip_torch_image_caption')
import_lazy_module('MonaiChannelBasedContrastEnhancementD', 'preprocessing.monai.monai_segmentation')
import_lazy_module('TensorboardTorch', 'callbacks.torch.torch_tensorboard')
import_lazy_module('TorchUtils', 'utils.torch_utils.torch_utils')
import_lazy_module('BlocksTorch', 'blocks.torch.blocks_torch')
import_lazy_module('ColorRecognitionCNNTorch', 'vision.color_recognition.cnn_color.torch.color_cnn_torch')
import_lazy_module('HaarcascadeCV2FaceDetector',
                   'vision.face_detection.haarcascade.cv2_.haarcascade_cv2_face_detection')
import_lazy_module('CVUtils', 'utils.opencv_utils.opencv_utils')
import_lazy_module('MTCNNTorchFaceDetector', 'vision.face_detection.mtcnn.torch.mtcnn_torch_face_detection')
import_lazy_module('YOLOV5TorchObjectDetector', 'vision.object_detection.yolo.v5.torch.yolo_v5_torch_object_detection')
import_lazy_module('YOLOV7TorchObjectDetector', 'vision.object_detection.yolo.v7.torch.yolo_v7_torch_object_detection')
import_lazy_module('ColorRecognitionCNNTorchPrediction',
                   'vision.color_recognition.cnn_color.torch.color_cnn_torch_pred')
import_lazy_module("CRNNInferenceTorch", "vision.ocr.crnn.torch.crnn_inference")
import_lazy_module("CRNNModelTorch", "vision.ocr.crnn.torch.crnn_model")
import_lazy_module("MTCNNTFFaceDetector", "vision.face_detection.mtcnn.tf.mtcnn_tf_face_detection")

if TYPE_CHECKING:
    from .utils.box_utils.boxes import Box, Point
    from .vision.face_detection.haarcascade.cv2_.haarcascade_cv2_face_detection import HaarcascadeCV2FaceDetector
    from .vision.face_detection.mtcnn.tf.mtcnn_tf_face_detection import MTCNNTFFaceDetector
    from .vision.face_detection.mtcnn.torch.mtcnn_torch_face_detection import MTCNNTorchFaceDetector
    from .vision.face_detection.haarcascade.cv2_.haarcascade_cv2_face_detection import HaarcascadeCV2FaceDetector
    from .callbacks.torch.torch_tensorboard import TensorboardTorch
    from .utils.os_utils.os_path import validate_file_extension, is_img, split_extension, split_all, get_file_name
    from .utils.dir_utils.dir_utils import (transfer_directory_items, dir_train_test_split, split_dir_of_dir,
                                            split_xy_dir, crawl_directory_dataset, remove_create, mkdir_incremental,
                                            file_incremental, cp_mv_all, split_segmentation_dirs, find_file,
                                            combine_directory_of_directories, DirUtils)
    from .preprocessing.monai.monai_segmentation import MonaiChannelBasedContrastEnhancementD
    from .utils.torch_utils.torch_utils import TorchUtils
    from .utils.tf_utils.main import TFUtils
    from .vision.object_detection.yolo.v5.torch.yolo_v5_torch_object_detection import YOLOV5TorchObjectDetector
    from .vision.object_detection.yolo.v7.torch.yolo_v7_torch_object_detection import YOLOV7TorchObjectDetector
    from .utils.opencv_utils.opencv_utils import CVUtils
    from .vision.image_caption.image_caption import ImageCaption
    from .vision.image_caption.blip.torch.blip_torch_image_caption import BlipTorchImageCaption
    from .utils.encodes.b64 import b64_to_img
    from .blocks.torch.blocks_torch import BlocksTorch
    from .vision.color_recognition.cnn_color.torch.color_cnn_torch import ColorRecognitionCNNTorch
    from .vision.color_recognition.cnn_color.torch.color_cnn_torch_pred import ColorRecognitionCNNTorchPrediction
    from .vision.ocr.crnn.torch.crnn_inference import CRNNInferenceTorch
    from .vision.ocr.crnn.torch.crnn_model import CRNNModelTorch
    from .utils.logging_utils.logging_utils import get_logger
    from .vision.image_editing.glide.glide_image_editing import ImageEditingGLIDE, ImageEditingGLIDETypes
    from .vision.text2box_visual_grounding.dino.visual_grounding_dino_torch import Text2BoxVisualGroundingDino
    from .utils.download_utils.download_utils import DownloadUtils
    from .utils.lr_scheduler_utils.warmup import cosine_reduce, warmup_cosine
    from .utils.py_utils.py_utils import PyUtils
    from .utils.json_utils.json_utils import JsonUtils
    from .utils.qdrant_utils.qdrant_utils import QdrantUtils
    from .utils.pickle_utils.pickle_utils import PickleUtils
    from .medical.sitk_utils.sitk_utils import SITKUtils
else:
    import sys

    sys.modules[__name__] = LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )
