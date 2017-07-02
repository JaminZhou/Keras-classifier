from keras.models import load_model
import coremltools

model = load_model('model')
coreml_model = coremltools.converters.keras.convert(model)
coreml_model.save("keras_model.mlmodel")