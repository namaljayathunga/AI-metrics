# The file was autogenerated by ../scrapers/wer.py

from datetime import date

from data.acoustics import speech_recognition, swb_hub_500
from scales import *


librispeech = speech_recognition.metric(name="LibriSpeech", scale=error_percent, attributes=['language'])
librispeech.measure(date(2016, 9, 2), 4.28, 'HMM-TDNN trained with MMI + data augmentation (speed) + iVectors + 3 regularizations', 'http://www.danielpovey.com/files/2016_interspeech_mmi.pdf')
librispeech.measure(date(2015, 8, 2), 4.83, 'HMM-TDNN + iVectors', 'http://speak.clsp.jhu.edu/uploads/publications/papers/1048_pdf.pdf')
librispeech.measure(date(2015, 12, 2), 5.33, '9-layer model w/ 2 layers of 2D-invariant convolution &amp; 7 recurrent layers, w/ 68M parameters trained on 11940h', 'http://arxiv.org/abs/1512.02595v1')
librispeech.measure(date(2015, 8, 2), 5.51, 'HMM-DNN + pNorm*', 'http://www.danielpovey.com/files/2015_icassp_librispeech.pdf')
librispeech.measure(date(2015, 8, 2), 8.01, 'HMM-(SAT)GMM', 'http://kaldi-asr.org/')

wsj = speech_recognition.metric(name="WSJ", scale=error_percent, attributes=['language'])
wsj.measure(date(2015, 4, 2), 3.47, 'TC-DNN-BLSTM-DNN', 'http://arxiv.org/pdf/1504.01482v1.pdf')
wsj.measure(date(2015, 8, 2), 3.63, 'test-set on open vocabulary (i.e. harder), model = HMM-DNN + pNorm*', 'http://www.danielpovey.com/files/2015_icassp_librispeech.pdf')
wsj.measure(date(2015, 12, 2), 3.60, '9-layer model w/ 2 layers of 2D-invariant convolution &amp; 7 recurrent layers, w/ 68M parameters', 'http://arxiv.org/abs/1512.02595v1')
wsj.measure(date(2014, 8, 2), 5.6, 'CNN over RAW speech (wav)', 'http://infoscience.epfl.ch/record/203464/files/Palaz_Idiap-RR-18-2014.pdf')

swb_hub_500.measure(date(2017, 3, 2), 5.5, 'ResNet + BiLSTMs acoustic model, with 40d FMLLR + i-Vector inputs, trained on SWB+Fisher+CH, n-gram + model-M + LSTM + Strided ( trous) convs-based LM trained on Switchboard+Fisher+Gigaword+Broadcast', 'https://arxiv.org/pdf/1703.02136.pdf')
swb_hub_500.measure(date(2016, 9, 2), 6.3, 'VGG/Resnet/LACE/BiLSTM acoustic model trained on SWB+Fisher+CH, N-gram + RNNLM language model trained on Switchboard+Fisher+Gigaword+Broadcast', 'http://arxiv.org/pdf/1609.03528v1.pdf')
swb_hub_500.measure(date(2016, 6, 2), 6.6, 'RNN + VGG + LSTM acoustic model trained on SWB+Fisher+CH, N-gram + "model M" + NNLM language model', 'http://arxiv.org/pdf/1604.08242v2.pdf')
swb_hub_500.measure(date(2016, 9, 2), 8.5, 'HMM-BLSTM trained with MMI + data augmentation (speed) + iVectors + 3 regularizations + Fisher', 'http://www.danielpovey.com/files/2016_interspeech_mmi.pdf')
swb_hub_500.measure(date(2016, 9, 2), 9.2, 'HMM-TDNN trained with MMI + data augmentation (speed) + iVectors + 3 regularizations + Fisher (10% / 15.1% respectively trained on SWBD only)', 'http://www.danielpovey.com/files/2016_interspeech_mmi.pdf')
swb_hub_500.measure(date(2014, 12, 2), 12.6, 'CNN + Bi-RNN + CTC (speech to letters), 25.9% WER if trainedonlyon SWB', 'http://arxiv.org/abs/1412.5567')
swb_hub_500.measure(date(2015, 8, 2), 11, 'HMM-TDNN + iVectors', 'http://speak.clsp.jhu.edu/uploads/publications/papers/1048_pdf.pdf')
swb_hub_500.measure(date(2013, 8, 2), 12.6, 'HMM-DNN +sMBR', 'http://www.danielpovey.com/files/2013_interspeech_dnn.pdf')
swb_hub_500.measure(date(2015, 8, 2), 12.9, 'HMM-TDNN + pNorm + speed up/down speech', 'http://www.danielpovey.com/files/2015_interspeech_augmentation.pdf')
swb_hub_500.measure(date(2014, 6, 2), 15, 'DNN + Dropout', 'http://arxiv.org/abs/1406.7806v2')
swb_hub_500.measure(date(2014, 8, 2), 10.4, 'CNN on MFSC/fbanks + 1 non-conv layer for FMLLR/I-Vectors concatenated in a DNN', 'http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202014/papers/p5609-soltau.pdf')
swb_hub_500.measure(date(2013, 8, 2), 11.5, 'CNN', 'http://www.cs.toronto.edu/~asamir/papers/icassp13_cnn.pdf')
swb_hub_500.measure(date(2015, 9, 2), 12.2, 'Deep CNN (10 conv, 4 FC layers), multi-scale feature maps', 'http://arxiv.org/pdf/1509.08967v1.pdf')

