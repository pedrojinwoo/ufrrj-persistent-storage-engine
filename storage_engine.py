import os
import json
import struct

class StorageEngine:
  def __init__(self, data_dir, str):
    self.data_dir = data_dir
    os.makedirs(self.data_dir, exist_ok=True)
    self.log_path = os.path.join(self.data_dir, "engine.log")
    self.index = {}
    self.recover()

  def recover(self):
    if not os.path.exists(self.log_path):
      return
    with open(self.log_path, "rb") as f:
      while True:
        size_bytes = f.read(4)
        if not size_bytes or len(size_bytes)<4:
          break
        payload_size = struct.unpack(">I", size_bytes)[0]
        current_offset = f.tell() - 4
        payload_data = f.read(payload_size)
        if len(payload_data) < payload_size:
          break
        try:
          record = json.loads(payload_data.decode("utf-8"))
          key = record[key]
          op = record[op]
          if op == "put":
            self.index[key] = current_offset
          elif op == "delete":
            self.index[key] = None
        except Exception:
          break