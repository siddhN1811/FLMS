import pickle


def predict(values):

    pickled_model = pickle.load(open('model.pkl', 'rb'))  # loading pickled model.pkl file
    precip = pickled_model.predict(values)

    # print(pickled_model.predict(values))  # debugging purpose
    print(int(precip))
    if int(precip) ==0:
        
        return 1
    return int(precip)


# x = [[28.0, 25.9, 26.7, 29.0, 95.0, 272.6]]  #TEST DATA - 'tempmax', 'tempmin','temp','feelslike', 'humidity','winddir'
# x2 = [[33.98, 31.93, 33.98, 38.0388889, 49,260]]
# a = predict(x)
# print(a)
