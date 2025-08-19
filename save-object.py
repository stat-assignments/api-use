import msgpack
def save_object(obj, file):
  try:
    with open(file, "wb") as f:
      packed=msgpack.packb(obj)
      f.write(packed)
  except Exception as ex:
    print("Error during packing object (Possibly unsupported):", ex)

def load_object(filename):
  try:
    with open(filename, "rb") as f:
      packed = f.read()
      return msgpack.unpackb(packed)
  except Exception as ex:
    print("Error during unpacking object (Possibly unsupported):", ex)
