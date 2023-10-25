# Detect-DeepFake-Using-CNN

<p> This study proposes a deep learning-based approach for Deepfake prediction using CNN. The preferred method involves training a CNN architecture on a dataset of real and fake images obtained in Kaggle, followed by transfer learning using Xception, which has already been trained on the ImageNet dataset. The model learns to distinguish between real and fake images by identifying patterns and features unique to each class. The results show that the proposed CNN-based approach performs decently in predicting fake images, and we are aiming forward to achieve better results. </p>

# Dataset Link: [DeepFake Dataset](https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images/data 'DeepFake Dataset')

# How to setup and run the code
<li> Download the dataset from the given link and extract the dataset</li>
<li> You need to place all the "real" image inside the "dataset/real" folder, to do that copy the real images from the downloaded folder and paste them inside "dataset/real" folder</li>
<li> You need to place all the "fake" image inside the "dataset/fake" folder, to do that copy the fake images from the downloaded folder and paste them inside "dataset/fake" folder</li>
<li> Install all the required package present in requirements.txt file </li>
<li> Run prepare_dataset.ipynb that file split your dataset into train, test and validation part and copy them into split_dataset folder automatically</li>
<li> Run train_CNN.ipynb </li>
<li> To start the GUI run app.py </li>

## Note: You can run the GUI even before run the train_CNN.ipynb because here the saved model is already present

# Need Any Support
<h3 align="left">Connect me</h3>
<p align="left">
<a href="https://linkedin.com/in/pritam-pips" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="pritam-pips" height="30" width="40" /></a>
</p>
