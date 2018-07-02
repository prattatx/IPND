import Algorithmia

input = "http://www.att.com/"
client = Algorithmia.client('simEHu1xk1DIPcgQ/gCS01olaaQ1')
algo = client.algo('util/Html2Text/0.1.6')
print(algo.pipe(input).result)