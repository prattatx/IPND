# import Algorithmia

# input = "prattatx"
# client = Algorithmia.client('simEHu1xk1DIPcgQ/gCS01olaaQ1')
# algo = client.algo('demo/Hello/')
# print algo.pipe(input)


# import Algorithmia

# input = "https://www.google.com/"
# client = Algorithmia.client('simEHu1xk1DIPcgQ/gCS01olaaQ1')
# algo = client.algo('util/Html2Text/0.1.6')
# print(algo.pipe(input))

import Algorithmia

input = {
  "image": "https://i.imgur.com/CWVZHwD.jpg",
  "output": "data://.algo/deeplearning/ObjectDetectionCOCO/temp/suit_and_tie.png",
  "min_score": 0.7,
  "model": "ssd_mobilenet_v1"
}
client = Algorithmia.client('simEHu1xk1DIPcgQ/gCS01olaaQ1')
algo = client.algo('deeplearning/ObjectDetectionCOCO/0.2.0')
print(algo.pipe(input))