fisher = speech_recognition.metric(name="Fisher", scale=error_percent, attributes=['language'])
fisher.measure(date(2016, 9, 2), 9.6, 'HMM-BLSTMtrained with MMI + data augmentation (speed) + iVectors + 3 regularizations + SWBD', 'http://www.danielpovey.com/files/2016_interspeech_mmi.pdf')
fisher.measure(date(2016, 9, 2), 9.8, 'HMM-TDNNtrained with MMI + data augmentation (speed) + iVectors + 3 regularizations + SWBD', 'http://www.danielpovey.com/files/2016_interspeech_mmi.pdf')

chime = speech_recognition.metric(name="CHiME (noisy speech)", scale=error_percent, attributes=['language'])
chime.measure(date(2015, 12, 2), 3.34, '9-layer model w/ 2 layers of 2D-invariant convolution &amp; 7 recurrent layers, w/ 68M parameters', 'http://arxiv.org/abs/1512.02595v1')
chime.measure(date(2014, 12, 2), 6.30, 'CNN + Bi-RNN + CTC (speech to letters)', 'http://arxiv.org/abs/1412.5567')

timit = speech_recognition.metric(name="TIMIT", scale=error_percent, attributes=['language'])
timit.measure(date(2015, 9, 2), 16.5, 'Hierarchical maxout CNN + Dropout', 'https://link.springer.com/content/pdf/10.1186%2Fs13636-015-0068-3.pdf')
timit.measure(date(2014, 8, 2), 16.7, 'CNN in time and frequency + dropout, 17.6% w/o dropout', 'http://www.inf.u-szeged.hu/~tothl/pubs/ICASSP2014.pdf')
timit.measure(date(2016, 3, 2), 17.3, 'RNN-CRF on 24(x3) MFSC', 'https://arxiv.org/abs/1603.00223')
timit.measure(date(2015, 6, 2), 17.6, 'Bi-RNN + Attention', 'http://arxiv.org/abs/1506.07503')
timit.measure(date(2013, 3, 2), 17.7, 'Bi-LSTM + skip connections w/ CTC', 'http://arxiv.org/abs/1303.5778v1')
timit.measure(date(2009, 8, 2), 23, '(first, modern) HMM-DBN', 'http://www.cs.toronto.edu/~asamir/papers/NIPS09.pdf')