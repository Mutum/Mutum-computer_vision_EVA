# Assignment:

Your new target is:
- 99.4% (this must be consistently shown in your last few epochs, and not a one-time achievement)
- Less than or equal to 15 Epochs
- Less than 10000 Parameters (additional points for doing this in less than 8000 pts)
- Do this in exactly 3 steps
- Each File must have "target, result, analysis" TEXT block (either at the start or the end)
- You must convince why have you decided that your target should be what you have decided it to be, and your analysis MUST be correct. 
- Evaluation is highly subjective, and if you target anything out of the order, marks will be deducted. 
- Explain your 3 steps using these target, results, and analysis with links to your GitHub files (Colab files moved to GitHub). 
- Keep Receptive field calculations handy for each of your models. 
- If your GitHub folder structure or file_names are messy, -100. 
- When ready, attempt SESSION 4 -Assignment Solution



# Solution, Step 1 [a link]([EVA8_S4_step1.ipynb](https://github.com/Mutum/Mutum-computer_vision_EVA/blob/main/Session%204%20-%20Coding%20Drill%20Down%20/%20EVA8_S4_step1.ipynb)
## Target
Create a Setup (dataset, data loader, train/test steps and log plots)
Defining simple model with Convolution block, GAP, dropout and batch normalization.
## Results
- Parameters: 7,432
- Best Train Accuracy 98.84%
- Best Test Accuracy 99.25%
## Analysis
Model with 7K parameters is able to reach till 99.25% accuracy in 15 epochs.
Model is sligthly underfitting


# Solution, Step 2 [a link]([EVA8_S4_step2.ipynb](https://github.com/Mutum/Mutum-computer_vision_EVA/blob/main/Session%204%20-%20Coding%20Drill%20Down%20/%20EVA8_S4_step2.ipynb)
### Target
- Add data augmentation, this will train harder. Add RandomAffine and RandomRotation . Note scaling input on mean + std were already in step_1 notebook
- Remove dropout from first convolution, inadvertently add in step_1 notebook
### Results
- Parameters: 7,432
- Best Train Accuracy 97.64
- Best test accuracy 99.28%
### Analysis
- The model is still underfitting
- Noticed we had larger gap between train and test metrics , this implies we can play on learning rate to learn more

# Solution, Step 3 [a link]([EVA8_S4_step3.ipynb](https://github.com/Mutum/Mutum-computer_vision_EVA/blob/main/Session%204%20-%20Coding%20Drill%20Down%20/EVA8_S4_step3.ipynb)
## Target
- Introduce StepLR rate scheduler with a higher learning rate of 0.02 .
- Remember we need to learn more as there were larger gap between train and test metrics
### Results
- Parameters: 7,432
- Best Train Accuracy 97.80
- Best test accuracy 99.40%
## Analysis
Model with 7.4K parameters had hit 99.40% accuracy at 10 epochs.
its only one time hit, we need to stabilized though

