import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model("checkpoints/yolov4-tiny-416/")
converter.target_spec.supported_ops = [
  tf.lite.OpsSet.TFLITE_BUILTINS, # enable TensorFlow Lite ops.
  tf.lite.OpsSet.SELECT_TF_OPS # enable TensorFlow ops.
]
tflite_model = converter.convert()
open("converted_tiny_model.tflite", "wb").write(tflite_model)


