import pickle

# Serializing (Pickling) to Binary Format
data = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}  # Data to be serialized
with open('Binary_data.pickle', 'wb') as file:
    pickle.dump(data, file) # Serialize the data to a file

# Deserializing (Unpickling) from Binary Format
with open('Binary_data.pickle', 'rb') as file:
    data_loaded = pickle.load(file) # Deserialize the data from the file
print(data_loaded)

import base64

# Serializing (Pickling) to Text Format
data = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'} # Data to be serialized
binary_data = pickle.dumps(data) # Serialize the data to a binary string
# Encode the binary data to a base64 string
text_data = base64.b64encode(binary_data).decode('utf-8')
with open('Text_data.pickle', 'w') as file:
    file.write(text_data)  # Save the base64 string to a text file


# Deserializing (Unpickling) from Text Format
with open('Text_data.pickle', 'r') as file:
    text_data = file.read()  # Read the base64 string from the text file
binary_data = base64.b64decode(text_data)  # Decode the base64 string to binary data
data_loaded = pickle.loads(binary_data) # Deserialize the binary data to a Python object
print(data_loaded) 

