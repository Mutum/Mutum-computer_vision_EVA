


**Objective** : Aim is to acheive 98-99 accuracy with less parameters. Here we reduced the number of parameters to **5,850**. In this notebook, we are refining the architecture with reference to [Kaggle Notebook](https://www.kaggle.com/enwei26/mnist-digits-pytorch-cnn-99)

Ideas implemented:
- Reducing the number output channels in conv block. Intuition behind using 10 channels is to represent each digits by one channels.
- Removing Bias from the network to reduce parameters
- Add transition block - Max pooling followed by 1*1 
- Add Batch normalization

Achieved 99% accuracy in 10 epochs

Training logs:

epoch=1 Loss=0.10399410873651505 batch_id=00468: 100%|██████████| 469/469 [00:22<00:00, 20.98it/s]
Test set: Average loss: 0.0729, Accuracy: 9795/10000 (97.95%)

epoch=2 Loss=0.02757311426103115 batch_id=00468: 100%|██████████| 469/469 [00:22<00:00, 20.64it/s]
Test set: Average loss: 0.0554, Accuracy: 9816/10000 (98.16%)

epoch=3 Loss=0.040557343512773514 batch_id=00468: 100%|██████████| 469/469 [00:22<00:00, 21.22it/s]
Test set: Average loss: 0.0480, Accuracy: 9847/10000 (98.47%)

epoch=4 Loss=0.020351147279143333 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.41it/s]
Test set: Average loss: 0.0438, Accuracy: 9857/10000 (98.57%)

epoch=5 Loss=0.025274403393268585 batch_id=00468: 100%|██████████| 469/469 [00:21<00:00, 22.09it/s]
Test set: Average loss: 0.0393, Accuracy: 9872/10000 (98.72%)

epoch=6 Loss=0.021971091628074646 batch_id=00468: 100%|██████████| 469/469 [00:21<00:00, 21.79it/s]
Test set: Average loss: 0.0383, Accuracy: 9878/10000 (98.78%)

epoch=7 Loss=0.01498644519597292 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.65it/s]
Test set: Average loss: 0.0459, Accuracy: 9858/10000 (98.58%)

epoch=8 Loss=0.09274668246507645 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.71it/s]
Test set: Average loss: 0.0322, Accuracy: 9895/10000 (98.95%)

epoch=9 Loss=0.06995870918035507 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.78it/s]
Test set: Average loss: 0.0324, Accuracy: 9897/10000 (98.97%)

epoch=10 Loss=0.05770690366625786 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.65it/s]
Test set: Average loss: 0.0326, Accuracy: 9900/10000 (99.00%)

epoch=11 Loss=0.04096147045493126 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.58it/s]
Test set: Average loss: 0.0292, Accuracy: 9902/10000 (99.02%)

epoch=12 Loss=0.035513609647750854 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.66it/s]
Test set: Average loss: 0.0263, Accuracy: 9916/10000 (99.16%)

epoch=13 Loss=0.01344356406480074 batch_id=00468: 100%|██████████| 469/469 [00:21<00:00, 21.93it/s]
Test set: Average loss: 0.0297, Accuracy: 9896/10000 (98.96%)

epoch=14 Loss=0.007912804372608662 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.37it/s]
Test set: Average loss: 0.0298, Accuracy: 9902/10000 (99.02%)

epoch=15 Loss=0.05655677616596222 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.43it/s]
Test set: Average loss: 0.0263, Accuracy: 9914/10000 (99.14%)

epoch=16 Loss=0.016426850110292435 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.46it/s]
Test set: Average loss: 0.0286, Accuracy: 9913/10000 (99.13%)

epoch=17 Loss=0.036421921104192734 batch_id=00468: 100%|██████████| 469/469 [00:21<00:00, 22.14it/s]
Test set: Average loss: 0.0256, Accuracy: 9913/10000 (99.13%)

epoch=18 Loss=0.03774150088429451 batch_id=00468: 100%|██████████| 469/469 [00:20<00:00, 22.42it/s]
Test set: Average loss: 0.0262, Accuracy: 9913/10000 (99.13%)

epoch=19 Loss=0.0114607447758317 batch_id=00468: 100%|██████████| 469/469 [00:21<00:00, 22.01it/s]
Test set: Average loss: 0.0296, Accuracy: 9910/10000 (99.10%)

Training and validation plot:
![image](https://user-images.githubusercontent.com/8687204/212421862-5e5f4c83-008e-494b-a590-73810690178b.png)
