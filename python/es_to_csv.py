from elasticsearch import Elasticsearch, helpers
import json

## Python 3.8에서 개발
## Python 3.4.8에서 사용

##  ES에서 데이터를 검색한다.
def search_es() : 
    index = '*'
    host = 'localhost' #0.0.0.0
    port = 9200
    es = Elasticsearch([{'host': host, 'port': port}])
    query = { 
      "size": 10000
    }   
    
    results = es.search(index=index, body=query)
    return results

## 검색된 ES 카운트를 반환한다.
def count_es(results) :
    return len(results['hits']['hits'])

##LIST 형태로 필드명만 반환. 정렬안되어 있으니 정렬 필요
def get_field_es(results) : 
    fields = set()
    for result in results['hits']['hits'] : 
        for key in result['_source'].keys() : 
            fields.add(key)
    return list(fields)

# ES 인덱스의 index명과 타입을 반환한다.
def get_index_info(results) :
    info_idx = set()
    info_type = set()
    for result in results['hits']['hits'] : 
        info_idx.add(result['_index'])
        info_type.add(result['_type'])
    return info_idx, info_type

# ES 데이터를 CSV형태로 통으로 만들어서 반환한다.
# 헤더에는 필드명들이 | 형태로 끊어져서 나타남
# 본문에는 필드값들이 | 형태로 끊어져서 나타남
def es_to_csv(results) :
    csv_rows = []
    csv_fields = get_field_es(results)
    csv_fields.sort()
    csv_header = '|'.join(csv_fields)
    print('CSV_HEADER :: {}'.format(csv_header))
    csv_rows.append(csv_header)

    for result in results['hits']['hits']:
        value_list = []
        for field in csv_fields :
            if result['_source'].get(field) != None :
                value_list.append(str(result['_source'].get(field)))
            else :
                value_list.append('')
        value_string = '|'.join(value_list)
        csv_rows.append(value_string)
    return csv_rows

def save_csv(csv_list) :
    print('START WRITING')
    file_nm = 'something.csv'
    file_path = '/some/where/'
    f = open(file_path + file_nm, 'w')
    contents = '\n'.join(csv_list)
    f.write(contents)
    print('END WRITING')
    f.close()

if __name__ == '__main__' :
    results = search_es()
    es_fields = get_field_es(results)
    print("ELASTIC COUNT        :: {}".format(count_es(results)))
    print("ELASTIC FIELD        :: {}".format(es_fields))
    print("ELASTIC FIELD COUNT  :: {}".format(len(es_fields)))
    print("ELASTIC INFO         :: {}".format(get_index_info(results)))
    csv_list = es_to_csv(results)

    # csv로 저장하기 위해서는 save_csv 함수의 파일명, 파일경로를 수정해야한다.
    # save_csv(csv_list)
