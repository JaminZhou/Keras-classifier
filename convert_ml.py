from keras.models import load_model
import coremltools

model = load_model('model')
coreml_model = coremltools.converters.keras.convert(model, input_names = 'image', image_input_names = 'image', output_names = 'output')
coreml_model.author = 'JaminZhou'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Cat or Dog'
coreml_model.input_description['image'] = 'image: CVPixelBuffer'
coreml_model.output_description['output'] = 'output: 0 or 1'
coreml_model.save("keras_model.mlmodel")

#let keras = keras_model()
#let imageBuffer: CVPixelBuffer
#let prediction = try keras1.prediction(image: imageBuffer)
#prediction.output[0] //the value 0 is cat, value 1 is dog
