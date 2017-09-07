import sys, string


def numLen(num):
    if(type(num) is int):
        return len(str(abs(num)))
    else:
        return len(str(num))
def representInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def convert(system,other_num):
	#conditional to run if the system being used is less than base-10
	if(10 > system):
	    #conditional to run if the input number is less than the base number of system (essentially, the number is the same in both systems)
	    if(other_num < system and not other_num < 0):
	        value = other_num
	
	    #conditional to run if the input number is zero
	    elif(other_num == 0):
	        value = other_num
	    else:
	        #passes the remainder of other_num / 10
	        mod = other_num % 10
	        #subtracts the remainder from other_num. Streamlines calculation.
	        new_num = other_num - mod

	        maxim = numLen(other_num) + 1

	        length = list(range(2, maxim))
	        passer = []
	        differential = 10 - system
	        for each in length:
	            divisor = 10 ** each
	            subtractor = (system ** (each - 1)) * differential * ((other_num / divisor) - ((other_num % divisor) / divisor))
	            passer.append(subtractor)
	        prevalue = other_num - (differential * (new_num / 10))
	        for i in passer:
	            prevalue = prevalue - i
	        value = prevalue

	#conditional to run if the system being used is greater than base-10
	else:
	    differential_list = list(range(10, system))
	    list_letters = list(string.ascii_letters)
	    alt_val_dict = dict(zip(list_letters, differential_list))
	    #Debug line: print(alt_val_dict)
	    other_num_length = numLen(other_num)
	    if(other_num_length == 1):
	        if(other_num < 10):
	            pass
	        else:
	            value = alt_val_dict[other_num]
	    else:
	        other_num_string = str(other_num)
	        temp = int(other_num_length) - 1
	        convert_list = []
	        for every in other_num_string:
	            #Debug line: print('Every value: %s. Every type: %s.' % (every, type(every)))
	            place = system ** temp
	            if(temp != 0):
	                if(not representInt(every)):
	                    conv = alt_val_dict[every]
	                    prevalue = conv * place
	                    convert_list.append(prevalue)
	
	                else:
	                    prevalue = int(every) * place
	                    convert_list.append(prevalue)
	                temp -= 1
	            else:
	                if(not representInt(every)):
	                    prevalue = int(alt_val_dict[every])
	                    convert_list.append(prevalue)
	                else:
	                    prevalue = int(every)
	                    convert_list.append(prevalue)
	        value = 0
	        for i in convert_list:
	            x = int(i)
	            value += x
	    # Remnant of a previous time: value = other_num + (differential * (new_num / 10))
	
	print('the base-%s value %s is equal to the base-10 value %s' % (system, other_num, value))
