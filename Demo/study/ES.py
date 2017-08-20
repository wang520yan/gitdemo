# -*- encoding:utf-8 -*-

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'127.0.0.1','port':9200}])
useIndex = 'logou'
doc_type = ['job']
# s = es.search(index=useIndex, doc_type=doc_type)
# params = {'comment': 20}
# nested_query = ({'query':{'match_all':{'comment':20}}})
# nested_query = Q('term', **params)
# s = s.query(nested_query)
# response = s.execute()
# for hit in response:
#     print dir(hit)
#     print hit
res_get = es.get(index=useIndex, doc_type=doc_type, id=1)
print res_get['_source']['title']
res = es.search(index=useIndex, doc_type=doc_type, body={"query":{"match":{'comment': 15}}})
for hit in res['hits']['hits']:
    print (hit['_source']['city'])