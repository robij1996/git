from scheduler import  Scheduler


if __name__ == '__main__':
   # print ( "asdasd" + Scheduler.makeArrays("data.txt"))
    
    sched = Scheduler()
    matrix = sched.make_arrays("data.txt")
    matrix = [ [ int(matrix[i][j]) for j in range(len(matrix[0]))]  for i in range(len(matrix)) ]
    
    cmax = sched.cmax_time(matrix)
    sort = sched.sort_operation_time(matrix)
