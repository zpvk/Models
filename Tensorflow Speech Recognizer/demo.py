import tflearn
import speech_data

learning_rate = 0.0001
traning_iters = 300000

batch = word_batch = speech_data.mfcc_batch_generator(64)

X,Y = next(batch)
trainX, traningY = x,Y
textX, textY, X,Y

net = ftlearn.input_data([None, 20, 80])
net = ftlearn.lsm(net, 128, dropout=0.8)
net = ftlearn.fully_connrcted()


