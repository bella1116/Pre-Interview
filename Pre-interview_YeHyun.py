class Tensor():

    def __init__(self, data, shape):
        self.data = data
        self.shape = shape
        self.tensor = Tensor(data,shape)

    #Multiply all the numbers in the shape and return to the 'count'.
    def Reshape(self, shape):
        count = 1
        for i in shape:
            count *= i
        return count

    #Adjust the quantity of the list 'data' to the 'count' value.
    def Add(self, data, max_count):
        a_data = []
        for i in range(max_count):
            try:
                a_data.append(data[i])
            except:
                #If the tensor pad is not enough, fill it with zero.
                a_data.append(0)
        return a_data

    def Tensor(self, data, shape):
        #Multiply all the numbers in the 'shape' list.
        max_count = self.Reshape(shape)
        #In the 'Reshape' function, put the value 'max_count' multiplied by the value of both the 'data' list and the value of the 'shape'.
        #If the number of lists is less than the value of 'max_count', it is created and filled with zero, and is so, it is truncated and returned.
        data = self.Add(data, max_count)

        #Run loop from the number of shapes to 1.
        for j in range((len(shape)-1), 0 -1):
            #Generate an empty list.
            a = []
            #From 0 to the number of 'data' lists, loop is executed.
            #It stretches as much as the shape[j]
            for i in range(0, len(data), shape[j]):
                # Generate an empty list.
                b = []
                #Run loop from 0 to shape[j]-1.
                for x in range(shape[j]):
                    x += i
                    #Store the data[x] value in the pre-generated 'b' list.
                    b.append(data[x])
                #Store 'b' data in list 'a'.
                a.append(b)
            #Secondary stored 'a' value is designated as a 'data' value.
            data = a
        #Print the 'data' value even after loop is finished.
        print(data)