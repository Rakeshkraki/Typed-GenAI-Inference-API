
def with_ctx_manager():
    with open("../test_logs/logs.log", 'r') as f:
        read_data = f.read()
        print(read_data)

#with_ctx_manager()

def normal_handling():
    f = open("../test_logs/logs.log", 'r')
    read_data = f.read()
    print(read_data)
    f.close()

normal_handling()