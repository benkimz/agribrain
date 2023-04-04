import pickle
import numpy as np
import tensorflow as tf

models_dir = "./ai/models/production/"
components_dir = "./ai/components/production/"

loaded_scaler = pickle.load(open("{}scaler.sav".format(components_dir), "rb"))
loaded_cropname_encoder = pickle.load(open("{}cropname_encoder.sav".format(components_dir), "rb"))
loaded_countyname_encoder = pickle.load(open("{}county_encoder.sav".format(components_dir), "rb"))
loaded_model = tf.keras.models.load_model("{}model-v1/".format(models_dir), 
                                          compile=False)

loaded_model.compile(optimizer='adam', loss='mse', metrics=['mae'])

def make_prediction(query: dict):
  year, area, _, _ = list(loaded_scaler.transform([[query["year"], 
                                                    query["area"], 
                                                    0, 0]])[0])
  crop = loaded_cropname_encoder.transform([query["crop"]])
  county = loaded_countyname_encoder.transform([query["county"]])
  inputs = np.array([[county[0], crop[0], year, area]], dtype=np.float32)
  preds = loaded_model.predict(inputs)
  raw_prod_res, raw_yield_res = tuple(preds[0])
  outputs = loaded_scaler.inverse_transform([[0, 0, raw_prod_res, raw_yield_res]])
  _, _, production, yields = list(outputs[0])
  return (production, yields)