from typing import Sequence, NamedTuple, List
import numpy as np

#pycharm środowisko do pythona



class Scheduler:

    def __init__(self):
        return None

    def read_file(self, filename):
        with open(filename) as file_obj:
            text = file_obj.read()
        return text

    def print_array(self, array ):
        s = 0
        for i in array:
            for j in i:
                print(j,end = " ")
            print()    
    
    def make_arrays(self, filename):
        file = self.read_file(filename)
        text_from_file = file.split()

        number_of_jobs = int(text_from_file.pop(0))        
        number_of_machine = int(text_from_file.pop(0))
        
       
        array = [ [ 0 for jobs in range(number_of_jobs)]  for i in range(number_of_machine) ]
        
        for jobs  in range(number_of_jobs ):
            for machines  in range(number_of_machine ):
                array[machines][jobs] = text_from_file.pop(0)
        
        #self.print_array(array)
        return array



    ## zwraca suma czasów wszystkich operacji na wszystkich maszynach dla danego zadania
    def operation_time(self,array):

        job_time = 0
        times = []
        
        
        for i in range(len(array[0])):
            for j in range(len(array)):           
                job_time += int(array[j][i])

            times.append(job_time)
            job_time =0
        return times



    def add_array(self, array, array_weight):

        new_array = [ [ 0 for jobs in range(len(array[0]))]  for i in range(len(array) +1) ]
        for i in range(len(array[0])):
            for j in range(len(array)):           
                new_array[j][i] = array[j][i]

        for i in range(len(new_array[0])):
            new_array[len(new_array) - 1][i] = array_weight[i]

        return new_array

    def swap_colums(self, array, firs, sec):
        temp = 0 
        if(firs > sec):
            for col in range(len(array)):
                temp = array[col][firs]
                array[col][firs] = array[col][sec]
                array[col][sec] = temp
        return array

    def max_value_id(self, array):
        
        id = []
        
        for i in array:
            x = array.index(max(array))
            array[x] = -1
            id.append(x)

        
        return id
            


    def sort_colums(self, array):

        new_array = [ [ 0 for jobs in range(len(array[0]))]  for i in range(len(array)) ]
        self.print_array(new_array)
        self.print_array(array)
        sort_operation = self.operation_time(array)
        id_array = self.max_value_id(sort_operation)
        print(id_array)
        for col in range(len(array)):
            array = self.swap_colums(array,id_array[col],col)
        print(len(array))
        self.print_array(new_array)



        return array
        


    
    def sort_operation_time(self, array):

        sort_oper = self.operation_time(array)
        array_weight = self.add_array(array,sort_oper)
        array = self.sort_colums(array)
        
        
        return sort_oper



    def array_with_zeros(self, array):

        array_zero = [ [ 0 for jobs in range(len(array[0]) + 1)]  for i in range(len(array) + 1 ) ]
        for i in range(len(array[0])):
            for j in range(len(array)):           
                array_zero[j+1][i+1] = array[j][i]
        return array_zero
        



    


    def cmax_time(self,array):
        machine_time = self.operation_time(array)
        cmax_table = self.array_with_zeros(array)

        
        for i in range(len(cmax_table[0])-1):
            for j in range(len(cmax_table)-1):
                cmax_table[j+1][i+1] = max(int(cmax_table[j+1][i]),int(cmax_table[j][i+1])) + int(cmax_table[j+1][i+1])
               

        return cmax_table


        
    

        
                

    
    
    




    
        
        
