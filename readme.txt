To create a virtual environment follow these steps-

1- Navigate to the directory where you want to create the virtual environment:
cd path\to\your\project

2- Create a virtual environment using the following command:
python -m venv venv

3- Activate the virtual environment:
venv\Scripts\activate

To run the requirements file that contains all the necessary libraries use the below command-
pip install -r requirements.txt

Verify that the dependencies have been installed correctly by checking the installed packages-
pip list


If you have trouble installing pytorch(torch) using requirements file, try running the below command
pip3 install torch torchvision torchaudio

or if your system have a GPU,
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


If you are having any issues with setting up the project, feel free to mail FSR-AI @ fsr-ai@b-tu.de