status=['CLOSED', 'PENDING_PAYMENT', 'COMPLETE', 'CLOSED', 'COMPLETE', 'COMPLETE', 'COMPLETE', 'PROCESSING', 'PENDING_PAYMENT', 'PENDING_PAYMENT']
status_set=set(status)
print(status_set)


status_list=[(x,status.count(x))for x in status_set]
print(status_list)
