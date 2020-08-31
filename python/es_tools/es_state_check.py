import elasticsearch
import elasticsearch.helpers
import json
import urllib.request
import time

# URL 접속 여부 확인
def url_check(ip, port) :
    url = "http://" + ip + ":" + str(port)
    print("GET {}".format(url))
    res2 = urllib.request.Request(url)
    
    try  :
        with urllib.request.urlopen(res2, timeout=0.1) as response :
            # response.read -> byte
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(e)
    
    except Exception as e2 :
        print(e2)

class ES :
    def __init__(self) :
        hosts = 'localhost'
        port = 9200
        timeout = 30
        id = None
        pw = None
        es = None
        
    def setHosts(self, hosts) : 
        self.hosts = hosts

    def setPort(self, port) :
        self.port = port
        
    def setTimeout(self, timeout) :
        self.timeout = timeout
        
    def setHttpAuth(self, id, pw) :
        self.id = id
        self.pw = pw
        
    def setES(self) :
        if self.id == None or self.pw == None :
            self.es = elasticsearch.Elasticsearch(hosts=self.hosts, 
                                 timeout=self.timeout,
                                 port=self.port
            )
            return True
        else :
            self.es = elasticsearch.Elasticsearch(hosts=self.hosts, 
                                 timeout=self.timeout,
                                 port=self.port,
                                 http_auth=(self.id, self.pw)
            )
            return True
        
    # return dict
    def getHealthOrigin(self) :
        return self.es.cluster.health(wait_for_status='yellow', request_timeout=1)
    
    def printHealthOrigin(self) :
        # cluster 전체 상태 체크
        c_hlth = self.getHealthOrigin();
        c_name = c_hlth.get('cluster_name')
        c_n_count = c_hlth.get('number_of_nodes')
        c_dn_count = c_hlth.get('number_of_data_nodes')
        c_s_count = c_hlth.get('active_shards')
        
        print("cluster_name          :: {}".format(c_name))
        print("number of node        :: {}".format(c_n_count))
        print("number of data node   :: {}".format(c_dn_count))
        print("number of shards      :: {}".format(c_s_count))
        print("heatlh                :: {}".format(c_hlth.get('status')))
            
    # return string
    def getHealthIndent(self) :
        cluster_health = self.es.cluster.health(wait_for_status='yellow', request_timeout=1)
        jsonString = json.dumps(cluster_health, indent=4)
        return jsonString
    
    def getTest(self) : 
        es_stats = self.es.cluster.stats()
        indice_count = es_stats['indices']['count']
        fielddata_memory = es_stats['indices']['fielddata']['memory_size_in_bytes']
        segment_count = es_stats['indices']['segments']['count']
        print('-' * 60)
        print('indice_count  :: {}'.format(indice_count))
        print('fielddata_memory  :: {}'.format(unitConv(fielddata_memory, "size")))
        print('segment_count  :: {}'.format(unitConv(segment_count, "count")))
            
    def getEsInfo(self) :
        return self.es.info()
    
    def pingEs(self) :
    # True if ping goes
        return self.es.ping()
    
    def getNodeStats(self) :
        return self.es.nodes.stats()
    
    def printFullNodeStats(self, kind) :
        es_stats = self.getNodeStats()
        total_indices_docs_count = 0
        total_indices_store_size = 0

        for node_id in self.getNodeStats().get('nodes').keys() : 
            node_stats = es_stats.get('nodes').get(node_id)
            node_stats_indices = node_stats.get('indices')
            if kind == 'full' :
                print('-' * 60)
                print('Node Name           :: {}'.format(node_stats.get('name')))
                print('Node Transport addr :: {}'.format(node_stats.get('transport_address')))
                print('Node Indices docs   :: {}'.format(node_stats_indices.get('docs')))
                print('Node Store          :: {}'.format(node_stats_indices.get('store')))
            total_indices_docs_count += node_stats_indices.get('docs').get('count')
            total_indices_store_size += node_stats_indices.get('store').get('size_in_bytes')
        print('-' * 60)
        print('total_indices_docs_count  :: {}'.format(total_indices_docs_count))
        print('total_indices_docs_human  :: {}'.format(unitConv(total_indices_docs_count, "count")))
        
        print('total_indices_store_size  :: {}'.format(total_indices_store_size))
        print('total_indices_store_human :: {}'.format(unitConv(total_indices_store_size, "size")))
    
def unitConv(value, kind) :
    if kind == 'size' :
        if (value // 1024) == 0 :
            return '%.3f' % value + 'B'
        elif (value // 1024 ** 2) == 0 :
            return '%.3f' % (value/1024**1) + 'KB'
        elif (value // 1024 ** 3) == 0 :
            return '%.3f' % (value/1024**2) + 'MB'
        elif (value // 1024 ** 4) == 0 :
            return '%.3f' % (value/1024**3) + 'GB'
        elif (value // 1024 ** 5) == 0 :
            return '%.3f' % (value/1024**4) + 'TB'
        
    elif kind == 'count' :
        result_str = ''
        if (value // 1000000000000) > 0 :
            result_str += str(value // 1000000000000) + '조 '
            value = value % 1000000000000
        if (value // 100000000) > 0 :
            result_str += str(value // 100000000) + '억 '
            value = value % 100000000
        if (value // 10000) > 0 :
            result_str += str(value // 10000) + '만 '
            value = value % 10000
        result_str += '건'
        
        return result_str
    
if __name__ == '__main__' :
    
    server_ip = "localhost"
    server_port = 9200
    
    # Setting ES
    es = ES()
    es.setHosts(server_ip)
    es.setPort(server_port)
    es.setTimeout(30)
    # if you have auth. modify below code. and if not no matter modify below code
    es.setHttpAuth('test', 'test')
    es.setES()
    
    # ES cluster health
    es.printHealthOrigin()
    
    # ES Node Status -- 'full' / 'simple'
    es.printFullNodeStats("simple")

    # Should change this method name
    es.getTest()
    