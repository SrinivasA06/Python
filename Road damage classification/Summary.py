from tensorflow.keras.applications import ResNet50
from tensorflow.keras.utils import plot_model

# Create a ResNet50 model
model = ResNet50(include_top=True, weights=None, input_shape=(224, 224, 3), classes=1000)

# Generate the model summary
model.summary()

# Save the model architecture diagram to a file
plot_model(model, to_file='resnet_architecture.png', show_shapes=True)
