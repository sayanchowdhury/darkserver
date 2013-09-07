def get_darkproducer_instances(rdb):
    darkproducer_keys = rdb.keys('darkproducer-status-*')
    darkproducer_instances = []
    for darkproducer_key in darkproducer_keys:
        dp_status = {}
        dp_status['arch'] = darkproducer_key
        dp_status['status'] = rdb.get(darkproducer_key)
        dp_status['remarks'] = rdb.get(
                'darkproducer-id-'+ darproducer_key.split('-')[2])

        darkproducer_instances.append(dp_status)

    return darkproducer_instances

def get_darkjobworkers(rdb):
    darkjobworker_keys = rdb.keys('darkjobworker:*')
    darkjobworkers = []
    for darkjobworker_key in darkjobworker_keys:
        dj_status = {}
        dj_status['id'] = darkjobworker_key
        dj_status['remarks'] = rdb.get(darkjobworker_key)

        darkjobworkers.append(dj_status)
    return darkjobworkers
