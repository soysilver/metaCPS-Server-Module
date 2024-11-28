import numpy as np
import tensorflow as tf
import pickle
import sqlite3

'''
what this part has to do:
1. make gui pop up 
2. prior to release, check https://kivy.org/doc/stable/guide/licensing.html
3. What each uses:
- tenserflow follows Apache License, Version 2.0
- ZMQ follows Modified BSD License

'''
global id
db = './database.db'

data_L5 = [
    (2831.752835, 248.5552327, 10),
    (2887.211223, 246.2053845, 11),
    (2944.518225, 243.777208, 12),
    (2999.976613, 241.4273598, 13),
    (3055.435002, 239.0775116, 14),
    (3110.89339, 236.7276634, 15),
    (3194.817763, 234.1624197, 16),
    (3281.539615, 231.5116678, 17),
    (3365.463987, 228.9464241, 18),
    (3449.38836, 226.3811804, 19),
    (3533.312733, 223.8159367, 20),
    (3600.926067, 221.027428, 21),
    (3670.793179, 218.1459691, 22),
    (3738.406514, 215.3574605, 23),
    (3806.019848, 212.5689519, 24),
    (3873.633182, 209.7804433, 25),
    (3961.836387, 206.8107672, 26),
    (4050.039592, 203.841091, 27),
    (4141.182903, 200.7724257, 28),
    (4229.386107, 197.8027496, 29),
    (4317.589312, 194.8330735, 30),
    (4388.603748, 192.541224, 31),
    (4459.618185, 190.2493746, 32),
    (4532.99977, 187.8811302, 33),
    (4604.014206, 185.5892807, 34),
    (4675.028643, 183.2974313, 35),
    (4768.043656, 180.5590366, 36),
    (4864.159169, 177.729362, 37),
    (4957.174182, 174.9909672, 38),
    (5050.189195, 172.2525725, 39),
    (5143.204208, 169.5141778, 40),
    (5221.477104, 166.7644976, 41),
    (5299.75, 164.0148175, 42),
    (5380.631992, 161.1734813, 43),
    (5458.904888, 158.4238012, 44),
    (5537.177784, 155.6741211, 45),
    (5634.713088, 152.9395215, 46),
    (5732.248391, 150.2049219, 47),
    (5833.034871, 147.379169, 48),
    (5930.570175, 144.6445694, 49),
    (6028.105478, 141.9099698, 50)
]

data_L6 = [
 (2734.327122, 248.9606791, 10),
    (2795.090619, 246.8675168, 11),
    (2857.879565, 244.7045825, 12),
    (2918.643062, 242.6114202, 13),
    (2979.406559, 240.5182579, 14),
    (3040.170056, 238.4250956, 15),
    (3116.170495, 235.8074964, 16),
    (3194.704283, 233.1026439, 17),
    (3270.704722, 230.4850448, 18),
    (3346.705161, 227.8674456, 19),
    (3422.705601, 225.2498464, 20),
    (3504.306529, 222.2296399, 21),
    (3585.907457, 219.2094333, 22),
    (3670.228416, 216.0885531, 23),
    (3751.829345, 213.0683465, 24),
    (3833.430273, 210.0481399, 25),
    (3907.555693, 207.1935075, 26),
    (3981.681113, 204.3388751, 27),
    (4058.27738, 201.3890883, 28),
    (4132.4028, 198.5344559, 29),
    (4206.52822, 195.6798235, 30),
    (4293.546085, 192.7468917, 31),
    (4380.563951, 189.8139599, 32),
    (4470.482412, 186.7832637, 33),
    (4557.500277, 183.8503319, 34),
    (4644.518143, 180.9174001, 35),
    (4718.580934, 178.3019324, 36),
    (4792.643724, 175.6864647, 37),
    (4869.175275, 172.9838148, 38),
    (4943.238066, 170.3683471, 39),
    (5017.300856, 167.7528795, 40),
    (5109.732769, 164.6369033, 41),
    (5202.164681, 161.5209272, 42),
    (5297.677657, 158.3010852, 43),
    (5390.109569, 155.1851091, 44),
    (5482.541481, 152.069133, 45),
    (5598.214097, 148.2587158, 46),
    (5713.886713, 144.4482987, 47),
    (5833.415083, 140.5108676, 48),
    (5949.087698, 136.7004505, 49),
    (6064.760314, 132.8900333, 50)
]

