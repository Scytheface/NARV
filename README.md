# NÄRV

1. venv
   
    alati venv
   
    alati alati venv
2. pip install -r requirements.txt

3. **lab** või notebook

4. ????

5. uus halb eesti muusika

# hetkelised mudelid

kood siin: https://colab.research.google.com/drive/1U-pLaNK-4rVNpk-nB86Hix1_bb-OFr2B?usp=sharing

## lyrics-weights-1layer
model = Sequential()
model.add(LSTM(256, input_shape=(maxlen, len(chars))))
model.add(Dropout(0.2))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.001, momentum=0.1)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

## lyrics-weights-symmetrical

model = Sequential()
model.add(LSTM(64, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64, input_shape=(maxlen, len(chars))))
model.add(Dropout(0.2))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.001, momentum=0.1)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

## lyrics-weights-narrow-deep

model = Sequential()
model.add(LSTM(64, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(32, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(16, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(8, input_shape=(maxlen, len(chars))))
model.add(Dropout(0.2))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.001, momentum=0.1)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)
