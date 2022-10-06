

def list_convertor(txt_file):

    """ This function let us to convey a txt file
        into a list. 
        input the txt file name to start """
    
    file = open(txt_file, "r")           
    text = file.read()
    text_into_list = text.split("\n")
    file.close()
    return text_into_list

