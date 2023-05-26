from pixellib.instance import instance_segmentation
from pixellib.tune_bg import alter_bg
from PIL import Image

Image_path = ""



def Start(Im, Val):

    print(Im)


    def object_detection_on_an_image():
        Image_path = Im
        Image_Topath = Val
        print(Image_path)
        segment_image = instance_segmentation()
        segment_image.load_model("mask_rcnn_coco.h5")

        target_class = segment_image.select_target_classes(person=True)
        segment_image.segmentImage(
            image_path=Image_path,
            show_bboxes=True,
            segment_target_classes=target_class,
            extract_segmented_objects=False,
            output_image_name=Image_Topath
        )


    def main():
        object_detection_on_an_image()

    main()

    filename = Val
    with Image.open(filename) as img:
        img.load()

    img.show()