#model custom components 
@tf.keras.utils.register_keras_serializable(package='Custom', name='SomeNetwork')
class SomeNetwork(tf.keras.Model):
    def __init__(self, input_shape, hidden_dim, output_dim):
        super(SomeNetwork, self).__init__()
        self.input_shape = input_shape
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.conv1 = tf.keras.layers.Conv1D(filters=32, kernel_size=2, activation='relu', input_shape=(input_dim, 1))
        self.conv2 = tf.keras.layers.Conv1D(filters=64, kernel_size=3, activation='leaky_relu')
        self.flatten = tf.keras.layers.Flatten()
        self.fc1 = tf.keras.layers.Dense(hidden_dim)
        self.bn1 = tf.keras.layers.BatchNormalization()
        self.fca = tf.keras.layers.Dense(hidden_dim)
        self.dropout = tf.keras.layers.Dropout(0.1) 
        self.bn2 = tf.keras.layers.BatchNormalization()
        self.fc2 = tf.keras.layers.Dense(output_dim)

    def call(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.flatten(x)
        x = tf.nn.relu(self.bn1(self.fc1(x)))
        x = self.dropout(x)
        x = tf.nn.leaky_relu(self.bn2(self.fca(x)))
        x = self.fc2(x)
        return x

    def get_config(self):
        return {
            "input_shape": self.input_shape,
            "hidden_dim": self.hidden_dim,
            "output_dim": self.output_dim
        }

    @classmethod
    def from_config(cls, config):
        return cls(**config)


#Custom loss function
@tf.keras.utils.register_keras_serializable(package='Custom', name='custom_loss')
def custom_loss(y_true, y_pred):
    loss1 = tf.reduce_mean(tf.square(y_true[:, 0] - y_pred[:, 0]))
    loss2 = tf.reduce_mean(tf.square(y_true[:, 1] - y_pred[:, 1]))

    loss = 10 * loss1 +  1000 * loss2
    return loss

# input, output channel
input_dim = 4
hidden_dim = 128
output_dim = 2


def addLarge():
    global id# Declare id as global to modify it globally
    with sqlite3.connect(db) as conn:
        num = 5
        for i in data_L5:
            conn.execute(
                'UPDATE pred2 SET Q = ?, P = ?, W = ?, Igv = ?, num = ?, T = ?, H = ? WHERE id = ?',
                (i[1], i[2], i[0], 0, num, 59, 21.3, id)
            )
            id += 1  # Increment id after each insertion
        num = 6
        for i in data_L6:
            conn.execute(
                'UPDATE pred2 SET Q = ?, P = ?, W = ?, Igv = ?, num = ?, T = ?, H = ? WHERE id = ?',
                (i[1], i[2], i[0], 0, num, 59, 21.3, id)
            )
            id += 1  # Increment id after each insertion
        

#function to update database
def UPDB(model_path, flowRate, pressure, T, H, scaler_X, scaler_Y, num):
    global id# Declare id as global to modify it globally
    model = tf.keras.models.load_model(model_path, custom_objects={'SomeNetwork': SomeNetwork})
    
    for f in range(flowRate - 100, flowRate + 51, 10):
        message = tf.stack([[pressure, f, T, H]])
        message = scaler_X.transform(message)
        predictions = model.predict(message.reshape(-1, 4, 1))
        predictions = scaler_Y.inverse_transform(predictions)
        
        predictions[:, 0] = np.where(predictions[:, 0] < 0, 0, predictions[:, 0])

        power = predictions[0][1]
        igv = predictions[0][0]
        
        # Open a connection, execute the query, and close the connection
        with sqlite3.connect(db) as conn:
            conn.execute(
                'UPDATE pred2 SET Q = ?, P = ?, W = ?, Igv = ?, num = ?, T = ?, H = ? WHERE id = ?',
                (f, pressure, float(power), float(igv), num, T, H, id)
            )
        id += 1  # Increment id after each insertion


def fetchModels(pressure):
    for j in [1, 2, 3, 4, 7, 8, 9]:
        model_path = f'D:/이사온친구들/새 폴더/RealData/models{j}.keras'
        
        # 스케일러 불러오기
        scaler_save_path = f'D:/이사온친구들/새 폴더/RealData/scalers{j}.pkl'
        with open(scaler_save_path, 'rb') as f:
            scalers = pickle.load(f)
            scaler_X = scalers['scaler_X']
            scaler_Y = scalers['scaler_Y']
        T = 0
        H = 0
        if j == 1:
            T = 21
            H = 57
        elif j == 2:
            T = 21.5
            H = 57
        elif j == 3:
            T = 21.5
            H = 62
        elif j == 4:
            T = 21.8
            H = 61
        elif j == 5:
            T = 21.3
            H = 59
        elif j == 6:
            T = 21.3
            H = 59
        elif j == 7:
            T = 21.6
            H = 61
        elif j == 8:
            T = 21.5
            H = 57
        elif j == 9:
            T = 21.8
            H = 61
        # UPDB 호출
        UPDB(model_path, 150, pressure, T, H, scaler_X, scaler_Y, j)


def runFile():
    global id
    id = 1
    fetchModels(10)
    fetchModels(11)
    fetchModels(12)
    fetchModels(13)
    fetchModels(14)
    fetchModels(15)
    fetchModels(16)
    fetchModels(17)
    fetchModels(18)
    fetchModels(19)
    fetchModels(20)
    fetchModels(21)
    fetchModels(22)
    fetchModels(23)
    fetchModels(24)
    fetchModels(25)
    fetchModels(26)
    fetchModels(27)
    fetchModels(28)
    fetchModels(29)
    fetchModels(30)
    fetchModels(31)
    fetchModels(32)
    fetchModels(33)
    fetchModels(34)
    fetchModels(35)
    fetchModels(36)
    fetchModels(37)
    fetchModels(38)
    fetchModels(39)
    fetchModels(40)
    fetchModels(41)
    fetchModels(42)
    fetchModels(43)
    fetchModels(44)
    fetchModels(45)
    fetchModels(46)
    fetchModels(47)
    fetchModels(48)
    fetchModels(49)
    fetchModels(50)
    addLarge()
    id = 1