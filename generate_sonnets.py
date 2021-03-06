from tensorflow.keras.models import load_model
import numpy as np


def load_data(maxlen=40, step=3):
    '''
    Load in training text and vectorize it into 3D tensor
    Args:
        maxlen: Maximum length of sequence
        step: Step size for sampling new sequence
    Returns:
        Numpy tensor of shape (samples, seq_len, num_chars)
    '''
    with open('shakespeare_sonnets_dataset.txt', 'r') as f:
        data = f.read().lower()
    sentences = []
    targets = []
    # Loop through sonnets and create sequences and associated targets
    datalen = len(data)
    for i in range(0, datalen - maxlen, step):
        sentences.append(data[i:i + maxlen])
        targets.append(data[maxlen + i])
    # Grab all unique characters in corpus
    chars = sorted(list(set(data)))

    # Dictionary mapping unique character to integer indices
    char_indices = dict((char, chars.index(char)) for char in chars)
    return data, char_indices, chars


def sample(preds, temperature=0.2):
    '''
    Reweight the predicted probabilities and draw sample from
    newly created probability distribution
    Args:
        preds: Numpy array of character probabilities
        temperature: Float representing randomness of reweighting probabilities
                     Higher temp, more randomn. Lower temp, more deterministic
    Returns:
        Index of largest probability from reweighted probabilities
    '''
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def generate_sonnet():
    '''
    Choose a random seed text and print 600 predicted characters to console
    Args:
        None
    Returns:
        x characters printed to console
		where x is the number in for loop(can be edited for larger sonnets)
		
    '''
    # Max length of each sequence
    maxlen = 40
    # Sample new sequence every step characters
    step = 3
    data, char_indices, chars = load_data(maxlen, step)

    # Load the trained model
    model = load_model('shakespeare_model.h5')
    # Choose random seed text
    start_idx = np.random.randint(0, len(data) - maxlen - 1)
    new_sonnet = data[start_idx:start_idx + maxlen]

    charlen = len(chars)
    generated_sonnet = []
	
	# Character limit has been set to 200 due to heroku limitation. Increase it to 600
    for i in range(200):
        # Vectorize generated text

        sampled = np.zeros((1, maxlen, charlen))
        for j, char in enumerate(new_sonnet):
            sampled[0, j, char_indices[char]] = 1.

        # Predict next character
        preds = model.predict(sampled, verbose=0)[0]
        pred_idx = sample(preds, temperature=0.2)
        next_char = chars[pred_idx]

        # Append predicted character to seed text
        new_sonnet += next_char
        new_sonnet = new_sonnet[1:]
		
        generated_sonnet.append(next_char)

    return "".join(generated_sonnet)


if __name__ == '__main__':
    ''' Run main program '''
    generate_sonnet()