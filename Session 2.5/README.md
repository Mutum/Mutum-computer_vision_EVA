
# Objective - Write a model to train an image from the MNIST dataset (say 5), and a random number between 0 and 9, (say 7) and gives two outputs:
- the "NUMBER" that was represented by the MNIST image (predict 5)
- the "SUM" of this number with the random number and the input image to the network (predict 5 + 7 = 12)
                 

Step:
1. Get MNIST dataset
2. Write custom class/function to output MNIST dataset and a random number (0-9)  
3. Write a classification model namely ("Network") having two inputs
MNIST images and random number . Network to predict MNIST label as well as the total (lable + the random number )
4. Train the Network for 20 epoch

Network summary:
- Random number - the numpy random number generated is int64
- The MNIST inpust is trained for two convulation layer
- The "random number" is then added to above output . 
  code line : x_new = torch.add(x, x_rand)
- Then followed by 2 FC layer 
- Lastly two prediction out for MNIST and SUM 

- cross_entropy loss function were used 
- Accuracy metrics for both the MNIST and SUM were produced

Training output:
<img width="1242" alt="training_output" src="https://user-images.githubusercontent.com/8687204/211121317-7cad0f36-d0b6-416a-8aac-444fa9c37bdf.png">

